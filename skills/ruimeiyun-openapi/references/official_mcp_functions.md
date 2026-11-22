# 睿美云官方 MCP 函数清单（自动生成 · 已脱敏）

> **生成**：`scripts/fetch_official_mcp_docs.py`｜2026-11-22 23:32:09  
> **端点**：`https://cdyangfu.hospital.realmerit.com.cn/ai/neuron-mcp`｜协议 `2025-11-25`  
> **规模**：`tools/list` 90 个工具、`readQueryMcpDocs` 47 组返回值文档、合并去重 **92 个函数**。  
> 🔴 **脱敏声明**：`readQueryMcpDocs` 的返回示例含真实客户姓名/订单号/金额/id，本文件**只保留字段名，不保留任何值**；原始响应不落盘。  
> 调用方式与凭证获取见 `official_mcp.md`；TPOS REST 全量接口见 `api_capability_map.md`。

## 1. 汇总

| 业务域 | 函数数 | 其中写操作 |
|---|---:|---:|
| 企微 / 录音 / ASR / 皮肤检测 | 7 | 0 |
| 其它 / 运维 | 1 | 0 |
| 员工 / 组织 / 岗位 / 部门 | 10 | 0 |
| 咨询 | 4 | 0 |
| 回访 | 4 | 0 |
| 客户档案 / 标签 / 线索 | 13 | 0 |
| 库存 / 出入库 | 9 | 0 |
| 开发计划 | 3 | 0 |
| 报备 | 4 | 0 |
| 接待 | 4 | 0 |
| 治疗 / 划扣 | 5 | 0 |
| 统计 / 每日小结 | 2 | 0 |
| 订单 / 收银 / 缴费 | 6 | 1 |
| 账号绑定 / 运维写入 | 2 | 2 |
| 项目 / 套餐 / 物料 / 销售项 | 14 | 0 |
| 预约 | 4 | 0 |
| **合计** | **92** | **3** |

## 2. 按业务域速查

> `入参` 来自 MCP 的 `inputSchema` / 文档参数表；`返回字段` 只列前 8 个，完整字段见 `official_mcp_functions.json` 的 `group_index`。  
> `📖` 查询 / `✍️` 写入 / `🔧` 自省。


### 2.1 企微 / 录音 / ASR / 皮肤检测（7）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getConversationByCustomerId` | 通过客户id查询客户在某个时间段或者最近几次次工牌录音的对话信息 | `customerId`, `startDate`, `endDate`, `number` | 客户为角度 | 门店名称, 录音时间, 咨询师, 客户id, 录音id, 客户名称, 门店id, 对话内容 | ✅ |
| 📖 | `getConversationByCustomerIdList` | 通过客户id查询客户在某个时间段或者最近几次次工牌录音的对话信息 | `customerId`, `startDate`, `endDate` | 所有角度 | 门店名称, 录音时间, 咨询师, 客户id, 录音id, 客户名称, 门店id, 对话内容 | ✅ |
| 📖 | `getConversationByDate` | 通过某个时间段查询客户在某个时间段或者最近几次工牌录音的对话信息 | `startDate`, `endDate` | 医院为角度 | 门店名称, 录音时间, 咨询师, 客户id, 录音id, 客户名称, 门店id, 对话内容 | ✅ |
| 📖 | `getRecordingByCustomerId` | 通过客户id查询客户在某个时间段或者最近几次麦克风录音的对话信息（腾讯ASR语音分析原始内容） | `customerId`, `startDate`, `endDate`, `number` | 客户为角度 | 门店名称, 录音时间, 录音类型, 录音人, 客户id, 录音id, 录音时长, 客户名称 | ✅ |
| 📖 | `getRecordingByDate` | 通过某个时间段查询麦克风录音的对话信息（腾讯ASR语音分析原始内容） | `startDate`, `endDate` | 医院为角度 | 门店名称, 录音时间, 录音类型, 录音人, 客户id, 录音id, 录音时长, 客户名称 | ✅ |
| 📖 | `getSkinDetection` | 根据客户Id获取皮肤检测信息 | `customerId` | 给外部提供的MCP工具 | 2022-05-13 17:30:59, 皮肤问题, 护理建议, 棕斑数量(个), 问题程度, 紫外光斑数量(个), 紫外光斑面积占比(%), 自然光斑数量(个) | ✅ |
| 📖 | `getWeChatMessage` | 查询指定客户和指定员工在对应的时间段内的企业微信文本聊天记录，最多查询1000条，如果没有明确时间范围，则默认查询最近30天的记录 | `customerId`, `userId`, `startDate`, `endDate` | 客户为角度 | 消息时间, 员工姓名, 消息内容 | ✅ |

