#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TPOS 只读接口生产抽样（可重复执行）：只发 GET / POST-查询，绝不触发任何写接口。
不打印任何客户数据，只记录 code / msg / 耗时 / 返回规模。
用法：python3 scripts/probe_readonly.py [结果JSON路径]
凭证从 ~/.workbuddy/secrets/ruimei_tpos.json 或 RMY_* 环境变量读取，不入版本库。
"""
import importlib.util, json, time, sys
from datetime import datetime, timedelta

P = "/Users/mac/.workbuddy/skills/ruimeiyun-openapi/references/rmy_client.py"
spec = importlib.util.spec_from_file_location("rmy_client", P)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
cli = m.RmyClient()

now = datetime.now()
start = (now - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
end = now.strftime("%Y-%m-%d %H:%M:%S")

CASES = [
    ("门店清单",            "GET",  "/api/v1/tpos/common/tenantList",                       {}, None),
    ("客户搜索",            "GET",  "/api/v1/tpos/customer/customer-search",               {"keyword": "测试", "page": 1, "size": 1}, None),
    ("客户详情",            "GET",  "/api/v1/tpos/customer/customer-by-id",                {"customerId": "1"}, None),
    ("部门树",              "GET",  "/api/v1/tpos/basic/dept-tree",                        {"tenantId": "1"}, None),
    ("在职员工",            "GET",  "/api/v1/tpos/user/get-page",                          {"tenantId": "1", "page": 1, "size": 1, "jobStatus": "false"}, None),
    ("岗位列表",            "GET",  "/api/v1/tpos/role/getRoleListV2",                     {"tenantId": "1", "page": 1, "size": 1}, None),
    ("回访类型",            "GET",  "/api/v1/tpos/visit/get-visit-type",                   {"tenantId": "1"}, None),
    ("回访方式",            "GET",  "/api/v1/tpos/visit/get-visit-way-type",               {"tenantId": "1"}, None),
    ("回访分页(待回访)",    "POST", "/api/v1/tpos/visit/get-visit-page",                   {"page": 1, "size": 1, "visitedFlag": ["1"]}, None),
    ("回访模板分类",        "GET",  "/api/v1/tpos/visit/visit-template-type",              {"tenantId": "1"}, None),
    ("订单列表",            "GET",  "/api/v1/tpos/order/billing-page",                    {"tenantId": "", "page": 1, "size": 1}, None),
    ("收银记录初始化",      "GET",  "/api/v1/tpos/report/cashier-record-init",             {"tenantId": "1"}, None),
    ("收银记录报表",        "POST", "/api/v1/tpos/report/cashier-record-page",             {"tenantId": "1", "current": 1, "limit": 1, "startTime": start, "endTime": end}, None),
    ("治疗分页(近7天)",     "GET",  "/api/v1/tpos/treat/treated-page-review",              {"tenantId": "1", "page": 1, "size": 1, "treatTimeStart": start, "treatTimeEnd": end}, None),
    ("项目分页",            "GET",  "/api/v1/tpos/basic/project-page",                    {"tenantId": "1", "page": 1, "size": 1}, None),
    ("卡券分页",            "GET",  "/api/v1/tpos/coupon/coupon-page",                    {"tenantId": "1", "page": 1, "size": 1}, None),
    ("入库分页",            "GET",  "/api/v1/tpos/inventory/storage-page",                {"tenantId": "1", "page": 1, "size": 1}, None),
    ("预约分页",            "GET",  "/api/v1/tpos/cusbespeak/get-page",                   {"tenantId": "1", "page": 1, "size": 1}, None),
    ("字典",                "GET",  "/api/v1/tpos/sysdict/dictlist",                      {"tenantId": "1", "code": "test"}, None),
    ("咨询分页",            "POST", "/api/v1/tpos/consultation/page",                     {"tenantId": "1", "page": 1, "size": 1}, 45),
    # 文档存疑项：只用 GET 试调（只读安全），验证路径/方法是否真的存在
    ("开发计划(存疑)",      "GET",  "/api/v1/tpos/customer/get-all-plan",                 {"customerId": "1"}, None),
    ("客户部分标签(存疑)",  "GET",  "/api/v1/tpos/customer/part-label-list",              {"tenantId": "1"}, None),
    ("接诊工具(存疑)",      "GET",  "/api/v1/tpos/consultation/acceptance-tool",          {"tenantId": "1"}, None),
    ("可购买权益卡(存疑)",  "GET",  "/api/v1/tpos/basic/get-can-buy-equity-card-list",     {"tenantId": "1"}, None),
    ("权益卡详情(存疑)",    "GET",  "/api/v1/tpos/basic/get-equity-card-detail",           {"tenantId": "1"}, None),
]


def verdict(d):
    if d.get("_error"):
        return "NETWORK"
    c = d.get("code")
    if c in (10000, 10001):
        return "OK"
    msg = str(d.get("msg") or "")
    if c in (401, 403) or any(k in msg for k in ("鉴权", "签名", "未授权", "timestamp", "tpos-")):
        return "AUTH"
    if c in (20002, 20004, 18000, 18001, 20001, 20003, 10002, 10003, 500):
        return "PARAM"
    return "OTHER"


def scale_of(d):
    data = d.get("data")
    if isinstance(data, dict):
        for k in ("records", "result", "list"):
            if isinstance(data.get(k), list):
                return f"{k}={len(data[k])}"
        return "dict"
    if isinstance(data, list):
        return f"list={len(data)}"
    return "-"


rows = []
for label, method, path, args, timeout in CASES:
    cli.timeout = timeout or 15
    t0 = time.time()
    try:
        d = cli.get(path, params=args) if method == "GET" else cli.post(path, json=args, retry=False)
    except Exception as e:
        d = {"code": None, "msg": str(e), "_error": type(e).__name__}
    sec = round(time.time() - t0, 2)
    v = verdict(d)
    row = dict(label=label, method=method, path=path, code=d.get("code"),
               msg=str(d.get("msg") or "")[:60], verdict=v, sec=sec,
               scale=scale_of(d))
    rows.append(row)
    print(f"{v:8s} | {label:20s} | {method:4s} | code={str(row['code']):6s} | {row['scale']:12s} | {sec:5.2f}s | {row['msg']}")

out_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/rmy_probe_result.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({"at": now.strftime("%Y-%m-%d %H:%M:%S"),
               "base_url": m.RMY_BASE_URL, "account": m.RMY_ACCOUNT,
               "window": [start, end], "rows": rows}, f, ensure_ascii=False, indent=2)

print("\n=== 汇总 ===")
from collections import Counter
print(Counter(r["verdict"] for r in rows))
print(f"结果写入 {out_path}")
