#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
拉取睿美云官方 MCP 的工具清单 + readQueryMcpDocs 返回值文档，生成脱敏后的函数清单。

用法：
    python3 scripts/fetch_official_mcp_docs.py

凭证只从 ~/.workbuddy/mcp.json 的 mcpServers.rmy 读取，不打印、不写入生成物。
🔴 安全：readQueryMcpDocs 的「函数返回值」是**真实业务数据样例**（含客户姓名/订单号/id），
   本脚本只提取字段名（key），绝不写入任何值。

产物：
    references/official_mcp_functions.md    人读：按业务域的函数速查表
    references/official_mcp_functions.json  机读：完整契约（函数名/描述/参数/返回字段名）
"""
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CFG_PATH = Path.home() / ".workbuddy" / "mcp.json"
OUT_MD = ROOT / "references" / "official_mcp_functions.md"
OUT_JSON = ROOT / "references" / "official_mcp_functions.json"

# 写操作 / 运维类：绝不自动调用，仅登记
WRITE_TOOLS = {"markManualOrder", "restoreWxByVipNums", "unbindWxByVipNums"}
SELF_TOOLS = {"readQueryMcpDocs"}

# 业务域归类：按顺序匹配，先匹配具体动作再匹配对象
DOMAIN_RULES = [
    ("治疗 / 划扣", ["Treatment"]),
    ("回访", ["Visit"]),
    ("咨询", ["Consult"]),
    ("接待", ["Reception"]),
    ("预约", ["Bespeak"]),
    ("报备", ["Preparation"]),
    ("开发计划", ["DevPlan"]),
    ("订单 / 收银 / 缴费", ["Billing", "Payment", "ManualOrder", "Order"]),
    ("库存 / 出入库", ["Storage", "OutInventory", "InInventory", "Inventory"]),
    ("项目 / 套餐 / 物料 / 销售项", ["Project", "Package", "Material", "SaleItem"]),
    ("员工 / 组织 / 岗位 / 部门", ["User", "Dept", "Role"]),
    ("企微 / 录音 / ASR / 皮肤检测", ["WeChat", "Conversation", "Recording", "SkinDetection"]),
    ("统计 / 每日小结", ["Statistics", "DailySummary"]),
    ("客户档案 / 标签 / 线索", ["Customer", "Label", "Clue"]),
    ("账号绑定 / 运维写入", ["restoreWx", "unbindWx"]),
]
FALLBACK_DOMAIN = "其它 / 运维"


def classify(name):
    for domain, keys in DOMAIN_RULES:
        if any(k.lower() in name.lower() for k in keys):
            return domain
    return FALLBACK_DOMAIN


def collect_keys(obj, acc):
    """只收集 key，绝不取 value —— 这是脱敏的关键。"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, str):
                acc.append(k)
            collect_keys(v, acc)
    elif isinstance(obj, list):
        for v in obj[:3]:
            collect_keys(v, acc)