### 2.2 其它 / 运维（1）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 🔧 | `readQueryMcpDocs` | 读取所有查询类型的MCP函数返回值文档 | — | — | — | ⚠️ 无返回值文档 |

### 2.3 员工 / 组织 / 岗位 / 部门（10）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getAllUser` | 根据条件模糊查询员工信息，如果不传任何值表示查询所有对应门店的员工 | `userName`, `phone`, `workNo` | 医院为角度/客户盘点/员工为角度 | 在职状态, 员工名称, 部门信息, name, id, 删除状态, 启用状态, 岗位信息 | ✅ |
| 📖 | `getDeptById` | 根据部门id查询部门信息 | `deptId` | 医院为角度 | 部门id, 部门名称 | ✅ |
| 📖 | `getDeptByName` | 根据部门名称模糊查询部门信息，如果部门名称为空则查询所有部门 | `deptName` | 医院为角度 | 部门id, 部门名称 | ✅ |
| 📖 | `getRoleById` | 根据岗位id查询岗位信息 | `roleId` | 医院为角度 | 岗位id, 岗位名称 | ✅ |
| 📖 | `getRoleByName` | 根据岗位名称模糊查询岗位信息，如果岗位名称为空则查询所有岗位 | `roleName` | 医院为角度 | 岗位id, 岗位名称 | ✅ |
| 📖 | `getStatisticsByUserId` | 查询具体员工(用户)对应时间段的查询会话(AI助理/客户分析/对话)统计数据，结果请严格用表格的形式输出 | `userId`, `startDate`, `endDate` | 医院为角度 | 员工姓名, 日期, 对话次数, 对话轮数, 客户姓名 | ⚠️ 文档有、tools/list 未暴露 |
| 📖 | `getUserByDept` | 根据部门名称模糊查询对应的所有员工 | `deptName` | 医院为角度 | 在职状态, 员工名称, 部门信息, name, id, 删除状态, 启用状态, 岗位信息 | ✅ |
| 📖 | `getUserById` | 根据用户Id查询员工信息 | `userId` | 医院为角度 | 在职状态, 员工名称, 部门信息, name, id, 删除状态, 启用状态, 岗位信息 | ✅ |
| 📖 | `getUserInfoByKeyword` | 根据员工姓名或者电话号码或者工号查询员工信息 | `userName` | 医院为角度/客户盘点/员工为角度 | 在职状态, 员工名称, 部门信息, name, id, 删除状态, 启用状态, 岗位信息 | ✅ |
| 📖 | `getUserToRole` | 根据岗位名称模糊查询对应的所有员工 | `roleName` | 医院为角度 | 在职状态, 员工名称, 部门信息, name, id, 删除状态, 启用状态, 岗位信息 | ✅ |

### 2.4 咨询（4）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getConsultInfoByCustomerId` | 通过客户id查询客户在某个时间段或者最近几次的咨询信息 | `customerId`, `startDate`, `endDate`, `number` | 客户为角度 | 咨询师, 鉴别诊断, 牙位诊断, 处理方案, 面诊提交时间, 月经是否正常, 咨询项目, 未成交原因 | ✅ |
| 📖 | `getConsultInfoByCustomerIdList` | 通过批量客户id查询客户在某个时间段的咨询信息 | `customerId`, `startDate`, `endDate`, `number` | 医院为角度/员工为角度 | 咨询师, 鉴别诊断, 牙位诊断, 处理方案, 面诊提交时间, 月经是否正常, 咨询项目, 未成交原因 | ✅ |
| 📖 | `getConsultInfoByDate` | 通过某个时间段或者最近几次的咨询信息 | `startDate`, `endDate`, `number` | 医院为角度 | 咨询师, 鉴别诊断, 牙位诊断, 处理方案, 面诊提交时间, 月经是否正常, 咨询项目, 未成交原因 | ✅ |
| 📖 | `getConsultInfoByUserId` | 通过咨询师id(员工id)查询在某个时间段或者最近几次的咨询信息 | `userId`, `startDate`, `endDate`, `number` | 员工为角度 | 咨询师, 鉴别诊断, 牙位诊断, 处理方案, 面诊提交时间, 月经是否正常, 咨询项目, 未成交原因 | ✅ |

