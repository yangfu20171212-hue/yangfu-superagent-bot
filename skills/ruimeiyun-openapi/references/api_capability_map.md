# 睿美云 TPOS 接口能力地图（按功能速查）

> **数据源**：飞书 wiki `JVkQwr4eAisxvHkgv9TcOm45nsf`《睿美云开放接口》的本地完整快照 `references/ruimeiyun_api_full.md`（11455 行）。  
> **生成**：`scripts/build_capability_map.py`（文档更新后重跑即可）｜更新于 2026-11-22  
> **规模**：178 个接口（57 个写接口，12 个文档未标注方法）；另有 5 个仅出现在截图/说明里的存疑路径。  
> **查阅顺序**：本文件定位接口 → `references/api_live_probe.md` 看生产实测差异 → `SKILL.md`「注意事项」看实战坑 → `references/ruimeiyun_api_full.md` 看完整字段契约 → `references/rmy_client.py` 发起调用。

## 0. 怎么用

1. 在 **第 1 节** 按「我要做什么」找到接口路径；
2. 在 **第 3 节** 核对 HTTP 方法、关键参数、备注里的坑；
3. 用 `RmyClient.get/post` 调用；涉及写入先过 **第 4 节** 审批门控；
4. 字段不确定时，按表里的 `L<行号>` 直接跳到 `ruimeiyun_api_full.md` 对应行；
5. 本文件只覆盖 **TPOS REST 直连**通道；若要走睿美云官方 MCP（appKey + `/ai/neuron-mcp`），见 `references/official_mcp.md`（配置/传输实测）与 `references/official_mcp_functions.md`（92 个函数清单，由 `readQueryMcpDocs` 实拉生成）；
6. **文档与生产不一致时以实测为准**：见 `references/api_live_probe.md`（2026-11-22 只读实测，含 3 处推翻/补充文档结论）；可重跑 `scripts/probe_readonly.py` 复核。


## 1. 按任务找接口（高频反查表）

| 我要做什么 | 方法 | 首选接口 | 关键提醒 |
|---|---|---|---|
| 查客户主档 / 按手机或姓名搜客户 | `GET` | `/api/v1/tpos/customer/customer-search` | 不能空搜；同名手机多档案，优先用 customerId |
| 按客户 id 查完整档案（含归属、会员等级） | `GET` | `/api/v1/tpos/customer/customer-by-id` | 写操作后回查落库的指定接口 |
| 拉全量客户（>1 万条） | `GET` | `/api/v1/tpos/customer/customer-search` | 20 页硬顶，必须 lastCustomerId 游标 + page 恒为 1 |
| 判断客户当前归属 / 企微在谁手里 | `GET` | `/api/v1/tpos/customer/customer-by-id` | 用 sysUserName 与 wechatSysuserId，绝不用 wechatSysUserName |
| 改客户归属 / 换客户池 | `POST` | `/api/v1/tpos/customer/transfer-pool` | 先 get-pool-info 拿 poolId，写入后 customer-by-id 回查；会推企微通知 |
| 查客户可转入的池与咨询师名单 | `GET` | `/api/v1/tpos/customer/get-pool-info` | 按客户建档门店返回；personalPool 按 (poolId,userName) 建索引 |
| 查客户能否同步企微关系 | `GET` | `/api/v1/tpos/customer/customer-qw-info` | data.changeAllow=true 才可转企微关系 |
| 判断客户是否新客（无消费无划扣） | `POST` | `/api/v1/tpos/customer/check-new-customer` | 手机号或客户 id 二选一 |
| 查客户开单 / 消费 / 购买次数 | `GET` | `/api/v1/tpos/order/billing-page` | tenantId 传空串拿全部门店；忽略时间参数，本地按 createDate 过滤 |
| 查收银记录（谁成交、谁服务、科室） | `POST` | `/api/v1/tpos/report/cashier-record-page` | 31 天窗口上限、必须串行；返回 data.result 不是 records |
| 查客户未划扣 / 剩余项目 | `GET` | `/api/v1/tpos/treat/untreated-page` | 或 POST /treat/scrmTreatList {treatFlag:false} |
| 查客户已治疗 / 已划扣记录 | `GET` | `/api/v1/tpos/treat/already-treated-page` | 真实执行次数看 treatCount，别信主档 |
| 拉全店到店/治疗明细（按日期） | `GET` | `/api/v1/tpos/treat/treated-page-review` | treatTimeStart/treatTimeEnd；客户端二次校验 treatmentTime；含 deductUserName |
| 拉客户回访记录 / 待回访清单 | `POST` | `/api/v1/tpos/visit/get-visit-page` | 查待回访必须 visitedFlag:["1"]；单窗口 1 万条硬顶，按时间分片 |
| 新建回访计划 | `POST` | `/api/v1/tpos/visit/create-visit` | 入参 type 用码值；缺 tenantId 会 20002 |
| 把待回访结清为已回访 | `POST` | `/api/v1/tpos/visit/complete-visit` | response 写清原因，可审计；是治标不是治本 |
| 直接新增一条已回访记录 | `POST` | `/api/v1/tpos/visit/quick-complete-visit` | MCP 工具 rmy_quick_visit 同能力 |
| 作废回访（不可逆） | `POST` | `/api/v1/tpos/visit/obsolete-visit` | contentId=planId；批量前手工验证 1:1 + 断点续传 + 对账 |
| 查回访类型 / 方式 / 模板 | `GET` | `/api/v1/tpos/visit/get-visit-type` | 另有 get-visit-way-type / visit-template-type / -data-type / -content |
| 查咨询记录（主诉、未成交信号） | `POST` | `/api/v1/tpos/consultation/page` | tenantId 必填、超时 ≥40s；高价值字段 mainComplaint / consumptionStatus |
| 查预约 / 新增 / 改 / 确认 / 取消 | `POST` | `/api/v1/tpos/cusbespeak/get-page` | 同族：add / update / confirm(PUT) / cancel(PUT) |
| 查客户接待 / 到店登记 | `POST` | `/api/v1/tpos/reception/reception_cus` | 可用分诊人名单：GET reception/triagetouserlist |
| 查在职员工名册 / 部门树 / 岗位 | `GET` | `/api/v1/tpos/user/get-page` | jobStatus=False 才在职；另 basic/dept-tree、role/getRoleListV2 |
| 查门店清单 | `GET` | `/api/v1/tpos/common/tenantList` | 1=凯德 / 2=双楠 / 3=远大 |
| 查客户卡券 / 发券 / 用券 | `GET` | `/api/v1/tpos/coupon/customer-coupon-page` | send-coupon / use-coupon / gift-coupon / receive-coupon |
| 查储值充值 / 抵扣 / 退款 / 转赠记录 | `GET` | `/api/v1/tpos/order/balance-recharge-page` | 同族 -deduction / -refund / -transfer-page |
| 查客户权益卡 | `GET` | `/api/v1/tpos/order/billing-equity-card-page` | 补遗：basic/get-can-buy-equity-card-list、get-equity-card-detail |
| 收银前查客户可用资产 / 抵扣 / 撤销 | `GET` | `/api/v1/tpos/order/get-customer-available-assets` | 抵扣 POST deduct-assets，撤销 POST cancel-deduct-assets |
| 开单 / 订单退款 | `POST` | `/api/v1/tpos/order/add-billing-review` | 退款 POST /order/refund；可操作订单项 GET /enable-billing |
| 三方小程序开单 / 退款 | `POST` | `/api/v1/tpos/order/add-order-external` | refund-order-external / refund-order-external-item |
| 治疗核销划扣 / 取消划扣 / 取消核销 | `POST` | `/api/v1/tpos/treat/treat-deduct-verify` | 同族 cancel-deduct / cancel-verify；写操作需审批 |
| 查项目/套餐/年卡/次卡/物料/供应商 | `GET` | `/api/v1/tpos/basic/project-page` | 同构：-page 分页 / -type-tree 分类树 / -detail 详情 |
| 查字典（按类型+门店） | `GET` | `/api/v1/tpos/sysdict/dictlist` | 枚举值统一入口 |
| 查库存入库/出库/盘点 | `GET` | `/api/v1/tpos/inventory/storage-page` | 同族 out-inventory-page / check-inventory-page + 详情 + 增改撤 |
| 上传照片 / 皮肤检测图 | `POST` | `/api/v1/tpos/common/addPhoto` | 另有 upload_customer_photo、skin_image/update_skin_file；查照片 GET common/photoPage |
| 查渠道 / 运营媒体 | `GET` | `/api/v1/tpos/channel/channelstypeinfo` | 通过类型取列表 specificchannellist；运营媒体 POST channelWeb/getChannelWebPage-review |
| 查企微聊天记录 | `POST` | `/api/v1/tpos/wechat/message/messageList` | 不分收发人用 cursorMessageInterList；cursor 分页 |
| 查面诊 / 病历 | `POST` | `/api/v1/assessment/get-cus-assessment-page` | 查询虽叫 get- 但方法是 POST；新增/确认/更新面诊同族；病历 medical-record/add、update、delete |
| 报备新增 / 查询 / 转交 | `POST` | `/api/v1/tpos/preparation/add` | 查询也是 POST：get-preparation；转交 POST customer/update-customer-preparation-info |
| 查积分 / 成长值 / 会员升级 | `GET` | `/api/v1/tpos/integral/getCusIntegral` | 明细 score-record-page；升级 query-customer-growth-upgrade |
| 查问卷 / 工牌 ASR 回传 | `POST` | `/api/v1/top/questionnaireCustomer/notYetList` | 工牌 smartworkcard/customerList、callback、jellyCallback |
| 查客户资产变更 / 确认 | `POST` | `/api/v1/top/paymentAssetChange/paymentAssetChangeList` | 明细 GET getOneRecord；确认 POST confirmAssetChange |
| 查客户返利 / 老带新 / 线索 / 标签 | `POST` | `/api/v1/tpos/customer/my-rebate-list` | 同族 my-recommend-customer-list / customer-clue-list / customer-label-list |
| 上传文件 | `POST` | `/api/v1/tpos/file/upload` | 通用文件入口 |

