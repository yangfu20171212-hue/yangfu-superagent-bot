#!/usr/bin/env python3
"""睿美云 TPOS 开放接口 —— 本地 stdio MCP Server（RSA 私钥体系）

- 凭据：~/.workbuddy/secrets/ruimei_tpos.json（权限 600，不参与 skill 的 iCloud 同步）
- 客户端：同技能 references/rmy_client.py（含重试/退避/服务器时钟补偿/nonce 加固）
- 覆盖：6 个内置高频工具 + rmy_call 通用透传（可调用全部 210 个 TPOS 接口）
- 安全：rmy_quick_visit 为写操作，会真实写入睿美云，调用前请确认

启动（由 MCP 客户端通过 stdio 拉起，勿手动运行）：
    python3 rmy_mcp_server.py

依赖：mcp>=2.0, requests, cryptography
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

# 让脚本能 import 同技能 references 目录下的 rmy_client
HERE = Path(__file__).resolve().parent
REF_DIR = HERE.parent / "references"
if str(REF_DIR) not in sys.path:
    sys.path.insert(0, str(REF_DIR))

import rmy_client  # noqa: E402
from mcp.server import MCPServer  # noqa: E402

app = MCPServer(
    name="ruimei-tpos",
    instructions=(
        "睿美云（realmerit）TPOS 开放接口。可查询客户、订单、回访、预约、库存等业务数据。"
        "内置高频工具；其余接口用 rmy_call 透传，路径形如 /api/v1/tpos/order/billing-page。"
        "rmy_quick_visit 为写操作，会真实写入睿美云，调用前需确认。"
    ),
)


def _dump(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, default=str)


def _cli() -> "rmy_client.RmyClient":
    return rmy_client.RmyClient()


def _wrap(data: dict) -> dict:
    """统一返回结构：响应分类信息 + 原始 data。"""
    info = rmy_client.classify_response(data)
    raw = data.get("data") if isinstance(data, dict) else None
    return {**info, "data": raw}


@app.tool(name="rmy_health", description="睿美云连通性自检：验证私钥签名、网络与接口授权（只读）。")
def rmy_health() -> str:
    return _dump(rmy_client.smoke_test())


@app.tool(
    name="rmy_search_customer",
    description="按关键字搜索客户（姓名/电话/档案号/会员号）。基于搜索引擎，新增档案有延迟；手机号可能对应多个档案。",
)
def rmy_search_customer(keyword: str) -> str:
    kw = (keyword or "").strip()
    if not kw:
        return _dump({"ok": False, "error": "keyword 不能为空"})
    recs = _cli().search_customer_raw(kw)
    return _dump({"ok": True, "count": len(recs), "records": recs})


@app.tool(name="rmy_get_customer", description="按睿美云客户 id（neuronCusId）查询客户详情。")
def rmy_get_customer(customer_id: str) -> str:
    cid = (customer_id or "").strip()
    if not cid:
        return _dump({"ok": False, "error": "customer_id 不能为空"})
    data = _cli().get("/api/v1/tpos/customer/customer-by-id", params={"customerId": cid})
    return _dump(_wrap(data))


@app.tool(name="rmy_visit_records", description="查询某客户的历史回访记录（已回访）。")
def rmy_visit_records(customer_id: str, limit: int = 5) -> str:
    recs = rmy_client.get_visit_records(_cli(), neuron_cus_id=(customer_id or "").strip(), n=int(limit or 5))
    return _dump({"ok": True, "count": len(recs), "records": recs})


@app.tool(
    name="rmy_quick_visit",
    description="【写操作·慎用】为客户快速创建一条「已回访」记录，可选创建下次回访计划。会真实写入睿美云。",
)
def rmy_quick_visit(customer_id: str, content: str, visited_by: str = "", next_follow_date: str = "") -> str:
    cid = (customer_id or "").strip()
    txt = (content or "").strip()
    if not cid or not txt:
        return _dump({"ok": False, "error": "customer_id 与 content 不能为空"})
    raw = rmy_client.quick_complete_visit(
        _cli(), cid, txt,
        visited_by=(visited_by or None),
        next_follow_date=next_follow_date or "",
    )
    return _dump(_wrap(raw))


@app.tool(
    name="rmy_call",
    description=(
        "通用透传：调用任意睿美云 TPOS 接口（覆盖全部 210 个接口）。"
        "path 形如 /api/v1/tpos/order/billing-page；"
        "params_json 为 GET query 的 JSON 字符串，body_json 为 POST body 的 JSON 字符串。"
        "GET 默认幂等可重试；POST 默认不重试以防重复写入，确需重试设 retry=true。"
    ),
)
def rmy_call(method: str, path: str, params_json: str = "", body_json: str = "", retry: bool = False) -> str:
    m = (method or "GET").upper()
    p = (path or "").strip()
    if m not in ("GET", "POST"):
        return _dump({"ok": False, "error": "method 仅支持 GET / POST"})
    if not p.startswith("/api/"):
        return _dump({"ok": False, "error": "path 需以 /api/ 开头"})
    try:
        params = json.loads(params_json) if params_json else {}
        body = json.loads(body_json) if body_json else {}
    except json.JSONDecodeError as exc:
        return _dump({"ok": False, "error": f"JSON 解析失败: {exc}"})
    data = _cli()._request(m, p, params=params, body=body, retry=bool(retry))
    return _dump(_wrap(data))


if __name__ == "__main__":
    app.run(transport="stdio")