### 2.5 回访（4）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getVisitInfoByCustomerId` | 通过客户id查询客户在某个时间段的回访信息 | `customerId`, `startDate`, `endDate` | 客户为角度 | 项目名称, 计划回访截止日期, 回访方式, 回访效果, 实际回访日期, 回访内容, 实际回访人姓名, 治疗回访对应的治疗时间 | ✅ |
| 📖 | `getVisitInfoByCustomerIdList` | 通过批量客户id查询客户在某个时间段的回访信息 | `customerId`, `startDate`, `endDate` | 医院为角度/员工为角度 | 项目名称, 计划回访截止日期, 回访方式, 回访效果, 实际回访日期, 回访内容, 实际回访人姓名, 治疗回访对应的治疗时间 | ✅ |
| 📖 | `getVisitInfoByDate` | 通过某个时间段的回访信息 | `startDate`, `endDate` | 医院为角度 | 项目名称, 计划回访截止日期, 回访方式, 回访效果, 实际回访日期, 回访内容, 实际回访人姓名, 治疗回访对应的治疗时间 | ✅ |
| 📖 | `getVisitInfoByUserId` | 通过员工id查询某个时间段的回访信息 | `userId`, `startDate`, `endDate` | 员工为角度 | 项目名称, 计划回访截止日期, 回访方式, 回访效果, 实际回访日期, 回访内容, 实际回访人姓名, 治疗回访对应的治疗时间 | ✅ |

### 2.6 客户档案 / 标签 / 线索（13）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getAllLabel` | 查询所有的标签信息 | — | 所有角度 | 标签id, 分类id, 标签名称, 标签分类 | ✅ |
| 📖 | `getCustomerBaseInfoByCustomerIdList` | 通过客户Id列表查询客户基本信息，姓名，会员号，档案号 | `customerId` | 所有角度 | 档案号, id, 客户姓名, 会员编号 | ✅ |
| 📖 | `getCustomerClueByCustomerId` | 通过客户id查询客户的线索信息 | `customerId` | 客户为角度 | 点赞数, 重要程度, 创建人姓名, 修改时间, 添加终端, 创建时间, 线索内容, 线索标签 | ✅ |
| 📖 | `getCustomerClueByCustomerIdList` | 通过批量客户id查询客户的线索信息 | `customerId` | 医院为角度/员工为角度 | 点赞数, 重要程度, 创建人姓名, 修改时间, 添加终端, 创建时间, 线索内容, 线索标签 | ✅ |
| 📖 | `getCustomerClueByDate` | 查询某个时间段的线索信息 | `startDate`, `endDate` | 医院为角度 | 点赞数, 重要程度, 创建人姓名, 修改时间, 添加终端, 客户id, 创建时间, 线索内容 | ✅ |
| 📖 | `getCustomerIdByKeyword` | 通过客户姓名或者电话号码或者会员号或者档案号查询客户的id | `Keyword` | 所有角度 | 查询关键字, 客户id | ✅ |
| 📖 | `getCustomerIdByKeywords` | 通过客户姓名或者电话号码或者会员号或者档案号查询客户的id | `Keyword` | 所有角度 | 查询关键字, 客户id | ✅ |
| 📖 | `getCustomerIdInfo` | 通过客户姓名或者电话号码或者会员号或者档案号只查询客户的id；如果查询多条数据则取第一条数据，因此建议提供完整的四个参数进行比较精准的查询 | `customerName`, `phoneNumber`, `vipNumber`, `documentNumber` | — | — | ⚠️ 无返回值文档 |
| 📖 | `getCustomerInfo` | 通过客户姓名或者电话号码或者会员号或者档案号查询客户信息；如果查询多条数据则取第一条数据，因此建议提供完整的四个参数进行比较精准的查询 | `customerName`, `phoneNumber`, `vipNumber`, `documentNumber` | 所有角度 | 地区, 客户来源备注, rfm中的m值, 是否有皮肤/整形治疗史, 报备人, 客户当前活跃度, 目标业绩, 会员号 | ✅ |
| 📖 | `getCustomerInfoById` | 通过客户id查询客户基本信息 | `customerId` | 客户为角度 | 地区, 客户来源备注, rfm中的m值, 是否有皮肤/整形治疗史, 报备人, 客户当前活跃度, 目标业绩, 会员号 | ✅ |
| 📖 | `getCustomerLabelByCustomerId` | 通过客户id查询客户的标签信息 | `customerId` | 客户为角度 | 生效时间, 失效时间, 激活状态, 有效期(天), 备注, id, 标签激活人, 标签分类id | ✅ |
| 📖 | `getCustomerLabelByCustomerIdList` | 通过客户id查询客户的标签信息 | `customerId` | 客户为角度 | 生效时间, 失效时间, 激活状态, 有效期(天), 备注, id, 标签激活人, 标签分类id | ✅ |
| 📖 | `getPageCustomerInfo` | 分页查询客户信息 | `page`, `size` | 给外部提供的MCP工具 | 地区, 客户来源备注, rfm中的m值, 是否有皮肤/整形治疗史, 报备人, 客户当前活跃度, 目标业绩, 会员号 | ✅ |