## 2. 模块总览

| 模块 | 接口数 | 读 | 写 | 覆盖能力 |
|---|---:|---:|---:|---|
| 客户 customer | 25 | 22 | 3 | 建档/搜索/详情、返利、推荐、线索、标签、金币、客户池、企微归属、岗位负责人、新客判定 |
| 门店 common | 1 | 1 | 0 | 门店清单 |
| 回访 visit | 10 | 6 | 4 | 类型/方式/模板、计划分页、创建、完成、快速回访、作废 |
| 报备 preparation | 3 | 1 | 2 | 新增/查询/转交报备人 |
| 员工/组织 user | 3 | 3 | 0 | 员工名册、部门树、岗位列表 |
| 卡券 coupon | 7 | 3 | 4 | 客户卡券查询、发放、使用、赠送、领取 |
| 营销 marketing | 2 | 2 | 0 | 线上预约名片、图文消息 |
| 积分 integral | 3 | 3 | 0 | 客户积分、积分/成长值分页、会员升级 |
| 订单/收银 order | 26 | 13 | 13 | 开单/退款、费用单、订单消费、收银记录、储值四类流水、权益卡、资产抵扣、三方小程序开单 |
| 治疗/划扣 treat | 12 | 9 | 3 | 未治疗/已治疗/全店治疗分页、核销划扣与撤销、手术间、治疗岗位、小程序我的治疗 |
| 照片 photo | 5 | 1 | 4 | 七牛/外部图转存、上传、分页查询、皮肤检测上传 |
| 基础数据 basic | 25 | 25 | 0 | 项目/套餐/年卡/次卡/物料/供应商/会员权益/会员规则 + 各自分类树与详情 |
| 字典 sysdict | 1 | 1 | 0 | 按字典类型与门店取枚举 |
| 库存 inventory | 13 | 7 | 6 | 入库/出库/盘点的分页、详情、新增、修正、撤销 + 仓库 |
| 预约 cusbespeak | 9 | 5 | 4 | 新增/修改/确认/取消/分页、可选医生、专家排班、设备手术间、名片 |
| 渠道 channel | 3 | 3 | 0 | 渠道类型、渠道列表、渠道信息 |
| 运营媒体 web | 1 | 1 | 0 | 运营媒体信息 |
| 接待 reception | 5 | 3 | 2 | 分诊人、新增接待、客户接待信息、扫码签到 |
| 咨询 consultation | 4 | 2 | 2 | 新增/修改/查询咨询、接诊工具 |
| 面诊 assessment | 4 | 1 | 3 | 历史面诊、新增、确认、更新 |
| 病历 medical_record | 3 | 0 | 3 | 新增/修改/删除病历 |
| 文件 file | 1 | 0 | 1 | 通用文件上传 |
| 报表 report | 2 | 2 | 0 | 收银记录初始化、收银记录报表 |
| 企微聊天记录 wechat | 2 | 2 | 0 | 单/双向聊天记录查询（cursor 分页） |
| 客户资产变更 assets | 3 | 2 | 1 | 变更列表、单条明细、确认变更 |
| 问卷 questionnaire | 2 | 2 | 0 | 未填写问卷、客户问卷记录 |
| 工牌/ASR smartworkcard | 3 | 1 | 2 | 当天接待客户、质检点/标签/ASR 回传、录音开始结束（见 full.md 补遗） |

## 3. 逐模块接口清单

> `读写` 列按**业务语义**判定（不是看 HTTP 方法）：📖 只读 / ✍️ 写入 / ❓ 语义未定；**写入接口一律先手工验证再批量**（见第 4 节）。  
> `L<数字>` = `ruimeiyun_api_full.md` 行号；`?` = 官方文档未标注 HTTP 方法（见第 5 节）；「补遗节」= 线上文档补入、旧快照缺失的接口。


