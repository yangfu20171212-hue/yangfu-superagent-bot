---
name: 睿美云开放接口（TPOS API）调用
description: 睿美云 realmerit 开放接口（TPOS）文档与调用指南。覆盖客户、订单、收银、储值、退款、回访、预约、卡券、库存、门店、员工、会员权益、营销、基础数据等业务模块的 REST 接口契约、TPOS(RSA) 鉴权与通用客户端。当需要调用睿美云接口拉取或写入业务数据（查客户/订单/回访/预约、做对账、未划扣、客户运营）时启用。
---

# 睿美云开放接口（TPOS API）调用技能

## 适用场景
需要调用睿美云（realmerit.cn）开放接口拉取或写入业务数据时启用：
- 客户档案 / 客户搜索 / 客户详情 / 客户池 / 老带新 / 新客判定
- 订单、收银、退款、权益卡、储值充值 / 抵扣 / 退储值 / 转储值、收银记录、可用资产
- 回访（创建 / 快速回访 / 模板）、预约（新增 / 修改 / 确认 / 取消 / 分页）、卡券（查询 / 使用 / 发放）
- 库存（入库 / 出库 / 盘点）、门店、员工 / 部门树、会员权益、营销图文、基础数据（项目 / 套餐 / 年卡 / 次卡 / 物料 / 供应商）、字典、照片

## 核心约定
- **Base URL**：每个机构独立部署，由睿美云线下提供（环境变量 `RMY_BASE_URL`）。文档中 `/api/v1/tpos/...` 前缀通常不变；文档里的前缀 `/api` 可能因机构部署不同而微调，以对接人提供的地址为准。
- **TPOS 鉴权**（详见 `references/auth.md`）：所有请求必须在 Header 带 4 个参数：
  - `tpos-account`：账号（睿美云提供）
  - `tpos-timestamp`：秒级时间戳（与服务器时间相差须 < 1 分钟）
  - `tpos-nonce-str`：随机字符串（同一分钟内不可重复）
  - `tpos-sign`：RSA（SHA256WithRSA，PKCS#1 v1.5）对 `{tpos-timestamp}&{tpos-nonce-str}` 用私钥签名后 base64
- **响应约定**：`code == 10000` 视为成功；`msg` 为提示，`data` 为业务数据（分页接口在 `data.records`、`data.total` 等）。
- **凭证安全**：私钥只走环境变量 / secret，禁止明文入库或提交到 git；测试环境与正式环境使用不同密钥，正式环境需按接口单独授权。

## 通用客户端（直接用，避免重复实现签名）
项目中已有机构无关客户端：`未划扣客户邀约/rmy_client.py`，已包含 RSA 签名、GET/POST 封装、分页拉取、客户搜索、回访写入等。若当前项目已有该文件，直接 `from rmy_client import RmyClient` 复用；否则可复制本技能 `references/rmy_client.py` 到脚本目录作为模板。

环境变量（缺省即走默认值）：
- `RMY_BASE_URL`：机构请求地址
- `RMY_ACCOUNT`：账号（默认 `boss`）
- `RMY_PRIVATE_KEY`：DER 格式私钥的 base64（必填，用于签名）
- `RMY_TIMEOUT`：超时秒数（默认 15）
- `RMY_SIGN_STRING_TEMPLATE`：签名串模板（默认 `{ts}&{nonce}`）

最小调用示例：
```python
from rmy_client import RmyClient
cli = RmyClient()  # 凭据取自环境变量
data = cli.get("/api/v1/tpos/customer/customer-search", params={"keyword": "138"})
print(data.get("code"), data.get("data"))
```

## 接口模块导航（功能地图见 `references/api_capability_map.md`）

> 🔴 **找接口先看功能地图**：`references/api_capability_map.md` 汇总了开放接口全部可调用功能——
> **178 个接口 / 27 个模块 / 57 个语义写接口**，含「按任务反查」44 条、逐接口的方法·路径·关键参数·
> 文档行号·实战坑位、写接口审批清单、文档未标注方法与存疑路径清单。
> 生成脚本 `scripts/build_capability_map.py`（飞书文档更新后重跑即可再生成）。
> 完整字段契约 `references/ruimeiyun_api_full.md`（11455 行，飞书 wiki `JVkQwr4eAisxvHkgv9TcOm45nsf` 的本地快照）；
> `references/api_index.md` 是早期导出的原始路径清单（含重复行与未标注方法），仅作兜底。
> **文档与生产不一致时以实测为准**：`references/api_live_probe.md`（2026-11-22 生产只读抽样，
> 25 个用例、0 个写接口，含 4 处推翻/补充文档结论）；复核重跑 `scripts/probe_readonly.py`。

### 高频调用速查（完整 44 条见功能地图第 1 节）

| 我要做什么 | 方法 | 接口 | 必看提醒 |
|---|---|---|---|
| 搜索客户 / 查客户主档 | `GET` | `customer/customer-search`、`customer/customer-by-id` | 不能空搜；同名手机多档案，优先用 `customerId` |
| 拉全量客户（>1 万条） | `GET` | `customer/customer-search` | 20 页硬顶，必须 `lastCustomerId` 游标 |
| 查当前归属 / 企微在谁手里 | `GET` | `customer/customer-by-id` | 用 `sysUserName` / `wechatSysuserId`，绝不用昵称 |
| 改归属 / 换客户池 | `POST` | `customer/transfer-pool` | 先 `get-pool-info`，后 `customer-by-id` 回查；会推企微通知 |
| 查开单 / 消费 / 购买次数 | `GET` | `order/billing-page` | `tenantId=""` 才跨门店；忽略所有时间参数；`size≤500` |
| 查收银记录（业绩播报） | `POST` | `report/cashier-record-page` | 31 天窗口、**必须串行**；返回 `data.result` |
| 查未划扣 / 剩余项目 | `GET` | `treat/untreated-page` | 或 `POST treat/scrmTreatList` `{treatFlag:false}` |
| 查已治疗 / 实际执行次数 | `GET` | `treat/already-treated-page` | 看 `treatCount`，别信主档的 0 |
| 拉全店到店与划扣执行人 | `GET` | `treat/treated-page-review` | `treatTimeStart/End`；唯一有 `deductUserName` 的接口 |
| 查待回访 / 回访记录 | `POST` | `visit/get-visit-page` | 待回访必须 `visitedFlag:["1"]`；单窗口 1 万条硬顶 |
| 建 / 完成 / 作废回访 | `POST` | `visit/create-visit`、`complete-visit`、`obsolete-visit` | 作废不可逆；写读字段口径不对称（注意事项 28） |
| 查咨询主诉与未成交信号 | `POST` | `consultation/page` | `tenantId` 必填、超时 ≥40s；看 `mainComplaint` / `consumptionStatus` |
| 查在职员工 / 部门 / 门店 | `GET` | `user/get-page`、`basic/dept-tree`、`common/tenantList` | `jobStatus=False` 才在职；`size` 不是 `limit` |
| 查预约 / 新增 / 确认 / 取消 | `POST` | `cusbespeak/get-page`、`add`、`update`、`confirm`、`cancel` | 确认/取消用 `PUT` |
| 查储值 / 权益卡 / 可用资产 | `GET` | `order/balance-*-page`、`billing-equity-card-page`、`get-customer-available-assets` | 抵扣 `deduct-assets`、撤销 `cancel-deduct-assets` |
| 查客户卡券 / 发券 / 用券 | `GET` | `coupon/customer-coupon-page` | 写入：`send-coupon` / `use-coupon` |
| 查项目/套餐/年卡/次卡/物料 | `GET` | `basic/*-page`、`*-type-tree`、`*-detail` | 同构三件套；字典走 `sysdict/dictlist` |
| 查库存 / 照片 / 企微聊天 | `GET` | `inventory/*-page`、`common/photoPage`、`wechat/message/messageList` | 聊天记录用 cursor 分页 |
| 渠道 / 面诊 / 病历 / 问卷 | `GET` | `channel/*`、`assessment/*`、`medical-record/*`、`questionnaireCustomer/*` | 多数实际是 `POST` 查询，以功能地图为准 |

> 路径统一前缀 `/api/v1/tpos/`（例外：`/api/v1/assessment/...`、`/api/v1/top/...`、`/api/v1/scrm/...`）。
> ⚠️ 上表只用于定位，**调用前必须回到功能地图第 3 节核对方法与参数**，再按第 4 节过写入审批门控。

### 模块粗览（逐接口清单见功能地图第 3 节）

| 模块 | 关键接口 | 说明 |
|---|---|---|
| 客户 customer | `POST /api/v1/tpos/customer/info-sync`（档案新增/编辑）、`GET /api/v1/tpos/customer/customer-search`（搜索）、`GET /api/v1/tpos/customer/customer-by-id`（详情） | 返利、推荐、线索、标签、金币、开发计划、客户池转移、合并、老带新、新客判定等 |
| 门店 common | `GET /api/v1/tpos/common/...`（门店信息）、岗位负责人配置 | 门店与组织 |
| 回访 visit | `POST /api/v1/tpos/visit/get-visit-page`、`create-visit`、`complete-visit`、`quick-complete-visit`、`obsolete-visit`（2026-09-27 已授权，见注意事项 4） | 类型/方式、分页、创建、完成、**作废**、模板 |
| 报备 preparation | `POST /api/v1/tpos/preparation/add`、`/get-preparation`、编辑报备人/部门 | 报备流转 |
| 员工 user | `GET /api/v1/tpos/basic/dept-tree`、`GET /api/v1/tpos/role/getRoleListV2` | 员工、部门树、岗位 |
| 卡券 coupon | `GET /api/v1/tpos/coupon/customer-coupon-page`、`POST /api/v1/tpos/coupon/use-coupon`、`POST /api/v1/tpos/coupon/send-coupon` | 查询/使用/发放/赠送/领取 |
| 营销 marketing | `GET /api/v1/tpos/marketing/appoint-card-page`、`/graphic-message-list`；积分 `GET /api/v1/tpos/integral/score-record-page` | 名片、图文、积分 |
| 订单 order | `GET /api/v1/tpos/order/billing-page`、`POST /api/v1/tpos/order/refund`、`GET /api/v1/tpos/order/balance-deduction-page`、`POST /api/v1/tpos/order/deduct-assets` | 收费/退款/储值/权益卡/收银记录/可用资产 |
| 治疗 treat | `GET /api/v1/tpos/treat/untreated-page`、已治疗核销划扣详情、治疗岗位列表 | 治疗/核销/划扣 |
| 预约 cusbespeak | `POST /api/v1/tpos/cusbespeak/get-page`、`/add`、`/update`、`/confirm`、`/cancel` | 预约全生命周期 |
| 基础 basic | 项目/套餐/年卡/次卡/物料/会员权益/供应商查询；字典 `sysdict` | 商品与基础数据 |
| 库存 inventory | 入库/出库/盘点 分页与详情；新增/修正/撤销 | 进销存 |
| 照片 photo | 七牛/外部照片转存、上传、分页查询、皮肤检测上传 | 影像资料 |

