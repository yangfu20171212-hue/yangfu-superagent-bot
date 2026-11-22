#!/usr/bin/env python3
"""
rmy_client.py —— 睿美云 TPOS 开放接口通用客户端（机构无关版 v3.0）

产品化改造核心目标：
  * 不硬编码任何机构（门店 / 人员 / 凭据）信息。
  * 凭据从环境变量读取（RMY_BASE_URL / RMY_ACCOUNT / RMY_PRIVATE_KEY(b64 DER)
    / RMY_TIMEOUT / RMY_SIGN_STRING_TEMPLATE），或通过 RmyClient.from_config(cfg)
    注入（多机构复制时使用）。
  * 签名算法与 relay_server.py 内联实现保持字节级一致：
        sign_data = "{ts}&{nonce}"  ->  RSA PKCS#1 v1.5 + SHA256  ->  base64
    使用 cryptography 库（纯 Python，跨平台，不依赖 openssl CLI）。

依赖：
  pip install requests cryptography

本文件替代已丢失的 ~/.workbuddy/skills/ruimei-crm-sync/scripts/rmy_client.py。
由 rmy_auth.py 重导出，保证 rmy_push_back.py / sync_rmy_staff.py /
manual_trial.py / test_rmy_real.py 零改动继续可用。
"""
from __future__ import annotations

import os
import re
import time
import json
import base64
import hashlib
import socket
import secrets
import logging
from pathlib import Path
from typing import Optional

import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# ============================ 常量 ============================
RMY_VISIT_TYPE_DEFAULT = "45"   # 回访类型（与 relay_server 一致）
RMY_VISIT_WAY_DEFAULT = "1"     # 回访方式默认值（机构可在 config 覆盖）
VISIT_STATUS_RESPONSE = {
    "contacted": "已联系",
    "booked": "已预约",
    "arrived": "已到店",
    "done": "已完成",
}
# status 枚举 -> 回访内容文本（push_visit_status 使用）
STATUS_TO_TEXT = {
    "contacted": "已联系客户",
    "booked": "已预约到店",
    "arrived": "已到店",
    "done": "已完成回访",
}
DEFAULT_SIGN_TEMPLATE = "{ts}&{nonce}"
VIP_FIELDS = ["vipNumber", "memberNumber", "cardNo", "memberNo", "vipNo", "vipNum", "medicalNo"]

# ============================ 重试 / 容错配置（2026-08-28 加固） ============================
# TPOS 要求：时间戳与服务器相差 < 1 分钟，nonce 1 分钟内不可重复
DEFAULT_MAX_RETRIES = 3          # HTTP 层最大重试次数（不含首次）
DEFAULT_BACKOFF_BASE = 0.5       # 退避基数（秒）：等待 = base * 2^(n-1)
RETRY_HTTP_STATUS = {429, 500, 502, 503, 504}   # 可重试的 HTTP 状态码
TIMEOUT_HTTP_STATUS = {408, 504}
# 响应 msg 中包含这些关键词时视为「鉴权/时序类错误」，GET 可安全重试
RETRYABLE_MSG_KEYS = ("签名", "时间戳", "nonce", "超时", "timeout", "signature")
# 已知业务码
CODE_SUCCESS = 10000

logger = logging.getLogger("rmy_client")
if not logger.handlers:
    logger.addHandler(logging.NullHandler())

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# 本地 secret 文件（不参与 skill 同步，权限 600；明文凭据统一存放于此）
SECRET_PATH = Path.home() / ".workbuddy" / "secrets" / "ruimei_tpos.json"


def _load_secret() -> dict:
    """从本地 secret 文件读取凭据（环境变量优先，secret 文件兜底）。"""
    if SECRET_PATH.exists():
        try:
            return json.loads(SECRET_PATH.read_text(encoding="utf-8")) or {}
        except Exception:
            return {}
    return {}


_secret = _load_secret()

# 模块级 env 常量（兼容 rmy_auth 重导出与旧脚本对 rmy_client.RMY_* 的引用）
# 优先级：环境变量 > ~/.workbuddy/secrets/ruimei_tpos.json
RMY_BASE_URL = os.environ.get("RMY_BASE_URL") or _secret.get("base_url") or ""
RMY_ACCOUNT = os.environ.get("RMY_ACCOUNT") or _secret.get("account") or "boss"
RMY_PRIVATE_KEY_B64 = os.environ.get("RMY_PRIVATE_KEY") or _secret.get("private_key") or ""
RMY_TIMEOUT = int(os.environ.get("RMY_TIMEOUT") or _secret.get("timeout") or "15")
RMY_SIGN_STRING_TEMPLATE = os.environ.get("RMY_SIGN_STRING_TEMPLATE") or _secret.get("sign_template") or DEFAULT_SIGN_TEMPLATE