### 3.1 客户 customer（25）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 客户档案新增（编辑） | `POST` | `/api/v1/tpos/customer/info-sync` | ✍️ | `businessType`, `customerName`, `mainPhone`, `neuronTenantId`, `sourceType` | L70 |
| 获取客户信息列表 | `GET` | `/api/v1/tpos/customer/customer-search` | 📖 | — | 不能空搜；每客户手机可能多档；20 页硬顶，超 1 万条用 lastCustomerId 游标（注意事项 1/2/11/24）  L118 |
| 通过客户id查询客户详情 | `GET` | `/api/v1/tpos/customer/customer-by-id` | 📖 | `customerId` | 写操作后回查落库的指定接口；不返回 poolId，只有 poolName（注意事项 23）  L304 |
| 返利（成交）列表 | `POST` | `/api/v1/tpos/customer/my-rebate-list` | 📖 | `current`, `size`, `receiverId` | L487 |
| 返利（成交）-详情 | `GET` | `/api/v1/tpos/customer/my-rebate-detail` | 📖 | — | L531 |
| 返利（成交）- 详情 - 明细记录 | `GET` | `/api/v1/tpos/customer/my-rebate-detail-list` | 📖 | `current`, `paymentItemDataId`, `receiverId`, `size` | L584 |
| 列表推荐人选项 | `GET` | `/api/v1/tpos/customer/my-rebate-recommend-options` | 📖 | `rebatesLevel`, `receiverId` | L621 |
| 返利（客户）列表 | `POST` | `/api/v1/tpos/customer/my-rebate-customer-list` | 📖 | `current`, `size` | L646 |
| 返利（客户）详情 | `GET` | `/api/v1/tpos/customer/my-rebate-customer-detail` | 📖 | `cusId`, `receiverId` | L688 |
| 返利（客户）详情-成交记录 | `GET` | `/api/v1/tpos/customer/my-rebate-customer-detail-list` | 📖 | `current`, `size`, `cusId`, `receiverId` | L726 |
| 推荐客户明细 | `POST` | `/api/v1/tpos/customer/my-recommend-customer-list` | 📖 | `receiverId`, `current`, `size` | L828 |
| 客户线索查询 | `POST` | `/api/v1/tpos/customer/customer-clue-list` | 📖 | `current`, `size` | L865 |
| 客户标签查询 | `GET` | `/api/v1/tpos/customer/customer-label-list` | 📖 | `type` | L913 |
| 客户金币查询接口 | `POST` | `/api/v1/tpos/customer/customer-gold-list` | 📖 | `customerId`, `page`, `size`, `goldCoinsNum` | L959 |
| 查询客户开发计划 | `GET` | `/api/v1/tpos/customer/get-all-plan` | 📖 | `customerId` | 🔴 2026-11-22 实测 GET 返回 code 10000 + 完整开发计划结构，接口已可用（旧注意事项 18「不存在」已更正）；首次对真实客户使用前仍需核对字段口径，见 api_live_probe.md §3.2  L1018 |
| 客户池转移 | `POST` | `/api/v1/tpos/customer/transfer-pool` | ✍️ | `customerId`, `poolId`, `syncVisitPlan` | 员工可见动作，逐客户推企微通知且无法关闭；批量前必须沟通（注意事项 23）  L1156 |
| 获取客户可以转移到的客户池信息 | `GET` | `/api/v1/tpos/customer/get-pool-info` | 📖 | `customerId` | L1192 |
| 客户是否同步企微关系 | `GET` | `/api/v1/tpos/customer/customer-qw-info` | 📖 | `customerId` | L1227 |
| 获取客户合并后最新的客户信息 | `GET` | `/api/v1/tpos/customer/get-merge-customer-detail` | 📖 | `customerId` | L1253 |
| 查询客户扫码签到记录 | `POST` | `/api/v1/tpos/customer/customer-sign-search` | 📖 | `current`, `size` | L1280 |
| 查询客户老带新关系 | `GET` | `/api/v1/tpos/customer/get-customer-relation` | 📖 | — | L1454 |
| 获取门店岗位负责人配置 | `GET` | `/api/v1/tpos/customer/get-customer-rolemanager-config` | 📖 | `tenantId` | L1491 |
| 编辑客户岗位负责人 | `POST` | `/api/v1/tpos/customer/edit-customer-rolemanager` | ✍️ | `customerId`, `roleManagerId`, `userIdList` | ⚠️ roleManagerId 取 config 的 id 还是 roleId 未实测，用前先测 1 条；userIdList 传空数组＝删除配置（注意事项 25）  L1540 |
| 通过手机号或者客户ID查询返回是否新客（无消费【院内总消费为0】，无划扣记录） | `POST` | `/api/v1/tpos/customer/check-new-customer` | 📖 | — | L1579 |
| 客户部分标签 | `?` | `/api/v1/tpos/customer/part-label-list` | 📖 | — | 🔴 实测 code 2001 未授权，开通前不可用，见 api_live_probe.md §3.4  补遗节 |

### 3.2 门店 common（1）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 获取门店信息列表 | `GET` | `/api/v1/tpos/common/tenantList` | 📖 | — | L1610 |

### 3.3 回访 visit（10）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 获取门店所有回访类型 | `GET` | `/api/v1/tpos/visit/get-visit-type` | 📖 | `tenantId` | L1631 |
| 获取回访方式类型 | `GET` | `/api/v1/tpos/visit/get-visit-way-type` | 📖 | — | L1670 |
| 获取回访数据接口 | `POST` | `/api/v1/tpos/visit/get-visit-page` | 📖 | `page`, `size` | 文档标 POST；查待回访必须带 visitedFlag:["1"]（注意事项 27h/28）  L1703 |
| 创建回访计划 | `POST` | `/api/v1/tpos/visit/create-visit` | ✍️ | `customerId`, `planContentVos`, `type`, `visitDate`, `day`, `userId` | 写读口径不对称：入参 type=码值、visitDate=字符串；回吐 type=中文、visitDate=毫秒戳（注意事项 28）  L1737 |
| 回访模板分类数据 | `GET` | `/api/v1/tpos/visit/visit-template-type` | 📖 | — | L1773 |
| 获取分类下的模板数据 | `GET` | `/api/v1/tpos/visit/visit-template-data-type` | 📖 | `typeId` | ⚠️ 实测返回的是「该分类下的项目列表」而非模板；缺 typeId 会 20004（注意事项 27b）  L1833 |
| 获取模板内容 | `GET` | `/api/v1/tpos/visit/visit-template-content` | 📖 | `id` | id 不匹配时返回 code:10000 + data:null，不报错（注意事项 27b）  L1879 |
| 完成回访计划 | `POST` | `/api/v1/tpos/visit/complete-visit` | ✍️ | `planId`, `response`, `visitType`, `visitedBy` | 把待回访结清为已回访，response 写明清理原因可审计；规则不合并则重复计划还会再长（注意事项 27g）  L1916 |
| 快速回访（直接新增一条已回访的回访数据） | `POST` | `/api/v1/tpos/visit/quick-complete-visit` | ✍️ | `customerId`, `visitedBy`, `planContentVos`, `response`, `visitType`, `type` | 直接新增一条「已回访」记录；MCP 工具 rmy_quick_visit 同能力  L1965 |
| 作废回访 | `POST` | `/api/v1/tpos/visit/obsolete-visit` | ✍️ | — | contentId 即 planId；作废不可逆，批量前手工验证 1:1（注意事项 4）  补遗节 |

### 3.4 报备 preparation（3）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 新增报备 | `POST` | `/api/v1/tpos/preparation/add` | ✍️ | `tenantId`, `projectInfo`, `projectId`, `preType`, `preTypeId` | 文档把 POST 误写为 `PSOT`；报备可不带客户 id 而用姓名+电话自动建档  L2019 |
| 查询报备 | `POST` | `/api/v1/tpos/preparation/get-preparation` | 📖 | `tenantId` | L2041 |
| 编辑客户报备人和报备部门（报备转交） | `POST` | `/api/v1/tpos/customer/update-customer-preparation-info` | ✍️ | — | L2123 |

### 3.5 员工/组织 user（3）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 员工查询 | `GET` | `/api/v1/tpos/user/get-page` | 📖 | `tenantId` | jobStatus=False 才是在职；size 不是 limit（注意事项 12/13/16）  L2156 |
| 获取部门树 | `GET` | `/api/v1/tpos/basic/dept-tree` | 📖 | `tenantId` | L2211 |
| 分页获取岗位信息 | `GET` | `/api/v1/tpos/role/getRoleListV2` | 📖 | — | L2263 |