## 常用枚举
- **缴费/收银类型 PaymentTypeEnum**：0 订单收费 / 1 订单退费 / 2 转项收费 / 3 定金收费 / 4 定金退费 / 5 充值 / 6 储值退费 / 7 转项退费 / 8 权益卡收费 / 9 权益卡退费
- **订单来源 BillingDataSourceEnum**：0 院内 / 1 小程序 / 2 APP / 3 有赞 / 4 微盟 / 5 新氧 / 6 美际 / 7 有赞美业 / 8 权益卡赠送 / 9 拼团
- **订单状态 BillingStatusEnum**：0 未付款 / 1 已付款 / 2 已作废 / 3 欠费

## 注意事项
1. 客户搜索基于搜索引擎，新增档案后数据有轻微延迟。
2. 不同客户可能共用手机号，按手机号查询会返回多个档案；建议优先使用 `customerId`（neuronCusId）查询。
3. 接口实际返回字段可能多于文档标注，文档仅描述关键字段。
4. **正式环境需对每个接口单独授权，未授权会返回鉴权错误；测试环境账号拥有全部权限。**
   **⚠️ 实战案例（2026-09-16）**：`POST /api/v1/tpos/visit/obsolete-visit`（作废回访）**接口存在但未授权**——
   任何入参（`planId` 待回访/已回访/已作废记录、`customerId`、文档自带样例、甚至不传）**一律返回
   `{"code":401,"msg":"没有找到您要的资源"}`**，而同一 client 同族接口 `get-visit-type`/`get-visit-page`
   均 `code:10000` 正常。**判别口诀：同族接口正常 + 传什么都一样 = 没授权，不是 id 传错，不是接口不存在。**
   **强判别旁证**：连**根本不存在的路径**（如 `/api/v1/tpos/visit/obsolete`）也返回**同一个 401** ⇒
   这是 `/api/v1/tpos/*` 鉴权层对"未授权/未识别资源"的**统一兜底码**，与路径/参数/id 全无关，
   **唯一变量是账号授权**。所以别再去试路径变体和参数名，直接找睿美云授权。
   解法是找睿美云**单独授权**该接口，不要去猜参数。
   - ⚠️ **但「路径/方法写错」会伪装成同一个 401（2026-09-20 实测）**：把
     `GET /api/v1/tpos/treat/treated-page-review` 误写成 `POST /api/v1/tpos/visit/treated-page-review`，
     得到的也是 `{"code":401,"msg":"没有找到您要的资源"}`。
     ⇒ **排查顺序：先核对「文档里的路径 + HTTP 方法」是否照抄（见注意事项 (i)），确认无误再怀疑账号授权**；
     仍然**不要**去盲目试路径变体/参数名（二者区别：核对 ≠ 试错）。
   （注：`code 401` 在本系统属"鉴权/资源范围"类，文档记载其含义为"身份信息已经过期，请重新登陆"，
   **不是"记录不存在"**。）
   另：`obsolete-visit` 的 `contentId`（文档写"回访id"）在全套 164 个接口中**只有它自己用到这个字段名**，
   无任何接口可产出 → 授权后仍需向睿美云确认取值（是否即 `planId`）。详见 `references/ruimeiyun_api_full.md` 补遗节。

   ✅ **2026-09-27 更新：该接口已获授权，实测可用，且 `contentId` 就是 `planId`**（不是新字段名）。
   正确契约（与注意事项 4 里"未授权"的旧结论相反，**以本条为准**）：
   ```
   POST /api/v1/tpos/visit/obsolete-visit
   body: {"contentId": "<planId>", "obsoleteReason": "<作废原因>", "tenantId": "1"}
   ```
   - `contentId` = `get-visit-page` 返回的 `planId`（两种格式都能作废：18 位数字 = 系统正常生成；
     32 位 hex = 历史导入脏数据，其 `customerId` 形如 `importTime165261119918722`）
   - `obsoleteReason` 会写进记录，可追溯 —— **批量清理务必写清原因**，别留空
   - 单次 1:1 生效；并发 4、每 500 条用「待回访降幅 vs 作废增幅」对账做安全阀，实测偏差 ≤10
   - 实战规模：两批合计作废 **84,765 条**，零失败零误伤，耗时 ~3.2 小时
   - ⚠️ **作废不可逆**，批量前必须：① 先跑 1-3 条手工验证 1:1 生效；② 断点续传文件；
     ③ 每批次做对账安全阀；④ 在职员工的真实任务先隔离，确认后再动
   - 🔴 **终验数字不要用脚本内即时读数（2026-09-30 实测）**：脚本作废完立刻打印「待回访 5,188 → 4,374」，
     但 4,374 是接口读数的**滞后值**；间隔 2 分钟后重查 → **4,274**，与 `5,188 − 914 = 4,274` 完全吻合。
     ⇒ **判定 1:1 生效的等式是「作废前 total − 成功数 = 稍后复查的 total」**，不是脚本内的 end 读数。
     若直接信 4,374，会误判成「有 100 条连锁 / 作废没生效」，白排查一轮。

4bis. **🔴 高频调用会触发服务端 502（2026-09-28 实测）+ 自动化清理必须带「数据完整性保护」**：

   **现象**：单日作废 89,932 条 + 大量扫描后，`visit` / `user` / `billing` **全部接口持续返回
   HTTP 502**（`rmy_client` 表现为 `code=None, msg="非 JSON 响应(HTTP 502)"`），持续数小时。

   ⚠️ 判断要点：
   - **502 不是鉴权问题**，重试无用；`total` 会变成 `0` / `None`，**不是"真的 0 条"**
   - 单日 9 万级写操作建议**分批跨天**，别一次性打完

   **自动化清理脚本的四重保护（缺一不可，已验证生效）**：
   | 保护 | 规则 | 本次实测 |
   |---|---|---|
   | P1 客户保底 | 每个客户至少保留 1 条，绝不清空某人全部待回访 | 触发 0 次 |
   | P2 有效期豁免 | 只删逾期 >N 天（默认 7），今天/未来该做的不动 | 拦下 28 条 |
   | P3 单日上限 | 作废量 >阈值（默认 300）只出报告不执行 | 848 条 → 被拦截 |
   | **P4 数据完整性** | **接口 total≤0、或枚举量 < 接口 total 的 50% → 直接中止** | 502 时生效，零作废 |

   ⚠️ **P4 最关键**：接口抽风时若只扫到少量数据，去重规则会把"某客户仅有的几条"误判为重复删掉。
   务必先拿接口 `total` 做基准，覆盖率不足就停下。

   **参考实现**：`未划扣客户邀约/daily_visit_cleanup.py`（每日 07:30 自动跑，规则：
   同客户 30 天窗口保 1 条 + 同客户同 typeId 保最近 1 条）。
   附 `--offline 快照.json` 演练模式（强制预览、不碰线上），接口挂了也能验证规则逻辑。

5. 修改客户档案可编辑字段有限，如有编辑需求及时与睿美云对接人沟通。
6. **⚠️ 官方 `rmy` MCP 的客户维度接口不可信（2026-08-29 实测）**：`getTreatmentByCustomerId`、
   `getBillingInfoByCustomerId`、`getVisitInfoByCustomerId`、`getConsultInfoByCustomerId`、
   `getCustomerReceptionByCustomerId`、`getDevPlanInfoByCustomerId` 一律返回「没有查到…」——
   即便客户主档明确显示有治疗和回访记录。**不要用「没查到」推断客户没有数据。**
   其 `number` 参数模式还会抛 Java NPE（`Map.get(Object) is null`）。
   官方 MCP 里真正可用的只有：`getPageCustomerInfo`、`getCustomerIdByKeyword`、
   `getCustomerLabelByCustomerId`、`getTreatmentByDate`（按日期拉全店，但**返回体无 customerId，无法关联客户**）。
   2026-11-22 补：`tools/list` 实拉到 90 个工具、`readQueryMcpDocs` 覆盖 86 个查询函数，
   完整清单见 `references/official_mcp_functions.md`；新增的 `...ByCustomerIdList` 批量版**尚未实测**。
7. **客户明细一律走直连通道**（见「调用流程建议」），已验证可用的接口组合：

   | 用途 | 方法 | 路径 | 关键参数 |
   |---|---|---|---|
   | 客户主档 | GET | `/api/v1/tpos/customer/customer-by-id` | `customerId` |
   | 订单/开单 | GET | `/api/v1/tpos/order/billing-page` | `customerId` + `tenantId`（**传空串可拿全部门店**，见下）+ `size≤500` |
   | **到店/治疗单（全店·按日期）** | **GET** | **`/api/v1/tpos/treat/treated-page-review`** | `tenantId`, **`treatTimeStart`/`treatTimeEnd`**, `page`, `size≤200` |
   | 已治疗记录（单客户） | GET | `/api/v1/tpos/treat/already-treated-page` | `customerId`, `size` |
   | 剩余/未治疗 | POST | `/api/v1/tpos/treat/scrmTreatList` | `{current,size,customerId,tenantId,treatFlag:false}`；`true` 为已治疗 |
   | 回访记录 | POST | `/api/v1/tpos/visit/get-visit-page` | `{page,size,customerId}`，或 `{page,size,visitedDateStart,visitedDateEnd}` 拉全量 |
   | 咨询记录 | POST | `/api/v1/tpos/consultation/page` | `{customerId,tenantId,page,size}`（`tenantId` 必填） |
   | 接待/到店 | POST | `/api/v1/tpos/reception/reception_cus` | `{customerId,tenantId}` |
   | 预约 | POST | `/api/v1/tpos/cusbespeak/get-page` | `{customerId,tenantId,page,size}` |
   | 储值抵扣 | GET | `/api/v1/tpos/order/balance-deduction-page` | `customerId` |

   `tenantId` 取客户主档的门店 id（如远大店 = `3`）。

   **🔴 到店数据（2026-09-30 补）**：一直以为「没有按日期拉全店到店的接口」——**错了**。
   权威源是 `GET /treat/treated-page-review`（不是 `/treat/page`，后者 401）：
   ```
   GET /api/v1/tpos/treat/treated-page-review
       ?tenantId=1&treatTimeStart=2026-09-01 00:00:00&treatTimeEnd=2026-09-30 23:59:59
       &page=1&size=200
   ```
   - ⚠️ **服务端时间筛选不严格**，必须客户端二次校验 `treatmentTime` 落窗
   - 这是**唯一能拿到「谁做了什么科室的项目」的接口**（回访/收银接口都取不到执行人）
   - 关键字段：`treatDeptName`（治疗科室）/ **`deductUserName`（实际划扣执行人姓名）** /
     `projectList[].billingItemName` / `treatmentTime` / `customerId` / `deductRecordId`
   - 按科室拆业务、算「皮肤管理师执行量」都用它

   **🔴 `report/cashier-record-page` 并发调用会静默丢数据（2026-09-30 实踩）**：
   并发 4 拉 8 月 → 返回 **0 条**（不报错）；改串行 → 正常 272 条。
   **必须串行 + 校验返回记录的 `date` 月份是否落在请求窗口内**，否则会拿到空数据当成「该月无收银」。

   **🔴 `order/billing-page` 忽略所有时间参数**：`startTime`/`endTime`/`billingDateStart`/
   `createTimeStart` 传了也白传，`total` 恒为全量（实测 61,750）。且 **`size` 硬上限 500**
   （传 1000/2000 也只回 500 条）。只能全量分页拉后本地按 `createDate` 过滤。
   分页**按 createDate 升序**（最早在前）→ 要近期数据直接从**最后一页**往前拉最省事。

   ### 🔴🔴 `billing-page` 的 `tenantId` 是「门店过滤器」，不是"必填校验"

   官方文档标 `tenantId = true`（必填），但实测（2026-09-25）：

   | tenantId | 返回 | 说明 |
   |---|---|---|
   | `"1"` | 只有凯德店订单 | **静默截断**，其他门店订单不报错、直接不返回 |
   | `"2"` | 只有双楠店 | 同上 |
   | `"3"` | 只有远大店 | 同上 |
   | `"4"` | `code=10002` 空 | 金牛店该客户无单 |
   | `""`（空串） | **全部门店合并** | ✅ 跨店客户核实用这个 |

   实测案例（客户「黄辉」，cid `98d10ed9…`）：
   ```
   tenantId="1"  → total=3   全在凯德店，无皮秒单
   tenantId="3"  → total=9   远大店「超皮秒-单模式」
   tenantId=""   → total=21  凯德 3 + 双楠 9「超皮秒祛斑」+ 远大 9「超皮秒-单模式」
   ```
   ⚠️ 用 `tenantId="1"` 做跨店核实会得出**「该客户没有这个项目」的错误结论**（不报错，
   只是少返回）。批量拉全量开单时若固定 `tenantId=1`，产出的缓存**全是单店数据**，
   后续用它核门店必然全对、毫无鉴别力 —— 这类"全对"是最危险的假阳性。