# ============================ 私钥加载 ============================
def _load_private_key(priv_b64: str):
    if not priv_b64:
        return None
    der = base64.b64decode(priv_b64)
    return serialization.load_der_private_key(der, password=None)


# ============================ 容错工具（2026-08-28 加固） ============================
class _Retryable(Exception):
    """内部标记：可重试的错误。"""


_time_offset = 0   # server_time - local_time（秒），由响应头 Date 学习


def _now_ts() -> int:
    """带时钟补偿的秒级时间戳（TPOS 要求与服务器相差 < 1 分钟）。"""
    return int(time.time()) + _time_offset


def _learn_time_offset(resp) -> None:
    """从 HTTP 响应头 Date 学习服务器时钟偏差；偏差 > 30 秒才修正，避免抖动。"""
    global _time_offset
    try:
        date_hdr = resp.headers.get("Date")
        if not date_hdr:
            return
        from email.utils import parsedate_to_datetime
        offset = int(parsedate_to_datetime(date_hdr).timestamp()) - int(time.time())
        if abs(offset) >= 30:
            _time_offset = offset
            logger.warning("本机与睿美云服务器时钟偏差 %s 秒，已自动补偿", offset)
    except Exception:
        pass


def classify_response(data: dict) -> dict:
    """把睿美云响应归类，便于上层判断是否重试/告警。

    返回: {"ok", "category", "retryable", "code", "msg"}
    category: success / auth（鉴权或时序问题，可重试）/ server / business（业务失败）
    说明：仅 10000 判定成功；其余按 msg 关键词归类，不臆造具体错误码。
    """
    if not isinstance(data, dict):
        return {"ok": False, "category": "server", "retryable": True,
                "code": None, "msg": "响应格式异常"}
    code = data.get("code")
    msg = (data.get("msg") or data.get("errorMsg") or "").strip()
    if code == CODE_SUCCESS:
        return {"ok": True, "category": "success", "retryable": False,
                "code": code, "msg": msg}
    category, retryable = "business", False
    low = msg.lower()
    if any(k.lower() in low for k in RETRYABLE_MSG_KEYS) or code in (401, 403):
        category = "auth"
        retryable = True
    elif isinstance(code, int) and code >= 50000:
        category = "server"
        retryable = True
    return {"ok": False, "category": category, "retryable": retryable,
            "code": code, "msg": msg}