### 3.6 卡券 coupon（7）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 客户卡券查询 | `GET` | `/api/v1/tpos/coupon/customer-coupon-page` | 📖 | `customerId` | L2313 |
| 客户卡券查询（返回结果与客户资产的优惠券数据对齐） | `GET` | `/api/v1/tpos/coupon/customer-coupon-list` | 📖 | `customerId` | L2355 |
| 使用卡券 | `POST` | `/api/v1/tpos/coupon/use-coupon` | ✍️ | `cardGiveOutId`, `tenantId` | L2410 |
| 分页获取卡券信息 | `GET` | `/api/v1/tpos/coupon/coupon-page` | 📖 | `tenantId` | L2438 |
| 发送卡券 | `POST` | `/api/v1/tpos/coupon/send-coupon` | ✍️ | `acceptMethod`, `destinationJson`, `peopleId`, `startDate`, `endDate`, `donorFlag` | L2547 |
| 卡券赠送（小程序分享） | `POST` | `/api/v1/tpos/coupon/gift-coupon` | ✍️ | `cardId`, `tenantId` | L2619 |
| 领取卡券（小程序分享） | `POST` | `/api/v1/tpos/coupon/receive-coupon` | ✍️ | `cardId`, `customerId`, `tenantId` | L2644 |

### 3.7 营销 marketing（2）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 线上预约-名片管理（分页） | `GET` | `/api/v1/tpos/marketing/appoint-card-page` | 📖 | `currentTenantId` | L2672 |
| 内容管理-图文消息 | `GET` | `/api/v1/tpos/marketing/graphic-message-list` | 📖 | `currentTenantId` | L2723 |

### 3.8 积分 integral（3）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 获取客户积分 | `GET` | `/api/v1/tpos/integral/getCusIntegral` | 📖 | — | L2759 |
| 获取客户积分/成长值分页信息 | `GET` | `/api/v1/tpos/integral/score-record-page` | 📖 | `customerId`, `scoreFlag` | L2792 |
| 查询会员升级信息 | `POST` | `/api/v1/tpos/integral/query-customer-growth-upgrade` | 📖 | `customerId`, `tenantId` | L2840 |

### 3.9 订单/收银 order（26）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 获取订单信息列表 | `GET` | `/api/v1/tpos/order/billing-page` | 📖 | `tenantId` | 忽略所有时间参数；size 上限 500；tenantId 传空串才跨门店（注意事项 7/14bis）  L2870 |
| 获取费用单详细信息 | `GET` | `/api/v1/tpos/order/payment-detail` | 📖 | — | L2981 |
| 开单 | `POST` | `/api/v1/tpos/order/add-billing-review` | ✍️ | `tenantId`, `uId`, `billing`, `customerId`, `id`, `projectId` | L3009 |
| 可操作的订单项 | `GET` | `/api/v1/tpos/order/enable-billing` | 📖 | `billingId`, `mark` | L3311 |
| 订单退款 | `POST` | `/api/v1/tpos/order/refund` | ✍️ | `billingId`, `billingItemId`, `deductPayMoney`, `shouldUserPrice`, `usePrice`, `useCount` | L3408 |
| 小程序-赠送项目（分享） | `POST` | `/api/v1/scrm/giftReceive/gift/project` | ✍️ | `oldBillingId`, `giftRecordId` | L3545 |
| 小程序-领取赠送项目 | `GET` | `/api/v1/scrm/giftReceive/receive/project` | 📖 | `giftRecordId` | L3578 |
| 小程序-项目转赠（小程序分享） | `POST` | `/api/v1/tpos/order/gift-project` | ✍️ | `customerId`, `oldBillingProjectId`, `scrmOperateTenant` | L3602 |
| 小程序-领取赠送项目（小程序分享） | `POST` | `/api/v1/tpos/order/receive-project` | ✍️ | `customerId`, `tenantId`, `giftRecordId` | L3629 |
| 获取客户权益卡列表 | `GET` | `/api/v1/tpos/order/billing-equity-card-page` | 📖 | `customerId` | L3655 |
| 储值充值记录 | `GET` | `/api/v1/tpos/order/balance-recharge-page` | 📖 | — | L3729 |
| 储值抵扣记录 | `GET` | `/api/v1/tpos/order/balance-deduction-page` | 📖 | `customerId`, `givenFlag` | L3776 |
| 储值退款记录 | `GET` | `/api/v1/tpos/order/balance-refund-page` | 📖 | `customerId` | L3811 |
| 储值转赠记录 | `GET` | `/api/v1/tpos/order/balance-transfer-page` | 📖 | `customerId` | L3854 |
| 获取积分兑换订单信息列表 | `GET` | `/api/v1/tpos/order/integral-mall-exchange-page` | 📖 | — | L3897 |
| 对接三方小程序开单 | `POST` | `/api/v1/tpos/order/add-order-external` | ✍️ | — | L3956 |
| 对接三方小程序退款 | `POST` | `/api/v1/tpos/order/refund-order-external` | ✍️ | — | L4364 |
| 对接三方小程序三方订单项退款 | `POST` | `/api/v1/tpos/order/refund-order-external-item` | ✍️ | — | L4749 |
| 查询客户订单消费记录 | `POST` | `/api/v1/tpos/order/get-customer-billing-list` | 📖 | `customerId`, `page`, `size` | L4816 |
| 查询收银记录 | `POST` | `/api/v1/tpos/order/get-cashierRecord-list` | 📖 | `current`, `limit` | L4890 |
| 收银时客户可用资产查询 | `POST` | `/api/v1/tpos/order/get-customer-available-assets` | 📖 | `customerId`, `tenantId`, `saleItemList`, `id`, `projectDataType`, `num` | L5336 |
| 客户资产抵扣 | `POST` | `/api/v1/tpos/order/deduct-assets` | ✍️ | `customerId`, `tenantId`, `thirdOrderId`, `payList`, `paymentItemMark`, `deductMoney` | L5421 |
| 客户资产抵扣撤销接口 | `POST` | `/api/v1/tpos/order/cancel-deduct-assets` | ✍️ | `customerId`, `tenantId`, `thirdOrderId` | L5450 |
| 余额充值（写入） | `?` | `/api/v1/tpos/order/add-balance-recharge` | ✍️ | — | 补遗接口：方法未标注；写操作需审批门控  补遗节 |
| 开单-权益卡（写入） | `?` | `/api/v1/tpos/order/add-billing-equity-card` | ✍️ | — | 补遗接口：方法未标注；写操作需审批门控  补遗节 |
| 定金（写入） | `?` | `/api/v1/tpos/order/add-deposit` | ✍️ | — | 补遗接口：方法未标注；写操作需审批门控  补遗节 |