8. **⚠️ 深分页会截断，`size` 参数会被忽略（2026-08-29 实测，拉全量必看）**：
   `visit/get-visit-page` 等分页接口，`size` 传 500 或 1 都一样——**服务端固定每页 500 条**。
   更要命的是**深分页返回空**：总量 19.4 万条 / 390 页时，直接跳第 300 页、第 380 页**均返回 0 条**；
   从第 1 页顺序翻也只拿到前面一部分（实测 2025-03 之后的数据全部丢失，命中日期最晚只到 2025-02）。
   **解法：按时间分片（推荐按月），把单批总量压到 3 万条以内，分片内再翻页。**
   ```python
   for s, e, ym in month_ranges("2024-01", "2026-08"):     # 逐月
       page = 1
       while True:
           d = cli.post("/api/v1/tpos/visit/get-visit-page",
                        {"page": page, "size": 500,
                         "visitedDateStart": s, "visitedDateEnd": e}).get("data") or {}
           recs = d.get("records") or []
           if not recs: break
           处理(recs)
           if len(recs) < 500: break      # 不满页 = 末页
           page += 1
           if page > 60: break            # 单月安全上限
   ```
   **校验方式**：跑完全量后，用已知客户反查确认没漏（如姜雪，2025-03-04 有回访记录）。

   #### 🔴🔴 拉全量待回访的真实姿势（2026-09-28 实测，比上面更狠）

   目标：枚举全部待回访（`visitedFlag:["1"]`）。**任何单一维度分片都拉不全**：

   | 分片方式 | 拉到 | 说明 |
   |---|---|---|
   | 不传日期，只翻页 | **3,000** | **硬上限**：page 7 起全空，与 size 无关 |
   | 按月分片 | 77,171 / 95,011 | 触顶月（total 显示 499/999/1500/3000 这类整数上限） |
   | 按旬分片 | 37,393 | 更细，但仍漏 |
   | 按天分片（1,792 天） | 8,847 | 较好 |
   | 按 `tenantId`×天 双重分片 | 5,611 | ⚠ **反而更少**——传 tenantId 会换一套过滤逻辑 |
   | **两者取并集** | **9,101** | ✅ 最佳（接口 total 10,246，仍有 1,145 条无法枚举，占 11%） |

   - `tenantId` 同样是门店过滤器：`""`=10,246 / `"1"`=凯德 5,238 / `"3"`=远大 4,917 / `"2"`=21 / `"4"`=70
   - ⚠ **坑中坑**：不传 tenantId 时接口**确实跨门店**（记录里有 `planVisitTenantId`，4 个门店都有），
     但传了 tenantId 反而拉得更少 ⇒ **不要指望"加个过滤条件就能分片更准"**，只能多维度取并集
   - `typeId` 参数**接口直接忽略**（传 0-11 全返回同样的 total），不能用来分片
   - **铁律**：① 扫描数 > 接口 `total` = 数据污染，立即停手；
     ② 合并后**必须按 `planId` 全局去重**（接口跨分片会重复返回同一条，实测 81,665 → 唯一 43,598）；
     ③ 接受"接口有枚举上限"这个事实，向下游报**下界**而非精确值
   - 安全阀：作废前后各查一次 `visitedFlag:["1"]` 的 total，降幅应 ≈ 作废数
9. **主档字段口径坑**：主档的 `消费总次数` / `治疗次数` 可能为 `0`，但客户实际有多次划扣。
   真实购买次数看 `order/billing-page` 的 `billingItemList[].numberOfTime`，
   实际执行看 `treat/already-treated-page` 的 `treatCount`。别拿主档的 0 当「没消费过」。
10. **回访记录 `response` 字段混装**：既存客户回应（短，如「怀孕」「微信已删」），
    也存员工话术（长，如「亲爱的 最近季节交替皮肤容易干燥缺水…需要帮您预约吗？」）。
    做文本分析时用长度过滤（≤30 字）区分，否则话术里的关键词会造成大量误判。
11. **`customer-search` 不能空搜全量**（报「搜索参数不能为空」）；官方 MCP `getPageCustomerInfo`
    分页不可靠（page=2 返回空模板对象）。**拉全量客户需另想办法**，如从回访/订单记录反查 customerId。

12. **⚠️⚠️「假版本错误」三连——最浪费排查时间的一类坑（2026-09-14 实测）**：

    | 现象 | 真实原因 | 正解 |
    |---|---|---|
    | `20002 您不是最新版本，请更新你的系统` | **方法不对**：该接口是 GET，你用了 POST。**跟"版本"毫无关系** | 改 GET |
    | `20002` 且 msg 为空 / `401 没有找到您要的资源` | **路径不对**（`base_url` 不含 `/api`，路径必须自带） | 核对路径前缀 |
    | 请求成功但读不到数据 | **成功码是 `10001` 不是 `10000`** | 判 `code in (10000, 10001)` |

    已知踩此坑的接口：`GET /api/v1/tpos/user/get-page`（员工名册）、
    `GET /api/v1/tpos/reception/triagetouserlist`（系统接诊可选人，权威咨询师名单）。
    **成功返回码不统一**，一律用 `rmy_client.classify_response()` 判成功，别硬编码 `== 10000`。

13. **分页参数是 `size` 不是 `limit`**：`user/get-page` 等接口写 `limit=500` **不报错但被忽略，
    永远只回 20 条**——悄无声息少 90% 数据。拉全量务必先打印 `data.total / data.pages` 对账。

14. **`report/cashier-record-page` 单次时间窗上限 31 天**：
    超了报 `20002 收费时间间隔有误，不在指定范围内（31天）`。拉 180 天需按 30 天分片循环。
    返回结构是 `data.result`（不是 `records`），每条含
    `feeBillingUser`（收费人=实际成交）/ `billingAssistantUser`（协助人=实际服务）/
    `chargeUser`（经办/充值）/ `paymentItemDepts`（项目科室）/ `cusTenantName`（门店）。
    **用它反查"谁是真正在干活的人"，比看任何名册字段都可靠。**

14bis. **🔴🔴 本地开单缓存只有 47%，绝不能用来判断"客户是否活跃 / 多久没来"（2026-09-28 实测）**：

    | 来源 | 开单条数 | 覆盖客户 |
    |---|---|---|
    | 本地缓存 `cache/billing_*.json`（241 文件） | 28,743 | 7,276 |
    | 接口 `GET /api/v1/tpos/order/billing-page`（无时间参数） | **61,741** | — |

    **覆盖率仅 47%。** 抽样 12 条「缓存判为零开单」的客户回查接口，**9 条误判**
    （毛雯静缓存显示零开单，接口实查 19 单）→ **误判率 75%**。

    ⚠️ 后果：拿缓存判断「客户沉睡/零开单」会把大量活跃客户错划成死客户，
    进而误作废在职员工的真实任务。

    **正解**：判断客户活跃度必须接口实时查。
    - 少量客户（<5,000）：逐客户 `GET billing-page?customerId=&tenantId=''&page=1&size=100`
      取 `records[].createDate` 最大值。并发 4、2,891 客户约 9.4 min、零失败。
    - 全量：按时间/门店分片拉（缓存本就是这么建的，但建的时候分片不全）。
    - ⚠️ `tenantId` 传**空串**才能拿全部门店（见注意事项 (b)）。

    交叉校验：`untreated_snapshot_*.json`（未划扣快照）的客户主键字段是 **`cid`**
    （不是 `customerId`），结构是 `{meta, records, errors}`，`records[]` 含
    `amount`/`n_left`/`bills`/`items`。用它判断"客户还有没有没做完的项目"很准。
    判断回访值不值得保留时，**"客户是否仍有未划扣"比"回访是否过期"更重要**——
    实测过期>1 年的回访里有 85 条客户仍有 ¥606,283 / 1,164 次未划扣，**绝不能作废**。

15. **⚠️ 归属字段口径：`sysUserName` 是当前归属，`relatedConsul` 是历史关联串**
    - `relatedConsul`：客户档案里**全部**有值，是逗号拼接的**历史**关联人
      （如 `沈威,向敏,陈巧智,曾秦刚,刘艳,潘婷`），一个客户串 5-7 个曾服务过他的人。
      **拿它当"当前负责人"会造出大规模假孤儿**（实测 19,518 池里误报 8,029 位"孤儿"）。
    - `sysUserName`：**当前归属**，但覆盖率低（实测 21.5%），且绝大部分本来就挂在在职员工名下。
    - `exclusiveServerName`：实测 100% 为空，**不可用**。
    - 皮肤管理师归属取 `roleManagerInfoList` 里 `roleName=皮肤管理师` 的 `userName`。
    - **判"某客户是否无人跟进"，先看 `sysUserName`，再用 `relatedConsul` 做参考，不要反过来。**

16. **在职判定**：`user/get-page` 的 `jobStatus` **`False` 才是在职**（`True` = 离职），
    `leaveDate` 为空表示未离职；`entryDate/leaveDate` 是**毫秒时间戳**；
    `roleName`/`deptName` 是 **JSON 数组字符串**（如 `"[\"皮肤管理师\", \"皮肤管理主管\"]"`），需 `json.loads`。
    **光看名册不够**——必须用第 14 条的收银记录做活跃度交叉验证，
    否则会把"在职但零业务痕迹"的人排进派单池（实测有 2 人 180 天 0 笔开单 0 笔服务 0 名客户）。