### 2.7 库存 / 出入库（9）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getMaterialInventoryInfoById` | 根据物料的id查询物料的库存信息 | `materialId` | 医院为角度 | 是否禁用, 产地, 仓库名称, 进价单位, 批次, 本仓库剩余数量, 规格, 物料分类 | ✅ |
| 📖 | `getMaterialInventoryInfoByName` | 根据物料的名称或者物料编码模糊查询物料的库存信息 | `materialName` | 医院为角度 | 是否禁用, 产地, 仓库名称, 进价单位, 批次, 本仓库剩余数量, 规格, 物料分类 | ✅ |
| 📖 | `getOutInventoryByDate` | 查询指定时间段内的出库单信息 | `startDate`, `endDate` | 医院为角度 | 出库完成时间, 调入仓库, 出库申请时间, 来源单号, 审批状态, 出库操作人, 开单时间, 客户id | ✅ |
| 📖 | `getOutInventoryByDateAndName` | 在指定时间范围内根据物料名称或者物料编码模糊搜索物料的出库情况 | `startDate`, `endDate`, `materialNameOrCode` | 医院为角度 | 出库单位, 进价单位, 批次, 出库操作人, 型号, 领用科室, 备注, 出库单状态 | ✅ |
| 📖 | `getOutInventoryDetailByNumber` | 根据出库单号查询当前出库单的出库信息 | `number` | 医院为角度 | 出库时间, 出库操作人, 领用科室, 出库单号, 备注, 相关客户电话, 出库单状态, 出库id | ✅ |
| 📖 | `getOutInventoryDetailByNumberList` | 根据出库单号列表批量查询当前出库单的出库信息 | `number` | 医院为角度 | 出库时间, 出库操作人, 领用科室, 出库单号, 备注, 相关客户电话, 出库单状态, 出库id | ✅ |
| 📖 | `getStorageInfoByStorageNumber` | 根据入库单号查询入库单信息 | `number` | 医院为角度 | 入库单状态, 部门, 入库时间, 审批状态, 仓库, 入库id, 入库物料信息, 含税进价 | ✅ |
| 📖 | `getStorageInfosByDate` | 查询某个时间段内的入库情况 | `startDate`, `endDate` | 医院为角度 | 入库时间, 来源单号, 审批状态, 仓库, 备注, 不含税入库金额, 入库类型, 入库单状态 | ✅ |
| 📖 | `getStorageInfosByDateAndName` | 在指定时间范围内根据物料名称或者物料编码模糊搜索物料的入库情况 | `startDate`, `endDate`, `materialNameOrCode` | 医院为角度 | 入库时间, 来源单号, 审批状态, 仓库, 备注, 不含税入库金额, 入库类型, 入库单状态 | ✅ |

### 2.8 开发计划（3）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getDevPlanInfoByCustomerId` | 通过客户id查询客户在某个时间段的开发计划信息 | `customerId`, `startDate`, `endDate` | 客户为角度 | 预计开发金额, 客户主诉, 失效截止时间, 开发计划标签, 开发人, 客户id, 实际开发金额, 名称 | ✅ |
| 📖 | `getDevPlanInfoByCustomerIdList` | 通过客户id查询客户在某个时间段的开发计划信息 | `customerId`, `startDate`, `endDate` | 客户为角度 | 预计开发金额, 客户主诉, 失效截止时间, 开发计划标签, 开发人, 客户id, 实际开发金额, 名称 | ✅ |
| 📖 | `getDevPlanInfoByDate` | 通过某个时间段查询开发计划信息 | `startDate`, `endDate` | 医院为角度 | 预计开发金额, 客户主诉, 失效截止时间, 开发计划标签, 开发人, 客户id, 实际开发金额, 名称 | ✅ |