# ============================ 客户端类 ============================
class RmyClient:
    def __init__(self, base_url=None, account=None, private_key_b64=None,
                 timeout=None, sign_template=None, max_retries=None, backoff_base=None):
        self.base_url = (base_url or os.environ.get("RMY_BASE_URL") or RMY_BASE_URL or "").rstrip("/")
        self.account = account or os.environ.get("RMY_ACCOUNT") or RMY_ACCOUNT
        self._priv_b64 = private_key_b64 or os.environ.get("RMY_PRIVATE_KEY") or RMY_PRIVATE_KEY_B64
        self.timeout = int(timeout or os.environ.get("RMY_TIMEOUT") or RMY_TIMEOUT)
        self.sign_template = sign_template or os.environ.get("RMY_SIGN_STRING_TEMPLATE") or RMY_SIGN_STRING_TEMPLATE
        self.max_retries = int(max_retries if max_retries is not None
                               else (os.environ.get("RMY_MAX_RETRIES") or DEFAULT_MAX_RETRIES))
        self.backoff_base = float(backoff_base if backoff_base is not None
                                  else (os.environ.get("RMY_BACKOFF_BASE") or DEFAULT_BACKOFF_BASE))
        self._key = _load_private_key(self._priv_b64) if self._priv_b64 else None

    @classmethod
    def from_config(cls, cfg: dict) -> "RmyClient":
        """从机构 config 注入凭据（多机构复制入口）。cfg 形如 {'ruimei': {...}}。"""
        rmy = (cfg.get("ruimei") or {}) if isinstance(cfg, dict) else {}
        return cls(
            base_url=rmy.get("base_url") or rmy.get("RMY_BASE_URL"),
            account=rmy.get("account") or rmy.get("RMY_ACCOUNT"),
            private_key_b64=rmy.get("private_key") or rmy.get("RMY_PRIVATE_KEY"),
            timeout=rmy.get("timeout"),
            sign_template=rmy.get("sign_template"),
        )

    # ---- 鉴权头（核心签名逻辑） ----
    def _auth_headers(self) -> Optional[dict]:
        if not self._key:
            return None
        ts = str(_now_ts())          # 带服务器时钟补偿
        nonce = _generate_nonce(ts)
        ctx = {"ts": ts, "timestamp": ts, "nonce": nonce}
        sign_data = self.sign_template.format_map(ctx)
        sig = self._key.sign(sign_data.encode("utf-8"), padding.PKCS1v15(), hashes.SHA256())
        sign = base64.b64encode(sig).decode("ascii")
        return {
            "tpos-account": self.account,
            "tpos-timestamp": ts,
            "tpos-nonce-str": nonce,
            "tpos-sign": sign,
            "Content-Type": "application/json",
        }

    # ---- 请求封装（2026-08-28 加固：重试 + 退避 + 时钟补偿） ----
    def _request(self, method: str, path: str, params=None, body=None,
                 retry: Optional[bool] = None) -> dict:
        """统一请求入口。

        - GET 默认视为幂等，允许重试（HTTP 5xx/429/网络异常 + 鉴权时序类错误）
        - POST 默认不重试，避免重复写入；确需重试请显式 retry=True
        - 每次响应都从 Date 头学习服务器时钟偏差，防止签名因时间漂移失败
        """
        if not self.base_url:
            raise RuntimeError("RMY_BASE_URL 未配置，无法请求睿美云")
        h = self._auth_headers()
        if not h:
            raise RuntimeError("RMY_PRIVATE_KEY 未配置，无法生成签名")

        method = method.upper()
        allow_retry = (method == "GET") if retry is None else bool(retry)
        max_tries = (self.max_retries + 1) if allow_retry else 1
        url = f"{self.base_url}{path}"
        last_err = None

        for attempt in range(max_tries):
            try:
                r = requests.request(method, url, params=params, json=body,
                                     headers=h, timeout=self.timeout)
                _learn_time_offset(r)
                if r.status_code in RETRY_HTTP_STATUS and attempt < max_tries - 1:
                    raise _Retryable(f"HTTP {r.status_code}")
                try:
                    data = r.json()
                except ValueError:
                    return {"code": None, "msg": f"非 JSON 响应(HTTP {r.status_code})",
                            "data": None, "_error": "invalid_json"}
                info = classify_response(data)
                if (not info["ok"]) and info["category"] == "auth" and attempt < max_tries - 1:
                    logger.warning("鉴权/时序错误，重新签名重试: %s", info["msg"])
                    h = self._auth_headers()   # 重新生成 ts/nonce/签名
                    raise _Retryable(info["msg"])
                return data
            except _Retryable as e:
                last_err = e
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout,
                    requests.exceptions.ChunkedEncodingError) as e:
                last_err = e
            if attempt < max_tries - 1:
                time.sleep(self.backoff_base * (2 ** attempt))

        logger.error("睿美云请求失败 %s %s: %s", method, path, last_err)
        return {"code": None, "msg": f"请求失败: {last_err}", "data": None,
                "_error": str(last_err) if last_err else "unknown"}

    def get(self, path: str, params=None) -> dict:
        return self._request("GET", path, params=params)

    def post(self, path: str, json=None, retry: bool = False) -> dict:
        return self._request("POST", path, body=json, retry=retry)

    # ---- 工具 ----
    def search_customer_raw(self, keyword: str) -> list:
        data = self.get("/api/v1/tpos/customer/customer-search", params={"keyword": str(keyword)})
        recs = (data.get("data") or {}).get("records") or data.get("data") or []
        if not isinstance(recs, list):
            recs = [recs] if recs else []
        return recs