17. **⚠️⚠️「会算错」的两个分页/筛选坑（2026-09-16 实测，比筛选失效更危险）**
    这两个坑**不报错、不告警，直接给你一份看起来正常的错数据**，必须主动防：

    | 坑 | 现象 | 正解 |
    |---|---|---|
    | **日期筛选不严格** | `visit/get-visit-page` 传 `visitDateStart/End=9/1~9/16`，服务端回 **1,399** 条，但**只有 1,022 条**的 `visitDate` 真在区间内；多出 377 条是 8/26(284)+8/29(93) 的**超期记录**（`delayFlag=True`）| **拉完必须在客户端按日期字段二次过滤**，否则数字虚高 ~37% |
    | **分页失败静默截断** | 同一查询 `total=1400 / pages=7`，某页超时后循环 break，**函数安静返回 1,021 条** | **单页失败重试 3 次**；仍失败则**显著告警并中止**，绝不用残缺数据下结论。页数多（total>1000）时尤其容易触发 |

    另：**`visit/get-visit-page` 的 `day` 字段恒为 `None`**（实测 1,012 条全为 None）
    → **不能用「第几天」判重**，只能靠 `content` 文本归一化后比对。
    按"同客户+同类型"粗判会把治疗后回访的 D1/D3/D7 多节点误杀（实测误判 631 条，真实重复仅 98 条）。

18. **`get-all-plan`（开发计划）已可用 —— 2026-11-22 生产实测更正**
    旧结论「接口不存在、需改走 `consultation/page`」**已过时**：`GET /api/v1/tpos/customer/get-all-plan?customerId=...`
    实测返回 `code 10000`，`data` 含 `actDevPlans` / `devInvalidDevPlans` /
    `expiredInvalidDevPlans` 三个数组、对应金额字段与 `haveInvalidData`。
    ⚠️ 但用不存在的客户 id 测时三个列表均为空，只证明**接口可达、契约完整**；
    首次对真实客户使用前，先拿 1 条真实数据核对字段含义再批量使用。
    详见 `references/api_live_probe.md` §3.2。

19. **`consultation/page`（查询咨询）要点**
    - **必带 `tenantId`**（string），否则 `20002 门店id不能为空`
    - **响应慢**：默认 15s 超时会失败，需 **≥40s**；必须缓存，不可逐客实时拉
    - 高价值字段：**`mainComplaint`（客户主诉）**、`treatmentPlan`、`conProjects`、
      **`consumptionStatus`（"未成交" = 有需求未转化的最精准信号）**、`consultationStatus`、
      `smartLabelList`、`customerType`、`receptionTime`、`userId/userName`（接诊人）
    - ⚠️ 含 `phoneNumber`，隐私铁律不取不写

20. **⚠️⚠️⚠️ 企微归属必须用 `wechatSysuserId` 判，绝不能用 `wechatSysUserName`（2026-09-16 血泪）**
    `customer-search` 返回两个企微字段，**用途完全不同**：

    | 字段 | 是什么 | 能不能用来判"企微在谁手里" |
    |---|---|---|
    | `wechatSysUserName` | 企微**昵称** | ❌ **不能**。员工跳店/改名/接手旧账号后会漂移 |
    | `wechatSysuserId` | 企微好友绑定的**睿美云员工账号** | ✅ 稳定，且与 `staff_push_config.json` 的 `userid` **同一命名空间** |
    | `wechatUserId` | 客户在企微里的 external contact id | 配合 `wechatSysuserId` 使用 |
    | `wxBindFlag` | ⚠️ **不是"是否加了企微"**（实测 6,453 位有企微的人里只有 1,942 位为 true） | ❌ 判"有没有企微"请看 `wechatSysuserId` 是否为空 |

    **昵称漂移实测**（同一账号多个昵称，用昵称判会严重误判）：

    | `wechatSysuserId` | 名下客户 | 该账号出现过的昵称 |
    |---|---|---|
    | `xiaoyang` | 2,205 | 漾肤-潘潘(1109) / 漾肤-花花(870) / 漾肤-曾曾(95) / 小漾-双楠店(92) / 漾肤-双楠(37) |
    | `ZhengYiQiu` | 1,439 | 汪怡辰(1334) / 郑义秋(105) |
    | `meiling` | 1,275 | 漾肤赵静(673) / 赵静(558) / 唐美玲(44) |
    | `YangShuLin01` | 125 | 杨舒琳(80) / **颜所远大-贝贝**(45) ← 曾被我误判成"竞品账号"，实为同一个人 |

    ⚠️ **注意 `wechatSysuserId` ≠ `namePy`（姓名拼音）**：`LiuYan/ChenHong/YanLi/huangdan/CaiWenYing/ZhangLiJia/ZouLi` 对得上，
    但 `ZhengYiQiu`(汪怡辰) / `meiling`(赵翊妗) / `xiaoyang`(潘婷) / `DaShiZi`(柳佩) / `WangMouMou`(王紫) / `alaso`(徐丽军)
    是**沿用旧人的登录账号**。→ **别用拼音猜人，用 `staff_push_config.json` 的 `userid` 字段**（生产已验证）。

21. **客户归属相关字段全表**（`customer-search`，2026-09-16 实测）

    | 字段 | 含义 | 实测覆盖率（19,519 池） |
    |---|---|---|
    | `sysUserId` | 当前归属人 **ID（32位hex，不是账号）** | 21.5% |
    | `sysUserName` | 当前归属人姓名 | 21.5% |
    | `wechatSysuserId` | 企微好友持有者**账号** | 33.1% |
    | `wechatSysUserName` | 企微好友持有者**昵称**（会漂） | 33.1% |
    | `roleManagerInfoList` | 岗位负责人（皮肤管理师/护士/医生） | 按角色分别有值 |
    | `crossHospitalSysUserName` | 跨院咨询师 | 实测 **0%**，不可用 |
    | `relatedConsul` | 历史关联串（**不是当前归属**，见第15条） | 100% |
    | `sysUserPhone` / `externalUserId` / `exclusiveServerName` | — | 实测 **0%**，不可用 |

    ⚠️ `sysUserId` 是 hex，`wechatSysuserId` 是短账号 —— **两者永远不相等，别写成 `sysUserId == wechatSysuserId` 判一致**。
    要比一致性必须先把两者都翻成姓名（hex 走 `user/get-page` 的 `id`，短账号走 `staff_push_config.json`）。

22. **门店清单**：`GET /api/v1/tpos/common/tenantList`
    实测返回：`1=成都漾肤--凯德店`、`2=成都漾肤-双楠店`、`3=成都漾肤-远大店`
    （另有 tenant 4 出现在个别员工 `catTenant` 里）。
    `customer-search` **不带 `tenantId` 会返回全机构**（实测全机构 28,107）；
    凯德店 **19,519** / 双楠 **926** / 远大 **4,422**。
    ⚠️ 做单店分析必须显式传 `tenantId`，否则池子混店。