### 2.9 报备（4）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getCustomerPreparationByCustomerId` | 通过客户id查询客户在某个时间段的报备信息 | `customerId`, `startDate`, `endDate` | 客户为角度 | 项目名称, 来源的运营媒体, 来源的市场渠道, 客户id, 报备说明, 客户姓名, 性别, 微信号 | ✅ |
| 📖 | `getCustomerPreparationByCustomerIdList` | 通过批量客户id查询客户在某个时间段的报备信息 | `customerId`, `startDate`, `endDate` | 医院为角度/员工为角度 | 项目名称, 来源的运营媒体, 来源的市场渠道, 客户id, 报备说明, 客户姓名, 性别, 微信号 | ✅ |
| 📖 | `getCustomerPreparationWithDate` | 查询在某个时间段的报备信息 | `startDate`, `endDate` | 医院为角度 | 项目名称, 来源的运营媒体, 来源的市场渠道, 客户id, 报备说明, 客户姓名, 性别, 微信号 | ✅ |
| 📖 | `getPreparationByUserId` | 查询在某个时间段某个员工（员工id）的报备信息 | `userId`, `startDate`, `endDate` | 员工为角度 | 项目名称, 来源的运营媒体, 来源的市场渠道, 客户id, 报备说明, 客户姓名, 性别, 微信号 | ✅ |

### 2.10 接待（4）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getCustomerReceptionByCustomerId` | 通过客户id查询客户在某个时间段的接待信息 | `customerId`, `startDate`, `endDate` | 客户为角度 | 就诊医生, 就诊项目, 是否是手动接待, 客户id, 接待咨询师, 会员号, 客户姓名, 就诊类型 | ✅ |
| 📖 | `getCustomerReceptionByCustomerIdList` | 通过批量客户id查询客户在某个时间段的接待信息 | `customerId`, `startDate`, `endDate` | 医院为角度/员工为角度 | 就诊医生, 就诊项目, 是否是手动接待, 客户id, 接待咨询师, 会员号, 客户姓名, 就诊类型 | ✅ |
| 📖 | `getReceptionByUserId` | 通过员工id查询某个时间段的接待信息 | `userId`, `startDate`, `endDate` | 员工为角度 | 就诊医生, 就诊项目, 是否是手动接待, 客户id, 接待咨询师, 会员号, 客户姓名, 就诊类型 | ✅ |
| 📖 | `getReceptionWithDate` | 查询在某个时间段的接待信息 | `startDate`, `endDate` | 医院为角度 | 就诊医生, 就诊项目, 是否是手动接待, 客户id, 接待咨询师, 会员号, 客户姓名, 就诊类型 | ✅ |

### 2.11 治疗 / 划扣（5）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getBillingAndPaymentAndTreatmentByCustomerId` | 通过客户id查询客户在某个时间段或者最近几次的订单信息和订单项目和订单缴费情况和治疗项目信息加起来的所有信息 | `customerId`, `startDate`, `endDate`, `number` | 客户为角度 | 订单来源, 折扣金额, 订单类型, 订单项目信息, 项目内容, 项目折扣金额, 项目总次数, 项目剩余次数 | ✅ |
| 📖 | `getBillingAndPaymentAndTreatmentByCustomerIdList` | 通过批量客户id查询客户在某个时间段的订单信息和订单项目和订单缴费情况和治疗项目信息加起来的所有信息 | `customerId`, `startDate`, `endDate` | 医院为角度/员工为角度 | 订单来源, 折扣金额, 订单类型, 订单项目信息, 项目内容, 项目折扣金额, 项目总次数, 项目剩余次数 | ✅ |
| 📖 | `getBillingAndPaymentAndTreatmentByDate` | 通过某个时间段查询订单信息和订单项目和订单缴费情况和治疗项目信息加起来的所有信息 | `startDate`, `endDate` | 医院为角度 | 订单来源, 折扣金额, 订单类型, 订单项目信息, 项目内容, 项目折扣金额, 项目总次数, 项目剩余次数 | ✅ |
| 📖 | `getTreatmentByCustomerId` | 通过客户id查询客户在某个时间段或者最近几次的治疗信息 | `customerId`, `startDate`, `endDate`, `number` | 客户为角度 | 是否划扣, 治疗门店, 是否核销, billingId, 项目, 治疗次数, 治疗时间, 治疗科室 | ✅ |
| 📖 | `getTreatmentByDate` | 查询某个时间段的治疗(划扣)信息 | `startDate`, `endDate` | 医院为角度 | 是否划扣, 治疗门店, 是否核销, billingId, 项目, 治疗次数, 治疗时间, 治疗科室 | ✅ |

