#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 references/ruimeiyun_api_full.md（飞书 wiki JVkQwr4eAisxvHkgv9TcOm45nsf 的本地快照）
生成 references/api_capability_map.md —— 按功能组织的接口速查地图。

文档更新后重跑本脚本即可再生成：
    python3 scripts/build_capability_map.py
"""
import re
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "references" / "ruimeiyun_api_full.md"
OUT = ROOT / "references" / "api_capability_map.md"

PATH_RE = re.compile(r"(/api/[A-Za-z0-9_/\-.]+)")
METHOD_RE = re.compile(r"\b(GET|POST|PUT|DELETE|PATCH|Post|Get|Put|Delete|post|get|put|delete)\b")

MODULE_MAP = {
    "客户相关（customer）": "客户 customer",
    "门店（common）": "门店 common",
    "回访（visit）": "回访 visit",
    "报备(preparation)": "报备 preparation",
    "员工（user）": "员工/组织 user",
    "卡券（coupon）": "卡券 coupon",
    "营销（marketing）": "营销 marketing",
    "积分（integral）": "积分 integral",
    "订单（order）": "订单/收银 order",
    "治疗（treat）": "治疗/划扣 treat",
    "照片（photo）": "照片 photo",
    "基础（basic）": "基础数据 basic",
    "字典（sysdict）": "字典 sysdict",
    "库存（inventory）": "库存 inventory",
    "预约（cusbespeak）": "预约 cusbespeak",
    "渠道（channel）": "渠道 channel",
    "运营媒体（web）": "运营媒体 web",
    "接待（reception）": "接待 reception",
    "咨询（consultation）": "咨询 consultation",
    "面诊（assessment）": "面诊 assessment",
    "病历（medical_record）": "病历 medical_record",
    "文件（file）": "文件 file",
    "报表（report）": "报表 report",
    "企微聊天记录": "企微聊天记录 wechat",
    "客户资产变更": "客户资产变更 assets",
    "问卷": "问卷 questionnaire",
    "工牌": "工牌/ASR smartworkcard",
}
MODULE_ORDER = list(MODULE_MAP.values()) + ["三方/其它"]

# 人工校正：路径 -> {func/method/module/note}
# 依据：文档原文 + SKILL.md 实战验证记录（注明来源）
OVERRIDES = {
    "/api/v1/tpos/visit/get-visit-page": dict(method="POST", note="文档标 POST；查待回访必须带 visitedFlag:[\"1\"]（注意事项 27h/28）"),
    "/api/v1/tpos/report/cashier-record-page": dict(func="收银记录（报表）", method="POST", note="31 天窗口上限；必须串行，并发会静默返 0 条（注意事项 14）"),
    "/api/v1/tpos/channel/getChannelPageInfo": dict(method="POST", note="文档写 Post（首字母大写）"),
    "/api/v1/tpos/treat/treated-page-review": dict(func="分页获取治疗数据 / 全店到店划扣明细", note="GET 不是 POST，路径在 /treat/ 不是 /visit/；唯一能取到 deductUserName 执行人的接口（注意事项 7/27i）"),
    "/api/v1/tpos/customer/get-all-plan": dict(note="🔴 2026-11-22 实测 GET 返回 code 10000 + 完整开发计划结构，接口已可用（旧注意事项 18「不存在」已更正）；首次对真实客户使用前仍需核对字段口径，见 api_live_probe.md §3.2"),
    "/api/v1/tpos/basic/getP/getProjectByType": dict(module="基础数据 basic", note="⚠️ 文档原文路径疑似笔误（getP 混入），用前须实测确认"),
    "/api/v1/tpos/basic/getProjectType": dict(module="基础数据 basic", note="全部项目分类查询（文档放在 treat 章节末尾，按功能归入基础数据）"),
    "/api/v1/tpos/visit/obsolete-visit": dict(func="作废回访", method="POST", module="回访 visit", note="contentId 即 planId；作废不可逆，批量前手工验证 1:1（注意事项 4）"),
    "/api/v1/tpos/basic/get-can-buy-equity-card-list": dict(func="可购买权益卡列表", module="基础数据 basic", note="🔴 实测 code 2001 未授权（GET→20002 not supported / POST→2001）；先找睿美云开通权限，方法疑为 POST，见 api_live_probe.md §3.4"),
    "/api/v1/tpos/basic/get-equity-card-detail": dict(func="权益卡详情", module="基础数据 basic", note="🔴 实测 code 2001 未授权，开通前不可用，见 api_live_probe.md §3.4"),
    "/api/v1/tpos/consultation/acceptance-tool": dict(func="接诊工具", module="咨询 consultation", note="🔴 实测 code 2001 未授权，开通前不可用，见 api_live_probe.md §3.4"),
    "/api/v1/tpos/customer/part-label-list": dict(func="客户部分标签", module="客户 customer", note="🔴 实测 code 2001 未授权，开通前不可用，见 api_live_probe.md §3.4"),
    "/api/v1/tpos/cusbespeak/get-page": dict(method="POST", note="🔴 服务端只收 POST（GET→20002 not supported）；customerId/手机号/专家ID 至少传一个，见 api_live_probe.md §3.3"),
    "/api/v1/tpos/order/add-balance-recharge": dict(func="余额充值（写入）", module="订单/收银 order", note="补遗接口：方法未标注；写操作需审批门控"),
    "/api/v1/tpos/order/add-billing-equity-card": dict(func="开单-权益卡（写入）", module="订单/收银 order", note="补遗接口：方法未标注；写操作需审批门控"),
    "/api/v1/tpos/order/add-deposit": dict(func="定金（写入）", module="订单/收银 order", note="补遗接口：方法未标注；写操作需审批门控"),
    "/api/v1/tpos/customer/transfer-pool": dict(note="员工可见动作，逐客户推企微通知且无法关闭；批量前必须沟通（注意事项 23）"),
    "/api/v1/tpos/customer/customer-by-id": dict(note="写操作后回查落库的指定接口；不返回 poolId，只有 poolName（注意事项 23）"),
    "/api/v1/tpos/order/billing-page": dict(note="忽略所有时间参数；size 上限 500；tenantId 传空串才跨门店（注意事项 7/14bis）"),
    "/api/v1/tpos/user/get-page": dict(note="jobStatus=False 才是在职；size 不是 limit（注意事项 12/13/16）"),
    "/api/v1/tpos/consultation/page": dict(note="tenantId 必填；响应慢需 ≥40s 超时；高价值字段 mainComplaint / consumptionStatus（注意事项 19）"),
    "/api/v1/tpos/customer/customer-search": dict(note="不能空搜；每客户手机可能多档；20 页硬顶，超 1 万条用 lastCustomerId 游标（注意事项 1/2/11/24）"),
    "/api/v1/tpos/visit/create-visit": dict(note="写读口径不对称：入参 type=码值、visitDate=字符串；回吐 type=中文、visitDate=毫秒戳（注意事项 28）"),
    "/api/v1/tpos/visit/complete-visit": dict(note="把待回访结清为已回访，response 写明清理原因可审计；规则不合并则重复计划还会再长（注意事项 27g）"),
    "/api/v1/tpos/visit/quick-complete-visit": dict(note="直接新增一条「已回访」记录；MCP 工具 rmy_quick_visit 同能力"),
    "/api/v1/tpos/preparation/add": dict(note="文档把 POST 误写为 `PSOT`；报备可不带客户 id 而用姓名+电话自动建档"),
    "/api/v1/tpos/visit/visit-template-data-type": dict(note="⚠️ 实测返回的是「该分类下的项目列表」而非模板；缺 typeId 会 20004（注意事项 27b）"),
    "/api/v1/tpos/visit/visit-template-content": dict(note="id 不匹配时返回 code:10000 + data:null，不报错（注意事项 27b）"),
    "/api/v1/tpos/customer/edit-customer-rolemanager": dict(note="⚠️ roleManagerId 取 config 的 id 还是 roleId 未实测，用前先测 1 条；userIdList 传空数组＝删除配置（注意事项 25）"),
    "/api/v1/tpos/basic/annual-card-detail": dict(func="年卡详情信息"),
    "/api/v1/tpos/integral/query-customer-growth-upgrade": dict(func="查询会员升级信息"),
    "/api/v1/tpos/marketing/appoint-card-page": dict(func="线上预约-名片管理（分页）"),
}

# 只出现在截图/说明文字中、没有正文契约的路径 → 附录
QUOTE_ONLY = {
    "/api/v1/tpos/yizhipai/uploadcustomerphoto": "截图 URL：皮肤检测图片上传接口的 Postman 示例，正文另定义为 /api/v1/tpos/skin_image/update_skin_file",
    "/api/v1/tpos/basic/package": "截图 URL 中 package - detail 被空格截断，正文真实路径为 /api/v1/tpos/basic/package-detail",
    "/api/v1/tpos/channel/channeltypeinfo": "截图 URL；正文加粗定义为 channelstypeinfo（多一个 s），两者差异未实测",
    "/api/v1/tpos/customer/check": "截图 URL 中 check - new - customer 被空格截断，正文真实路径为 check-new-customer",
    "/api/v1/tpos/wechat/message/cursorMessage": "正文推荐「查两人对话用此接口」，但未给出契约（参数/响应）；同族可用 messageList / cursorMessageInterList",
}

TASK_ROWS = [
    ("查客户主档 / 按手机或姓名搜客户", "GET", "/api/v1/tpos/customer/customer-search", "不能空搜；同名手机多档案，优先用 customerId"),
    ("按客户 id 查完整档案（含归属、会员等级）", "GET", "/api/v1/tpos/customer/customer-by-id", "写操作后回查落库的指定接口"),
    ("拉全量客户（>1 万条）", "GET", "/api/v1/tpos/customer/customer-search", "20 页硬顶，必须 lastCustomerId 游标 + page 恒为 1"),
    ("判断客户当前归属 / 企微在谁手里", "GET", "/api/v1/tpos/customer/customer-by-id", "用 sysUserName 与 wechatSysuserId，绝不用 wechatSysUserName"),
    ("改客户归属 / 换客户池", "POST", "/api/v1/tpos/customer/transfer-pool", "先 get-pool-info 拿 poolId，写入后 customer-by-id 回查；会推企微通知"),
    ("查客户可转入的池与咨询师名单", "GET", "/api/v1/tpos/customer/get-pool-info", "按客户建档门店返回；personalPool 按 (poolId,userName) 建索引"),
    ("查客户能否同步企微关系", "GET", "/api/v1/tpos/customer/customer-qw-info", "data.changeAllow=true 才可转企微关系"),
    ("判断客户是否新客（无消费无划扣）", "POST", "/api/v1/tpos/customer/check-new-customer", "手机号或客户 id 二选一"),
    ("查客户开单 / 消费 / 购买次数", "GET", "/api/v1/tpos/order/billing-page", "tenantId 传空串拿全部门店；忽略时间参数，本地按 createDate 过滤"),
    ("查收银记录（谁成交、谁服务、科室）", "POST", "/api/v1/tpos/report/cashier-record-page", "31 天窗口上限、必须串行；返回 data.result 不是 records"),
    ("查客户未划扣 / 剩余项目", "GET", "/api/v1/tpos/treat/untreated-page", "或 POST /treat/scrmTreatList {treatFlag:false}"),
    ("查客户已治疗 / 已划扣记录", "GET", "/api/v1/tpos/treat/already-treated-page", "真实执行次数看 treatCount，别信主档"),
    ("拉全店到店/治疗明细（按日期）", "GET", "/api/v1/tpos/treat/treated-page-review", "treatTimeStart/treatTimeEnd；客户端二次校验 treatmentTime；含 deductUserName"),
    ("拉客户回访记录 / 待回访清单", "POST", "/api/v1/tpos/visit/get-visit-page", "查待回访必须 visitedFlag:[\"1\"]；单窗口 1 万条硬顶，按时间分片"),
    ("新建回访计划", "POST", "/api/v1/tpos/visit/create-visit", "入参 type 用码值；缺 tenantId 会 20002"),
    ("把待回访结清为已回访", "POST", "/api/v1/tpos/visit/complete-visit", "response 写清原因，可审计；是治标不是治本"),
    ("直接新增一条已回访记录", "POST", "/api/v1/tpos/visit/quick-complete-visit", "MCP 工具 rmy_quick_visit 同能力"),
    ("作废回访（不可逆）", "POST", "/api/v1/tpos/visit/obsolete-visit", "contentId=planId；批量前手工验证 1:1 + 断点续传 + 对账"),
    ("查回访类型 / 方式 / 模板", "GET", "/api/v1/tpos/visit/get-visit-type", "另有 get-visit-way-type / visit-template-type / -data-type / -content"),
    ("查咨询记录（主诉、未成交信号）", "POST", "/api/v1/tpos/consultation/page", "tenantId 必填、超时 ≥40s；高价值字段 mainComplaint / consumptionStatus"),
    ("查预约 / 新增 / 改 / 确认 / 取消", "POST", "/api/v1/tpos/cusbespeak/get-page", "同族：add / update / confirm(PUT) / cancel(PUT)"),
    ("查客户接待 / 到店登记", "POST", "/api/v1/tpos/reception/reception_cus", "可用分诊人名单：GET reception/triagetouserlist"),
    ("查在职员工名册 / 部门树 / 岗位", "GET", "/api/v1/tpos/user/get-page", "jobStatus=False 才在职；另 basic/dept-tree、role/getRoleListV2"),
    ("查门店清单", "GET", "/api/v1/tpos/common/tenantList", "1=凯德 / 2=双楠 / 3=远大"),
    ("查客户卡券 / 发券 / 用券", "GET", "/api/v1/tpos/coupon/customer-coupon-page", "send-coupon / use-coupon / gift-coupon / receive-coupon"),
    ("查储值充值 / 抵扣 / 退款 / 转赠记录", "GET", "/api/v1/tpos/order/balance-recharge-page", "同族 -deduction / -refund / -transfer-page"),
    ("查客户权益卡", "GET", "/api/v1/tpos/order/billing-equity-card-page", "补遗：basic/get-can-buy-equity-card-list、get-equity-card-detail"),
    ("收银前查客户可用资产 / 抵扣 / 撤销", "GET", "/api/v1/tpos/order/get-customer-available-assets", "抵扣 POST deduct-assets，撤销 POST cancel-deduct-assets"),
    ("开单 / 订单退款", "POST", "/api/v1/tpos/order/add-billing-review", "退款 POST /order/refund；可操作订单项 GET /enable-billing"),
    ("三方小程序开单 / 退款", "POST", "/api/v1/tpos/order/add-order-external", "refund-order-external / refund-order-external-item"),
    ("治疗核销划扣 / 取消划扣 / 取消核销", "POST", "/api/v1/tpos/treat/treat-deduct-verify", "同族 cancel-deduct / cancel-verify；写操作需审批"),
    ("查项目/套餐/年卡/次卡/物料/供应商", "GET", "/api/v1/tpos/basic/project-page", "同构：-page 分页 / -type-tree 分类树 / -detail 详情"),
    ("查字典（按类型+门店）", "GET", "/api/v1/tpos/sysdict/dictlist", "枚举值统一入口"),
    ("查库存入库/出库/盘点", "GET", "/api/v1/tpos/inventory/storage-page", "同族 out-inventory-page / check-inventory-page + 详情 + 增改撤"),
    ("上传照片 / 皮肤检测图", "POST", "/api/v1/tpos/common/addPhoto", "另有 upload_customer_photo、skin_image/update_skin_file；查照片 GET common/photoPage"),
    ("查渠道 / 运营媒体", "GET", "/api/v1/tpos/channel/channelstypeinfo", "通过类型取列表 specificchannellist；运营媒体 POST channelWeb/getChannelWebPage-review"),
    ("查企微聊天记录", "POST", "/api/v1/tpos/wechat/message/messageList", "不分收发人用 cursorMessageInterList；cursor 分页"),
    ("查面诊 / 病历", "POST", "/api/v1/assessment/get-cus-assessment-page", "查询虽叫 get- 但方法是 POST；新增/确认/更新面诊同族；病历 medical-record/add、update、delete"),
    ("报备新增 / 查询 / 转交", "POST", "/api/v1/tpos/preparation/add", "查询也是 POST：get-preparation；转交 POST customer/update-customer-preparation-info"),
    ("查积分 / 成长值 / 会员升级", "GET", "/api/v1/tpos/integral/getCusIntegral", "明细 score-record-page；升级 query-customer-growth-upgrade"),
    ("查问卷 / 工牌 ASR 回传", "POST", "/api/v1/top/questionnaireCustomer/notYetList", "工牌 smartworkcard/customerList、callback、jellyCallback"),
    ("查客户资产变更 / 确认", "POST", "/api/v1/top/paymentAssetChange/paymentAssetChangeList", "明细 GET getOneRecord；确认 POST confirmAssetChange"),
    ("查客户返利 / 老带新 / 线索 / 标签", "POST", "/api/v1/tpos/customer/my-rebate-list", "同族 my-recommend-customer-list / customer-clue-list / customer-label-list"),
    ("上传文件", "POST", "/api/v1/tpos/file/upload", "通用文件入口"),
]

IRON_RULES = [
    ("鉴权", "4 个 Header 缺一不可；时间戳与服务器差 <1 分钟；正式环境按接口单独授权", "SKILL.md「核心约定」「注意事项 4」"),
    ("成功码", "不统一：code 10000 或 10001 都算成功，用 RmyClient.classify_response()，别硬编码 ==10000", "注意事项 12"),
    ("401 排查", "先核对文档里的路径 + HTTP 方法是否照抄，再怀疑账号未授权；不要盲试路径变体", "注意事项 4"),
    ("分页", "参数是 size 不是 limit；深分页会静默截断；按时间分片且单批 <1 万条；失败要重试+告警，不能用残缺数据", "注意事项 8/13/17"),
    ("写操作", "POST 默认不重试；任何写入前先 1-3 条手工验证，再批量；写入后用指定接口回查验落库", "内置容错 + 注意事项 23/28"),
    ("全量数据", "接口 total 有枚举上限，向下游报下界不报精确值；扫描数 > total = 数据污染，立即停手", "注意事项 8/9"),
    ("隐私", "咨询/客户接口的 phoneNumber 等字段不取不写；客户明细走直连通道，不用官方 MCP 客户维度接口", "注意事项 6/19"),
    ("字段口径", "归属看 sysUserName（当前）不看 relatedConsul（历史）；企微看 wechatSysuserId 不看昵称；主档消费次数可能为 0", "注意事项 9/15/20/21/25"),
]

# HTTP 方法是 POST，但业务语义是「查询」→ 不计入写接口审批门控
READ_POST = {
    "/api/v1/tpos/customer/my-rebate-list",
    "/api/v1/tpos/customer/my-rebate-customer-list",
    "/api/v1/tpos/customer/my-recommend-customer-list",
    "/api/v1/tpos/customer/customer-clue-list",
    "/api/v1/tpos/customer/customer-gold-list",
    "/api/v1/tpos/customer/customer-sign-search",
    "/api/v1/tpos/customer/check-new-customer",
    "/api/v1/tpos/visit/get-visit-page",
    "/api/v1/tpos/preparation/get-preparation",
    "/api/v1/tpos/integral/query-customer-growth-upgrade",
    "/api/v1/tpos/order/get-customer-billing-list",
    "/api/v1/tpos/order/get-cashierRecord-list",
    "/api/v1/tpos/order/get-customer-available-assets",
    "/api/v1/scrm/treatment/page",
    "/api/v1/tpos/treat/scrmTreatList",
    "/api/v1/tpos/basic/getProjectType",
    "/api/v1/tpos/basic/getP/getProjectByType",
    "/api/v1/tpos/cusbespeak/get-page",
    "/api/v1/tpos/cusbespeak/get-available-experts-schedule",
    "/api/v1/tpos/cusbespeak/getAppointCardList",
    "/api/v1/tpos/channel/getChannelPageInfo",
    "/api/v1/tpos/channelWeb/getChannelWebPage-review",
    "/api/v1/tpos/reception/reception_cus",
    "/api/v1/tpos/reception/scrm-check-in-config",
    "/api/v1/tpos/consultation/page",
    "/api/v1/assessment/get-cus-assessment-page",
    "/api/v1/tpos/report/cashier-record-page",
    "/api/v1/tpos/wechat/message/messageList",
    "/api/v1/tpos/wechat/message/cursorMessageInterList",
    "/api/v1/top/paymentAssetChange/paymentAssetChangeList",
    "/api/v1/top/questionnaireCustomer/notYetList",
    "/api/v1/top/questionnaireCustomer/page",
    "/api/v1/tpos/smartworkcard/customerList",
}

# 文档未标注方法、但语义明确是写 → 仍纳入写接口清单
SEMANTIC_WRITE_EXTRA = {
    "/api/v1/tpos/inventory/storage-add",
    "/api/v1/tpos/inventory/storage-update",
    "/api/v1/tpos/inventory/storage-undo",
    "/api/v1/tpos/inventory/outInventory-update",
    "/api/v1/tpos/inventory/outInventory-undo",
    "/api/v1/tpos/order/add-balance-recharge",
    "/api/v1/tpos/order/add-billing-equity-card",
    "/api/v1/tpos/order/add-deposit",
    "/api/v1/tpos/preparation/add",
}

# 语义不明确、不能按名字猜读写的接口
UNCERTAIN_SEMANTIC = {"/api/v1/tpos/consultation/acceptance-tool"}

# 2026-11-22 生产实测：code 2001「您无法访问该资源，请联系管理员开通！」
# 这类接口不是「方法没标」，是账号没权限，试调前必须先申请授权
NEED_AUTH = {
    "/api/v1/tpos/customer/part-label-list",
    "/api/v1/tpos/consultation/acceptance-tool",
    "/api/v1/tpos/basic/get-equity-card-detail",
    "/api/v1/tpos/basic/get-can-buy-equity-card-list",
}


def is_write(r):
    if r["path"] in SEMANTIC_WRITE_EXTRA:
        return True
    if r["path"] in READ_POST:
        return False
    return r["method"] in ("POST", "PUT", "DELETE", "PATCH")


def clean_title(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\*\*|\*|`|#", "", s)
    return re.sub(r"\s+", " ", s).strip().strip("：: ·")


def extract_params(lines, start, end):
    """从接口段落里抽必填参数：先定位表头列，再取数据行（兼容 md 表格与整行 HTML table）。"""
    state = {"req_col": None}
    params = []

    def handle(cells):
        if not cells or len(cells) < 2:
            return
        joined = " ".join(cells[:6])
        if re.search(r"参数名称|字段|Field|参数名", joined) and re.search(r"是否必|是否必须|必填|required", joined):
            for k, c in enumerate(cells[:6]):
                if re.search(r"是否必|必填|required", c):
                    state["req_col"] = k
                    break
            return
        if re.match(r"^[-: ]+$", "".join(cells)):
            return
        name = re.sub(r"[^A-Za-z0-9_]", "", cells[0].lstrip("\u2003 "))
        if not name or len(name) > 38 or name.lower() in ("参数名称", "字段", "field", "code", "data", "msg"):
            return
        rc = state["req_col"]
        is_req = bool(rc is not None and rc < len(cells)
                      and re.search(r"\btrue\b|^是$|必填|required", cells[rc], re.I))
        if is_req and name not in params:
            params.append(name)

    for j in range(start, min(end, start + 60)):
        l = lines[j].strip()
        if re.match(r"^#{1,4}\s", l):
            break
        if "<tr" in l:
            for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", l, re.S):
                cells = [re.sub(r"<[^>]+>", "", c).strip().strip("*").strip()
                         for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
                handle(cells)
        elif l.startswith("|") and "|" in l[1:]:
            handle([c.strip().strip("*").strip() for c in l.split("|")[1:-1]])
    return params[:6]


def main():
    lines = SRC.read_text(encoding="utf-8").splitlines()
    cur_mod, cur_iface = "", ""
    raw = []
    for i, ln in enumerate(lines):
        s = ln.strip()
        m1 = re.match(r"^#\s+(.*)", s)
        if m1 and not s.startswith("##"):
            cur_mod, cur_iface = clean_title(m1.group(1)), ""
            continue
        m2 = re.match(r"^#{2,4}\s+(.*)", s)
        if m2:
            cur_iface = clean_title(m2.group(1))
            continue
        flat = s.replace("**", "").replace("``", "").replace("`", "")
        paths = [p.rstrip("/.,;:)") for p in PATH_RE.findall(flat)]
        paths = [p for p in paths if not p.startswith("/api/file") and len(p) > 13]
        if not paths:
            continue
        no_path = PATH_RE.sub(" ", flat)
        no_path = re.sub(r"\bPSOT\b", "POST", no_path, flags=re.I)  # 文档笔误：报备新增写成 PSOT
        mm = METHOD_RE.search(no_path)
        method = mm.group(1).upper() if mm else ""
        # 文档另一种写法：「接口地址」与「请求方式」分成两行
        if not method:
            for k in range(i + 1, min(i + 5, len(lines))):
                nxt = lines[k].strip()
                if re.match(r"^#{1,4}\s", nxt) or PATH_RE.search(nxt.replace("`", "")):
                    break
                if "请求方式" in nxt:
                    m3 = re.search(r"\b(GET|POST|PUT|DELETE|PATCH|PSOT|Post|Get)\b", nxt, re.I)
                    if m3:
                        method = "POST" if m3.group(1).upper() == "PSOT" else m3.group(1).upper()
                    break
        is_quote = s.startswith("![") or bool(re.search(r"建议使用接口|的返回数据|报表返回数据", s))
        for p in paths:
            # 找本行所在标题的段落终点
            end = i + 1
            while end < len(lines) and not re.match(r"^#{1,4}\s", lines[end].strip()):
                end += 1
            raw.append(dict(line=i + 1, module=cur_mod, func=cur_iface, method=method,
                            path=p, required=extract_params(lines, i + 1, end), quote=is_quote))

    # 合并：优先正文定义 > 截图/说明引用；同路径保留信息最全者
    by_path = {}
    for r in raw:
        p = r["path"]
        if p in QUOTE_ONLY:
            continue
        if p not in by_path:
            by_path[p] = dict(r)
            continue
        old = by_path[p]
        if old["quote"] and not r["quote"]:      # 正文定义覆盖引用
            keep_req = old["required"]
            by_path[p] = dict(r)
            if not by_path[p]["required"]:
                by_path[p]["required"] = keep_req
            continue
        if r["quote"] and not old["quote"]:
            continue
        if not old["method"] and r["method"]:
            old["method"] = r["method"]
        if not old["required"] and r["required"]:
            old["required"] = r["required"]

    # 人工校正
    for p, fix in OVERRIDES.items():
        if p in by_path:
            by_path[p].update(fix)
        else:
            by_path[p] = dict(line=0, module=fix.get("module", "三方/其它"),
                              func=fix.get("func", p.rsplit("/", 1)[-1]),
                              method=fix.get("method", ""), path=p,
                              required=[], quote=False, note=fix.get("note", ""))

    def module_of(r):
        raw_mod = r["module"]
        if raw_mod in MODULE_MAP.values():      # OVERRIDES 已归好模块
            return raw_mod
        if raw_mod.startswith("补遗"):
            return "三方/其它"
        return MODULE_MAP.get(raw_mod, "三方/其它")

    groups = {}
    for r in by_path.values():
        groups.setdefault(module_of(r), []).append(r)
    for g in groups.values():
        g.sort(key=lambda x: (x["line"] == 0, x["line"]))

    total = sum(len(g) for g in groups.values())
    writes = [r for g in groups.values() for r in g if is_write(r)]
    unknown = [r for g in groups.values() for r in g if not r["method"]]

    out = []
    out.append("# 睿美云 TPOS 接口能力地图（按功能速查）\n")
    out.append(f"> **数据源**：飞书 wiki `JVkQwr4eAisxvHkgv9TcOm45nsf`《睿美云开放接口》的本地完整快照 "
               f"`references/ruimeiyun_api_full.md`（{len(lines)} 行）。  \n"
               f"> **生成**：`scripts/build_capability_map.py`（文档更新后重跑即可）｜更新于 {date.today().isoformat()}  \n"
               f"> **规模**：{total} 个接口（{len(writes)} 个写接口，{len(unknown)} 个文档未标注方法）；"
               f"另有 {len(QUOTE_ONLY)} 个仅出现在截图/说明里的存疑路径。  \n"
               "> **查阅顺序**：本文件定位接口 → `references/api_live_probe.md` 看生产实测差异 → "
               "`SKILL.md`「注意事项」看实战坑 → `references/ruimeiyun_api_full.md` 看完整字段契约 → "
               "`references/rmy_client.py` 发起调用。\n")
    out.append("## 0. 怎么用\n")
    out.append("1. 在 **第 1 节** 按「我要做什么」找到接口路径；\n"
               "2. 在 **第 3 节** 核对 HTTP 方法、关键参数、备注里的坑；\n"
               "3. 用 `RmyClient.get/post` 调用；涉及写入先过 **第 4 节** 审批门控；\n"
               "4. 字段不确定时，按表里的 `L<行号>` 直接跳到 `ruimeiyun_api_full.md` 对应行；\n"
               "5. 本文件只覆盖 **TPOS REST 直连**通道；若要走睿美云官方 MCP（appKey + `/ai/neuron-mcp`），"
               "见 `references/official_mcp.md`（配置/传输实测）与 `references/official_mcp_functions.md`"
               "（92 个函数清单，由 `readQueryMcpDocs` 实拉生成）；\n"
               "6. **文档与生产不一致时以实测为准**：见 `references/api_live_probe.md`（2026-11-22 只读实测，"
               "含 3 处推翻/补充文档结论）；可重跑 `scripts/probe_readonly.py` 复核。\n")

    out.append("\n## 1. 按任务找接口（高频反查表）\n")
    out.append("| 我要做什么 | 方法 | 首选接口 | 关键提醒 |\n|---|---|---|---|")
    for task, meth, path, note in TASK_ROWS:
        out.append(f"| {task} | `{meth}` | `{path}` | {note} |")

    out.append("\n## 2. 模块总览\n")
    out.append("| 模块 | 接口数 | 读 | 写 | 覆盖能力 |\n|---|---:|---:|---:|---|")
    MODULE_DESC = {
        "客户 customer": "建档/搜索/详情、返利、推荐、线索、标签、金币、客户池、企微归属、岗位负责人、新客判定",
        "门店 common": "门店清单",
        "回访 visit": "类型/方式/模板、计划分页、创建、完成、快速回访、作废",
        "报备 preparation": "新增/查询/转交报备人",
        "员工/组织 user": "员工名册、部门树、岗位列表",
        "卡券 coupon": "客户卡券查询、发放、使用、赠送、领取",
        "营销 marketing": "线上预约名片、图文消息",
        "积分 integral": "客户积分、积分/成长值分页、会员升级",
        "订单/收银 order": "开单/退款、费用单、订单消费、收银记录、储值四类流水、权益卡、资产抵扣、三方小程序开单",
        "治疗/划扣 treat": "未治疗/已治疗/全店治疗分页、核销划扣与撤销、手术间、治疗岗位、小程序我的治疗",
        "照片 photo": "七牛/外部图转存、上传、分页查询、皮肤检测上传",
        "基础数据 basic": "项目/套餐/年卡/次卡/物料/供应商/会员权益/会员规则 + 各自分类树与详情",
        "字典 sysdict": "按字典类型与门店取枚举",
        "库存 inventory": "入库/出库/盘点的分页、详情、新增、修正、撤销 + 仓库",
        "预约 cusbespeak": "新增/修改/确认/取消/分页、可选医生、专家排班、设备手术间、名片",
        "渠道 channel": "渠道类型、渠道列表、渠道信息",
        "运营媒体 web": "运营媒体信息",
        "接待 reception": "分诊人、新增接待、客户接待信息、扫码签到",
        "咨询 consultation": "新增/修改/查询咨询、接诊工具",
        "面诊 assessment": "历史面诊、新增、确认、更新",
        "病历 medical_record": "新增/修改/删除病历",
        "文件 file": "通用文件上传",
        "报表 report": "收银记录初始化、收银记录报表",
        "企微聊天记录 wechat": "单/双向聊天记录查询（cursor 分页）",
        "客户资产变更 assets": "变更列表、单条明细、确认变更",
        "问卷 questionnaire": "未填写问卷、客户问卷记录",
        "工牌/ASR smartworkcard": "当天接待客户、质检点/标签/ASR 回传、录音开始结束（见 full.md 补遗）",
        "三方/其它": "线上补遗接口与其它路径",
    }
    for mod in MODULE_ORDER:
        g = groups.get(mod, [])
        if not g:
            continue
        nw = sum(1 for r in g if is_write(r))
        out.append(f"| {mod} | {len(g)} | {len(g)-nw} | {nw} | {MODULE_DESC.get(mod,'—')} |")

    out.append("\n## 3. 逐模块接口清单\n")
    out.append("> `读写` 列按**业务语义**判定（不是看 HTTP 方法）：📖 只读 / ✍️ 写入 / ❓ 语义未定；"
               "**写入接口一律先手工验证再批量**（见第 4 节）。  \n"
               "> `L<数字>` = `ruimeiyun_api_full.md` 行号；`?` = 官方文档未标注 HTTP 方法（见第 5 节）；"
               "「补遗节」= 线上文档补入、旧快照缺失的接口。\n")
    for idx, mod in enumerate(MODULE_ORDER, 1):
        g = groups.get(mod, [])
        if not g:
            continue
        out.append(f"\n### 3.{idx} {mod}（{len(g)}）\n")
        out.append("| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |\n|---|---|---|---|---|---|")
        for r in g:
            meth = r["method"] or "?"
            kind = ("✍️" if is_write(r) else
                    ("❓" if meth == "?" and r["path"] in UNCERTAIN_SEMANTIC else "📖"))
            params = ", ".join(f"`{x}`" for x in r["required"]) or "—"
            note = r.get("note", "")
            loc = "补遗节" if (not r["line"] or r["line"] >= 11271) else f"L{r['line']}"
            note_txt = (note + "  " if note else "") + loc
            func = r["func"].replace("|", "\\|")
            out.append(f"| {func} | `{meth}` | `{r['path']}` | {kind} | {params} | {note_txt} |")

    excluded = sum(1 for g in groups.values() for r in g
                   if r["method"] in ("POST", "PUT", "DELETE", "PATCH") and not is_write(r))
    extra_w = sum(1 for g in groups.values() for r in g
                  if r["path"] in SEMANTIC_WRITE_EXTRA and r["method"] not in ("POST", "PUT", "DELETE", "PATCH"))
    out.append("\n## 4. 写接口清单（审批门控）\n")
    out.append(f"共 **{len(writes)}** 个**语义写**接口（按业务效果判定：POST 但只做查询的 {excluded} 个已排除；"
               f"文档未标方法但语义为写的 {extra_w} 个已纳入）。铁律：`RmyClient` 对 POST 默认不重试（防重复写入）；"
               "任何批量写入前先 1–3 条手工验证 1:1 生效，写入后必须用指定读接口回查；"
               "涉及员工可见动作（`transfer-pool` 等）须先与业务方沟通。\n")
    out.append("| 模块 | 方法 | 路径 | 功能 |\n|---|---|---|---|")
    for mod in MODULE_ORDER:
        for r in groups.get(mod, []):
            if is_write(r):
                out.append(f"| {mod} | `{r['method'] or '?'}` | `{r['path']}` | {r['func'].replace('|','\\|')} |")

    out.append("\n## 5. 文档未标注方法 / 存疑路径（用前必须实测）\n")
    out.append(f"### 5.1 文档未标注 HTTP 方法（{len(unknown)} 个）\n")
    out.append("| 路径 | 功能 | 建议 |\n|---|---|---|")
    for r in sorted(unknown, key=lambda x: x["path"]):
        if r["path"] in NEED_AUTH:
            hint = "🔴 实测 code 2001 未授权：先找睿美云开通该接口权限，再测方法（api_live_probe.md §3.4）"
        elif r["path"] in UNCERTAIN_SEMANTIC:
            hint = "语义未定：先确认接口用途与授权，再用 1 条样本试调，勿批量"
        elif is_write(r):
            hint = "语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量"
        else:
            hint = "语义读：先确认该接口已授权，用 1 条样本按 GET 试调（不写库），勿批量"
        out.append(f"| `{r['path']}` | {r['func'].replace('|','\\|')} | {hint} |")
    out.append("\n### 5.2 仅出现在截图/说明文字中的路径（无契约，勿直接调用）\n")
    out.append("| 路径 | 说明 |\n|---|---|")
    for p, why in QUOTE_ONLY.items():
        out.append(f"| `{p}` | {why} |")
    out.append("\n### 5.3 生产实测校准（2026-11-22，详见 `api_live_probe.md`）\n")
    out.append("- 🔴 `GET /api/v1/tpos/customer/get-all-plan`：旧结论「线上无」**已推翻**，实测 `code 10000` + 完整开发计划结构；接口可用，但数据口径待真实客户复核（§3.2）。\n"
               "- ⚠️ `POST /api/v1/tpos/cusbespeak/get-page`：`GET` 报 20002「GET not supported」；`customerId`/手机号/专家ID 至少传一个（§3.3）。\n"
               "- 🔴 补遗 4 个接口（`part-label-list` / `acceptance-tool` / `get-equity-card-detail` / `get-can-buy-equity-card-list`）：实测 `code 2001` 未授权，需睿美云开通（§3.4）。\n"
               "- ⏱ `POST /api/v1/tpos/consultation/page` 单次 22.6s，客户端超时须 ≥40s（§3.5）。\n"
               "- `POST /api/v1/tpos/visit/obsolete-visit`：2026-09-27 已获授权可用，`contentId` 即 `planId`（注意事项 4）。\n"
               "- `POST /api/v1/tpos/basic/getP/getProjectByType`：文档原文路径疑似笔误，用前实测。\n"
               "- 官方 `rmy` MCP 的 6 个客户维度接口一律返回「没有查到…」，客户明细必须走直连通道（注意事项 6）。\n")

    out.append("\n## 6. 调用铁律速记\n")
    out.append("| 主题 | 规则 | 详见 |\n|---|---|---|")
    for topic, rule, ref in IRON_RULES:
        out.append(f"| {topic} | {rule} | {ref} |")

    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"已生成 {OUT}")
    print(f"接口 {total}（写 {len(writes)} / 方法未标注 {len(unknown)}），模块 {len(groups)}，任务反查 {len(TASK_ROWS)} 行")


if __name__ == "__main__":
    main()