23. **✅ 企微客户关系转移三件套（可用，是"归属错位"的原生解法）**

    | 接口 | 实测 |
    |---|---|
    | `GET /api/v1/tpos/customer/customer-qw-info?customerId=` | ✅ `code:10000`，`data.changeAllow=true` 表示可转企微关系 |
    | `GET /api/v1/tpos/customer/get-pool-info?customerId=` | ✅ `code:10000`，返回 `commonPool[]`（默认非个人池/报备池/失效顾客/退费纠纷流失顾客…） |
    | `POST /api/v1/tpos/customer/transfer-pool` | ✅ 已实测写入（2026-09-16；**2026-10-10 完成含还原的双向闭环验证**，见下方）。body: `{customerId, poolId(必填), sysUserId, syncVisitPlan(必填bool), transferWxFlag:false, needApprovalFlag, reason, transTenantId}` |
    | `GET /api/v1/tpos/customer/customer-by-id?customerId=` | ✅ `code:10000`，单条回查归属：返回 `sysUserId` / `sysUserName` / `poolName`（**验证写操作是否真落库的指定接口**） |

    ### 🔴 `sysUserId` 只在转入「个人池」时生效（2026-09-16 实测，最易踩的坑）
    同一个 client、同一天、只差 `poolId`，结果完全不同：

    | 目标池类型 | 返回 | `sysUserId` 是否写入 |
    |---|---|---|
    | **公共池**（如 `流失-非星级`） | `code:10000` `data:true` | ❌ **不写**，归属仍为空（**静默失败**，只 `updateDate` 变了） |
    | **个人池**（如 `1-3000`，id `aa2b3b9c519bbf059a758b00d4e6cdcd`） | `code:10000` | ✅ 写入 `sysUserId=b941c6e2…` + `sysUserName=潘婷` |

    ⇒ **`code:10000 data:true` 不等于成功**。批量改归属前必须先选一个**个人池**；
    入库后必须用 `customer-by-id` 抽检，别信返回值。
    → 实测批量认领 3,742 条，随机抽 20 条回查 **20/20 归属与池子均正确写入**。

    ⚠️ 还有一层坑：客户在**公共池**时**无法直接认领给某个人**——个人池是唯一载体。
    所以「把无归属客户认领给咨询师」这件事，本质是先决定**入池规则**（属客户资产划分决策，不是技术问题）。
    凯德店已知个人池 id：`1-3000`=`aa2b3b9c519bbf059a758b00d4e6cdcd`、
    `3000-10000`=`a810e4f3b393b02d7e9b926795f86657`、
    `星级活跃`=`1f22bd294e300d76bddb30929b693ee3`、    `星级非活跃`=`def7546146192947d505e6ba70d5bf00`。

    ### ✅ 写入链路端到端验证：同池换人 = 秒级 1:1 生效，且可无损还原（2026-10-10 实测）

    真实客户跑完整闭环（李雪华 · 凯德建档/无单/无消费/无未划扣 · 归属赵翊妗 · 池 `3000-10000`）：

    | 步骤 | 动作 | `customer-by-id` 回查 | 判定 |
    |---|---|---|---|
    | 0 | — | 赵翊妗 / `3000-10000` / updateDate `01:00:10` | 前置基线 |
    | 1 | `transfer-pool` → 潘婷（**同池**、`syncVisitPlan=false`、`transferWxFlag=false`） | — | `code:10000 data:true` |
    | 2 | 回查 | **潘婷** / `3000-10000` / updateDate **`14:05:55`** | ✅ 已生效 |
    | 3 | `transfer-pool` → 还原赵翊妗 | — | `code:10000 data:true` |
    | 4 | 回查 | **赵翊妗** / `3000-10000` / updateDate `14:06:00` | ✅ 已还原 |

    ⇒ 结论：
    - **`sysUserId` 在同池内改人 = 立即落库**（`updateDate` 秒级刷新）——凌晨 3:00 的延迟**只针对 `syncVisitPlan`**，不影响归属本身
    - **只换咨询师、不换池子**可行：`poolId` 传当前池 id 原样即可
    - **完全可逆**：反向再调一次即还原，净效果为零 → 批量清洗归属前可先小批试跑再放量
    - `syncVisitPlan=false` + `transferWxFlag=false` 时**回访计划与企微关系均未被触及**（副作用隔离成功）
    - 验证脚本：`漾肤/数据之眼/verify_transfer_pool.py`（`--dry-run` 只读核对 / `--restore` 中断补救）

    ### 🔴🔴 `transfer-pool` 是**员工可见动作**：每次调用必推企微通知，且**无法关闭**（2026-10-10 事故）

    - 实测：连续迁移 20 位，员工的企微应用持续收到
      「**将【原咨询师】的客户【客户名】转交给【新咨询师】** 客户转交」通知 —— **一条客户一条通知**，会刷屏
    - ⚠ **`transferWxFlag` 不是通知开关**！它只管「企微好友关系是否一起转」；
      `syncVisitPlan` 只管「回访计划是否一起转」→ **两者都无法抑制通知**
    - ⚠ 通知里的操作人显示为 **`【null】`**（接口授权账号没有中文名）→ 员工看到会困惑，建议给 API 账号起名
    - ⇒ **铁律：归属迁移不是纯数据操作，是组织行为。**
      批量跑之前**必须**：
      1. 先与**当事员工**沟通（否则原咨询师会看到"我的客户被转走了"，造成同事误会/军心问题）
      2. 说明迁移对象的性质（例：本次 20 位全是 **7.7~8.2 年未到店的零价值僵尸**，不是活跃客）
      3. 分批跑并控制单批规模，避免通知刷屏
    - ⇒ **不得静默批量执行**；`--execute` 前必须已确认已与业务方沟通过
    - 🔴 **回滚同样会推通知**（实测 2026-10-10）：反向调用 `transfer-pool` 会推
      「将【新咨询师】的客户【X】转交给【原咨询师】」→ **轮到新咨询师看到客户被转走**
      ⇒ **回滚 ≠ 无痕撤销**：一次写入 + 一次回滚 = **两轮通知**。
      ⇒ 所以「要不要做」必须在**写入前**想清楚，别指望事后悄无声息地撤
    - ✅ 回滚正确性验证法（`batch_transfer_pool.py rollback` 只校验归属）：
      **必须额外校验 `poolName`** —— 正确回滚应还原到**原池**（实测 20/20 归属+池 双一致）

    ### 🔴🔴 `get-pool-info` 的池列表按**客户建档门店**返回（2026-10-10 实测，最易踩）

    同一个接口、同一个账号，客户建档门店不同 → **可用咨询师名单完全不同**：

    | 客户建档门店 | personalPool | 出现的咨询师 |
    |---|---|---|
    | **凯德店**（tenantId=1） | **46 条 / 9 个池** | **汪怡辰 / 赵翊妗 / 潘婷** ＋ 曾秦刚 / 张莉佳 / 李曜 |
    | 金牛店（tenantId=4） | 40 条 / 8 个池 | 沈威 / 向敏 / 王晓娟 / 郑义秋 / 蔡文英 |

    ⇒ **要把客户转给凯德店的三位在职咨询师，客户必须是在凯德店建档的**；
    金牛店建档的客户在该接口里**根本看不到这三人**。
    ⚠️ `tenant` 参数**不改变结果**（传 `1` 与不传完全一样，默认就按建档门店）——别指望用它切换。

    ⚠️ **`personalPool[]` 每条 = `(poolId, userId, userName)` 组合，`poolId` 全店共用**；
    同一个 `poolId` 会**重复出现多次**（每次 `userId` 不同，括号里是该咨询师在该池的现有人数/上限）
    → 解析必须按 `(poolId, userName)` 建索引，**不能 `{poolName: poolId}` 直接覆盖**。

    ✅ **凯德店实测池 id（2026-10-10，9 个）**：

    | 池名 | poolId |
    |---|---|
    | 1-3000 | `aa2b3b9c519bbf059a758b00d4e6cdcd` |
    | 3000-10000 | `a810e4f3b393b02d7e9b926795f86657` |
    | 星级活跃 | `1f22bd294e300d76bddb30929b693ee3` |
    | 星级非活跃 | `def7546146192947d505e6ba70d5bf00` |
    | 新客池 | `cccccccccccccccccccccccccccccccc` |
    | 渠道顾客 | `181810003366117378` |
    | 外地顾客 | `181809946453606404` |
    | 备孕/孕期 | `181809877935456259` |
    | 退费意向 | `181816639845564417` |

    ✅ **凯德店实测「公共池」id（2026-10-10，8 个）—— ⚠ 转这些池会「清空归属」**（`sysUserId` 不写）：

    | 池名 | poolId |
    |---|---|
    | 默认非个人池 | `dddddddddddddddddddddddddddddddd` |
    | 报备池 | `e` |
    | 失效顾客 | `cb577d96518be1469026c3041e989ea6` |
    | 退费纠纷流失顾客 | `491a5df1fa76ce6e3bc34685d56e91e0` |
    | 手动调整 | `900c5942fd4411ef898adfc7e29af39d` |
    | 流失-非星级 | `516c9ad9e641c8208af149eaec9102eb` |
    | 流失星级 | `302075783101284353` |
    | 黑名单客户池 | `6e639f55c3c711f0b0b20242ac110003` |

    ⚠ **池 = 价值分层** → 只换归属人时**必须保留原池**：先 `customer-by-id` 读 `poolName`，
    再把它当 key 去 `get-pool-info` 的 `personalPool[]` 反查 `poolId` 原样传回。
    `personalPool[].poolName` 带 `(人数/上限)` 后缀（如 `3000-10000 (943/2000)`）→ **匹配前先 `.split(" (")[0]`**。

    **批量迁移流水线**：`漾肤/数据之眼/batch_transfer_pool.py`
    （`plan` 生成计划 → `run --execute` 写入 → `verify` 回查 → `rollback` 还原；默认 dry-run、JSONL 台账）
    实测（2026-10-10）：赵翊妗 → 汪怡辰 20 条，**写入 20/20 成功、全量回查 20/20 一致**。

    ### 🔴🔴 「相关咨询师」`relatedConsul` 的顺序**不可靠**（2026-10-10 纠错，推翻旧结论）

    - `relatedConsul` 的中文名**就是「相关咨询师」**（文档字段表 226 行）；本地快照的 `owner_hist` 与之**集合 100% 相同、但顺序不同**
    - ❌ **旧结论（已推翻）**：「串按旧→新拼接 → 取串中最后出现者，回测 95.2% 正确」
      —— 那个 95.2% 是**被无歧义样本拉高的假象**：绝大多数客户串里只有 1 位候选，怎么取都对
    - ✅ **实测（2026-10-10）**：
      - 实时抽 60 位 vs master 快照：**集合相同 100%，但完全同序仅 36.7%、末位相同仅 45%**（顺序会漂移）
      - 用**实时数据**回测 144 位已知归属客户：整体 79.2%；其中 **113 位串里只有一位三人成员**（天然 100%）
      - **真有歧义的仅 14 位 → 命中 5/14 = 35.7%（≈抛硬币，三人时随机概率 33%）**
    - ⇒ **铁律：「取串中最后一位」只对「串里只有一位候选」有效；一旦冲突，它就是随机的，不可用于生产决策**
    - ⚠ 串里混有非咨询师账号（`网咨工作号-露露`、`英子`、`刘艳`、`杨婷婷` 等）→ 必须用白名单过滤，不能直接取末位
    - 该字段**没有时间戳**，`customer-by-id` 也不返回归属变更历史

    ### ✅ 冲突时的正确信号 = **企微归属** `wechatSysuserId`（2026-10-10 实测）

    - `customer-by-id` 返回 `wechatSysUserName`（显示名）与 `wechatSysuserId`（拼音短号）+ `wxBindFlag`
    - 🔴 **必须用 `wechatSysuserId` 短号做 key** —— **显示名会改名骗人**：
      汪怡辰的企微账号显示名居然叫 **「郑义秋」**；赵翊妗的账号显示名是 **「漾肤赵静」**；潘婷是 **「漾肤-潘潘」**，
      另有 **「漾肤-花花」** 与潘潘**同短号 `xiaoyang`**
    - 凯德映射（实测反推）：**赵翊妗 = `meiling` ｜ 汪怡辰 = `ZhengYiQiu` ｜ 潘婷 = `xiaoyang`**
    - 准确率：**87.9%**（199 位有企微绑定的已知归属客户）；但**仅约 65% 客户有企微绑定**（赵翊妗名下尤其低，仅 55%）
    - ⚠ 所以企微归属是**补充信号**，不能单独作为唯一依据

    ### 🔴 归属判定的最终三级规则（李刚 2026-10-10 定稿，已进代码）

    由 `build_claim_lists.py apply_resolution()` 实现，**逐客户**按顺序命中即停：

    | 级别 | 触发条件 | 判定 | 实测占比 |
    |---|---|---|---|
    | ① **唯一候选** | `relatedConsul` 串里**只有 1 位**三人成员 | 直接用 | 3,524 / 3,918 = 89.9% |
    | ② **企微归属** | 有冲突（≥2 位）**且** `wechatSysuserId` 命中三人之一 | 用企微那位 | 231 / 3,918 = 5.9% |
    | ③ **回落原串序** | 有冲突 **且** 无企微绑定 / 企微人对不上 | 取串中**最后一位** | 163 / 3,918 = 4.2% |

    - ②③ 的冲突判定结果落盘在 `out/claim_public_pool/conflict_resolution.json`（`resolve` 子命令生成，只读）
    - ⚠ 三级规则下 **3,918 位全部可判定**，不再有人工空白；`06/07/08_冲突*.csv` 三表把 394 位冲突客户按判定依据拆开给业务方复核
    - ⚠ ③ 是**已知的抛硬币级信号**（见上节 35.7%），仅作兜底；若要严格，③ 部分须人工确认

    ### 池 = **会员等级**分层，不是消费金额（2026-10-10 采样反推）


    | 会员等级 `memberLevelName` | → 个人池 | 回测命中 |
    |---|---|---|
    | `非会员` | `1-3000`（**25% 实际进 `新客池`**） | 9/12 |
    | `零星` | `1-3000` | 10/12 |
    | `零星3000` | `3000-10000` | **12/12** |
    | `一星10000` ~ `三星30000` | `星级活跃` / `星级非活跃` | 10-11/12 |
    | `四星40000` | 星级 | **12/12** |
    | `五星50000` | 星级活跃（**实际 50/50**） | 11/12 |

    反证：`零星` 消费 ¥1,380 → `流失-非星级`；`零星3000` 消费 ¥2,980 → `3000-10000` —— **跟等级不跟金额**。

    **回测（2026-10-10）**：拿 96 位**已有归属**的凯德老客户逐等级分层核验，**总命中 88.5%** ——
    规则方向正确，但有两处例外维度必须知道：
    - `非会员` 有约 25% 实际落在 **`新客池`**
    - 各等级都有零星客户落在 **`外地顾客`**（凯德共 **9 种池**：`新客池`/`渠道顾客`/`外地顾客`/`备孕·孕期`/`退费意向`/`1-3000`/`3000-10000`/`星级活跃`/`星级非活跃`）
    - ⚠ 星级「活跃/非活跃」在各等级内约 **50/50**，与「近 365 天到店」的对应**弱** → 该判定只是**近似**

    ⚠ 公共池 `流失-非星级` / `失效顾客` 是「无归属」客户的默认落点，**不是价值分层**，
    所以「公共池客户划回个人池」时必须**重新按等级选池**，不能沿用原池。

    ⚠️ **业务提醒**：公共池无归属客户普遍**已深度沉睡**（抽检 20 位中 19 位 497~1,746 天未到店，最久 4.8 年）
    → 按等级直接送进 `1-3000`/`3000-10000`/`星级非活跃` 会**让咨询师的池虚胖**（僵尸混入在营池）。
    放量前必须先与业务方确定目标池策略。

    **公共池划回流水线**：`漾肤/数据之眼/claim_public_pool.py`
    （`build` 全量清单 / `demo --who X` 单客户只读效果预览 / `run --execute` / `verify` / `rollback`；
    `--who` 支持逗号多选，可传 cid / 姓名 / 会员号）

    🔴🔴 **硬约束（李刚 2026-10-10 定）：三位咨询师名下「现在已有归属」的客户一律不转交** ——
    只处理「公共池 + 归属为空」的客户。落实在三处，缺一不可：
    1. 清单侧：`targets()` 只取 `consultant` 为空者
    2. 写入侧：`cmd_run` 里**无条件硬拦截**（`if st["sysUserName"]: 🔒跳过`），无任何开关可绕过
    3. **快照滞后修正**：master 快照落后于实际，必须再剔除「本地台账显示已写入」的 cid
       （`build_claim_lists.py active_written_cids()` = 全部写入 ledger − 全部回滚 ledger）

    **明细生成流水线（100% 只读，给业务方确认用）**：`漾肤/数据之眼/build_claim_lists.py`
    （`build` 生成 3 份按咨询师拆分明细 + 全量 + 高价值优先 + 总览 CSV；`verify-live --n 300` 抽样实时核对；`report` 生成 HTML 总览）
    产出 `out/claim_public_pool/lists_<stamp>/`。
    实测（2026-10-10）：**3,918 位**（已剔 5 位台账已写入者：姜宥萌+张鸣/李薇/吕妍+彭影）；
    判定依据 = 唯一命中 3,524 ／ 企微归属 231 ／ 回落串序 163；抽样 300 位实时核对 **已有归属=0、不在公共池=0** ✅

    实测（2026-10-10）：姜宥萌（消费 ¥38,690 / 三星30000 / 无归属 / 池 `失效顾客`）→ **`星级非活跃` + 归属 汪怡辰**；
    另跑 3 人（张鸣/李薇/吕妍，覆盖 `1-3000`/`星级非活跃`/`3000-10000` 三种池）**3/3 成功 + 独立回查一致**。
    其中李薇的 `relatedConsul` = `刘艳,汪怡辰`，**「刘艳」是店长不是咨询师，被白名单正确滤掉** ✅

    **🔴 归属划回写入流水线（李刚 2026-10-10 指令）**：`漾肤/数据之眼/claim_highvalue.py`
    （`plan` 只读预览+落清单 / `run --execute` 写入 / `verify --ledger` 独立回查）
    - **它复用 `build_claim_lists.apply_resolution()` 三级判定** —— ⚠ 与老 `claim_public_pool.py run` 的
      「直接取串中末位」**不同**，批量写必须用这个，否则判定口径与批准清单不一致
    - 参数：**`--days-le N`**（未到店天数上限）｜**`--hv N|none`**（价值门槛，默认 `3000`；`none` = 不过滤）
    - 过滤链 = 公共池无归属有价值 → 剔台账已写入 → 三级判定 → `--days-le` → `--hv` → **排除李刚本人档案**（`vip 003834`）
    - ⚠ **口径陷阱**：`build_claim_lists` 里 `prio(x)>=2` 实为「未划扣>0 **或 消费≥¥10,000**」，
      与它自己打印的标签「≥¥3,000」**不一致**（旧 bug，3,918 时应为 1xx 却显示 87）
    - ⚠ **沉睡天数的「缺失值」口径**：`build_claim_lists` 把 `days_no_arrive=None` 当 `0` 计入「≤365 天」；
      `claim_highvalue` 当「未知」**排除**（更正确）。实测差 1 位 = `【游客】优优`（vip 011141，无到店日期）
    - 实测（2026-10-10，两批共 **267 位**，**全部写入 100% + 独立 verify 0 不一致**）：
      | 批次 | 条数 | 归属分布 |
      |---|---|---|
      | ① 高价值（`--hv 3000`） | **108** | 汪怡辰 52 ／ 潘婷 29 ／ 赵翊妗 27 |
      | ② 沉睡≤365 天（`--days-le 365 --hv none`） | **159** | 赵翊妗 61 ／ 汪怡辰 57 ／ 潘婷 41 |
      台账 `out/claim_public_pool/20261010_164851_高价值划回_ledger.jsonl` ／ `20261010_170153_归属划回_ledger.jsonl`
    - ⚠ 写入后清单要**重跑**（`build_claim_lists.py build`）——`active_written_cids()` 会把这批剔掉，
      3,918 → 3,809（剔①）→ **3,650**（再剔②）

    **安全检查流水线（全只读）**：`漾肤/数据之眼/spot_check_claim.py`
    （`ledger` 证明台账真写了几位 + 随机抽查目标客户是否仍无归属 / `sample --n 20` 分层抽检池规则核对 /
    `backtest --per-level 12` 用已有归属客户回测「等级→池」命中率）

    **凯德店三位在职咨询师的 hex id（即 `transfer-pool.sysUserId` 应传的值）**：
    潘婷 `b941c6e29da42369cc06e78e386f3ac5` ｜ 汪怡辰 `e8ba5317e58db26282e5620eee861a02` ｜
    赵翊妗 `bcf0b12bfb2ba63e37a34ae0576cd9f1`
    ⚠️ `customer-by-id` **不返回 `poolId`**（只有 `poolName`）→ 「取当前池原样传回」必须先用
    `poolName` 去 `get-pool-info` 反查 `poolId`。

    **最小可用调用链（只读两查 + 一写）**：
    ```python
    info = cli.get("/api/v1/tpos/customer/get-pool-info", params={"customerId": cid})  # 拿 poolId
    cli.post("/api/v1/tpos/customer/transfer-pool", {
        "customerId": cid,
        "poolId": POOL_ID,                       # 必填；决定「哪个池」
        "sysUserId": CONSULTANT_HEX,             # 决定「归谁」；只在个人池生效
        "syncVisitPlan": True,                   # 必填；回访计划一并转（凌晨 3 点执行）
        "transferWxFlag": False,                 # 企微好友是否一起转（先用 customer-qw-info 判）
        "reason": "归属调整",
    })
    # 回查验证（必做）：
    cli.get("/api/v1/tpos/customer/customer-by-id", params={"customerId": cid})  # 看 sysUserId/sysUserName/poolName
    ```

    - **`transferWxFlag=true`** 把**企微好友关系一起转**（文档注明"只能是企微客户才能操作"，用 `customer-qw-info` 判）
    - **`syncVisitPlan=true`** 把原咨询师的**回访计划一起转**给新咨询师
    - ⚠️ `syncVisitPlan` **不是实时**，**每天凌晨 3:00 定时执行** —— 不要当天转完就期待立即生效
    - ⚠️ `poolId` 是**必填**。只想换咨询师、不想换池子 → 先用 `get-pool-info` 拿到当前池 id 原样传回
    - ⚠️ 客户资料字段里的归属人是 **hex id**，`transfer-pool` 的 `sysUserId` 要传 **hex**（走 `user/get-page` 的 `id`），不是短账号