def rpc(url, headers, method, params=None, rid=1, notify=False, timeout=180):
    body = {"jsonrpc": "2.0", "method": method}
    if not notify:
        body["id"] = rid
    if params is not None:
        body["params"] = params
    r = requests.post(url, json=body, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r


def parse_json_or_sse(r):
    txt = r.text
    if "text/event-stream" in r.headers.get("Content-Type", ""):
        txt = "\n".join(l[5:].strip() for l in txt.splitlines() if l.startswith("data:"))
    for line in txt.splitlines():
        if line.strip().startswith("{"):
            try:
                return json.loads(line)
            except Exception:
                pass
    return json.loads(txt)


def fetch():
    cfg = json.loads(CFG_PATH.read_text(encoding="utf-8"))
    rmy = cfg["mcpServers"]["rmy"]
    url = rmy["url"]
    h = dict(rmy.get("headers", {}))
    h.update({"Content-Type": "application/json",
              "Accept": "application/json, text/event-stream"})

    init = rpc(url, h, "initialize", {
        "protocolVersion": "2024-11-05", "capabilities": {},
        "clientInfo": {"name": "workbuddy-mcp-doc-builder", "version": "1.0"}}, rid=1)
    protocol = parse_json_or_sse(init).get("result", {}).get("protocolVersion", "")
    sid = init.headers.get("Mcp-Session-Id")
    if sid:
        h["Mcp-Session-Id"] = sid
    rpc(url, h, "notifications/initialized", notify=True)

    tools = parse_json_or_sse(rpc(url, h, "tools/list", {}, rid=2))["result"]["tools"]
    docs_raw = parse_json_or_sse(rpc(url, h, "tools/call",
                                     {"name": "readQueryMcpDocs", "arguments": {}}, rid=3))
    texts = [c.get("text", "") for c in docs_raw.get("result", {}).get("content", [])
             if c.get("type") == "text"]
    groups = json.loads("\n".join(texts))
    return url, protocol, tools, groups


def build():
    url, protocol, tools, groups = fetch()

    funcs = {}
    for t in tools:
        props = (t.get("inputSchema") or {}).get("properties") or {}
        params = [{"name": k, "desc": str(v.get("description", ""))} for k, v in props.items()]
        funcs[t["name"]] = {
            "name": t["name"], "description": t.get("description", ""),
            "domain": classify(t["name"]), "view": [], "params": params,
            "return_fields": [], "in_tools": True, "in_docs": False,
            "is_write": t["name"] in WRITE_TOOLS, "is_self": t["name"] in SELF_TOOLS,
        }

    group_index = []
    for g in groups:
        names = g.get("具有相同返回值的函数名称", []) or []
        keys = []
        collect_keys(g.get("函数返回值", []), keys)
        # 去重保序
        seen, fields = set(), []
        for k in keys:
            if k not in seen:
                seen.add(k)
                fields.append(k)
        group_index.append({"names": [f.get("name", "") for f in names], "fields": fields})
        for f in names:
            n = f.get("name", "")
            if not n:
                continue
            if n not in funcs:
                funcs[n] = {"name": n, "description": f.get("description", ""),
                            "domain": classify(n), "view": [], "params": [],
                            "return_fields": [], "in_tools": False, "in_docs": True,
                            "is_write": False, "is_self": False}
            funcs[n]["in_docs"] = True
            if f.get("description"):
                funcs[n]["description"] = f["description"]
            funcs[n]["view"] = f.get("函数视角", []) or []
            dparams = [{"name": p.get("参数名称", ""), "desc": p.get("参数说明", "")}
                       for p in (f.get("函数参数") or [])]
            if dparams:
                funcs[n]["params"] = dparams
            funcs[n]["return_fields"] = fields

    ordered = sorted(funcs.values(), key=lambda x: (x["domain"], x["name"]))
    payload = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "endpoint": url,
        "protocol_version": protocol,
        "tool_count": len(tools),
        "doc_group_count": len(groups),
        "function_count": len(ordered),
        "write_tools": sorted(WRITE_TOOLS),
        "self_tools": sorted(SELF_TOOLS),
        "safety": "只保留接口契约；返回值示例中的真实业务数据值已全部丢弃，仅保留字段名",
        "group_index": group_index,
        "functions": ordered,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    domains = {}
    for f in ordered:
        domains.setdefault(f["domain"], []).append(f)

    md = []
    md.append("# 睿美云官方 MCP 函数清单（自动生成 · 已脱敏）\n")
    md.append(f"> **生成**：`scripts/fetch_official_mcp_docs.py`｜{payload['generated_at']}  \n"
              f"> **端点**：`{url}`｜协议 `{protocol}`  \n"
              f"> **规模**：`tools/list` {len(tools)} 个工具、`readQueryMcpDocs` {len(groups)} 组返回值文档、"
              f"合并去重 **{len(ordered)} 个函数**。  \n"
              "> 🔴 **脱敏声明**：`readQueryMcpDocs` 的返回示例含真实客户姓名/订单号/金额/id，"
              "本文件**只保留字段名，不保留任何值**；原始响应不落盘。  \n"
              "> 调用方式与凭证获取见 `official_mcp.md`；TPOS REST 全量接口见 `api_capability_map.md`。\n")
    md.append("## 1. 汇总\n")
    md.append("| 业务域 | 函数数 | 其中写操作 |\n|---|---:|---:|")
    for d, fs in domains.items():
        md.append(f"| {d} | {len(fs)} | {sum(1 for f in fs if f['is_write'])} |")
    md.append(f"| **合计** | **{len(ordered)}** | **{sum(1 for f in ordered if f['is_write'])}** |\n")

    md.append("## 2. 按业务域速查\n")
    md.append("> `入参` 来自 MCP 的 `inputSchema` / 文档参数表；`返回字段` 只列前 8 个，"
              "完整字段见 `official_mcp_functions.json` 的 `group_index`。  \n"
              "> `📖` 查询 / `✍️` 写入 / `🔧` 自省。\n")
    for i, (d, fs) in enumerate(domains.items(), 1):
        md.append(f"\n### 2.{i} {d}（{len(fs)}）\n")
        md.append("| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |\n|---|---|---|---|---|---|---|")
        for f in fs:
            kind = "✍️" if f["is_write"] else ("🔧" if f["is_self"] else "📖")
            params = ", ".join(f"`{p['name']}`" for p in f["params"]) or "—"
            view = "/".join(v.replace("以", "").replace("的问题", "").replace("问题", "")
                            for v in f["view"]) or "—"
            fields = ", ".join(f["return_fields"][:8]) or "—"
            flags = []
            if f["is_write"]:
                flags.append("🔴 写操作，需审批")
            if not f["in_tools"]:
                flags.append("⚠️ 文档有、tools/list 未暴露")
            if not f["in_docs"]:
                flags.append("⚠️ 无返回值文档")
            desc = f["description"].replace("|", "\\|")[:120]
            md.append(f"| {kind} | `{f['name']}` | {desc} | {params} | {view} | {fields} | "
                      f"{'；'.join(flags) or '✅'} |")

    md.append("\n## 3. 写操作（🔴 审批门控，绝不自动调用）\n")
    md.append("| 函数 | 说明 | 限制 |\n|---|---|---|")
    for f in ordered:
        if f["is_write"]:
            md.append(f"| `{f['name']}` | {f['description'].replace('|','\\|')[:200]} | "
                      "修改线上数据，需睿美云开通权限 + 李刚明确确认 |")
    md.append("\n> 官方 MCP 的写操作与 TPOS REST 写接口是**两套独立的门控**，"
              "不要因为 REST 侧验证过就自动放行 MCP 写操作。\n")

    md.append("\n## 4. 与 TPOS REST 通道的对照\n")
    md.append("| 能力 | 官方 MCP 函数（示例） | REST 接口 | 结论 |\n|---|---|---|---|")
    md.append("| 客户搜索 | `getCustomerIdByKeyword(s)` / `getCustomerInfo` | `GET /customer/customer-search` | REST 可控性更好 |\n"
              "| 客户详情 | `getCustomerInfoById` | `GET /customer/customer-by-id` | **客户明细一律走 REST**（注意事项 6） |\n"
              "| 订单/开单 | `getBillingInfoByDate` / `getBillingInfoByCustomerId` | `GET /order/billing-page` | REST 可分页、可跨门店 |\n"
              "| 缴费 | `getPaymentByDate` / `getPaymentByCustomerId` | `POST /report/cashier-record-page` | REST 才有完整收银口径 |\n"
              "| 治疗/划扣 | `getTreatmentByDate` / `getTreatmentByCustomerId` | `GET /treat/treated-page-review` | REST 才有 `deductUserName` 执行人 |\n"
              "| 回访 | `getVisitInfoByDate` / `getVisitInfoByCustomerId` | `POST /visit/get-visit-page` | REST 才能按 `visitedFlag` 精确筛待回访 |\n"
              "| 咨询/接待/预约/报备 | `getConsultInfoByDate`、`getReceptionWithDate`、`getCustomerBespeakByDate`、`getCustomerPreparationWithDate` | `consultation/page`、`reception/*`、`cusbespeak/*`、`preparation/*` | 按字段需求择一 |\n"
              "| 员工/部门/岗位 | `getAllUser`、`getDeptByName`、`getRoleByName` | `user/get-page`、`basic/dept-tree`、`role/getRoleListV2` | 等价 |\n"
              "| 项目/套餐/物料/库存 | `getAllProjectNames`、`getPackageInfoByName`、`getAllMaterial`、`getStorageInfosByDate` | `basic/*-page`、`inventory/*-page` | REST 字段更全 |\n"
              "| 企微聊天/录音/ASR | `getWeChatMessage`、`getRecordingByDate`、`getConversationByCustomerId` | `wechat/message/*` | MCP 封装更贴近语义检索 |\n")
    md.append("🔴 **注意事项 6 仍有效**：`getTreatmentByCustomerId`、`getBillingInfoByCustomerId`、"
              "`getVisitInfoByCustomerId`、`getConsultInfoByCustomerId`、`getCustomerReceptionByCustomerId`、"
              "`getDevPlanInfoByCustomerId` 这 6 个客户维度函数实测一律返回「没有查到…」，"
              "**不要用它们推断客户没有数据**。本次清单新增的 `...ByCustomerIdList` 批量版未实测，"
              "首次使用前须用已知有数据的客户验证。\n")

    md.append("\n## 5. 复跑方法\n")
    md.append("```bash\npython3 scripts/fetch_official_mcp_docs.py\n```\n")
    md.append("凭证读 `~/.workbuddy/mcp.json` 的 `mcpServers.rmy`（`appKey` 不入版本库）；"
              "脚本走 streamable HTTP（POST JSON-RPC），已验证该端点 **不支持旧 SSE**（GET 返回 405）。\n")

    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"tools/list: {len(tools)} 个工具")
    print(f"readQueryMcpDocs: {len(groups)} 组 / 合并去重 {len(ordered)} 个函数")
    print(f"已生成 {OUT_MD.name} ({OUT_MD.stat().st_size} 字节)")
    print(f"已生成 {OUT_JSON.name} ({OUT_JSON.stat().st_size} 字节)")
    print("脱敏：仅保留返回字段名，未写入任何业务数据值")


if __name__ == "__main__":
    try:
        build()
    except Exception as e:
        print("拉取失败:", type(e).__name__, str(e)[:300], file=sys.stderr)
        sys.exit(1)