### 3.10 治疗/划扣 treat（12）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 查询客户未治疗记录查询 | `GET` | `/api/v1/tpos/treat/untreated-page` | 📖 | — | L5478 |
| 查询客户已治疗记录查询 | `GET` | `/api/v1/tpos/treat/already-treated-page` | 📖 | — | L5542 |
| 分页获取治疗数据 / 全店到店划扣明细 | `GET` | `/api/v1/tpos/treat/treated-page-review` | 📖 | — | GET 不是 POST，路径在 /treat/ 不是 /visit/；唯一能取到 deductUserName 执行人的接口（注意事项 7/27i）  L5632 |
| 获取治疗时查询的手术间信息 | `GET` | `/api/v1/tpos/treat/get-operating-room-list` | 📖 | `tenantId` | L5750 |
| 获取治疗中和已治疗的数据 | `GET` | `/api/v1/tpos/treat/get-begin-treat-info` | 📖 | `billingItemId` | L5799 |
| 进行核销和划扣 | `POST` | `/api/v1/tpos/treat/treat-deduct-verify` | ✍️ | `deductAndVerifyPostDTO`, `deductDeptId`, `deductUserId`, `deductUserName`, `operateId`, `tenantId` | L5855 |
| 取消划扣 | `POST` | `/api/v1/tpos/treat/cancel-deduct` | ✍️ | `operateId`, `tenantId`, `treatRecordId` | L5966 |
| 取消核销 | `POST` | `/api/v1/tpos/treat/cancel-verify` | ✍️ | `operateId`, `tenantId`, `treatRecordId`, `verifyRecordId` | L6002 |
| 已治疗的核销和划扣详情信息 | `GET` | `/api/v1/tpos/treat/get-treated-deduct-and-verify-detail` | 📖 | `tenantId`, `treatRecordId` | L6041 |
| 获取所有的治疗岗位列表 | `GET` | `/api/v1/tpos/treat/get-treatment-roles` | 📖 | `tenantId` | L6339 |
| 小程序-我的治疗(旧版) | `POST` | `/api/v1/scrm/treatment/page` | 📖 | `current`, `size`, `customerId`, `treatmentTime`, `isGroup` | L6393 |
| 小程序-我的治疗（新版） | `POST` | `/api/v1/tpos/treat/scrmTreatList` | 📖 | `current`, `size`, `customerId`, `treatFlag`, `tenantId` | L6482 |

### 3.11 照片 photo（5）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 外部七牛照片转存至睿美云 | `POST` | `/api/v1/tpos/common/addPhoto` | ✍️ | `photoInfoDTOList`, `path`, `name`, `phone`, `tenantId` | L6629 |
| 外部照片路径转存至睿美云 | `POST` | `/api/v1/tpos/common/addPhotoOpen` | ✍️ | `photoInfoDTOList`, `path`, `name`, `phone`, `tenantId` | L6653 |
| 上传照片到睿美云 | `POST` | `/api/v1/tpos/common/upload_customer_photo` | ✍️ | — | L6689 |
| 通过客户id分页查询照片信息 | `GET` | `/api/v1/tpos/common/photoPage` | 📖 | `customerId` | L6716 |
| 皮肤检测类图片上传 | `POST` | `/api/v1/tpos/skin_image/update_skin_file` | ✍️ | — | L6766 |

### 3.12 基础数据 basic（25）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 所有的项目分类查询 | `POST` | `/api/v1/tpos/basic/getProjectType` | 📖 | — | 全部项目分类查询（文档放在 treat 章节末尾，按功能归入基础数据）  L6599 |
| 项目或套餐搜索（需要门店） | `POST` | `/api/v1/tpos/basic/getP/getProjectByType` | 📖 | — | ⚠️ 文档原文路径疑似笔误（getP 混入），用前须实测确认  L6613 |
| 获取项目信息 | `GET` | `/api/v1/tpos/basic/project-page` | 📖 | `tenantId` | L6805 |
| 获取项目分类树 | `GET` | `/api/v1/tpos/basic/project-type-tree` | 📖 | `tenantId` | L6851 |
| 项目详情信息 | `GET` | `/api/v1/tpos/basic/project-detail` | 📖 | `id` | L6893 |
| 获取套餐信息 | `GET` | `/api/v1/tpos/basic/package-page` | 📖 | `tenantId` | L7030 |
| 获取套餐分类树 | `GET` | `/api/v1/tpos/basic/package-type-tree` | 📖 | `tenantId` | L7076 |
| 套餐详情信息 | `GET` | `/api/v1/tpos/basic/package-detail` | 📖 | `id` | L7120 |
| 获取年卡信息 | `GET` | `/api/v1/tpos/basic/annual-card-page` | 📖 | `tenantId` | L7160 |
| 获取年卡分类树 | `GET` | `/api/v1/tpos/basic/annual-card-type-tree` | 📖 | `tenantId`, `id` | L7216 |
| 年卡详情信息 | `GET` | `/api/v1/tpos/basic/annual-card-detail` | 📖 | `id` | L7259 |
| 获取次卡信息 | `GET` | `/api/v1/tpos/basic/time-card-page` | 📖 | `tenantId` | L7293 |
| 获取次卡分类树 | `GET` | `/api/v1/tpos/basic/time-card-type-tree` | 📖 | `tenantId` | L7350 |
| 次卡详情信息 | `GET` | `/api/v1/tpos/basic/time-card-detail` | 📖 | `id` | L7392 |
| 获取物料信息 | `GET` | `/api/v1/tpos/basic/material-page` | 📖 | `tenantId` | L7427 |
| 获取物料分类树 | `GET` | `/api/v1/tpos/basic/material-type-tree` | 📖 | `tenantId` | L7481 |
| 物料详情 | `GET` | `/api/v1/tpos/basic/material-detail` | 📖 | `id` | L7523 |
| 1.会员权益列表（会员等级）（弃用） | `GET` | `/api/v1/tpos/basic/member-level-info` | 📖 | `tenantId` | L7577 |
| 2.会员权益列表（会员等级）（完整版） | `GET` | `/api/v1/tpos/basic/member-level-review` | 📖 | `tenantId` | L7621 |
| 3.会员权益的固定奖励 | `GET` | `/api/v1/tpos/basic/member-task` | 📖 | `tenantId` | L7679 |
| 4.会员规则 | `GET` | `/api/v1/tpos/basic/member-rules` | 📖 | `tenantId` | L7737 |
| 获取供应商信息 | `GET` | `/api/v1/tpos/basic/supplier-page` | 📖 | `tenantId` | L7827 |
| 获取供应商分类树 | `GET` | `/api/v1/tpos/basic/supplier-type-tree` | 📖 | `tenantId` | L7874 |
| 可购买权益卡列表 | `?` | `/api/v1/tpos/basic/get-can-buy-equity-card-list` | 📖 | — | 🔴 实测 code 2001 未授权（GET→20002 not supported / POST→2001）；先找睿美云开通权限，方法疑为 POST，见 api_live_probe.md §3.4  补遗节 |
| 权益卡详情 | `?` | `/api/v1/tpos/basic/get-equity-card-detail` | 📖 | — | 🔴 实测 code 2001 未授权，开通前不可用，见 api_live_probe.md §3.4  补遗节 |

### 3.13 字典 sysdict（1）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 通过字典类型和门店获取字典 | `GET` | `/api/v1/tpos/sysdict/dictlist` | 📖 | `tenantId` | L7920 |