24. **深翻页硬限：`customer-search` 翻到第 21 页返回 `code:20002`**
    `page` 分页最多约 **20 页 × 500 = 10,000 条**（实测第 21 页即失败）。
    → 超过 1 万条必须改用 **`lastCustomerId` 游标**：把上一批最后一条的 `id` 传进去，`page` 恒传 1。
    实测用游标 40 批拉完 19,519 条，**47 秒**，无一次失败。
    （`get-visit-page` 没有游标参数，只能靠第 17 条的"失败重试 + 中止告警"兜底。）

25. **🔴 客户档案里「咨询师 / 归属」是三个不同字段，别混用（2026-09-16 实测）**

    | 字段 | 含义 | 认知 |
    |---|---|---|
    | `sysUserId` / `sysUserName` | **客户池归属人**（系统主归属，当前负责人） | ✅ 唯一权威的「当前咨询师归属」 |
    | `relatedConsul` | **历史关联咨询师串**（逗号拼接，记录**谁曾经服务过**） | ❌ **不是当前归属**，是历史事实；不会随转移而更新 |
    | `roleManagerInfoList[roleName=咨询师]` | **岗位负责人**（客户档案页那个区） | 独立字段，**非标配**，全店仅 3.7% 客户有 |

    实测：`transfer-pool` 只改 ①`sysUserName`，**不动 ②③**。
    两者都有值时 ① 与 ③ 一致率 99.5%（③ 是跟着 ① 手填的，不是自动同步）。

    ⚠️ **最易踩的坑**：写派单/归属解析逻辑时若把 `relatedConsul` 排在 `sysUserName` 之前，
    会把客户派给「历史上第一个服务过的人」而不是「现在的负责人」——
    实测抽样正确率只有 70%，全量 931 位（4.8%）派错。
    **正确顺序：`sysUserName` → 其他 → `relatedConsul` 兜底**（老公共池客户 `sysUserName` 为空才回退）。

    「岗位负责人」相关接口：
    - `GET /api/v1/tpos/customer/get-customer-rolemanager-config?tenantId=` → 门店可配岗位
      （凯德店 4 个：皮肤管理师 / 护士 / **咨询师 `daefdb7d4d392d2846563c1e6dd89f89`** / 医生）
    - `POST /api/v1/tpos/customer/edit-customer-rolemanager` body `{customerId, roleManagerId, userIdList}`
      （`userIdList` 传空数组＝删除配置）
      ⚠️ `roleManagerId` 文档写「负责岗位id」但未说明取 config 的 `id` 还是 `roleId` —— **未实测，用前先测 1 条**。

    📊 **岗位负责人覆盖率与池子价值正相关**（凯德店 19,519 位，2026-09-16 普查）：
    1-3000 池 5.1% / 3000-10000 池 11.4% / 星级活跃 12.1% / 星级非活跃 14.9% / 外地顾客 23.1%；
    流失-非星级 2.2%、默认非个人池 0%、报备池 0%。→ **它是高价值客户的运营习惯，不是系统强制字段。**
    → 批量给客户补「咨询师」岗位负责人之前，先确认下游逻辑是否真的读它（多数只读 `sysUserName`）。