# ============================ 公共函数（供旧脚本经 rmy_auth 调用） ============================
def _resolve_neuron_id(recs: list, member_id) -> Optional[str]:
    mid = str(member_id)
    for r in recs:
        if not isinstance(r, dict):
            continue
        for f in VIP_FIELDS:
            v = r.get(f)
            if v is not None and str(v) == mid:
                return r.get("neuronCusId") or r.get("id") or r.get("customerId")
    if len(recs) == 1 and isinstance(recs[0], dict):
        return recs[0].get("neuronCusId") or recs[0].get("id") or recs[0].get("customerId")
    return None


def search_customer_by_vip(cli: RmyClient, vip) -> Optional[str]:
    """按会员号/关键字搜索，返回 neuronCusId；找不到返回 None。"""
    return _resolve_neuron_id(cli.search_customer_raw(vip), vip)


resolve_customer_id = search_customer_by_vip  # 别名


def load_staff_map() -> dict:
    """读取 data/rmy_staff_sync/rmy_staff_map.json -> {wecom_userid: {...}}；不存在返回 {}。"""
    p = Path(__file__).parent / "data" / "rmy_staff_sync" / "rmy_staff_map.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def resolve_rmy_user_id(staff_key, staff_map: Optional[dict] = None) -> Optional[str]:
    """企微 userid / 中文名 -> 睿美云员工 id。"""
    m = staff_map if staff_map is not None else load_staff_map()
    if staff_key in m:
        return m[staff_key].get("rmy_user_id")
    for wecom, info in m.items():
        if info.get("rmy_name") == staff_key or info.get("display_name") == staff_key:
            return info.get("rmy_user_id")
    return None


def quick_complete_visit(cli, customer_id, response_text, visited_by=None,
                         vtype=RMY_VISIT_TYPE_DEFAULT, next_follow_date="") -> dict:
    """快速回访（已回访）+ 可选创建回访计划。返回睿美云原始响应 dict。"""
    body1 = {
        "customerId": customer_id,
        "visitedBy": visited_by,
        "planContentVos": [{"response": response_text or "已完成", "type": "81", "visitType": vtype}],
    }
    r1 = cli.post("/api/v1/tpos/visit/quick-complete-visit", json=body1)
    if next_follow_date and isinstance(next_follow_date, str) and next_follow_date[:4].isdigit():
        body2 = {
            "customerId": customer_id,
            "planContentVos": [{
                "type": "81",
                "visitDate": next_follow_date,
                "day": 1,
                "userId": [visited_by] if visited_by else [],
                "content": response_text or "",
            }],
        }
        cli.post("/api/v1/tpos/visit/create-visit", json=body2)
    return r1


def push_visit_status(cli, member, status, staff, dry_run=False) -> dict:
    """高层封装：搜索客户 -> 写回访状态。返回 {'raw':..., 'neuron_cus_id':...}。"""
    nid = search_customer_by_vip(cli, str(member))
    if dry_run or not nid:
        return {
            "raw": {"code": 0 if dry_run else -1,
                    "msg": "dry_run" if dry_run else "客户未匹配"},
            "neuron_cus_id": nid,
        }
    text = STATUS_TO_TEXT.get(status, status)
    raw = quick_complete_visit(cli, nid, text, visited_by=staff)
    return {"raw": raw, "neuron_cus_id": nid}


def get_visit_records(cli, neuron_cus_id=None, member=None, n=5) -> list:
    """拉取客户历史回访记录（已回访）。"""
    if neuron_cus_id is None and member:
        neuron_cus_id = search_customer_by_vip(cli, str(member))
    if not neuron_cus_id:
        return []
    body = {"page": 1, "size": max(n, 1), "customerId": neuron_cus_id, "visitedFlag": ["2"]}
    r = cli.post("/api/v1/tpos/visit/get-visit-page", json=body)
    if r.get("code") != 10000:
        return []
    d = r.get("data")
    return (d.get("records") if isinstance(d, dict) else None) or []


# ============================ 其他兼容函数（旧脚本未强制调用，给合理默认实现） ============================
def info_sync_remark(cli, customer_id, remark) -> dict:
    """同步档案备注。"""
    return cli.post("/api/v1/tpos/customer/update-remark",
                    json={"customerId": customer_id, "remark": remark})


def rmy_write(cli, path: str, json=None) -> dict:
    return cli.post(path, json=json)


def paginate_get(cli, path: str, params=None, size=500, max_pages=50) -> list:
    out, page = [], 1
    while page <= max_pages:
        p = dict(params or {})
        p.update({"page": page, "size": size})
        d = cli.get(path, params=p)
        recs = (d.get("data") or {}).get("records") or []
        if not recs:
            break
        out.extend(recs)
        total = (d.get("data") or {}).get("total", 0)
        if page * size >= total:
            break
        page += 1
    return out


