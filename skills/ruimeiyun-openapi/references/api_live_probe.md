# TPOS 接口生产实测校准（2026-11-22）

> **性质**：对**成都武侯漾肤生产环境**做的**只读**抽样，用于校准 `api_capability_map.md` 的文档结论。
> **环境**：`https://cdyangfu.hospital.realmerit.com.cn`｜账号 `boss`｜凭证来自
> `~/.workbuddy/secrets/ruimei_tpos.json`（本文件不记录任何私钥 / appKey / 密码）。
> **范围**：25 个只读用例 + 3 个诊断用例，**0 个写接口**（57 个语义写接口一个都没碰）。
> **复现**：`python3 scripts/probe_readonly.py [结果JSON路径]`，串行、每条 `size=1`、不打印客户数据。
> 探测窗口：近 7 天；执行时间 2026-11-22 23:19。

## 1. 汇总

| 判定 | 数量 | 含义 |
|---|---:|---|
| ✅ OK（`code 10000` / `10001`） | 20 | 接口可达且正常返回 |
| ⚠️ `code 20002` | 2 | 请求方法/参数不被受理（见 §3） |
| 🔴 `code 2001` | 3 | **账号未授权**，需睿美云开通（见 §3） |
| 网络失败 / 鉴权失败 | 0 | TPOS RSA 签名、时间戳、账号权限均正常 |

响应耗时：常规接口 **0.07–2.13s**；`consultation/page` **22.6s**（唯一慢接口）。

## 2. 逐接口结果

| 用例 | 方法 | 路径 | code | 判定 | 耗时 | 返回规模 |
|---|---|---|---:|---|---:|---|
| 门店清单 | `GET` | `/api/v1/tpos/common/tenantList` | 10000 | OK | 0.12s | list=2 |
| 客户搜索 | `GET` | `/api/v1/tpos/customer/customer-search` | 10000 | OK | 0.18s | records=1 |
| 客户详情 | `GET` | `/api/v1/tpos/customer/customer-by-id` | 10000 | OK | 0.09s | - |
| 部门树 | `GET` | `/api/v1/tpos/basic/dept-tree` | 10000 | OK | 0.08s | list=1 |
| 在职员工 | `GET` | `/api/v1/tpos/user/get-page` | 10001 | OK | 0.13s | records=1 |
| 岗位列表 | `GET` | `/api/v1/tpos/role/getRoleListV2` | 10001 | OK | 0.11s | list=36 |
| 回访类型 | `GET` | `/api/v1/tpos/visit/get-visit-type` | 10000 | OK | 0.10s | list=30 |
| 回访方式 | `GET` | `/api/v1/tpos/visit/get-visit-way-type` | 10000 | OK | 0.09s | list=6 |
| 回访分页(待回访) | `POST` | `/api/v1/tpos/visit/get-visit-page` | 10000 | OK | 0.23s | records=1 |
| 回访模板分类 | `GET` | `/api/v1/tpos/visit/visit-template-type` | 10000 | OK | 0.16s | list=1 |
| 订单列表 | `GET` | `/api/v1/tpos/order/billing-page` | 10001 | OK | 0.70s | records=1 |
| 收银记录初始化 | `GET` | `/api/v1/tpos/report/cashier-record-init` | 10000 | OK | 0.68s | dict |
| 收银记录报表 | `POST` | `/api/v1/tpos/report/cashier-record-page` | 10000 | OK | 2.13s | result=1 |
| 治疗分页(近7天) | `GET` | `/api/v1/tpos/treat/treated-page-review` | 10000 | OK | 0.52s | records=1 |
| 项目分页 | `GET` | `/api/v1/tpos/basic/project-page` | 10000 | OK | 0.13s | records=1 |
| 卡券分页 | `GET` | `/api/v1/tpos/coupon/coupon-page` | 10000 | OK | 0.13s | records=1 |
| 入库分页 | `GET` | `/api/v1/tpos/inventory/storage-page` | 10000 | OK | 0.99s | records=1 |
| 预约分页 | `GET` | `/api/v1/tpos/cusbespeak/get-page` | 20002 | ⚠️ | 0.29s | - |
| 字典 | `GET` | `/api/v1/tpos/sysdict/dictlist` | 10000 | OK | 0.08s | list=0 |
| 咨询分页 | `POST` | `/api/v1/tpos/consultation/page` | 10000 | OK | 22.60s | records=1 |
| 开发计划(存疑) | `GET` | `/api/v1/tpos/customer/get-all-plan` | 10000 | OK | 0.09s | dict |
| 客户部分标签(存疑) | `GET` | `/api/v1/tpos/customer/part-label-list` | 2001 | 🔴 | 0.12s | - |
| 接诊工具(存疑) | `GET` | `/api/v1/tpos/consultation/acceptance-tool` | 2001 | 🔴 | 0.07s | - |
| 可购买权益卡(存疑) | `GET` | `/api/v1/tpos/basic/get-can-buy-equity-card-list` | 20002 | ⚠️ | 0.30s | - |
| 权益卡详情(存疑) | `GET` | `/api/v1/tpos/basic/get-equity-card-detail` | 2001 | 🔴 | 0.07s | - |