### 2.12 统计 / 每日小结（2）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getDailySummaryByDate` | 查询当前员工指定日期小结信息(运营) | `startDate`, `endDate` | 每日小结 | 2026-10-29, 咨询小结, 接诊人数, 开单笔数, 开单总金额, 收费总额, 实收金额, 欠费金额 | ✅ |
| 📖 | `getStatistics` | 根据时间段查询会话(AI助理/客户分析/对话)统计数据，结果请严格用表格的形式输出 | `startDate`, `endDate` | 医院为角度 | 员工姓名, 日期, 对话次数, 对话轮数, 客户姓名 | ⚠️ 文档有、tools/list 未暴露 |

### 2.13 订单 / 收银 / 缴费（6）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getBillingInfoByCustomerId` | 通过客户id查询客户在某个时间段或者最近几次的订单信息 | `customerId`, `startDate`, `endDate`, `number` | 客户为角度 | 订单来源, 折扣金额, 订单类型, 订单项目信息, 项目内容, 项目折扣金额, 项目总次数, 项目剩余次数 | ✅ |
| 📖 | `getBillingInfoByCustomerIdList` | 通过批量客户id查询客户在某个时间段的订单信息 | `customerId`, `startDate`, `endDate` | 客户为角度 | 订单来源, 折扣金额, 订单类型, 订单项目信息, 项目内容, 项目折扣金额, 项目总次数, 项目剩余次数 | ✅ |
| 📖 | `getBillingInfoByDate` | 查询在某个时间段的所有订单信息 | `startDate`, `endDate` | 医院为角度 | 订单来源, 折扣金额, 订单类型, 订单项目信息, 项目内容, 项目折扣金额, 项目总次数, 项目剩余次数 | ✅ |
| 📖 | `getPaymentByCustomerId` | 通过客户id查询客户在某个时间段或者最近几次的订单缴费情况 | `customerId`, `startDate`, `endDate`, `number` | 客户为角度 | 实收/实退的支付方式, 实收/实退, billingId, 赠送储值抵扣金额, 积分抵扣金额, 权益卡抵扣金额, 储值抵扣金额, 应收/应退 | ✅ |
| 📖 | `getPaymentByDate` | 查询某个时间段的订单缴费情况 | `startDate`, `endDate` | 医院为角度 | 实收/实退的支付方式, 实收/实退, billingId, 赠送储值抵扣金额, 积分抵扣金额, 权益卡抵扣金额, 储值抵扣金额, 应收/应退 | ✅ |
| ✍️ | `markManualOrder` | 根据订单号标记为手工订单，会同时修改billing表和payment表的import_type为1;因为是修改数据所以必须具有对应的权限才能调用，请联系睿美云客服开通权限； | `billingNo` | — | — | 🔴 写操作，需审批；⚠️ 无返回值文档 |

### 2.14 账号绑定 / 运维写入（2）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| ✍️ | `restoreWxByVipNums` | 根据会员号批量恢复客户小程序，多个会员号以英文分号（;）分隔 | `vipNums` | — | — | 🔴 写操作，需审批；⚠️ 无返回值文档 |
| ✍️ | `unbindWxByVipNums` | 根据会员号批量解绑客户小程序，多个会员号以英文分号（;）分隔，例如 V001;V002;V003;因为是修改数据所以必须具有对应的权限才能调用，请联系睿美云客服开通权限； | `vipNums` | — | — | 🔴 写操作，需审批；⚠️ 无返回值文档 |