### 3.14 库存 inventory（13）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 入库管理分页数据 | `GET` | `/api/v1/tpos/inventory/storage-page` | 📖 | `tenantId` | L7968 |
| 入库详情数据 | `GET` | `/api/v1/tpos/inventory/storage-info` | 📖 | `id` | L8026 |
| 入库新增 | `?` | `/api/v1/tpos/inventory/storage-add` | ✍️ | `tenantId`, `departmentId`, `responsibleId`, `type`, `remark`, `warehouseId` | L8096 |
| 入库修正（需要tpos鉴权） | `?` | `/api/v1/tpos/inventory/storage-update` | ✍️ | `id`, `userId`, `tenantId`, `departmentId`, `responsibleId`, `type` | L8186 |
| 入库撤销（需要tpos鉴权） | `?` | `/api/v1/tpos/inventory/storage-undo` | ✍️ | `userId`, `id` | L8276 |
| 分页获取仓库信息 | `GET` | `/api/v1/tpos/inventory/warehouse-page` | 📖 | `tenantId` | L8320 |
| 出库管理分页数据 | `GET` | `/api/v1/tpos/inventory/out-inventory-page` | 📖 | `tenantId` | L8391 |
| 出库详情数据 | `GET` | `/api/v1/tpos/inventory/out-inventory-info` | 📖 | `id` | L8450 |
| 出库新增 | `POST` | `/api/v1/tpos/inventory/outInventory-add` | ✍️ | `warehouseId`, `handleId`, `tenantId`, `outBoundType`, `outMaterialList`, `inventoryId` | L8536 |
| 出库修正（需要tpos鉴权） | `?` | `/api/v1/tpos/inventory/outInventory-update` | ✍️ | `id`, `warehouseId`, `userId`, `handleId`, `deptId`, `recipientId` | L8610 |
| 出库撤销（需要tpos鉴权） | `?` | `/api/v1/tpos/inventory/outInventory-undo` | ✍️ | `id`, `userId` | L8690 |
| 物料盘点分页数据 | `GET` | `/api/v1/tpos/inventory/check-inventory-page` | 📖 | `tenantId` | L8737 |
| 物料盘点详情数据 | `GET` | `/api/v1/tpos/inventory/check-inventory-info` | 📖 | `tenantId`, `id` | L8788 |

### 3.15 预约 cusbespeak（9）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 新增预约 | `POST` | `/api/v1/tpos/cusbespeak/add` | ✍️ | `customerId`, `bespeakProject`, `dataId`, `dataType`, `bespeakTypeValue`, `startTime` | L8883 |
| 修改预约 | `POST` | `/api/v1/tpos/cusbespeak/update` | ✍️ | — | L8929 |
| 确认预约 | `PUT` | `/api/v1/tpos/cusbespeak/confirm` | ✍️ | `bespeakId` | L8951 |
| 取消预约 | `PUT` | `/api/v1/tpos/cusbespeak/cancel` | ✍️ | `id`, `reason` | L8975 |
| 预约分页查询 | `POST` | `/api/v1/tpos/cusbespeak/get-page` | 📖 | `tenantId` | 🔴 服务端只收 POST（GET→20002 not supported）；customerId/手机号/专家ID 至少传一个，见 api_live_probe.md §3.3  L9000 |
| 获取可选择的预约医生 | `GET` | `/api/v1/tpos/cusbespeak/get-available-experts` | 📖 | `tenantId` | L9047 |
| 查询预约专家排班 | `POST` | `/api/v1/tpos/cusbespeak/get-available-experts-schedule` | 📖 | `expertId`, `tenantId`, `name` | L9077 |
| 获取设备或者根据设备获取配置的手术间 | `GET` | `/api/v1/tpos/cusbespeak/getEquipmentOrRoom` | 📖 | `type`, `dateTime`, `tenantId` | L9366 |
| 获取线上预约的名片管理 | `POST` | `/api/v1/tpos/cusbespeak/getAppointCardList` | 📖 | — | L9386 |

### 3.16 渠道 channel（3）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 整合渠道类型选择（建档，报备） | `GET` | `/api/v1/tpos/channel/channelstypeinfo` | 📖 | `tenantId`, `channelType` | L9500 |
| 通过渠道类型获取渠道列表 | `GET` | `/api/v1/tpos/channel/specificchannellist` | 📖 | `tenantId`, `channelType`, `typeId` | L9539 |
| 查询渠道信息 | `POST` | `/api/v1/tpos/channel/getChannelPageInfo` | 📖 | — | 文档写 Post（首字母大写）  L9570 |

### 3.17 运营媒体 web（1）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 查询运营媒体信息 | `POST` | `/api/v1/tpos/channelWeb/getChannelWebPage-review` | 📖 | — | L9593 |

### 3.18 接待 reception（5）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 可用的接待分诊人列表 | `GET` | `/api/v1/tpos/reception/triagetouserlist` | 📖 | `tenantId` | L9643 |
| 新增接待 | `POST` | `/api/v1/tpos/reception/receptionadd` | ✍️ | `receiverId`, `receptionType`, `tenantId` | L9678 |
| 查询客户接待信息 | `POST` | `/api/v1/tpos/reception/reception_cus` | 📖 | — | L9710 |
| 客户扫码签到初始化数据(小程序) | `POST` | `/api/v1/tpos/reception/scrm-check-in-config` | 📖 | `customerId`, `tenantId` | L9759 |
| 客户扫码签到(小程序) | `POST` | `/api/v1/tpos/reception/scrm-check-in` | ✍️ | `customerId`, `visitTypeConfig`, `receptionType`, `receptionTypeName`, `projectTypeConfig`, `dataId` | L9885 |

### 3.19 咨询 consultation（4）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 新增咨询 | `POST` | `/api/v1/tpos/consultation/add` | ✍️ | `userId`, `customerId`, `tenantId` | L9941 |
| 修改咨询 | `POST` | `/api/v1/tpos/consultation/update` | ✍️ | `id`, `userId`, `customerId`, `tenantId` | L9980 |
| 查询咨询 | `POST` | `/api/v1/tpos/consultation/page` | 📖 | `page`, `size`, `tenantId` | tenantId 必填；响应慢需 ≥40s 超时；高价值字段 mainComplaint / consumptionStatus（注意事项 19）  L10024 |
| 接诊工具 | `?` | `/api/v1/tpos/consultation/acceptance-tool` | ❓ | — | 🔴 实测 code 2001 未授权，开通前不可用，见 api_live_probe.md §3.4  补遗节 |

### 3.20 面诊 assessment（4）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 查询客户历史面诊 | `POST` | `/api/v1/assessment/get-cus-assessment-page` | 📖 | `customerId`, `size`, `page` | L10141 |
| 新增面诊 | `POST` | `/api/v1/assessment/add-assessment` | ✍️ | `customerId`, `operateDoctorId`, `receptionType`, `tenantId`, `arriveFlag`, `mainComplaint` | L10194 |
| 确认面诊 | `POST` | `/api/v1/assessment/confirm-assessment` | ✍️ | `id` | L10247 |
| 更新面诊 | `POST` | `/api/v1/assessment/update-assessment` | ✍️ | `id`, `customerId`, `operateDoctorId`, `receptionType`, `tenantId`, `arriveFlag` | L10285 |

### 3.21 病历 medical_record（3）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 新增病历 | `POST` | `/api/v1/tpos/medical-record/add` | ✍️ | `customerId`, `type`, `content`, `dossierId`, `createBy`, `creatorName` | L10345 |
| 修改病历 | `POST` | `/api/v1/tpos/medical-record/update` | ✍️ | `id`, `dossierId`, `contentList`, `content`, `type` | L10377 |
| 删除病历 | `DELETE` | `/api/v1/tpos/medical-record/delete` | ✍️ | `id` | L10408 |

### 3.22 文件 file（1）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 上传文件 | `POST` | `/api/v1/tpos/file/upload` | ✍️ | `customerId`, `typeName`, `tenantId` | L10449 |

### 3.23 报表 report（2）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 收银记录初始化 | `GET` | `/api/v1/tpos/report/cashier-record-init` | 📖 | `tenantId` | L10485 |
| 收银记录（报表） | `POST` | `/api/v1/tpos/report/cashier-record-page` | 📖 | `tenantId`, `current`, `limit` | 31 天窗口上限；必须串行，并发会静默返 0 条（注意事项 14）  L10616 |