> 「返回规模」只记录条数/结构，**不含任何客户数据**。`list=0` 的字典用例用了占位 `code=test`，属正常空结果。

## 3. 关键结论（🔴 = 会直接误导调用）

### 3.1 成功码确实是两种，别硬编码 `==10000`
`10000`（msg「操作成功」）与 `10001`（msg「成功获取数据，数据非空」）在本次抽样中**都代表成功**
（在职员工、岗位列表、订单列表均为 10001）。调用一律走 `RmyClient.classify_response()`。
→ 实证 `SKILL.md` 注意事项 12。

### 3.2 🔴 推翻旧结论：`get-all-plan` 现在可用
```
GET /api/v1/tpos/customer/get-all-plan?customerId=1
→ code 10000，data 结构：
  actDevPlans / devInvalidDevPlans / expiredInvalidDevPlans（三个 list）
  actDevPlanDevMoney / devInvalidDevPlanDevMoney / expiredInvalidDevPlanDevMoney（int）
  haveInvalidData（bool）
```
旧「注意事项 18」写的「接口不存在、POST→20002 / GET→20004，需改走 `consultation/page`」
**已过时**，本次已更正。原因（推断）：接口后续上线或权限已开通。

⚠️ 但本次用的是**不存在的客户 id**，三个列表都是空的 —— **只证明接口可达、返回契约完整，
不证明数据口径正确**。首次用到真实客户时，仍需拿 1 条真实数据核对字段含义后再批量使用。

### 3.3 ⚠️ `cusbespeak/get-page`：服务端只收 POST，且必填三选一
| 试法 | 结果 |
|---|---|
| `GET` | `20002` 「您不是最新版本，请更新你的系统 Request method 'GET' not supported」 |
| `POST {"tenantId":"1","page":1,"size":1}` | `20002` 「客户id或手机号或专家ID不能同时为空」 |

→ 能力地图已标 **POST**（文档该处方法写法混乱，脚本按「请求方式」行纠正过）；
本次补上文档参数表没写清的硬条件：**`customerId` / 手机号 / 专家ID 至少传一个**。

### 3.4 🔴 补遗接口不是「方法未标注」，是「账号没权限」
`code 2001` 的原文是「**您无法访问该资源，请联系管理员开通！**」，命中：

- `/api/v1/tpos/customer/part-label-list`
- `/api/v1/tpos/consultation/acceptance-tool`
- `/api/v1/tpos/basic/get-equity-card-detail`

`/api/v1/tpos/basic/get-can-buy-equity-card-list`：`GET` 报 20002「GET not supported」，
`POST` 报 2001 未授权 → 方法**疑为 POST**（推断），但**无论如何先要开通权限**。

→ 能力地图第 5.1 节原先建议「用 1 条样本按 GET 试调」**不够**，已改为
「先找睿美云开通该接口权限，再测方法」；这几条在开通前一律视为不可用。

### 3.5 ⏱ 慢接口实证
`POST /api/v1/tpos/consultation/page` 单次 **22.6s** → 客户端超时必须 ≥40s
（实证 `SKILL.md` 注意事项 19）。`report/cashier-record-page` 2.13s，仍需串行（注意事项 14）。

### 3.6 门店清单只返回 2 条（不下结论）
`common/tenantList` 返回 `list=2`，与旧记录的「1=凯德 / 2=双楠 / 3=远大」不一致。
可能原因（**均为推断**）：门店停用、账号可见范围过滤、机构配置变更。
**不做推断结论**，涉及门店枚举时以本次接口实时返回为准，并请业务侧确认。

## 4. 本次未覆盖 / 边界

- ❌ **57 个语义写接口一个都没测**，`api_capability_map.md` 第 4 节的可写性仍以文档契约为准；
  批量写入前必须按审批门控手工验证 1:1 生效，并回查验落库。
- ❌ 未测需要真实客户 id 才能出数的接口（`customer-coupon-page`、`get-pool-info` 等），避免触碰客户数据。
- ❌ 未测官方 MCP 通道（本机 `rmy` 连接器仍 disabled），见 `official_mcp.md`。
- ⚠️ 本结果是 **2026-11-22 的时点快照**，接口权限/方法可能随睿美云发版变化；
  发现 `code 2001` / `20002` 时先重跑 `scripts/probe_readonly.py` 复核，别直接改业务代码。