### 2.15 项目 / 套餐 / 物料 / 销售项（14）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getAllMaterial` | 分页获取所有物料信息 | `page`, `size` | 医院为角度 | 成本业绩单位, 售价, 型号, 备注, 默认用药天数(天), 成本业绩, 物料分类, 折损率(%) | ✅ |
| 📖 | `getAllProjectNames` | 查询门店所有的项目(品相)的名称信息,如果需要查询全量项目时，可以优先使用该方法找到合适的项目，在通过方法返回的id查询具体的项目信息 | — | 所有角度 | name, id | ✅ |
| 📖 | `getAllSaleItemType` | 获取所有销售项分类，和睿美云系统内部的选项目抽屉一样 | — | 给外部提供的MCP工具/客户盘点 | projectType, id, title, key, value, groupInfoId, children, settingFlag | ✅ |
| 📖 | `getEfficaciousExpirePackageInfoAll` | 查询所有有效并且到期的套餐信息 | — | 所有角度 | 折扣率, 是否可打折, 总价, 可购买的客户类型, 套餐名称, 套餐分类, 可购买会员等级, id | ✅ |
| 📖 | `getEfficaciousPackageInfoAll` | 查询所有有效并未到期的套餐信息 | — | 所有角度 | 折扣率, 是否可打折, 总价, 可购买的客户类型, 套餐名称, 套餐分类, 可购买会员等级, id | ✅ |
| 📖 | `getInvalidPackageInfoAll` | 查询所有无效(包括到期)的套餐信息，没有明确要求尽量少调这个函数 | — | 所有角度 | 折扣率, 是否可打折, 总价, 可购买的客户类型, 套餐名称, 套餐分类, 可购买会员等级, id | ✅ |
| 📖 | `getMaterialById` | 通过物料id查询物料信息 | `materialId` | 医院为角度 | 成本业绩单位, 售价, 型号, 备注, 默认用药天数(天), 成本业绩, 物料分类, 折损率(%) | ✅ |
| 📖 | `getMaterialByName` | 通过物料名称或物料编码模糊查询物料信息，最多查询30条数据 | `materialName` | 医院为角度 | 成本业绩单位, 售价, 型号, 备注, 默认用药天数(天), 成本业绩, 物料分类, 折损率(%) | ✅ |
| 📖 | `getPackageInfoAllById` | 根据套餐Id查询套餐信息，不区分是否有效 | `packageId` | 所有角度 | 折扣率, 是否可打折, 总价, 可购买的客户类型, 套餐名称, 套餐分类, 可购买会员等级, id | ✅ |
| 📖 | `getPackageInfoByName` | 根据套餐名称查询套餐信息 | `packageName` | 所有角度 | 折扣率, 是否可打折, 总价, 可购买的客户类型, 套餐名称, 套餐分类, 可购买会员等级, id | ✅ |
| 📖 | `getProjectInfo` | 根据项目（品项）名称模糊查询项目（品项）信息，最多30条数据，请尽量名称完整 | `projectName` | 所有角度 | 项目名称, 缴费后项目有效期(单位天), 项目时长, 是否是检查项目, 麻醉金额, 是否是注射项目, 是否被删除, 是否属于划扣项目 | ✅ |
| 📖 | `getProjectInfoAll` | 查询门店所有的项目（品相）信息,查询的数据量会很大，请谨慎调用 | — | 所有角度 | 项目名称, 缴费后项目有效期(单位天), 项目时长, 是否是检查项目, 麻醉金额, 是否是注射项目, 是否被删除, 是否属于划扣项目 | ✅ |
| 📖 | `getProjectInfoById` | 通过项目（品项）id查询对应项目的项目（品项）信息 | `projectId` | 所有角度 | 项目名称, 缴费后项目有效期(单位天), 项目时长, 是否是检查项目, 麻醉金额, 是否是注射项目, 是否被删除, 是否属于划扣项目 | ✅ |
| 📖 | `getSaleItemList` | 根据类型获取对应的项目套餐次卡年卡等信息，和睿美云系统内部的选项目抽屉一样，最多查询30条数据，输入的搜索条件越精准，查询越精准 | `saleItemType`, `name` | — | — | ⚠️ 无返回值文档 |

### 2.16 预约（4）

| 类型 | 函数名 | 说明 | 入参 | 视角 | 主要返回字段 | 状态 |
|---|---|---|---|---|---|---|
| 📖 | `getCustomerBespeakByCustomerId` | 通过客户id查询客户预约信息 | `customerId`, `startDate`, `endDate` | 客户为角度 | 预约状态, 预约创建人, 会员名字, 预约项目, 预约结束时间, 客户id, 邀约人, id | ✅ |
| 📖 | `getCustomerBespeakByCustomerIdList` | 通过批量客户id查询客户预约信息 | `customerId`, `startDate`, `endDate` | 医院为角度/员工为角度 | 预约状态, 预约创建人, 会员名字, 预约项目, 预约结束时间, 客户id, 邀约人, id | ✅ |
| 📖 | `getCustomerBespeakByDate` | 通过预约的时间查询预约信息（不是创建时间） | `startDate`, `endDate` | 医院为角度 | 预约状态, 预约创建人, 会员名字, 预约项目, 预约结束时间, 客户id, 邀约人, id | ✅ |
| 📖 | `getCustomerBespeakByUserId` | 通过员工id查询某个时间段的预约信息 | `userId`, `startDate`, `endDate` | 员工为角度 | 预约状态, 预约创建人, 会员名字, 预约项目, 预约结束时间, 客户id, 邀约人, id | ✅ |