26. **⚠️⚠️⚠️ `visit/get-visit-page` 三连坑：单窗口 1 万条硬顶 + 执行人字段 + 企微群发回写（2026-09-17 实测）**

    **(a) 单窗口最多 1 万条，第 51 页返回 `code:20002`** —— **极端密度下必须拆到「秒级」**：

    | 切窗粒度 | 8/28 单日实得 | 结果 |
    |---|---|---|
    | 按小时 | 10,000 | ❌ 撞顶，静默少 1,938 |
    | 按分钟（10:17） | 10,000 | ❌ **单分钟就超 1 万** |
    | **按 10 秒** | 1,386 + 10,496 = **11,882** | ✅ 对上 |

    → **判据：分窗求和必须 = 服务端当日 total**（本批 11,938 = 11,882 伪标 + 56 真实），
    对不上就是还在撞顶，**不会报错**。同类硬限：`customer-search` 第 21 页起 20002。

    **(b) 「计划执行人」是 `userId`（字符串数组，形如 `['"e8ba5317…"']`），不是 `visitedBy`**
    `visitedBy` / `visitedById` 是**实际回访人**；**待回访记录本来就为空**。
    → 曾拿 `visitedBy` 判「待回访有没有指派」→ 误得「100% 未指派」，实际指派率 **97.4%**。
    → 归属人取 `userId`（regex 抠 32 位 hex），完成情况看 `visitedFlag`（`True`/`False`）。

    **(c) 🔴 数据污染识别：`visitTypeName = 「企业微信」` + 同秒批量 + `response` 去重=1**
    实测 2026-08-28 **11,882 条**「已回访」压在 **10:16:57–10:17:14 共 16 秒**内、
    `visitedById` 同一人、`response` 去重 **= 1**（同一句营销话术）、`delayFlag=True` 11,601 条
    → **一次企微营销群发被系统回写成「回访完成」**。
    → **渠道枚举可作判据**：实测真实回访 100% 为 `visitTypeName=电话`（8/19/8/25/9/10 共 370 条全是电话），
      而 8/28 那批 **100% 为「企业微信」** —— 渠道字段一拉就能把批量污染筛出来。
    → **凡「已回访量」突增，先按 `visitedDate` 秒级聚簇 + `response` 去重 + `visitTypeName` 三查**；此类批不得计入考核。

27. **🔴 回访模板 / 计划生成机制（2026-09-17 实测，文档与实现不一致）**

    **(a) `get-visit-page` 不回吐 `templateId`，也不回吐 `day`**
    - `content` = 模板正文（**「第 N 天」是写在正文文字里的**，不是字段）
    - `day` **恒为 `None`** → 想按天节点分析，只能从 `content` 里正则抠
    - `type` / `typeId` = 计划类型：`1` 治疗后回访 ｜ `81` 邀约回访 ｜ `11` 疗程教育回访 ｜ `2` 咨询未成交回访
    - `visitType` / `visitTypeName` = 回访渠道（`40` 电话 ｜ `45` 企业微信 ｜ `41` 微信 ｜ `42` 现场），**待回访记录该字段为空**

    **(b) 模板相关三个端点（⚠️ 文档描述与实现不符，勿照文档写）**

    | 端点 | 文档说返回 | **实测返回** | 可用参数 |
    |---|---|---|---|
    | `visit/visit-template-type` | 模板类型 | ✅ **项目分类树**（皮肤管理／皮肤科(轻医美)／无创科(轻医美)） | 无 |
    | `visit/visit-template-data-type` | `label`=模板id、`value`=模板名 | ⚠️ **该分类下的项目列表**（不是模板） | `typeId`=**项目分类 value**（缺 → `20004`） |
    | `visit/visit-template-content` | `SysTemplateVo` | ✅ 一致（`name`/`type`/`contentList`/`visitManIdAndNameVos`） | `id`=**模板 id**（缺 → `20004`；id 不匹配 → `10000` + `data:null`，不报错） |

    分类 value 实测：皮肤管理 `211ceccec76011eca1100242ac110003`、皮肤科(轻医美) `211ced0dc76011eca1100242ac110003`、无创科(轻医美) `211ced59c76011eca1100242ac110003`。

    **(c) 🚫 没有「列出全部回访模板」的端点** → 需要模板清单时，只能**从计划记录 `content` 去重反推**
    （本项目实测：3,346 条计划 → 38 个模板变体／21 个「动作 × 天节点」语义族）。

    **(d) `create-visit` 支持 `templateId` / `templateName` 入参，但 `get-visit-page` 不回吐** →
    **新建计划时能带，事后无法做「计划 → 模板」反查**。若业务需要模板级追踪，必须在**写入时自行落库记录**。

    **(e) 🔴 计划重复的机制性根因（业务侧，非接口 bug）** —— 2026-09-17 李刚权威口径修正
    🔑 **「回访模板和项目没有关联，只有回访规则才和项目有关联。」**
    → **模板与项目解耦**（38 个模板是人工建的）；真正决定「生成几条计划」的是**回访规则**，
      规则**按项目分别建了多份**（平行规则）→ 一个客户同一天命中多条 → 重复计划。
    → 实测近 30 天同客户×同日×同语义族重复 **767 条（22.9%）**，同客户同日挂多个执行人 **136 组**。
    → 767 条拆解（决定性）：**743 条（96.9%）= 不同模板 = 不同项目规则**（合规则可消）；
      **24 条 = 同模板被触发两次**（规则配重 / 触发重复）。
    → 根治顺序：**① 合并平行回访规则（纯配置、零研发消 96.9%）② 合并模板（配套）③ 生成层唯一键去重（仅当规则只能选 1 个项目时）**。
    ⚠️ 只做模板合并 **不减计划条数**（模板与项目无关联）——别把两者收益混算。

    **(f) 🚫🚫 模板与「回访规则」**全无写能力**，只能人工在后台改（2026-09-18 复核）**
    - 文档内 `api/v1/tpos/` 路径共 **161 个**；含 `template` 的**只有 3 个，且全是 GET**
      （`visit-template-type` / `visit-template-data-type` / `visit-template-content`）
      → **没有「改模板名 / 删模板 / 改模板内容 / 批量编辑模板」任何写接口**。
    - **「回访规则」连读接口都没有**：全文检索 161 个路径，`rule` 仅命中 `basic/member-rules`（会员规则，与回访无关）；
      文档正文「回访规则」四字**零出现** → 规则既读不到也改不了。
    - ⇒ 模板 / 规则的任何变更，**只有两条路**：① 睿美云后台人工点（推荐，可控可审计）
      ② 浏览器自动化模拟后台操作（未文档化内部接口，**不猜不调**；需先抓包确认接口存在 + 有回滚）。
    - ⇒ 反过来看：既然模板改动**不影响业务结果**，为它引入「未文档化接口 + 无回滚」风险**不划算**。

    **(g) ✅ 计划层「清理重复」的可自动化通道（2026-09-18 复核）**
    - 🚫 `visit/obsolete-visit`（真作废）**实测对开放账号一律 `code:401`**，其 `contentId` 为孤儿字段
      （无任何接口产出/消费）→ **契约缺陷，不可用**，待睿美云答复。
    - ✅ **替代通道：`visit/complete-visit`** —— `{planId, visitedBy, visitType, response}` 可把记录
      从「待回访」**结清为「已回访」**，`response` 写明清理原因 → 效果等同「从队列清掉」且**可审计**。
    - 现成脚本：`数据之眼/void_0826_marketing.py`（默认 dry-run、`.void_state_*.json` 断点续传、
      逐条回读校验、限速 0.3s/条；换目标特征即可复用）。
    - ⚠️ **这是治标**：规则不合并，清掉的重复还会再长出来。且重复项里**已回访的不用清**
      （实测 767 条中：448 条已回访 / **319 条待回访且已过期** ← 只有这 319 条是活噪音）。

    **(h) ✅✅ `get-visit-page` 支持 `customerId` 过滤（2026-09-20 新发现，查单个客户强烈建议用）**
    - 以前查一个客户只能按月开窗全量翻（全区间 **33,574 条**）、慢且易因窗口/分页漏记录；
      带 `customerId` 后**一次请求返回该客户全部计划**（实测某客户全区间 **44 条**，1 次调用）。
    - ⚠️ **`vipNum` 传了会被静默忽略**（实测传会员号仍返回全量 33,574 条，`code=10000` 不报错）→ **只能用 `customerId`**（`customerIds` 数组亦可）。
    - ⚠️ 仍建议客户端二次过滤 `[x for x in lst if x["customerId"]==CID]`（防参数被忽略时静默拿到全量）。
    - `visitedFlag` 三桶**实测语义**：`"1"`=待回访 ｜ `"2"`=已回访 ｜ `"3"`=空桶（某客户实测 1→4 条、2→2 条、3→0 条）；
      **`["1","2"]` 与 `["1","2","3"]` 结果相同** ⇒ `"3"` 对本店无贡献。
      - 🔴 **更正（2026-10-12）**：旧记「`"0"` 与不传等效（=全量）」**不成立** —— 实测客户 `003653`：`["0"]`=758 ｜ **不传=614** ｜ `["1"]`=1。
        且**不传时接口默认把「已回访」排在前**（page1-3 共 613 条全是 `visitedFlag=True`，待回访那条在 page4）
        ⇒ **查待回访必须显式带 `["1"]`**，用「不传」当全量或只查 page1 都会误判。详见注意事项 28。

    **(i) 🔴 `treated-page-review`（到店/治疗记录）三个易错点（2026-09-20 实测全踩）**
    - **路径在 `/api/v1/tpos/treat/`，不是 `/visit/`** —— 写错返回 **`code=401`「没有找到您要的资源」，
      伪装成鉴权失效**（实际是路径错）。
    - **方法是 GET，不是 POST** —— POST 返回 `code=20002`「Request method 'POST' not supported」。
    - **时间参数名是 `treatTimeStart` / `treatTimeEnd`**（不是 `startTime`/`endTime`）；
      返回的时间字段是 **`treatmentTime`**（不是 `treatTime`），另含 `deductTime` / `deductUserName` /
      `verifyTime` / `verifyStatus` / `treatDeptName` / `treatRecordNo` / `projectList`。
    - ✅ 同样支持 **`customerId`** 过滤（GET + `customerId`）。