### 3.24 企微聊天记录 wechat（2）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 聊天记录查询 | `POST` | `/api/v1/tpos/wechat/message/messageList` | 📖 | — | L10668 |
| 聊天记录查询 | `POST` | `/api/v1/tpos/wechat/message/cursorMessageInterList` | 📖 | — | L10717 |

### 3.25 客户资产变更 assets（3）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 客户资产变更列表 | `POST` | `/api/v1/top/paymentAssetChange/paymentAssetChangeList` | 📖 | `index`, `size` | L10768 |
| 得到资产变动记录 | `GET` | `/api/v1/top/paymentAssetChange/getOneRecord` | 📖 | `id` | L10791 |
| 确认资产变更 | `POST` | `/api/v1/top/paymentAssetChange/confirmAssetChange` | ✍️ | `assetChangeRecordId`, `customerId`, `assetPassword` | L10807 |

### 3.26 问卷 questionnaire（2）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 1. 未填写的问卷列表 | `POST` | `/api/v1/top/questionnaireCustomer/notYetList` | 📖 | — | L10823 |
| 获取客户的问卷记录 | `POST` | `/api/v1/top/questionnaireCustomer/page` | 📖 | `customerId`, `page`, `size` | L10933 |

### 3.27 工牌/ASR smartworkcard（3）

| 功能 | 方法 | 路径 | 读写 | 关键参数 | 备注 / 文档定位 |
|---|---|---|---|---|---|
| 分页查询当天接待客户列表 | `POST` | `/api/v1/tpos/smartworkcard/customerList` | 📖 | `tenantId` | L11003 |
| 质检点、客户标签、ASR转写结果推送(随行天使) | `POST` | `/api/v1/tpos/smartworkcard/jellyCallback` | ✍️ | `eventType`, `tenantId`, `userId`, `startTime`, `endTime`, `result` | L11046 |
| 质检点、客户标签、ASR转写结果推送，适用于工牌录音同步到睿美云(通用) | `POST` | `/api/v1/tpos/smartworkcard/callback` | ✍️ | `eventType`, `platformType`, `tenantId`, `userId`, `startTime`, `endTime` | L11090 |

## 4. 写接口清单（审批门控）

共 **57** 个**语义写**接口（按业务效果判定：POST 但只做查询的 33 个已排除；文档未标方法但语义为写的 8 个已纳入）。铁律：`RmyClient` 对 POST 默认不重试（防重复写入）；任何批量写入前先 1–3 条手工验证 1:1 生效，写入后必须用指定读接口回查；涉及员工可见动作（`transfer-pool` 等）须先与业务方沟通。

| 模块 | 方法 | 路径 | 功能 |
|---|---|---|---|
| 客户 customer | `POST` | `/api/v1/tpos/customer/info-sync` | 客户档案新增（编辑） |
| 客户 customer | `POST` | `/api/v1/tpos/customer/transfer-pool` | 客户池转移 |
| 客户 customer | `POST` | `/api/v1/tpos/customer/edit-customer-rolemanager` | 编辑客户岗位负责人 |
| 回访 visit | `POST` | `/api/v1/tpos/visit/create-visit` | 创建回访计划 |
| 回访 visit | `POST` | `/api/v1/tpos/visit/complete-visit` | 完成回访计划 |
| 回访 visit | `POST` | `/api/v1/tpos/visit/quick-complete-visit` | 快速回访（直接新增一条已回访的回访数据） |
| 回访 visit | `POST` | `/api/v1/tpos/visit/obsolete-visit` | 作废回访 |
| 报备 preparation | `POST` | `/api/v1/tpos/preparation/add` | 新增报备 |
| 报备 preparation | `POST` | `/api/v1/tpos/customer/update-customer-preparation-info` | 编辑客户报备人和报备部门（报备转交） |
| 卡券 coupon | `POST` | `/api/v1/tpos/coupon/use-coupon` | 使用卡券 |
| 卡券 coupon | `POST` | `/api/v1/tpos/coupon/send-coupon` | 发送卡券 |
| 卡券 coupon | `POST` | `/api/v1/tpos/coupon/gift-coupon` | 卡券赠送（小程序分享） |
| 卡券 coupon | `POST` | `/api/v1/tpos/coupon/receive-coupon` | 领取卡券（小程序分享） |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/add-billing-review` | 开单 |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/refund` | 订单退款 |
| 订单/收银 order | `POST` | `/api/v1/scrm/giftReceive/gift/project` | 小程序-赠送项目（分享） |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/gift-project` | 小程序-项目转赠（小程序分享） |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/receive-project` | 小程序-领取赠送项目（小程序分享） |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/add-order-external` | 对接三方小程序开单 |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/refund-order-external` | 对接三方小程序退款 |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/refund-order-external-item` | 对接三方小程序三方订单项退款 |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/deduct-assets` | 客户资产抵扣 |
| 订单/收银 order | `POST` | `/api/v1/tpos/order/cancel-deduct-assets` | 客户资产抵扣撤销接口 |
| 订单/收银 order | `?` | `/api/v1/tpos/order/add-balance-recharge` | 余额充值（写入） |
| 订单/收银 order | `?` | `/api/v1/tpos/order/add-billing-equity-card` | 开单-权益卡（写入） |
| 订单/收银 order | `?` | `/api/v1/tpos/order/add-deposit` | 定金（写入） |
| 治疗/划扣 treat | `POST` | `/api/v1/tpos/treat/treat-deduct-verify` | 进行核销和划扣 |
| 治疗/划扣 treat | `POST` | `/api/v1/tpos/treat/cancel-deduct` | 取消划扣 |
| 治疗/划扣 treat | `POST` | `/api/v1/tpos/treat/cancel-verify` | 取消核销 |
| 照片 photo | `POST` | `/api/v1/tpos/common/addPhoto` | 外部七牛照片转存至睿美云 |
| 照片 photo | `POST` | `/api/v1/tpos/common/addPhotoOpen` | 外部照片路径转存至睿美云 |
| 照片 photo | `POST` | `/api/v1/tpos/common/upload_customer_photo` | 上传照片到睿美云 |
| 照片 photo | `POST` | `/api/v1/tpos/skin_image/update_skin_file` | 皮肤检测类图片上传 |
| 库存 inventory | `?` | `/api/v1/tpos/inventory/storage-add` | 入库新增 |
| 库存 inventory | `?` | `/api/v1/tpos/inventory/storage-update` | 入库修正（需要tpos鉴权） |
| 库存 inventory | `?` | `/api/v1/tpos/inventory/storage-undo` | 入库撤销（需要tpos鉴权） |
| 库存 inventory | `POST` | `/api/v1/tpos/inventory/outInventory-add` | 出库新增 |
| 库存 inventory | `?` | `/api/v1/tpos/inventory/outInventory-update` | 出库修正（需要tpos鉴权） |
| 库存 inventory | `?` | `/api/v1/tpos/inventory/outInventory-undo` | 出库撤销（需要tpos鉴权） |
| 预约 cusbespeak | `POST` | `/api/v1/tpos/cusbespeak/add` | 新增预约 |
| 预约 cusbespeak | `POST` | `/api/v1/tpos/cusbespeak/update` | 修改预约 |
| 预约 cusbespeak | `PUT` | `/api/v1/tpos/cusbespeak/confirm` | 确认预约 |
| 预约 cusbespeak | `PUT` | `/api/v1/tpos/cusbespeak/cancel` | 取消预约 |
| 接待 reception | `POST` | `/api/v1/tpos/reception/receptionadd` | 新增接待 |
| 接待 reception | `POST` | `/api/v1/tpos/reception/scrm-check-in` | 客户扫码签到(小程序) |
| 咨询 consultation | `POST` | `/api/v1/tpos/consultation/add` | 新增咨询 |
| 咨询 consultation | `POST` | `/api/v1/tpos/consultation/update` | 修改咨询 |
| 面诊 assessment | `POST` | `/api/v1/assessment/add-assessment` | 新增面诊 |
| 面诊 assessment | `POST` | `/api/v1/assessment/confirm-assessment` | 确认面诊 |
| 面诊 assessment | `POST` | `/api/v1/assessment/update-assessment` | 更新面诊 |
| 病历 medical_record | `POST` | `/api/v1/tpos/medical-record/add` | 新增病历 |
| 病历 medical_record | `POST` | `/api/v1/tpos/medical-record/update` | 修改病历 |
| 病历 medical_record | `DELETE` | `/api/v1/tpos/medical-record/delete` | 删除病历 |
| 文件 file | `POST` | `/api/v1/tpos/file/upload` | 上传文件 |
| 客户资产变更 assets | `POST` | `/api/v1/top/paymentAssetChange/confirmAssetChange` | 确认资产变更 |
| 工牌/ASR smartworkcard | `POST` | `/api/v1/tpos/smartworkcard/jellyCallback` | 质检点、客户标签、ASR转写结果推送(随行天使) |
| 工牌/ASR smartworkcard | `POST` | `/api/v1/tpos/smartworkcard/callback` | 质检点、客户标签、ASR转写结果推送，适用于工牌录音同步到睿美云(通用) |