def paginate_post(cli, path: str, json=None, size=500, max_pages=50) -> list:
    out, page = [], 1
    while page <= max_pages:
        body = dict(json or {})
        body.update({"page": page, "size": size})
        d = cli.post(path, json=body)
        recs = (d.get("data") or {}).get("records") or []
        if not recs:
            break
        out.extend(recs)
        total = (d.get("data") or {}).get("total", 0)
        if page * size >= total:
            break
        page += 1
    return out


class IdempotentLog:
    """简单的幂等日志（文件 key -> 记录）。"""

    def __init__(self, path):
        self.path = Path(path)
        self._data = {}
        if self.path.exists():
            try:
                self._data = json.loads(self.path.read_text(encoding="utf-8"))
            except Exception:
                self._data = {}

    def seen(self, key) -> bool:
        return key in self._data

    def mark(self, key, value=None):
        self._data[key] = value or {"at": time.strftime("%Y-%m-%d %H:%M:%S")}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self._data, ensure_ascii=False, indent=2), encoding="utf-8")


# ============================ 签名底层（供测试 / 审计） ============================
def _generate_nonce(ts=None) -> str:
    """生成 1 分钟内全局唯一的随机串：主机标识 + 进程号 + 强随机。

    加固点：原实现为 md5(ts+monotonic_ns)[:16]，多进程 / 多机器并发时存在碰撞
    风险，会被睿美云拒绝（nonce 1 分钟内不可重复）。改为 hostname 摘要 + pid +
    secrets 强随机，保证跨机器、跨进程唯一。
    """
    host = socket.gethostname() or "host"
    host_tag = hashlib.md5(host.encode()).hexdigest()[:4]
    return f"{host_tag}{os.getpid():x}{secrets.token_hex(8)}"


def _build_sign_string(ts: str, nonce: str, template: str = DEFAULT_SIGN_TEMPLATE) -> str:
    return template.format_map({"ts": ts, "timestamp": ts, "nonce": nonce})


def _private_key_sign(priv_key, sign_data: str) -> str:
    sig = priv_key.sign(sign_data.encode("utf-8"), padding.PKCS1v15(), hashes.SHA256())
    return base64.b64encode(sig).decode("ascii")


def _serialize_body(obj) -> str:
    return json.dumps(obj, ensure_ascii=False)


def _generate_auth_headers(account: str, priv_key, template: str = DEFAULT_SIGN_TEMPLATE) -> dict:
    ts = str(_now_ts())          # 带服务器时钟补偿
    nonce = _generate_nonce(ts)
    sign = _private_key_sign(priv_key, _build_sign_string(ts, nonce, template))
    return {
        "tpos-account": account,
        "tpos-timestamp": ts,
        "tpos-nonce-str": nonce,
        "tpos-sign": sign,
        "Content-Type": "application/json",
    }


# ============================ 自测 ============================
def smoke_test(base_url=None, account=None, private_key_b64=None) -> dict:
    """连通性自测（不写数据）。"""
    cli = RmyClient(base_url, account, private_key_b64)
    if not cli.base_url:
        return {"ok": False, "msg": "RMY_BASE_URL 未配置"}
    if not cli._key:
        return {"ok": False, "msg": "RMY_PRIVATE_KEY 未配置"}
    try:
        data = cli.get("/api/v1/tpos/customer/customer-search", params={"keyword": "测试"})
        return {"ok": True, "code": data.get("code"), "msg": data.get("msg")}
    except Exception as e:
        return {"ok": False, "msg": str(e)}


def _self_test():
    """模块内自检（签名算法正确性，无需网络）。"""
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import hashes as _h
    k = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    sd = _build_sign_string("1700000000", "abc123")
    sig = _private_key_sign(k, sd)
    k.public_key().verify(base64.b64decode(sig), sd.encode(), padding.PKCS1v15(), _h.SHA256())
    print("✅ 签名自检通过（RSA PKCS#1 v1.5 SHA256）")


if __name__ == "__main__":
    _self_test()
    print("base_url:", os.environ.get("RMY_BASE_URL", "(未配置)"))
    print("account :", os.environ.get("RMY_ACCOUNT", "boss"))