28. **🔴🔴 写回访计划后「回查」的两个致命误判（2026-10-12 实测 1,143 条写入验证中踩全）**

    背景：用 `visit/create-visit` 批量建计划（2026-10-12 实写 1,143 条，2 批，**零失败 + 逐条回查 100% 一致**），
    回查环节踩了两个坑，**都会把「写入成功」误判为「写入失败」**。

    **(a) 写读口径不对称：`create-visit` 入参与 `get-visit-page` 回吐不是同一套值**

    | 字段 | 写入（`create-visit`） | 回吐（`get-visit-page`） |
    |---|---|---|
    | `type` | **码值** `"81"`（邀约回访） | **中文名** `"邀约回访"` |
    | `visitDate` | **日期字符串** `"2026-10-12"` | **毫秒时间戳 int** `1791734400000` |
    | `userId` | `["<32hex>"]` 数组 | **带内嵌双引号** `'"e8ba5317…"'` （须 `strip('"')` 或抠 32 位 hex） |

    ⇒ 回查判据必须写：
    ```python
    CST = timezone(timedelta(hours=8))
    ts2d = lambda v: datetime.fromtimestamp(int(v)/1000, CST).strftime("%Y-%m-%d")
    is_ours = (ts2d(x["visitDate"]) == "2026-10-12"
               and str(x["type"]).strip() == "邀约回访"      # ⚠ 不是 "81"
               and not x["visitedFlag"])                     # ⚠ False = 待回访
    ```

    **(b) 🔴🔴 查「待回访」必须带 `visitedFlag:["1"]`；不带则接口默认把「已回访」排在前面**
    实测客户 `003653`：不传 `visitedFlag` 时 `total=614`，**page1/2/3 共 613 条全是 `visitedFlag=True`**，
    那条待回访计划落在 **page4 第 14 条** ⇒ **逐客户只查 page1 必误报「完全查不到」**。

    - ⚠ **字段值方向相反**：**筛选** `"1"` = **待回访**；**记录字段** `visitedFlag` 回吐**布尔**，**`False` 才是待回访**。
    - ⚠ **桶 `total` 互不相等**（同客户）：`["1"]`=**1** ｜ `["0"]`=**758** ｜ **不传=614**
      ⇒ 旧记「`"0"` 与不传等效 = 全量」**不成立**，别拿不传当全量。
    - ⚠ 带 `customerId` 时**响应仍混入其他客户记录** → 必须再按 `x["customerId"]==cid` 过滤；单客户全量可达 4 页。
    - ⚠ `size=200` 会被大客户 200+ 条历史挤掉 → 建后回查用 `visitedFlag:["1"]` 时 total 精确 = 1，最干净。

    **(c) ✅ 全量对账正解：按 `content + visitDate` 归集，不要按 `userId` 数**
    - 同一天必然并存「本次计划」与「日常治疗后回访」→ 只用「今天/某执行人」计数会把两者混算。
    - 正解：拉 `visitedFlag:["1"]` 全量翻页（**用响应 `pages` 判停，不能用「不满页=末页」**），
      按 `content == "<计划标题>"` 且 `ts2d(visitDate) == <日期>` 命中归集。
    - 实测：全店待回访 5,598，命中本次标题 **1,138 条** ＋ **5 条当天已被员工标记完成** = 计划 1,143 **1:1 闭合**；
      「同标题但非今天」的记录 = **0** ⇒ 归集唯一，无重名污染。
    - 现成实现：`数据之眼/断联回访计划_20261012/{plan_visit.py, reconcile_visit.py, check_drift.py}`。
    - ⚠️ 缺 `tenantId` → `code=20002`（同族接口通病）。

    **(j) 🔑 计划「生成机制」正解 —— 治疗日一次性铺满整串（2026-09-20 立，回答「为什么有 N 条」必读）**
    - **计划不是每天滚动生成，而是治疗日当天把整串节点一次建完**；日期到达只是把某条从「未到期」
      变成「今日待回访」，**不会再新增记录**；只有**再做一次治疗**才会长出新的一串。
      ⇒ 客户问「昨天生成了 N 条、今天为什么没有生成」，答案是「本来就不该每天生成」。
    - **节点数 = 「这次做了几个项目 × 各项目对应规则有几个时间点」**，与模板无关
      （再次印证 (e) 的李刚口径）。
      实测同客户：单项目「超光子全模式」→ **4 条**（偏移 `+1/+29/+59/+89`，两次治疗完全同构）；
      双项目「胶原针-三型+超光子全模式」→ **7 条**；双项目「水光针-胶原+超光子AOPT」→ **5 条**。
      注射类另有远期节点（`+270` 天级）。
    - **判「同一批」的依据 = planId 连号**（planId 是单调递增雪花号）。实测某批 4 条落在
      `542299379319439365` ~ `542299380565147651` 窄区间，且在全店当日新生成记录里**位置连续**。
      ⚠️ planId **有两种形态**：① 数字雪花（系统按规则自动生成，可聚批）
      ② **32 位 hex**（如 `82c148cbf6f445659d0020ea85d3c361`，疑似**人工在后台建单**）→ 两者不能混比。
      聚批阈值参考：同批相邻间隔 ≤ 6.5e8、换批间隔 ≥ 1.0e10 → **取 2e9 安全**。
    - 🔴 **业务副产物：原生「治疗后回访」执行人 = 划扣/治疗执行人**（不是客户档案归属咨询师）。
      轻医美中心的划扣人是**护士**、皮肤管理中心是**皮管师** → 归属咨询师**在自己的待回访里看不到这些客户**。
      这是「计划指派 vs 客户档案归属一致率低」的机制性成因，做归属解析/派单时必须知道。
    - 现成工具：`数据之眼/diag_customer_plans.py <客户名|cid>` —— 单客计划诊断
      （输出计划表 + 治疗表 + planId 聚批 + 今日到期 + 待回访合计）。

## 调用流程建议
1. **先按任务定位接口**：查 `references/api_capability_map.md` 第 1 节反查表 → 第 3 节核对方法/路径/关键参数/坑位；写入需求再看第 4 节审批清单与第 5 节「文档未标注方法」。若确定走官方 MCP 通道，改读 `references/official_mcp.md`。
2. 确认凭据已配置（环境变量或 `~/.workbuddy/secrets/ruimei_tpos.json`）。
3. 用 `references/rmy_client.py` 的 `RmyClient.get/post` 发起请求，自动附带 TPOS 签名（成功码用 `classify_response()` 判定，别硬编码 `==10000`）。
4. 分页接口用 `paginate_get` / `paginate_post` 自动翻页；按时间分片把单批压到 1 万条以内，失败要重试+告警，别用残缺数据下结论。
5. 遇到字段/枚举不确定，按能力地图给的 `L<行号>` 跳到 `references/ruimeiyun_api_full.md` 对应章节；枚举看本文件「常用枚举」。

## 内置容错（2026-08-28 加固，已内置于 rmy_client，无需额外编码）

| 能力 | 行为 |
|---|---|
| 服务器时钟补偿 | 每次响应从 `Date` 头学习本机与服务器偏差，偏差 > 30 秒自动补偿签名时间戳（TPOS 容差 1 分钟） |
| 重试与退避 | GET 默认可重试 3 次（HTTP 429/5xx、网络异常、鉴权时序错误），等待 0.5s → 1s → 2s 指数退避 |
| 写操作保护 | POST 默认**不重试**（防重复写入）；确需重试显式传 `retry=True` |
| nonce 加固 | `hostname 摘要 + pid + secrets 强随机`，保证 1 分钟内跨进程、跨机器全局唯一 |
| 响应分类 | `classify_response()` 返回 `success / auth / server / business`，`retryable` 指明是否可重试 |

可调环境变量：`RMY_MAX_RETRIES`（默认 3）、`RMY_BACKOFF_BASE`（默认 0.5）。

## MCP 调用（跨工具入口）

睿美云数据有 **3 条通道**，别混用：

| 通道 | 认证 | 能力 | 何时用 |
|---|---|---|---|
| **TPOS REST 直连**（`references/rmy_client.py`） | TPOS RSA 签名 4 Header | 178 个接口可读可写、参数粒度最细 | **默认**，客户明细必走这里 |
| **自带 stdio MCP `ruimei-tpos`**（`scripts/rmy_mcp_server.py`） | 内部封装同一套签名 | 6 个快捷工具 + `rmy_call` 透传 | 跨工具调用、快速自检 |
| **睿美云官方 MCP `rmy`** | `appKey`，权限继承睿美云账号 | **92 个函数**（86 查询 + 3 写 + 1 自省 + 2 文档独有），清单见 `references/official_mcp_functions.md` | 只查官方封装好的数据 |

🔴 官方 MCP 的完整资料见 **`references/official_mcp.md`**（2026-11-22 从飞书《睿美云 MCP 工具》
11月20日版整理）：配置写法、`appKey` 与 MCP url 取值步骤、测试环境地址、传输方式实测结论。
**全量函数清单**（2026-11-22 实拉 `readQueryMcpDocs` + `tools/list`）见
`references/official_mcp_functions.md`（人读）/ `.json`（机读）；
刷新重跑 `python3 scripts/fetch_official_mcp_docs.py`。

⚠️ **官方 MCP 客户维度函数不可信**（注意事项 6/11）：治疗/开单/回访/咨询/接待/开发计划
一律返回「没有查到…」，`getPageCustomerInfo` 分页不可靠；**不要用「没查到」推断客户没有数据**。
新增的 `...ByCustomerIdList` 批量版未实测，首次使用须用已知有数据的客户验证。
3 个写工具（`markManualOrder` / `restoreWxByVipNums` / `unbindWxByVipNums`）**绝不自动调用**。
本机 `rmy` 已改为 `type: streamable-http` + `disabled: false`（旧 SSE 实测 405，见 `official_mcp.md` §7）；
配置改动不会自动激活当前会话，仍需在「连接器管理 → 自定义连接器」对 `rmy` 点「信任」。

### 自带 stdio MCP：`ruimei-tpos`

已在 `~/.workbuddy/mcp.json` 注册，与官方 `rmy` 并存、互不冲突。

| 工具 | 作用 | 类型 |
|---|---|---|
| `rmy_health` | 连通性自检（验证签名 / 网络 / 授权） | 只读 |
| `rmy_search_customer` | 按关键字搜索客户 | 只读 |
| `rmy_get_customer` | 按客户 id 查详情 | 只读 |
| `rmy_visit_records` | 查历史回访记录 | 只读 |
| `rmy_quick_visit` | 快速创建「已回访」记录 | **写入** |
| `rmy_call` | 通用透传，可调用全部 TPOS 接口 | 视方法而定 |

启用：打开 WorkBuddy「连接器管理 → 自定义连接器」，对 `ruimei-tpos` 点击「信任」后生效。其它支持 MCP 的客户端（Claude Desktop / Cursor 等）可复用同一配置。

## 跨机器使用（Mac mini / MacBook Air / 服务器）

1. 技能本体已放入 iCloud 共享技能库（`shared-skills/sources/codex-custom/ruimeiyun-openapi`），本地 `~/.workbuddy/skills/ruimeiyun-openapi` 为 symlink，双机自动一致。
2. **凭据不同步**：`~/.workbuddy/secrets/ruimei_tpos.json` 不参与 iCloud 同步，每台机器需单独放置（或用环境变量 `RMY_*` 注入），避免明文私钥上传云端。
3. 新机器接入：拉取 iCloud 后执行
   `ln -s "$HOME/Library/Mobile Documents/com~apple~CloudDocs/Downloads/workbuddy/.workbuddy/shared-skills/sources/codex-custom/ruimeiyun-openapi" "$HOME/.workbuddy/skills/ruimeiyun-openapi"`
4. **必须开启 NTP 自动对时**：TPOS 签名依赖时间戳（容差 1 分钟），时钟漂移会直接导致签名失败。
5. 部署到 VPS（如企微侧边栏 relay_server）时，凭据走服务器环境变量或 600 权限文件，禁止从 iCloud 拉取。