## 5. 文档未标注方法 / 存疑路径（用前必须实测）

### 5.1 文档未标注 HTTP 方法（12 个）

| 路径 | 功能 | 建议 |
|---|---|---|
| `/api/v1/tpos/basic/get-can-buy-equity-card-list` | 可购买权益卡列表 | 🔴 实测 code 2001 未授权：先找睿美云开通该接口权限，再测方法（api_live_probe.md §3.4） |
| `/api/v1/tpos/basic/get-equity-card-detail` | 权益卡详情 | 🔴 实测 code 2001 未授权：先找睿美云开通该接口权限，再测方法（api_live_probe.md §3.4） |
| `/api/v1/tpos/consultation/acceptance-tool` | 接诊工具 | 🔴 实测 code 2001 未授权：先找睿美云开通该接口权限，再测方法（api_live_probe.md §3.4） |
| `/api/v1/tpos/customer/part-label-list` | 客户部分标签 | 🔴 实测 code 2001 未授权：先找睿美云开通该接口权限，再测方法（api_live_probe.md §3.4） |
| `/api/v1/tpos/inventory/outInventory-undo` | 出库撤销（需要tpos鉴权） | 语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量 |
| `/api/v1/tpos/inventory/outInventory-update` | 出库修正（需要tpos鉴权） | 语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量 |
| `/api/v1/tpos/inventory/storage-add` | 入库新增 | 语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量 |
| `/api/v1/tpos/inventory/storage-undo` | 入库撤销（需要tpos鉴权） | 语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量 |
| `/api/v1/tpos/inventory/storage-update` | 入库修正（需要tpos鉴权） | 语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量 |
| `/api/v1/tpos/order/add-balance-recharge` | 余额充值（写入） | 语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量 |
| `/api/v1/tpos/order/add-billing-equity-card` | 开单-权益卡（写入） | 语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量 |
| `/api/v1/tpos/order/add-deposit` | 定金（写入） | 语义写：先确认该接口已授权，用 1 条样本按 POST 试调并回查验落库，勿批量 |

### 5.2 仅出现在截图/说明文字中的路径（无契约，勿直接调用）

| 路径 | 说明 |
|---|---|
| `/api/v1/tpos/yizhipai/uploadcustomerphoto` | 截图 URL：皮肤检测图片上传接口的 Postman 示例，正文另定义为 /api/v1/tpos/skin_image/update_skin_file |
| `/api/v1/tpos/basic/package` | 截图 URL 中 package - detail 被空格截断，正文真实路径为 /api/v1/tpos/basic/package-detail |
| `/api/v1/tpos/channel/channeltypeinfo` | 截图 URL；正文加粗定义为 channelstypeinfo（多一个 s），两者差异未实测 |
| `/api/v1/tpos/customer/check` | 截图 URL 中 check - new - customer 被空格截断，正文真实路径为 check-new-customer |
| `/api/v1/tpos/wechat/message/cursorMessage` | 正文推荐「查两人对话用此接口」，但未给出契约（参数/响应）；同族可用 messageList / cursorMessageInterList |

### 5.3 生产实测校准（2026-11-22，详见 `api_live_probe.md`）

- 🔴 `GET /api/v1/tpos/customer/get-all-plan`：旧结论「线上无」**已推翻**，实测 `code 10000` + 完整开发计划结构；接口可用，但数据口径待真实客户复核（§3.2）。
- ⚠️ `POST /api/v1/tpos/cusbespeak/get-page`：`GET` 报 20002「GET not supported」；`customerId`/手机号/专家ID 至少传一个（§3.3）。
- 🔴 补遗 4 个接口（`part-label-list` / `acceptance-tool` / `get-equity-card-detail` / `get-can-buy-equity-card-list`）：实测 `code 2001` 未授权，需睿美云开通（§3.4）。
- ⏱ `POST /api/v1/tpos/consultation/page` 单次 22.6s，客户端超时须 ≥40s（§3.5）。
- `POST /api/v1/tpos/visit/obsolete-visit`：2026-09-27 已获授权可用，`contentId` 即 `planId`（注意事项 4）。
- `POST /api/v1/tpos/basic/getP/getProjectByType`：文档原文路径疑似笔误，用前实测。
- 官方 `rmy` MCP 的 6 个客户维度接口一律返回「没有查到…」，客户明细必须走直连通道（注意事项 6）。


## 6. 调用铁律速记

| 主题 | 规则 | 详见 |
|---|---|---|
| 鉴权 | 4 个 Header 缺一不可；时间戳与服务器差 <1 分钟；正式环境按接口单独授权 | SKILL.md「核心约定」「注意事项 4」 |
| 成功码 | 不统一：code 10000 或 10001 都算成功，用 RmyClient.classify_response()，别硬编码 ==10000 | 注意事项 12 |
| 401 排查 | 先核对文档里的路径 + HTTP 方法是否照抄，再怀疑账号未授权；不要盲试路径变体 | 注意事项 4 |
| 分页 | 参数是 size 不是 limit；深分页会静默截断；按时间分片且单批 <1 万条；失败要重试+告警，不能用残缺数据 | 注意事项 8/13/17 |
| 写操作 | POST 默认不重试；任何写入前先 1-3 条手工验证，再批量；写入后用指定接口回查验落库 | 内置容错 + 注意事项 23/28 |
| 全量数据 | 接口 total 有枚举上限，向下游报下界不报精确值；扫描数 > total = 数据污染，立即停手 | 注意事项 8/9 |
| 隐私 | 咨询/客户接口的 phoneNumber 等字段不取不写；客户明细走直连通道，不用官方 MCP 客户维度接口 | 注意事项 6/19 |
| 字段口径 | 归属看 sysUserName（当前）不看 relatedConsul（历史）；企微看 wechatSysuserId 不看昵称；主档消费次数可能为 0 | 注意事项 9/15/20/21/25 |