## 3. 写操作（🔴 审批门控，绝不自动调用）

| 函数 | 说明 | 限制 |
|---|---|---|
| `markManualOrder` | 根据订单号标记为手工订单，会同时修改billing表和payment表的import_type为1;因为是修改数据所以必须具有对应的权限才能调用，请联系睿美云客服开通权限； | 修改线上数据，需睿美云开通权限 + 李刚明确确认 |
| `restoreWxByVipNums` | 根据会员号批量恢复客户小程序，多个会员号以英文分号（;）分隔 | 修改线上数据，需睿美云开通权限 + 李刚明确确认 |
| `unbindWxByVipNums` | 根据会员号批量解绑客户小程序，多个会员号以英文分号（;）分隔，例如 V001;V002;V003;因为是修改数据所以必须具有对应的权限才能调用，请联系睿美云客服开通权限； | 修改线上数据，需睿美云开通权限 + 李刚明确确认 |

> 官方 MCP 的写操作与 TPOS REST 写接口是**两套独立的门控**，不要因为 REST 侧验证过就自动放行 MCP 写操作。


## 4. 与 TPOS REST 通道的对照

| 能力 | 官方 MCP 函数（示例） | REST 接口 | 结论 |
|---|---|---|---|
| 客户搜索 | `getCustomerIdByKeyword(s)` / `getCustomerInfo` | `GET /customer/customer-search` | REST 可控性更好 |
| 客户详情 | `getCustomerInfoById` | `GET /customer/customer-by-id` | **客户明细一律走 REST**（注意事项 6） |
| 订单/开单 | `getBillingInfoByDate` / `getBillingInfoByCustomerId` | `GET /order/billing-page` | REST 可分页、可跨门店 |
| 缴费 | `getPaymentByDate` / `getPaymentByCustomerId` | `POST /report/cashier-record-page` | REST 才有完整收银口径 |
| 治疗/划扣 | `getTreatmentByDate` / `getTreatmentByCustomerId` | `GET /treat/treated-page-review` | REST 才有 `deductUserName` 执行人 |
| 回访 | `getVisitInfoByDate` / `getVisitInfoByCustomerId` | `POST /visit/get-visit-page` | REST 才能按 `visitedFlag` 精确筛待回访 |
| 咨询/接待/预约/报备 | `getConsultInfoByDate`、`getReceptionWithDate`、`getCustomerBespeakByDate`、`getCustomerPreparationWithDate` | `consultation/page`、`reception/*`、`cusbespeak/*`、`preparation/*` | 按字段需求择一 |
| 员工/部门/岗位 | `getAllUser`、`getDeptByName`、`getRoleByName` | `user/get-page`、`basic/dept-tree`、`role/getRoleListV2` | 等价 |
| 项目/套餐/物料/库存 | `getAllProjectNames`、`getPackageInfoByName`、`getAllMaterial`、`getStorageInfosByDate` | `basic/*-page`、`inventory/*-page` | REST 字段更全 |
| 企微聊天/录音/ASR | `getWeChatMessage`、`getRecordingByDate`、`getConversationByCustomerId` | `wechat/message/*` | MCP 封装更贴近语义检索 |

🔴 **注意事项 6 仍有效**：`getTreatmentByCustomerId`、`getBillingInfoByCustomerId`、`getVisitInfoByCustomerId`、`getConsultInfoByCustomerId`、`getCustomerReceptionByCustomerId`、`getDevPlanInfoByCustomerId` 这 6 个客户维度函数实测一律返回「没有查到…」，**不要用它们推断客户没有数据**。本次清单新增的 `...ByCustomerIdList` 批量版未实测，首次使用前须用已知有数据的客户验证。


## 5. 复跑方法

```bash
python3 scripts/fetch_official_mcp_docs.py
```

凭证读 `~/.workbuddy/mcp.json` 的 `mcpServers.rmy`（`appKey` 不入版本库）；脚本走 streamable HTTP（POST JSON-RPC），已验证该端点 **不支持旧 SSE**（GET 返回 405）。

