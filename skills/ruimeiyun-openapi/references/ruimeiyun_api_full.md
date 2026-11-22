<title>睿美云开放接口</title>

# TPOS鉴权

<synced_reference src-block-id="YXOvdNbZoss8dabWrdxchLy9nEd" src-token="Ncapd7ovKo95WlxMnuXcf65xnZb"></synced_reference>

# 公共实体

## 结构化数据

### 项目 - 项目分类（ProjectJsonEntity）

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| dataId | 是 | string | 项目/项目分类id |  |
| dataType | 是 | int | 项目：0  <br/>项目分类：1 |  |
| dataName |  | string | 数据名称（项目名称或项目分类名称） |  |



## 枚举值

### 缴费，收银类型（PaymentTypeEnum）

| **名称** | **枚举值** | **描述** |
|-|-|-|
| PAYMENT | 0 | 订单收费 |
| REFUND | 1 | 订单退费 |
| TRANSFER_PROJECT | 2 | 转项收费 |
| DEPOSIT_PAYMENT | 3 | 定金收费 |
| DEPOSIT_REFUND | 4 | 定金退费 |
| BALANCE_RECHARGE | 5 | 充值收费 |
| BALANCE_REFUND | 6 | 储值退费 |
| TRANSFER_REFUND | 7 | 转项退费 |
| EQUITY_PAYMENT | 8 | 权益卡收费 |
| EQUITY_REFUND | 9 | 权益卡退费 |

### 订单 - 订单来源（BillingDataSourceEnum）

| **名称** | **枚举值** | **描述** |
|-|-|-|
| CLIENT | 0 | 院内 |
| WX | 1 | 睿美云小程序 |
| APP | 2 | app |
| YZ | 3 | 有赞微商城 |
| WM | 4 | 微盟智慧零售 |
| SO_YANG | 5 | 新氧平台 |
| MIRAGE | 6 | 美际订单 |
| YZMY | 7 | 有赞美业 |
| EQUITY_CARD | 8 | 权益卡赠送 |
| SCRM_GROUP_PURCHASING | 9 | 系统小程序【拼团】 |

### 订单 - 订单状态（BillingStatusEnum）

| **名称** | **枚举值** | **描述** |
|-|-|-|
| WAIT_PAID | 0 | 未付款 |
| PAID | 1 | 已付款 |
| CANCEL | 2 | 已作废 |
| PART_PAID | 3 | 欠费 |

# **客户相关（customer）**

## [**客户档案新增（编辑）**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#doxcnJm4mDHNXRaQabgwnA7YBHf)

> **目前可编辑的字段较少，如有编辑客户的需要，请及时沟通**

- 请求URL（需要tpos鉴权）

**`/api/``v1/tpos/customer/info-sync`     POST**

- 参数说明

| 参数名称 | 参数说明 | in | 是否必须 | 数据类型 | 备注 |
|-|-|-|-|-|-|
| alterFieldList | 所需编辑字段名List | body | **编辑时必填** | array | ["customerName"]  <br/>表示要修改客户姓名 |
| businessType | 1-新增,2-编辑 | body | **必填** | integer(int32) |  |
| customerName | 客户姓名 | body | **新增时必填** | string |  |
| mainPhone | 主号码 | body | **必填** | string | 手机号不允许编辑 |
| neuronTenantId | 门店id | body | **新增时必填** |  |  |
| neuronCusId | 睿美云客户id | body | **编辑的时候必传** | string |  |
| platformCusId | 三方平台客户id | body |  | string | 2024-03-19：  <br/>新增时可传  <br/>修改时，不支持此参数 |
| idCardNumber | 身份证号 |      body |  | string |  |
| remark | 客户档案备注 | body |  | string |  |
| sex | 1-男,2-女 | body |  | integer(int32) |  |
| sourceType | 0："运营媒体"  <br/>1："市场渠道"  <br/>2："老带新"  <br/>3："其他"  <br/>4："员工"  <br/>5："自然到院"  <br/>6："SCRM-新客户"  <br/>7："SCRM-老带新" | body | **必填** | integer(int32) | 不确定的就传3 |
| sourceTypeDetailAll | source_type=0 则为运营媒体或运营媒体类型id  <br/>source_type=1 则为市场渠道或市场渠道类型id  <br/>source_type=2 则老带新客户id  <br/>source_type=3 则其他描述  <br/>source_type=4 则为员工id  <br/>source_type=5 则为空  <br/>source_type=6 则为空  <br/>source_type=7 则老带新客户id | body | **视情况而定** | string |  |
| sourceTypeDetailType | source_type为0,1时需要传该字段，值为：obh/type  <br/>obj : 表示source_type_detail_all字段存储为具体渠道id;  <br/>type: 表示source_type_detail_all字段存储为渠道类型id; | body |  | string | 取值 "obj" 或 "type" |
| birthday | 生日 | body |  | string |  |
| oldCustomerPhone | 客户来源是老带新时，这个参数和sourceTypeDetailAll二选一 | body |  | string |  |
| area | 现住地址 | body |  | string |  |
| marriedFlag | 婚姻状况  <br/>0-未婚 1-已婚 2-未知 3-离异 | body |  | int |  |
| fertilityFlag | 生育状况  <br/> 0-未生育 \* 1-已生育 | body |  | int |  |
| passportNum | 护照号码 | body |  | string |  |
| passportType | 护照类型：  <br/>外交护照  <br/>*PASSPORT_TYPE_DIPLOMATIC*  <br/>公务护照  <br/>*PASSPORT_TYPE_OFFICIAL*  <br/>普通护照  <br/>*PASSPORT_TYPE_GENERAL*  <br/>特区护照  <br/>*PASSPORT_TYPE_SPECIAL* | body |  | string |  |
| createUserId | 建档人id | body |  | string |  |

- **返回结果**

1. 成功建档，status是true，返回的neuronCusId即睿美云建档成功后的客户id，如果已经有相同电话的档案，则返回对应档案的客户id，如果有多个相同电话的档案，则随机返回一个档案id

![图片展示的是Postman中客户档案新增接口的测试界面。请求方法为POST，URL为https://api.v1.rumei.cn/api/v1/tpos/customer/info-sync。Body部分以JSON格式发送数据，包含多个字段，如mainPhone、customerName等。右侧响应结果中，code为10000，status为true，msg显示“操作成功”，data部分各字段值为空。该图片与文档中客户档案新增接口的返回结果部分对应，直观呈现了接口成功返回的数据情况。](https://feishu.cn/file/GC8fbZGJzonqlJxOjn7czDVknIg)

1. 建档失败，status是false，errorMsg会给出错误信息

![图片展示的是睿美云开放接口中客户档案新增（编辑）的接口测试结果。请求地址为127.0.0.1:60005/api/v1/tpos/customer/info-sync，请求方法为POST。Body部分输入了客户信息，包括主手机号、客户姓名、业务类型、neuronTenantId和sourceType等。返回结果中，code为18000，data部分显示客户id、错误信息、外部客户id等，status为false，msg为“操作成功”。该图片与文档中客户档案新增（编辑）的返回结果部分对应，直观呈现了接口测试情况。](https://feishu.cn/file/NkkdbOwb9olhFvxjlCKcTzEYnfd)



---

## [**获取客户信息列表**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#XIVKdgciao63HFxj2WpcmIyLnDb)

> **查询的是搜索引擎，系统内部新增客户后，搜索引擎数据略微有延迟）**

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/customer/customer-search    GET**

- 参数说明

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><b>字段</b></td><td><b>是否必填</b></td><td><b>类型</b></td><td><b>说明</b></td><td><b>备注</b></td></tr><tr><td>keyword</td><td rowspan="3" vertical-align="middle">关键字和时间区间二选一</td><td>string</td><td>关键字</td><td>支持姓名，电话，档案号，会员号的模糊查询</td></tr><tr><td>createDateStart</td><td>string</td><td>建档时间开始日期</td><td>yyyy-MM-dd格式的字符串</td></tr><tr><td>createDateEnd</td><td>string</td><td>建档时间结束日期</td><td>yyyy-MM-dd格式的字符串</td></tr><tr><td>tenantId</td><td>否</td><td>string</td><td>门店id</td><td>如果指定门店id，则只会查这个门店下的客户，否则查全机构的客户</td></tr><tr><td>page</td><td>否</td><td>int</td><td>当前页码</td><td>默认为：1，最小为：1</td></tr><tr><td>size</td><td>否</td><td>int</td><td>每页数量</td><td>默认为：20，最大为：500</td></tr><tr><td>lastCustomerId</td><td>否</td><td>string</td><td>上一个客户id（如果有值，则下一批客户的id一定会大于它）</td><td>避免搜索引擎深度翻页，如有有大量数据查询要求，建议传递此参数</td></tr><tr><td>   unionId</td><td>           否</td><td>     string</td><td>小程序union_id</td><td></td></tr></tbody></table>

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 |  |  |
| data | 结果内容 |  |  |
|   current |  | integer(int64) | 当前页 |
|   pages |  | integer(int64) | 页码总数 |
|   records |  | array | NormalCustomerTo |
|     activeStatus | 客户当前活跃度 | string |  |
|     activeStatusDesc | 客户当前活跃度描述 | string |  |
|     address | 地址 | string |  |
|     age | 年龄 | string |  |
|     allergyFlag | 过敏史 | integer |  |
|     allergyFlagDesc | 是否有过敏史 | string |  |
|     allergyLabelsName | 过敏标签名称 | string |  |
|     allergyRemark | 过敏史备注 | string |  |
|     area | 地区 | string |  |
|     areaProvince | 现址地址 | string |  |
|     arrears | 欠费金额 | string |  |
|     arrearsFlag | 是否有欠费记录 | string |  |
|     arriveDay | 来院年限 | string |  |
|     balance | 账户余额 | string |  |
|     givenBalance | 赠送余额 | string |  |
|     birthday | 生日 | string |  |
|     cardCount | 卡券数量 | string |  |
|     career | 职业 | string |  |
|     channelMaintainUser | 市场渠道开发人(渠道咨询师) | string |  |
|     channelType | 了解途径 | string |  |
|     channelTypeRemark | 了解途径其他描述 | string |  |
|     context | 客户阶段 | string |  |
|     costAmount | 消费总额 | string |  |
|     costPower | 消费能力 | string |  |
|     costThisYear | 今年消费 | string |  |
|     costTime | 消费次数(消费总次数) | string |  |
|     country | 国籍 | string |  |
|     createBy | 建档人id | string |  |
|     createByName | 建档人 | string |  |
|     createDate | 创建时间 | string |  |
|     crossHospitalSysUserName | 跨院咨询师 | string |  |
|     currentTransInDate | 入池时间 | string |  |
|     cusPoolType | 客户池类型,可用值:TYPE_PERSONAL,TYPE_NON_PERSONAL | string |  |
|     cusPoolTypeDesc | 客户池类型描述 | string |  |
|     delFlag | 删除状态 | boolean |  |
|     deposit | 定金金额 | string |  |
|     documentId | 档案号 | string |  |
|     email | 邮箱 | string |  |
|     exclusiveServerId | 专属客服id | string |  |
|     exclusiveServerName | 专属客服 | string |  |
|     exclusiveServerPhone | 专属客服电话 | string |  |
|     existVisitFlag | 有无回访计划 | string |  |
|     expandInfo | 扩展信息 | string |  |
|     externalUserId | 企微id（来自三方平台） | string |  |
|     fertilityFlag | 生育状况 | string |  |
|     fertilityFlagName | 生育状况描述 | string |  |
|     firstCostDate | 首次消费日期 | string |  |
|     firstRealTreatDate | 首次治疗时间 | string |  |
|     firstTreatDate | 初诊日期 | string |  |
|     firstVisitedDate | 首次回访 | string |  |
|     fscore | 最近一年消费次数，得分 | string |  |
|     groupSourceId | 来源如果是线上线下，并且由集团下发的，返给对应集团的来源的id | string |  |
|     id | 客户id | string |  |
|     idCardNumber | 身份证号码 | string |  |
|     income | 收入 | string |  |
|     integral | 积分 | string |  |
|     integralTotal | 成长值 | integer |  |
|     latestArriveDate | 最近到院时间 | string |  |
|     latestCostDate | 最近消费日期 | string |  |
|     latestVisitedDate | 最近回访时间 | string |  |
|     latestTreatDate | 最近治疗时间 | string |  |
|     levelFourthCustomerSource | 客户来源四级 | string |  |
|     levelSecondCustomerSource | 客户来源二级 | string |  |
|     levelThirdCustomerSource | 客户来源三级 | string |  |
|     mainPhone | 主电话号码 | string |  |
|     marriedFlag | 婚姻状况标识 | string |  |
|     marriedFlagName | 婚姻状况 | string |  |
|     medicalNo | 病历号 | string |  |
|     memberLevelName | 会员等级名称 | string |  |
|     memberLevelId | 会员等级id | string |  |
|     mscore | 最近一年消费总额，得分 | string |  |
|     name | 客户姓名 | string |  |
|     neuronCusId | 客户Id | string |  |
|     newCustomerCount | 推荐客户数量 | string |  |
|     nickName | 昵称 | string |  |
|     noVisitDay | 未回访天数 | string |  |
|     oldId | 介绍人id（谁介绍的我） | string |  |
|     oldName | 介绍人名称（（谁介绍的我） | string |  |
|     passportNum | 护照编号 | string |  |
|     passportType | 护照类型 | string |  |
|     perResidence | 常驻地址 | string |  |
|     personLabelsName | 个人标签名称 | string |  |
|     phoneNumber | 电话号码 | string |  |
|     plasticFlag | 皮肤/整形治疗史 | integer |  |
|     plasticFlagDesc | 有无皮肤/整形治疗史 | string |  |
|     plasticRemark | 院外治疗备注 | string |  |
|     poolName | 客户池 | string |  |
|     preDate | 报备时间 | string |  |
|     preDeptName | 报备部门 | string |  |
|     preProNames | 报备项目 | string |  |
|     preUserName | 报备人 | string |  |
|     propensity | 意向项目 | string |  |
|     propensityFriend | 朋友意向 | string |  |
|     relatedConsul | 相关咨询师 | string |  |
|     relatedDoctor | 相关医生 | string |  |
|     relatedServer | 相关客服 | string |  |
|     remark | 客户档案备注 | string |  |
|     rfm | rfm值 | string |  |
|     rfmTypeName | rfm类型(单独计算) | string |  |
|     roleManagerInfoList | 岗位负责人 | array | RoleManagerInfo |
|       customerId | 客户id | string |  |
|       id | 数据Id | string |  |
|       roleId | 岗位id | string |  |
|       roleManagerId | 配置负责岗位id | string |  |
|       roleName | 岗位名称 | string |  |
|       userId | 负责用户id | string |  |
|       userName | 负责用户姓名 | string |  |
|       userPhoneNumber | 负责用户手机号 | string |  |
|     rscore | 最近一次消费距今天数，得分 | string |  |
|     seedFlag | 是否是种子客户 | boolean |  |
|     sex | 性别 | string |  |
|     sexDesc | 性别描述 | string |  |
|     sickHistory | 既往史 | string |  |
|     sickHistoryRemark | 既往史备注 | string |  |
|     smartLabelCommonName | 公共标签 | string |  |
|     smartLabelPersonName | 个人标签 | string |  |
|     sourcePathName | 来源路径 | string |  |
|     sourcePathNameSecondAll | 客户第二来源路径 | string |  |
|     sourcePathNameThirdAll | 客户第三来源路径 | string |  |
|     sourceType | 来源 | string |  |
|     sourceTypeDetailAll | 具体来源 | string |  |
|     sourceTypeDetailType | obj表示具体来源，type表示分类 | string |  |
|     sourceTypeRemark | 来源备注 | string |  |
|     sourceTypeSecond | 客户第二来源类型 | string |  |
|     sourceTypeThird | 客户第三来源类型 | string |  |
|     sureType | 确认纠正,可用值:NOT_CONFIRMED,TO_BE_CONFIRMED,CONFIRMED | string |  |
|     sureTypeDesc | 确认纠正描述 | string |  |
|     sysUserId | 咨询师id | string |  |
|     sysUserName | 咨询师姓名 | string |  |
|     sysUserPhone | 咨询师电话 | string |  |
|     tenantId | 客户门店id | string |  |
|     tenantName | 建档门店 | string |  |
|     treatTime | 治疗次数 | string |  |
|     type | 客户类型 | string | 初诊/复诊/老客人/其他/空 |
|     typeDesc | 客户类型描述 | string |  |
|     unionId | unionId | string |  |
|     updateBy | 修改人id | string |  |
|     updateDate | 修改时间 | string |  |
|     urgentContactCall | 紧急联系人电话 | string |  |
|     urgentContactName | 紧急联系人 | string |  |
|     vipActiveDate | 会员有效期至 | string |  |
|     vipNum | 会员号 | string |  |
|     wechatSysUserName | 微信咨询师名称 | string |  |
|     wechatSysuserId | 微信咨询师id | string |  |
|     wechatUserId | 企业微信客户用户id | string |  |
|     weiXin | 微信 | string |  |
|     workState | 工作状况 | string |  |
|     workStateRemark | 工作状况其他描述 | string |  |
|     wxBindDate | 微信绑定时间（小程序绑定时间） | string |  |
|     wxBindFlag | 微信绑定标识 | boolean |  |
|     wxBindFlagDesc | 微信绑定描述 | string |  |
|     wxName | 微信昵称 | string |  |
|     wxPhotoURL | 微信头像地址 | string |  |
|             goldNum | 金币数量 | int |  |
|             latestTreatProject | 最近治疗项目 | String |  |
|             characterTag | 性格标签 | array |  |
|       id | 标签id | string |  |
|       name | 标签名称 | string |  |
|       color | 标签颜色 | string |  |
|             officialOpenId | 公众号openId | string |  |
|             miniOpenId | 小程序openId | string |  |
|   size |  | integer(int64) | 每页数据量 |
|   total |  | integer(int64) | 数据总数 |
| msg | 响应消息 | string |  |

## **通过客户id查询客户详情**

> **查询的是搜索引擎，系统内部新增客户后，搜索引擎数据略微有延迟）**

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/customer/customer-by-id    GET**

- 参数说明

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| customerId | 客户id | true | string |

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 |  |  |
| data | 结果内容 |  |  |
|   activeStatus | 客户当前活跃度 | string |  |
|   activeStatusDesc | 客户当前活跃度描述 | string |  |
|   address | 地址 | string |  |
|   age | 年龄 | string |  |
|   allergyFlag | 过敏史 | integer |  |
|   allergyFlagDesc | 是否有过敏史 | string |  |
|   allergyLabelsName | 过敏标签名称 | string |  |
|   allergyRemark | 过敏史备注 | string |  |
|   area   | 地区 | string |  |
|   areaProvince | 现址地址 | string |  |
|   arrears | 欠费金额 | string |  |
|   arrearsFlag | 是否有欠费记录 | string |  |
|   arriveDay | 来院年限 | string |  |
|   balance | 账户余额 | string |  |
|   givenBalance | 赠送余额 | string |  |
|   birthday | 生日 | string |  |
|   cardCount | 卡券数量 | string |  |
|   career | 职业 | string |  |
|   channelMaintainUser | 市场渠道开发人(渠道咨询师) | string |  |
|   channelType | 了解途径 | string |  |
|   channelTypeRemark | 了解途径其他描述 | string |  |
|   context | 客户阶段 | string |  |
|   costAmount | 消费总额 | string |  |
|   costPower | 消费能力 | string |  |
|   costThisYear | 今年消费 | string |  |
|   costTime | 消费次数(消费总次数) | string |  |
|   country   | 国籍 | string |  |
|   createBy | 建档人id | string |  |
|   createByName | 建档人 | string |  |
|   createDate | 创建时间 | string |  |
|   crossHospitalSysUserName | 跨院咨询师 | string |  |
|   currentTransInDate | 入池时间 | string |  |
|   cusPoolType | 客户池类型,可用值:TYPE_PERSONAL,TYPE_NON_PERSONAL | string |  |
|   cusPoolTypeDesc   | 客户池类型描述 | string |  |
|   deposit | 定金金额 | string |  |
|   documentId | 档案号 | string |  |
|   email   | 邮箱 | string |  |
|   exclusiveServerId | 专属客服id | string |  |
|   exclusiveServerName | 专属客服 | string |  |
|   exclusiveServerPhone | 专属客服电话 | string |  |
|   existVisitFlag | 有无回访计划 | string |  |
|   expandInfo | 扩展信息 | string |  |
|   externalUserId | 企微id（来自三方平台） | string |  |
|   fertilityFlag | 生育状况 | string |  |
|   fertilityFlagName | 生育状况描述 | string |  |
|   firstCostDate | 首次消费日期 | string |  |
|   firstRealTreatDate | 首次治疗时间 | string |  |
|   firstTreatDate | 初诊日期 | string |  |
|   firstVisitedDate | 首次回访 | string |  |
|   fscore | 最近一年消费次数，得分 | string |  |
|   groupSourceId | 来源如果是线上线下，并且由集团下发的，返给对应集团的来源的id | string |  |
|   id | 客户id | string |  |
|   idCardNumber | 身份证号码 | string |  |
|   income | 收入 | string |  |
|   integral | 积分 | string |  |
|   integralTotal | 成长值 | integer |  |
|   latestArriveDate | 最近到院时间 | string |  |
|   latestCostDate | 最近消费日期 | string |  |
|   latestVisitedDate | 最近回访时间 | string |  |
|   latestTreatDate | 最近治疗时间 | string |  |
|   levelFourthCustomerSource | 客户来源四级 | string |  |
|   levelSecondCustomerSource | 客户来源二级 | string |  |
| **  **levelThirdCustomerSource | 客户来源三级 | string |  |
| **  **mainPhone | 主电话号码 | string |  |
|   marriedFlag | 婚姻状况标识 | string |  |
|   marriedFlagName | 婚姻状况 | string |  |
|   medicalNo | 病历号 | string |  |
|   memberLevelName | 会员等级名称 | string |  |
|   memberLevelId | 会员等级id | string |  |
|   memberLevelId | 会员等级id | string |  |
|   mscore | 最近一年消费总额，得分 | string |  |
|   name | 客户姓名 | string |  |
|   neuronCusId | 客户Id | string |  |
|   newCustomerCount | 推荐客户数量 | string |  |
|   nickName | 昵称 | string |  |
|   noVisitDay | 未回访天数 | string |  |
|   oldId | 介绍人id | string |  |
|   oldName | 介绍人名称 | string |  |
|   passportNum | 护照编号 | string |  |
|   passportType | 护照类型 | string |  |
|   perResidence | 常驻地址 | string |  |
|   personLabelsName | 个人标签名称 | string |  |
|   phoneNumber | 电话号码 | string |  |
|   plasticFlag | 皮肤/整形治疗史 | integer |  |
|   plasticFlagDesc | 有无皮肤/整形治疗史 | string |  |
|   plasticRemark   | 院外治疗备注 | string |  |
|   poolName | 客户池 | string |  |
|   preDate | 报备时间 | string |  |
|   preDeptName | 报备部门 | string |  |
|   preProNames | 报备项目 | string |  |
|   preUserName | 报备人 | string |  |
|   propensity | 意向项目 | string |  |
|   propensityFriend | 朋友意向 | string |  |
|   relatedConsul | 相关咨询师 | string |  |
|   relatedDoctor | 相关医生 | string |  |
|   relatedServer | 相关客服 | string |  |
|   remark | 客户档案备注 | string |  |
|   rfm | rfm值 | string |  |
|   rfmTypeName | rfm类型(单独计算) | string |  |
|   roleManagerInfoList | 岗位负责人 | array | RoleManagerInfo |
| **    **customerId | 客户id | string |  |
|     id     | 数据Id | string |  |
|     roleId | 岗位id | string |  |
|     roleManagerId | 配置负责岗位id | string |  |
|     roleName | 岗位名称 | string |  |
|     userId | 负责用户id | string |  |
|     userName | 负责用户姓名 | string |  |
|     userPhoneNumber | 负责用户手机号 | string |  |
|   rscore | 最近一次消费距今天数，得分 | string |  |
|   seedFlag | 是否是种子客户 | boolean |  |
|   sex | 性别 | string |  |
|   sexDesc | 性别描述 | string |  |
|   sickHistory | 既往史 | string |  |
|   sickHistoryRemark | 既往史备注 | string |  |
|   smartLabelCommonName | 公共标签 | string |  |
|   smartLabelPersonName | 个人标签 | string |  |
|   sourcePathName | 来源路径 | string |  |
|   sourcePathNameSecondAll | 客户第二来源路径 | string |  |
|   sourcePathNameThirdAll | 客户第三来源路径 | string |  |
|   sourceType | 来源 | string |  |
|   sourceTypeDetailAll | 具体来源 | string |  |
|   sourceTypeDetailType | obj表示具体来源，type表示分类 | string |  |
|   sourceTypeRemark | 来源备注 | string |  |
|   sourceTypeSecond   | 客户第二来源类型 | string |  |
|   sourceTypeThird | 客户第三来源类型 | string |  |
|   sureType | 确认纠正,可用值:NOT_CONFIRMED,TO_BE_CONFIRMED,CONFIRMED | string |  |
|   sureTypeDesc | 确认纠正描述 | string |  |
|   sysUserId   | 咨询师id | string |  |
|   sysUserName | 咨询师姓名 | string |  |
|   sysUserPhone | 咨询师电话 | string |  |
|   tenantId | 客户门店id | string |  |
|   tenantName | 建档门店 | string |  |
|   treatTime | 治疗次数 | string |  |
|   type | 客户类型 | string |  |
|   typeDesc   | 客户类型描述 | string |  |
|   unionId | unionId | string |  |
|   updateBy | 修改人id | string |  |
|   updateDate | 修改时间 | string |  |
|   urgentContactCall | 紧急联系人电话 | string |  |
|   urgentContactName   | 紧急联系人 | string |  |
|   vipActiveDate | 会员有效期至 | string |  |
|   vipNum | 会员号 | string |  |
|   wechatSysUserName | 微信咨询师名称 | string |  |
|   wechatSysuserId | 微信咨询师id | string |  |
|   wechatUserId | 企业微信客户用户id | string |  |
|   weiXin | 微信 | string |  |
|   workState | 工作状况 | string |  |
|   workStateRemark | 工作状况其他描述 | string |  |
|   wxBindDate | 微信绑定时间（小程序绑定时间） | string |  |
|   wxBindFlag | 微信绑定标识 | boolean |  |
|   wxBindFlagDesc | 微信绑定描述 | string |  |
|   wxName | 微信昵称 | string |  |
|   wxPhotoURL | 微信头像地址 | string |  |
|   goldNum | 金币数量 | int |  |
|   latestTreatProject | 最近治疗项目 | String |  |
|   characterTag | 性格标签 | array |  |
| **    **id | 标签id | string |  |
| **    **name | 标签名称 | string |  |
| **    **color | 标签颜色 | string |  |
| msg | 响应消息 | string |  |





## 返利（成交）列表

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/tpos/customer/my-rebate-list `POST`**

- **参数说明**

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>  current</td><td>页数</td><td>true</td><td>integer(int32)</td></tr><tr><td>  size</td><td>每页条数</td><td>true</td><td>integer(int32)</td></tr><tr><td>  receiverId</td><td>客户Id</td><td>true</td><td>string</td></tr><tr><td>  customerInfo</td><td>客户姓名或手机号（搜索框）</td><td>false</td><td>string</td></tr><tr><td>  settledFlag</td><td>成交状态：<br/>0为全部,<br/>1为已结算,<br/>2为未结算</td><td>false</td><td>integer(int32)</td></tr><tr><td>  rebatesLevel</td><td>返利级别：1（本级）,2,3</td><td>false</td><td>integer(int32)</td></tr><tr><td>  referrerIds</td><td>推荐人ID<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>false</td><td>array</td></tr><tr><td>      wayBuy</td><td>成交方式：<br/> 0-推荐购买; 1-自主购买</td><td>false</td><td>integer(int32)</td></tr><tr><td>  dealDateEnd</td><td>成交截止日期</td><td>false</td><td>string(date-time)</td></tr><tr><td>  dealDateStart</td><td>成交起始日期</td><td>false</td><td>string(date-time)</td></tr><tr><td>  dealMoneyEnd</td><td>成交截止金额</td><td>false</td><td>number</td></tr><tr><td>  dealMoneyStart</td><td>成交起始金额</td><td>false</td><td>number</td></tr><tr><td>  tenantFilter</td><td>所属门店<br/>(0-本店，1-其他门店, 2-全部)</td><td>false</td><td>integer(int32)</td></tr></tbody></table>

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOfRebateListDTO | IPageOfRebateListDTO |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | RebateListDTO |
|     customerIdCost | 消费客户id | string |  |
|     customerName | 消费客户姓名 | string |  |
|     customerPhoneNum | 消费客户手机号 | string |  |
|     dealDate | 成交时间 | string |  |
|     dealMoney | 成交金额 | number |  |
|     giftMoney | 赠送金额 | number |  |
|     goldNum | 赠送金币 | number |  |
|     integral | 赠送积分 | number |  |
|     paymentItemDataId | 关联业务id | string |  |
|     rebateGiftMoneyRatio | 返利赠送金额比例（%） | integer |  |
|     rebateGoldNumRatio | 返利赠送金币比例（%） | integer |  |
|     rebateIntegralRatio | 返利赠送积分比例（%） | integer |  |
|     rebatesLevel | 返利等级 | string |  |
|     recommendId | 推荐人id | string |  |
|     recommendName | 推荐人姓名 | string |  |
|     settledFlag | 是否结算 | boolean |  |
|     tenantName | 门店名称 | string |  |
|     wayBuy | 成交方式 | integer |  |
|     wayTrigger | 触发方式 | string |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## 返利（成交）-详情

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/tpos/customer/my-rebate-detail `GET`**

- **请求参数**:

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>paymentItemDataId</td><td>关联业务id<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>false</td><td>string</td></tr><tr><td>receiverId</td><td>当前用户id</td><td>false</td><td>string</td></tr></tbody></table>

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | 成交信息详情 | 成交信息详情 |
|   consumeInfo | 消费信息 | array |  |
|     billingItemName | 项目名称 | string |  |
|             numberOfTime | 数量 | integer |  |
|   customerIdCost | 客户Id | string |  |
|   customerName | 客户姓名 | string |  |
|   customerPhoneNum | 客户电话 | string |  |
|   dealDate | 成交时间 | string |  |
|   dealMoney | 成交金额 | string |  |
|   giftMoney | 赠送金 | string |  |
|   goldNum | 金币 | string |  |
|   integral | 积分 | string |  |
|   paymentItemDataId | 订单ID | string |  |
|   rebateGiftMoneyRatio | 补贴比例-赠送金 | string |  |
|   rebateGoldNumRatio | 补贴比例-金币 | string |  |
|   rebateIntegralRatio | 补贴比例-积分 | string |  |
|   rebatesLevel | 返利级别 | string |  |
|   recommendId | 推荐人ID | string |  |
|   recommendName | 推荐人名称 | string |  |
|   refundDate | 退款日期 | string |  |
|   refundPrice | 退款金额 | string |  |
|   settledFlag | 结算状态 | boolean |  |
|   settledTime | 结算次数 | string |  |
|   tenantName | 门店名 | string |  |
|   totalGiftMoney | 总返利赠送金 | string |  |
|   totalGold | 总返利金币 | string |  |
|   totalIntegral | 总返利积分 | string |  |
|   uncollectedPrice | 欠款 | string |  |
|   wayBuy | 0-推荐购买; 1-自主购买 | integer(int32) |  |
|   wayTrigger | 结算核定：  <br/>0->划扣；  <br/>1->缴费； | string |  |
| msg | 响应消息 | string |  |





## 返利（成交）- 详情 - 明细记录

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/tpos/customer/my-rebate-detail-list  GET**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| current | 当前页 | query | true | integer(int32) |  |
| paymentItemDataId | 关联业务id | query | true | string |  |
| receiverId | 当前用户id | query | true | string |  |
| size | 每页数量 | query | true | integer(int32) |  |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOfRebateDetailListDTO | IPageOfRebateDetailListDTO |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | RebateDetailListDTO |
|     giftMoney | 赠送金 | string |  |
|     goldNum | 金币 | string |  |
|     integral | 积分 | string |  |
|     rebateType | 返利类型  <br/>0付款;  <br/>1转项补缴费;  <br/>2转项退款;  <br/>3退款; | integer |  |
|     rebatesDate | 返利时间 | string |  |
|     settledStatus | 是否结算 | boolean |  |
|     tenantName | 门店名称 | string |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## 列表推荐人选项

- 请求URL（需要tpos鉴权）

**`接口地址`**`: `**`/api/``v1/tpos/customer/my-rebate-recommend-options GET`**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| rebatesLevel | 返利等级 | query | true | integer(int32) |  |
| receiverId | 受益人id | query | true | string |  |

**返回结果**

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | array | LabelValueEntity |
|   label | 推荐人名称 | string |  |
|   value | 推荐人id | string |  |
| msg | 响应消息 | string |  |

## 返利（客户）列表

- 请求URL（需要tpos鉴权）

**`接口地址`**`:`**` ``/api/``v1/tpos/customer/my-rebate-customer-list`**` ``      `**`POST`**



**请求参数**:

<table><colgroup><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>请求类型</td><td>是否必须</td><td>数据类型</td><td>schema</td></tr><tr><td>  current</td><td>页数</td><td></td><td>true</td><td>integer(int32)</td><td></td></tr><tr><td>  size</td><td>每页条数</td><td></td><td>true</td><td>integer(int32)</td><td></td></tr><tr><td>  cusStatus</td><td>客户成交状态：<br/>1-&gt;已成交，<br/>2-&gt;未成交，<br/>3-&gt;无效</td><td></td><td>false</td><td>integer(int32)</td><td></td></tr><tr><td>  customerInfo</td><td>客户姓名或手机号</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  rebatesCountEnd</td><td>返利次数截止</td><td></td><td>false</td><td>integer(int32)</td><td></td></tr><tr><td>  rebatesCountStart</td><td>返利次数起始</td><td></td><td>false</td><td>integer(int32)</td><td></td></tr><tr><td>  rebatesLevel</td><td>返利层级：1,2,3</td><td></td><td>false</td><td>integer(int32)</td><td></td></tr><tr><td>  referrerIds</td><td>推荐人ID<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td></td><td>false</td><td>array</td><td>string</td></tr><tr><td>  recommendDateEnd</td><td>推荐截止时间</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  recommendDateStart</td><td>推荐起始时间</td><td></td><td>false</td><td>string</td><td></td></tr></tbody></table>

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOfRebateCustomerListDTO | IPageOfRebateCustomerListDTO |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | RebateCustomerListDTO |
|     cusId | 消费客户id | string |  |
|     cusName | 消费客户姓名 | string |  |
|     cusPhone | 消费客户手机号 | string |  |
|         dealStatus | 客户成交状态  <br/>"1"->已成交，  <br/>"2"->未成交，  <br/>"3"->无效 | string |  |
|     giftMoney | 赠送金额 | number |  |
|     goldNum | 赠送金币 | number |  |
|     integral | 赠送积分 | number |  |
|     rebateCount | 返利次数 | integer |  |
|     recommendDate | 返利时间 | string |  |
|     recommendId | 推荐人id | string |  |
|     recommendName | 推荐人姓名 | string |  |
|     tenantName | 门店名称 | string |  |
|     wayBuy | 购买方式  <br/>0-推荐购买; 1-自主购买 | integer |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |



## 返利（客户）详情

- 请求URL（需要tpos鉴权）

**接口地址**:  **/api/v1/tpos/customer/my-rebate-customer-detail  GET**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| cusId | 消费客户id | query | true | string |  |
| receiverId | 当前用户id | query | true | string |  |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | 客户信息 | 客户信息 |
|   cusId | 客户id | string |  |
|   cusName | 客户姓名 | string |  |
|   cusPhone | 客户手机号 | string |  |
|   dealStatus | 客户成交状态  <br/>"1"->已成交，  <br/>"2"->未成交，  <br/>"3"->无效 | string |  |
|   giftMoney | 赠送金 | string |  |
|   goldNum | 金币 | string |  |
|   integral | 积分 | string |  |
|   rebateCount | 补贴次数 | string |  |
|   rebateTenantName | 返利门店 | string |  |
|   rebatesLevel | 返利级别 | string |  |
|   recommendDate | 推荐时间 | string |  |
|   recommendId | 推荐人ID | string |  |
|   recommendName | 推荐人名称 | string |  |
|   tenantName | 门店名称 | string |  |
|   wayBuy | 推荐方式：  <br/>0-推荐购买; 1-自主购买 | integer(int32) |  |
| msg | 响应消息 | string |  |

## 返利（客户）详情-成交记录

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/tpos/customer/my-rebate-customer-detail-list  GET**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| current | 页数 | query | true | integer(int32) |  |
| size | 每页条数 | query | true | integer(int32) |  |
| cusId | 消费人id | query | true | string |  |
| receiverId | 受益人id | query | true | string |  |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | IPageOf成交信息 |
|   current |  | integer(int64) |
|   pages |  | integer(int64) |
|   records |  | array |
|     customerIdCost | 客户Id | string |
|     customerName | 客户姓名 | string |
|     customerPhoneNum | 客户电话 | string |
|     dealDate | 成交时间 | string |
|     dealMoney | 成交金额 | string |
|     giftMoney | 赠送金 | string |
|     goldNum | 金币 | string |
|     integral | 积分 | string |
|     paymentItemDataId | 订单ID | string |
|     rebateGiftMoneyRatio | 补贴比例-赠送金 | string |
|     rebateGoldNumRatio | 补贴比例-金币 | string |
|     rebateIntegralRatio | 补贴比例-积分 | string |
|     rebatesLevel | 返利级别 | string |
|     recommendId | 推荐人ID | string |
|     recommendName | 推荐人名称 | string |
|     settledFlag | 结算状态 | boolean |
|     tenantName | 门店名 | string |
|     wayBuyType | 0：推荐购买，  <br/>1：推荐新客，  <br/>2：推荐新客，推荐购买 | integer |
|     wayTrigger | 结算核定：  <br/>0->划扣；  <br/>1->缴费 | string |
|   size |  | integer(int64) |
|   total |  | integer(int64) |
| msg | 响应消息 | string |

## 返利（客户）详情-成交记录



- 请求URL（需要tpos鉴权）

**接口地址**:**/api/v1/tpos/customer/my-rebate-customer-detail-list   GET**



- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| current | 页数 | query | true | integer(int32) |  |
| size | 每页条数 | query | true | integer(int32) |  |
| cusId | 消费人id | query | true | string |  |
| receiverId | 受益人id | query | true | string |  |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | IPageOf成交信息 |
|   current |  | integer(int64) |
|   pages |  | integer(int64) |
|   records |  | array |
|     customerIdCost | 客户Id | string |
|     customerName | 客户姓名 | string |
|     customerPhoneNum | 客户电话 | string |
|     dealDate | 成交时间 | string |
|     dealMoney | 成交金额 | string |
|     giftMoney | 赠送金 | string |
|     goldNum | 金币 | string |
|     integral | 积分 | string |
|     paymentItemDataId | 订单ID | string |
|     rebateGiftMoneyRatio | 补贴比例-赠送金（%） | string |
|     rebateGoldNumRatio | 补贴比例-金币（%） | string |
|     rebateIntegralRatio | 补贴比例-积分（%） | string |
|     rebatesLevel | 返利级别 | string |
|     recommendId | 推荐人ID | string |
|     recommendName | 推荐人名称 | string |
|     settledFlag | 结算状态 | boolean |
|     tenantName | 门店名 | string |
|     wayBuy | 购买方式：  <br/>0-> 推荐购买；  <br/>1-> 自主购买； | integer |
|     wayTrigger | 结算核定：  <br/>0->划扣；1->缴费 | string |
|   size |  | integer(int64) |
|   total |  | integer(int64) |
| msg | 响应消息 | string |

## 推荐客户明细

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/tpos/customer/my-recommend-customer-list   POST**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
|   receiverId | 受益人Id（当前客户id） |  | true | string |  |
|   current | 页数 |  | true | integer(int32) |  |
|   size | 每页条数 |  | true | integer(int32) |  |
|   customerInfo | 姓名或者电话（关键字） |  | false | string |  |
|   consumeSituation | 消费状况（0-全部；1-有消费；2-无消费） |  | false | integer(int32) |  |
|   rebatesSituation | 返利状况（0-全部；1-有返利；2-无返利） |  | false | integer(int32) |  |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOfRebatesRecommendCustomerDTO | IPageOfRebatesRecommendCustomerDTO |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | RebatesRecommendCustomerDTO |
|     cusName | 推荐人手机号 | string |  |
|     cusPhoneNumber | 推荐人手机号 | string |  |
|     payInfo | 有无消费 | string |  |
|     rebatesInfo | 有无返利 | string |  |
|     relation | 关系 | string |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## 客户线索查询

- 请求URL（需要tpos鉴权）

**接口地址**:**/api/v1/tpos/customer/customer-clue-list   POST**

- **请求参数**:

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>  current</td><td>分页参数-页数</td><td>true</td><td>integer(int32)</td></tr><tr><td>  size</td><td>分页参数-每页数据量</td><td>true</td><td>integer(int32)</td></tr><tr><td>  customerPhone</td><td>客户电话号码精确查询</td><td>false<br/><b>不能和neuronCusId同时为空</b></td><td>string</td></tr><tr><td>  neuronCusId</td><td>客户id</td><td>false<br/><b>不能和customerPhone同时为空</b></td><td>string</td></tr><tr><td>  clueTagList</td><td>线索标签<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>false</td><td>array</td></tr><tr><td>  clueUpdateTimeEnd</td><td>线索更新时间</td><td>false</td><td>string(date-time)</td></tr><tr><td>  clueUpdateTimeStart</td><td>线索更新时间</td><td>false</td><td>string(date-time)</td></tr></tbody></table>

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) |  |
| data | 结果内容 | IPageOf客户线索 |  |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array |  |
|     id | 客户姓名 | string | 客户基础信息 |
|     name | 客户姓名 | string |  |
|     nickName | 昵称 | string |  |
|     sex | 性别 | string |  |
|     career | 职业 | string |  |
|     age | 年龄 | string |  |
|     birthday | 生日 | string |  |
|             customerType | 客户类型 | string |  |
|     documentId | 档案号 | string |  |
|     marriedFlagName | 婚姻状况 | string |  |
|     fertilityFlagName | 生育状况 | string |  |
|     areaProvince | 现址地址 | string |  |
|     perResidence | 常驻地址 | string |  |
|             clueCreateTime | 线索创建时间 | string | 线索信息 |
|     addUser | 新增人 | string |  |
|     content | 线索内容 | string |  |
|     clueTagList | 线索标签 | array |  |
|     cluePicUrl | 线索图片地址 | string |  |
|     relatedSuggest | 关联建议 | string |  |
|     clueUpdateTime | 线索更新时间 | string |  |
|     updateUser | 最近更新人 | string |  |
|     addTenantName | 新增门店 | string |  |
|     upNum | 点赞数 | integer |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## 客户标签查询

- 请求URL（需要tpos鉴权）

**接口地址**:**/api/v1/tpos/customer/customer-label-list  GET**



- **请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| type | 1：个性标签  <br/>2：过敏标签  <br/>4：线索标签 | true | integer(int32) |

- **响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | array |  |
| msg | 响应消息 | string |  |

- 返回结果

**响应示例**

```JSON
{
    "code": 10000,
    "data": [
        "11111",
        "2222",
        "车辆信息",
        "川川而起",
        "不过尔尔",
        "咨询记录同步",
        "天气真好啊"
    ],
    "msg": "操作成功"
}
```





## 客户金币查询接口

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/tpos/customer/customer-gold-list   POST**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
|   customerId | 客户id |  | true | string |
|   page | 当前页 |  | true | integer(int32) |
|   size | 一页记录数 |  | true | integer(int32) |
|   bussinessId | 关联的业务id |  | false | string |
|   bussinessType | 关联业务类型,可用值:PAYMENT,WITHDRAW,SYSTEM_ADJUSTMENT_GOLD_COINS,TRIPARTITE_SYSTEM_ADJUSTMENT |  | false | string |
|   changeReason | 变更原因，仅用于手动调整积分选择备注 |  | false | string |
|   endTime | 创建时间的查询结束时间 |  | false | string(date-time) |
|   goldCoinsNum | 金币 |  | true | integer(int32) |
|   goldMark | 金币标识,可用值:CONSUMER_REBATE,CONSUMER_WITHDRAW,MANUAL_ADJUSTMENT,CHANGE_SCORE |  | false | string |
|   minusFlag | true：减少金币，false增加金币 |  | false | boolean |
|   rebateCustomerId | 返利客户手机号 |  | false | string |
|   rebateOrderNo | 返利订单号 |  | false | string |
|   remark | 备注 |  | false | string |
|   startTime | 创建时间的查询开始时间 |  | false | string(date-time) |
|   tenantIdList | 操作门店id集合 |  | false | array |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | IPageOfCustomerGoldRecordRes |
|   current |  | integer(int64) |
|   pages |  | integer(int64) |
|   records |  | array |
|     bussinessId | 关联的业务id | string |
|     bussinessType | 关联业务类型,  <br/>可用值:PAYMENT（缴费）,  <br/>WITHDRAW（提现）,  <br/>SYSTEM_ADJUSTMENT_GOLD_COINS（系统调整金币）,  <br/>TRIPARTITE_SYSTEM_ADJUSTMENT（三方系统调整） | string |
|     changeReason | 变更原因，仅用于手动调整积分选择备注 | string |
|     creator | 创建人/操作人 | string |
|     customerId | 客户id | string |
|     goldCoinsNum | 金币 | integer |
|     goldMark | 金币标识,可用值:  <br/>CONSUMER_REBATE(消费返利),  <br/>CONSUMER_WITHDRAW(消费提现),  <br/>MANUAL_ADJUSTMENT(手动调整),  <br/>CHANGE_SCORE(金币兑换积分) | string |
|     goldMarkMessage | 金币标识信息 | string |
|     id | 数据Id | string |
|     minusFlag | true：减少金币，false增加金币 | boolean |
|     rebateCustomerId | 返利客户id | string |
|     rebateCustomerName | 返利客户 | string |
|     rebateCustomerPhone | 返利客户手机号 | string |
|     rebateOrderId | 返利订单id | string |
|     rebateOrderNo | 返利订单号 | string |
|     remark | 备注 | string |
|     tenantName | 操作门店 | string |
|             createDate | 操作时间 | date |
|   size |  | integer(int64) |
|   total |  | integer(int64) |
| msg | 响应消息 | string |

## 查询客户开发计划

- **请求URL（需要tpos鉴权）**

**接口地址**:**/api/v1/tpos/customer/get-all-plan   GET**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| customerId | customerId | query | true | string |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | 开发计划DTO |
|   actDevPlanDevMoney | 开发金额 | number |
|   actDevPlans | 预计开发计划 | array |
|     id | 数据Id | string |
|     dataId | 意向项目或类型Id | string |
|     projectName | 意向项目名称 | string |
|     projectIdType | 项目Id类型  <br/>  *0项目类型*  <br/>  *1项目*  <br/>  *2套餐类型*  <br/>  *3套餐*  <br/>  *4年卡类型*  <br/>  *5年卡*  <br/>  *6次卡类型*  <br/>  *7次卡* | integer |
|     addByName | 添加人姓名 | string |
|     beforeInvalid | 失效前提醒 | array |
|       value | 天数 | integer |
|     beforeStart | 开始前提醒 | array |
|       value | 天数 | integer |
|     color | 颜色 | string |
|     customerId | 客户Id | string |
|     devBy | 开发人Id | string |
|     devByName | 开发人姓名 | string |
|     devLevel | 开发等级 | integer |
|     devLevelName | 开发等级名称 | string |
|     devMoney | 开发金额 | number |
|     expectDevBy | 预计开发人 | string |
|     expectDevByName | 预计开发人姓名 | string |
|     expectDevDate | 预计开发时间 | string |
|     expectDevMoney | 预计开发金额 | number |
|     expectDevNum | 预计开发数量 | integer |
|     invalidDate | 失效日期 | string |
|     organizationColor | 机构建议等级颜色 | string |
|     organizationDevLevel | 机构建议等级 | integer |
|     organizationDevLevelName | 机构建议等级名称 | string |
|     clueIds | 客户线索ids | array |
|     remark | 备注 | string |
|   devInvalidDevPlanDevMoney | 失效的预计开发计划金额 | number |
|   devInvalidDevPlans | 失效的开发计划 | array |
|     id | 数据Id | string |
|     dataId | 意向项目或类型Id | string |
|     projectName | 意向项目名称 | string |
|     projectIdType | 项目Id类型  <br/>  *0项目类型*  <br/>  *1项目*  <br/>  *2套餐类型*  <br/>  *3套餐*  <br/>  *4年卡类型*  <br/>  *5年卡*  <br/>  *6次卡类型*  <br/>  *7次卡* | integer |
|     actualInvalidDate | 实际失效日期 | string |
|     addByName | 添加人姓名 | string |
|     beforeInvalid | 失效前提醒 | array |
|       value | 天数 | integer |
|     beforeStart | 开始前提醒 | array |
|       value | 天数 | integer |
|     causeOfFailure | 失效原因可用值:  <br/>PAYMENT_LAPSE（*缴费后失效*）,  <br/>SCRATCH_FAILURE（*划扣后失效*） | string |
|     clueIds | 客户线索ids | array |
|     color | 颜色 | string |
|     customerId | 客户Id | string |
|     devBy | 开发人Id | string |
|     devByName | 开发人姓名 | string |
|     devLevel | 开发等级 | integer |
|     devLevelName | 开发等级名称 | string |
|     devMoney | 开发金额 | number |
|     expectDevBy | 预计开发人 | string |
|     expectDevByName | 预计开发人姓名 | string |
|     expectDevDate | 预计开发时间 | string |
|     expectDevMoney | 预计开发金额 | number |
|     expectDevNum | 预计开发数量 | integer |
|     invalidDate | 失效日期 | string |
|     organizationColor | 机构建议等级颜色 | string |
|     organizationDevLevel | 机构建议等级 | integer |
|     organizationDevLevelName | 机构建议等级名称 | string |
|     partLabelList | 关联部位标签列表 | array |
|       color | 部位标签颜色 | string |
|       developmentPlanId | 开发计划id | string |
|       id | 数据Id | string |
|       partLabelId | 部位标签id | string |
|       partLabelName | 部位标签名称 | string |
|     remark | 备注 | string |
|     remindBeforeInvalidVisitUserId | 失效前提醒计划回访人（多个id用','隔开） | string |
|     remindBeforeInvalidVisitUserName | 失效前提醒计划回访姓名 | string |
|     remindBeforeStartVisitUserId | 开始前提醒计划回访人（多个id用','隔开） | string |
|     remindBeforeStartVisitUserName | 开始前提醒计划回访人姓名 | string |
|     tagStatus | 标签状态（0-激活、1-开发失效、2-过期失效） | integer |
|   expiredInvalidDevPlanDevMoney | 过期的预计开发计划金额 | number |
|   expiredInvalidDevPlans | 过期的预计开发计划 | array |
|     id | 数据Id | string |
|     dataId | 意向项目或类型Id | string |
|     projectName | 意向项目名称 | string |
|     projectIdType | 项目Id类型  <br/>  *0项目类型*  <br/>  *1项目*  <br/>  *2套餐类型*  <br/>  *3套餐*  <br/>  *4年卡类型*  <br/>  *5年卡*  <br/>  *6次卡类型*  <br/>  *7次卡* | integer |
|     actualInvalidDate | 实际失效日期 | string |
|     addByName | 添加人姓名 | string |
|     beforeInvalid | 失效前提醒 | array |
|       value | 天数 | integer |
|     beforeInvalidBackVisitPlanList | 失效前回访计划 | array |
|       additionalProperty1 |  | MapOfstringAndobject |
|     beforeInvalidDateStr | 失效前提醒(列表渲染用) | string |
|     beforeStart | 开始前提醒 | array |
|       value | 天数 | integer |
|     beforeStartBackVisitPlanList | 开始前回访计划 | array |
|       additionalProperty1 |  | MapOfstringAndobject |
|     beforeStartDateStr | 开始前提醒(列表渲染用) | string |
|     causeOfFailure | 失效原因可用值:  <br/>PAYMENT_LAPSE（*缴费后失效*）,  <br/>SCRATCH_FAILURE（*划扣后失效*） | string |
|     clueIds | 客户线索ids | array |
|     color | 颜色 | string |
|     customerId | 客户Id | string |
|     customerRemark | 客户主诉 | string |
|     devBy | 开发人Id | string |
|     devByName | 开发人姓名 | string |
|     devLevel | 开发等级 | integer |
|     devLevelName | 开发等级名称 | string |
|     devMoney | 开发金额 | number |
|     expectDevBy | 预计开发人 | string |
|     expectDevByName | 预计开发人姓名 | string |
|     expectDevDate | 预计开发时间 | string |
|     expectDevMoney | 预计开发金额 | number |
|     expectDevNum | 预计开发数量 | integer |
|     invalidDate | 失效日期 | string |
|     organizationColor | 机构建议等级颜色 | string |
|     organizationDevLevel | 机构建议等级 | integer |
|     organizationDevLevelName | 机构建议等级名称 | string |
|     partLabelList | 关联部位标签列表 | array |
|       color | 部位标签颜色 | string |
|       developmentPlanId | 开发计划id | string |
|       id | 数据Id | string |
|       partLabelId | 部位标签id | string |
|       partLabelName | 部位标签名称 | string |
|     remark | 备注（不能超过500个字） | string |
|     tagStatus | 标签状态（0-激活、1-开发失效、2-过期失效） | integer |
| msg | 响应消息 | string |

## 客户池转移

- 请求URL（需要tpos鉴权）

**接口地址**:**/api/v1/tpos/customer/transfer-pool   POST**



- **请求参数**:

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td><td>schema</td></tr><tr><td>  customerId</td><td>客户id</td><td>true</td><td>string</td><td></td></tr><tr><td>  poolId</td><td>转移到的客户池</td><td>true</td><td>string</td><td></td></tr><tr><td>  sysUserId</td><td>转移到的咨询师</td><td>false</td><td>string</td><td></td></tr><tr><td>  syncVisitPlan</td><td>是否同步更新客户的回访计划(将原来咨询师的回访计划转移给新的咨询师)<br/>不是实时触发，每天凌晨3点定时执行</td><td>true</td><td>boolean</td><td></td></tr><tr><td>  transferWxFlag</td><td>是否转移企业微信客户（只能是企微客户才能操作）<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite><br/>请用这个接口判断</td><td>false</td><td>boolean</td><td></td></tr><tr><td>  needApprovalFlag</td><td>是否需要审批，默认不需要</td><td>false</td><td>boolean</td><td></td></tr><tr><td>  reason</td><td>转移原因</td><td>false</td><td>string</td><td></td></tr><tr><td>  transTenantId</td><td>转移门店id,默认是客户建档门店</td><td>false</td><td>string</td><td></td></tr></tbody></table>

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | boolean |  |
| msg | 响应消息 | string |  |

**响应示例**:

```JSON
{
    "code": 10000,
    "data": true,
    "msg": ""
}
```





## 获取客户可以转移到的客户池信息

- **请求URL（需要tpos鉴权）**

**接口地址**:`/api/v1/tpos/customer/get-pool-info`  `GET`



- **请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|
| customerId | 客户id | true | string |  |
| tenant | 门店ID（默认是建档门店） | false | string |  |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | 客户池信息 |
|       commonPool | 公共池 | array |
|         poolId | 客户池id | string |
|         poolName | 客户池名称 | string |
|       personalPool | 个人池 | array |
|         poolId | 客户池id | string |
|         poolName | 客户池名称 | string |
|         userId | 咨询师id | string |
|         userName | 咨询师名称(现有人数/最大人数) | string |
| msg | 响应消息 | string |





## 客户是否同步企微关系

**接口地址**:**/api/v1/tpos/customer/customer-qw-info   GET**

- **请求URL（需要tpos鉴权）**

**请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| customerId | customerId | query | true | string |  |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | object |  |
|       changeAllow | 是否绑定 | boolean |  |
|       reason | 原因 | string |  |
| msg | 响应消息 | string |  |

## 获取客户合并后最新的客户信息

- **请求URL（需要tpos鉴权）**

**接口地址**:`/api/v1/tpos/customer/get-merge-customer-detail` `GET`



- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| customerId | customerId | query | true | string |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | 客户信息 | 客户信息 |
|   id | 客户最新id | string |  |
|   mainPhone | 客户主号 | string |  |
|   name | 客户姓名 | string |  |
| msg | 响应消息 | string |  |

## 查询客户扫码签到记录

- 请求URL（需要tpos鉴权）

**接口地址: /api/v1/tpos/customer/customer-sign-search   POST**

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| current | 分页参数-页数 | true | Integer |
| size | 分页参数-每页数据量 | true | Integer |
| startTime | 开始时间 年月日 格式:yyyy-MM-dd | false | String |
| endTime | 结束时间 年月日 格式:yyyy-MM-dd | false | String |

- 返回结果

**响应参数**:

```JSON
{
    "code": 10000,
    "data": {
        "countId": "",
        "current": 1,// 当前查询页码
        "maxLimit": null,
        "optimizeCountSql": true,
        "orders": [],
        "pages": 1,// 总页数
        "records": [
            {
                "customerId": "aa7f60e60441477ca24fe83a5102b109",// 客户id
                "customerName": "测试",// 客户姓名
                "id": "376051523911680005",// 记录主键id
                "signInfos": [
                    {
                        "choiceInfos": [
                            {
                                "choiceDesc": "", // 选项描述 非必填
                                "choiceRemark": "", // 选项备注 非必填
                                "choiceValue": "玻尿酸"// 选择的选项
                            },
                            {
                                "choiceDesc": "",// 选项描述 非必填
                                "choiceRemark": "",// 选项备注 非必填
                                "choiceValue": "光子嫩肤"// 选择的选项
                            },
                            {
                                "choiceDesc": "啊哈项目",// 选项描述 非必填
                                "choiceRemark": "",// 选项备注 非必填
                                "choiceValue": "其他"// 选择的选项
                            }
                        ],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "如果有以下的项目你会选择哪一个？",// 题目名称
                        "textType": 1,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },// 单选或者多选的时候 选项内容  单选的时候只会有一个
                    {
                        "choiceInfos": [],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "你喜欢什么颜色",// 题目名称
                        "textType": 2,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "我喜欢什么颜色" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "咨询项目",// 题目名称
                        "textType": 2,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "光电" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "客户来源",// 题目名称
                        "textType": 2,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "自然到院" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [
                            {
                                "choiceDesc": "",// 选项描述 非必填
                                "choiceRemark": "",// 选项备注 非必填
                                "choiceValue": "没有"// 选择的选项
                            },
                            {
                                "choiceDesc": "",// 选项描述 非必填
                                "choiceRemark": "你猜我有媒体",// 选项备注 非必填
                                "choiceValue": "有"// 选择的选项
                            }
                        ],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "你最近有皮肤看问题困扰吗？企标",// 题目名称
                        "textType": 1,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "到院目的",// 题目名称
                        "textType": 2,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "瘦脸,性能" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [
                            {
                                "choiceDesc": "",// 选项描述 非必填
                                "choiceRemark": "应该有用",// 选项备注 非必填
                                "choiceValue": "1"// 选择的选项
                            }
                        ],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "应该不用",// 题目名称
                        "textType": 1,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "备注",// 题目名称
                        "textType": 2,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "备注一下" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "是否有病史",// 题目名称
                        "textType": 2,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "否" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "预约医生",// 题目名称
                        "textType": 2,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "张医生" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "就诊类型",// 题目名称
                        "textType": 2,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "咨询" // 如果是文本类型的题目 该字段有值 文本输入内容
                    },
                    {
                        "choiceInfos": [
                            {
                                "choiceDesc": "就是选有",// 选项描述 非必填
                                "choiceRemark": "",// 选项备注 非必填
                                "choiceValue": "1"// 选择的选项
                            }
                        ],// 单选或者多选的时候 选项内容  单选的时候只会有一个
                        "fieldName": "单选",// 题目名称
                        "textType": 0,// 题目类型:0-单选;1-多选;2-文本
                        "textValue": "" // 如果是文本类型的题目 该字段有值 文本输入内容
                    }
                ],// 签到内容
                "signTime": "2025-06-17 16:54:30"// 签到时间
            }
        ],
        "searchCount": true,
        "size": 20,// 每页数据量-参数传入的分页数量
        "total": 1// 符合条件的总数
    },
    "msg": "操作成功"
}
```

## 查询客户老带新关系

- 请求URL（需要tpos鉴权）

**接口地址:  /v1/tpos/customer/get-customer-relation   GET请求**

**请求参数**:

<sheet sheet-id="8qCGFk" token="shtcnTKOlDjgLChPQvGBfiOv2Eg"></sheet>

- 返回结果

**响应参数**:

<sheet sheet-id="d6cgIb" token="shtcnTKOlDjgLChPQvGBfiOv2Eg"></sheet>

- 示例

```Plain Text
请求
curl --location --request GET 'http://192.168.2.174:8080/api/v1/tpos/customer/get-customer-relation?customerId&phoneNumber=18268927033&tenantId=1' 
返回值：
{
    "code": 10000,
    "data": {
        "childrenCustomers": [
            {
                "childrenCustomers": [],
                "customerId": "351762824877309955",
                "customerName": "测试报备22343",
                "customerPhone": "18268927033",
                "parentCustomer": null
            }
        ],
        "customerId": "000e10ea91144557b7f75c977f4ae54f",
        "customerName": "喵喵",
        "customerPhone": "18268927033",
        "parentCustomer": {
            "childrenCustomers": [],
            "customerId": "58e59df3ba5b4fe2b9eb78a5952adbf6",
            "customerName": "YYY",
            "customerPhone": "18268927033",
            "parentCustomer": null
        }
    },
    "msg": "操作成功"
}
```





## 获取门店岗位负责人配置

- 请求URL（需要tpos鉴权）

**接口地址**:`/api/v1/tpos/customer/get-customer-rolemanager-config`

**请求方式**:`GET`

**请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| tenantId | tenantId | query | true | string |  |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | array | RoleManagerConfig |
|   id | 数据Id | string |  |
|   roleId | 岗位id | string |  |
|   roleName | 岗位名称 | string |  |
|   statisticFlag | 是否参与统计 | boolean |  |
| msg | 响应消息 | string |  |



**响应示例**:

```JSON
{
    "code": 10000,
    "data": [
        {
            "id": "6d0d33077fb540ec9658960b0c389b31",
            "roleId": "0aa0e2c7e9e987b192f223901dfa82cc",
            "roleName": "护士长",
            "statisticFlag": true
        }
    ],
    "msg": "操作成功"
}
```



## 编辑客户岗位负责人

- 请求URL（需要tpos鉴权）

**接口地址**:`/api/v1/tpos/customer/edit-customer-rolemanager`

**请求方式**:`POST`

**请求示例**:

```JSON
{
    "customerId": "xxx",
    "roleManagerId": "xxxx",
    "userIdList": [
        "xxx",
        "xxxx"
    ]
}
```



**请求参数**:

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>  customerId</td><td>客户id</td><td>true</td><td>string</td></tr><tr><td>  roleManagerId</td><td>负责岗位id<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>true</td><td>string</td></tr><tr><td>  userIdList</td><td>员工id数组（传空数组表示删除客户身上的配置）</td><td>true</td><td>array</td></tr></tbody></table>

- 返回结果

**响应示例**:

```JavaScript
{
        "code": 10000,
        "data": true,
        "msg": "操作成功"
}
```

## 通过手机号或者客户ID查询返回是否新客（无消费【院内总消费为0】，无划扣记录）

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/tpos/customer/check-new-customer**   **POST**

- **请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| id | 客户id | false(id 和 电话号码必传其一)以客户id为主 | string |
| phoneNumber | 电话号码 | false(id 和 电话号码必传其一)以客户id为主 | string |

- **返回结果**

返回参数：

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | array |
| msg | 响应消息 | string |

返回示例：

![图片展示的是通过Postman模拟请求接口“通过手机号或者客户ID查询返回是否新客（无消费【院内总消费为0】，无划扣记录）”的界面。请求方式为POST，接口地址为{{ip}}/api/v1/tpos/customer/check - new - customer，参数部分为id和phoneNumber，id为528881792871038981，phoneNumber为18222297787。响应结果为code为10000，data为false，msg为“操作成功”，且响应时间为211ms。该图片与文档中介绍的接口请求示例部分对应，直观呈现了请求与响应情况。](https://feishu.cn/file/GpAMbsVYFo4nB8xiIMAcQSDpn7g)



# 门店（common）

## [**获取门店信息列表**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#doxcnjdDnGdIlvKLCZlEUSPEnRg)

**请求URL（需要tpos鉴权）** 

**GET:**`/api/``v1/tpos/common/tenantList`

- **返回结果**

```JSON
{
        "code":"int",
        "msg":"string",
        "data":[{
               "id":"1",     //    门店id
               "name":"门店1"    //    门店名称
        }]
}
```

# 回访（visit）

## 获取门店所有回访类型

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/tpos/visit/get-visit-type**   **GET**

- **请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| tenantId | 门店id | true | string |

- **返回结果**

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | array |
|   name | 回访类型名称 | string |
|   value | 回访类型值 | string |
| msg | 响应消息 | string |

**响应示例**:

```JSON
{
    "code": 0,
    "data": [
        {
            "name": "治疗后回访",
            "value": "1"
        }
    ],
    "msg": ""
}
```

## 获取回访方式类型

- **请求URL（需要tpos鉴权）**

**接口地址**: **/api/v1/tpos/visit/get-visit-way-type**   **GET**

- **响应详情**:

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | array |
|   name | 回访方式名称 | string |
|   value | 回访类型值 | string |
| msg | 响应消息 | string |

**响应示例**:

```JSON
{
    "code": 0,
    "data": [
        {
            "name": "企业微信",
            "value": "45"
        }
    ],
    "msg": ""
}
```

## 获取回访数据接口

- **请求URL（需要tpos鉴权）**

**接口地址**: **/api/v1/tpos/visit/get-visit-page   POST**



**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
|   page | 查询页 | true | integer(int32) |
|   size | 查询条数 | true | integer(int32) |
|   content | 计划回访内容 | false | string |
|   customerId | 客户id | false | string |
|   customerIds | 客户id集合 | false | array |
|   customerName | 客户信息 | false | string |
|   type | 回访类型 | false | array |
|   visitDateEnd | 查询-计划回访结束时间 | false | string(date-time) |
|   visitDateStart | 查询-计划回访开始时间 | false | string(date-time) |
|   visitType | 回访方式 | false | array |
|   visitedDateStart | 查询-实际回访开始时间 | false | string(date-time) |
|   visitedDateEnd | 查询-实际回访结束时间 | false | string(date-time) |
|   visitedFlag | 回访状态  <br/>回访状态  <br/>("1"：待回访，"2"：已回访，"3":作废) | false | array |

- **响应详情**:

**响应参数**:

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>类型</td></tr><tr><td>code</td><td>响应结果</td><td>integer(int32)</td></tr><tr><td>data</td><td>结果内容</td><td>IPageOf计划回访内容</td></tr><tr><td>  current</td><td></td><td>integer(int64)</td></tr><tr><td>  pages</td><td></td><td>integer(int64)</td></tr><tr><td>  records</td><td></td><td>array</td></tr><tr><td>    content</td><td>计划回访内容</td><td>string</td></tr><tr><td>    customerId</td><td>客户id</td><td>string</td></tr><tr><td>    vipNum</td><td>客户会员号</td><td>string</td></tr><tr><td>    customerName</td><td>客户姓名</td><td>string</td></tr><tr><td>    day</td><td>第几天</td><td>integer</td></tr><tr><td>    devPlanIds</td><td>回访计划关联开发计划</td><td>array</td></tr><tr><td>    expectedLevel</td><td>快速回访-预期达标情况</td><td>string</td></tr><tr><td>    planId</td><td>计划回访id</td><td>string</td></tr><tr><td>    quickFlag</td><td>是否是快速回访</td><td>boolean</td></tr><tr><td>    response</td><td>回访结果</td><td>string</td></tr><tr><td>    type</td><td>回访类型</td><td>string</td></tr><tr><td>    userId</td><td>计划回访人</td><td>array</td></tr><tr><td>    visitDate</td><td>计划回访日期</td><td>string</td></tr><tr><td>    visitType</td><td>快速回访-回访方式<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>string</td></tr><tr><td>    visitTypeName</td><td>回访方式名称</td><td>string</td></tr><tr><td>    visitedDate</td><td>快速回访-实际回访时间</td><td>string</td></tr><tr><td>    visitedFlag</td><td>回访状态默认false,true已回访，false待回访</td><td>boolean</td></tr><tr><td>    visitedById</td><td>实际回访人id</td><td>string</td></tr><tr><td>    visitedBy</td><td>实际回访人姓名</td><td>string</td></tr><tr><td>    appendUrl</td><td>附件</td><td>array</td></tr><tr><td>      size</td><td>文件大小</td><td>integer</td></tr><tr><td>      realUrl</td><td>文件绝对路径</td><td>string</td></tr><tr><td>      url</td><td>文件相对路径</td><td>string</td></tr></tbody></table>

## 创建回访计划

和完成回访计划是配套的接口

- **请求URL（需要tpos鉴权）**

**接口地址**: **/api/v1/tpos/visit/create-visit**   **POST**

**请求参数**:

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td><td>示例</td></tr><tr><td>  customerId</td><td>需要回访的客户ID</td><td>true</td><td>string</td><td></td></tr><tr><td>  defineId</td><td>项目分类/项目ID</td><td>false</td><td>string</td><td></td></tr><tr><td>      templateId</td><td>回访模板id</td><td>false</td><td>string</td><td></td></tr><tr><td>      templateName</td><td>回访模板名称</td><td>false</td><td>string</td><td></td></tr><tr><td>  planContentVos</td><td>计划回访内容</td><td>true</td><td>array</td><td></td></tr><tr><td>    type</td><td>回访类型<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>true</td><td>string</td><td>1</td></tr><tr><td>            visitDate</td><td>计划回访时间</td><td>true</td><td>date</td><td>2026-05-21</td></tr><tr><td>    day</td><td>第几天</td><td>true</td><td>integer</td><td>1</td></tr><tr><td>            userId</td><td>计划回访人id</td><td>true</td><td>array</td><td> ["userid1", "userid2"]</td></tr><tr><td>    content</td><td>回访内容</td><td>false</td><td>string</td><td></td></tr><tr><td>    devPlanIds</td><td>回访计划关联开发计划</td><td>false</td><td>array</td><td></td></tr><tr><td>    relatedSourceMaterialIdList</td><td>关联的素材id信息</td><td>false</td><td>array</td><td></td></tr><tr><td>  tenantId</td><td>门店id（默认是客户的建档门店）</td><td>false</td><td>string</td><td></td></tr></tbody></table>

- **响应详情**:



**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | boolean |  |
| msg | 响应消息 | string |  |

**响应示例**:

```JavaScript
{
        "code": 10000,
        "data": true,
        "msg": ""
}
```



## 回访模板分类数据

- **请求URL（需要tpos鉴权）**

**请求URL（需要tpos鉴权）**

**/api/v1/tpos/visit/visit-template-type    GET**

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| name | 分类名称 | false | string |

- **响应详情**:

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | array |
|   children | 下级分类 | array |
|         title | 模板名称 | string |
|         pid | 上级分类id | string |
|         value | 分类id | string |
|             children | 下级分类... | array |
|   title | 模板名称 | string |
|   pid | 上级分类id | string |
|   value | 分类id | string |
| msg | 响应消息 | string |

**响应示例**:

```JSON
{
    "code": 10000,
    "data": [
        {
            "children": [
                {
                    "children": [
                        {

                        }
                    ],
                    "pid": "",
                    "title": "",
                    "value": ""
                }
            ],
            "pid": "",
            "title": "",
            "value": ""
        }
    ],
    "msg": ""
}
```



## 获取分类下的模板数据

- **请求URL（需要tpos鉴权）**

**接口地址**:`/api/v1/tpos/visit/visit-template-data-type`

**请求方式**:`GET`

**请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| typeId | typeId | query | true | string |  |
| tenant | 门店ID | header | false | string |  |

- **响应详情**:

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | array | RelatedLabel |
|   label | 模板id | string |  |
|   value | 模板名称 | string |  |
| msg | 响应消息 | string |  |



**响应示例**:

```JSON
{
    "code": 10000,
    "data": [
        {
            "label": "",
            "value": ""
        }
    ],
    "msg": ""
}
```



## 获取模板内容

- **请求URL（需要tpos鉴权）**

**接口地址**:`/api/v1/tpos/visit/visit-template-content`

**请求方式**:`GET`

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| id | 模板id | true | string |

- **响应详情**:

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | SysTemplateVo |
|   code | 模版编号 | string |
|   contentList | 计划回访内容 | array |
|     content | 回访内容 | string |
|     day | 天数 | integer |
|     relatedSourceMaterialIdList | 素材id集合 | array |
|   id | 模板Id | string |
|   name | 模板名称 | string |
|   type | 回访类型 | string |
|   visitManIdAndNameVos | 计划回访人 | array |
|     key | 回访人id | string |
|     label | 回访人姓名 | string |
| msg | 响应消息 | string |

## 完成回访计划

和创建回访计划是配套的接口

- **请求详情：（需要tpos鉴权）**

**接口地址**:`/api/v1/tpos/visit/complete-visit`

**请求方式**:`POST`

**请求示例**:

```JSON
{
    "planId": "242113228518195204",//计划回访id
    "visitedBy":"xxxxxxxxxxxx",// 实际回访人
    "visitType": "45",//回访方式
    "response": "顶顶顶"//回访结果
}
```



**请求参数**:



<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>  planId</td><td><b>计划回访id</b></td><td>true</td><td>string</td></tr><tr><td>  <b>response</b></td><td>回访结果</td><td>true</td><td>string</td></tr><tr><td>      <b>visitType</b></td><td>回访方式<cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>true</td><td>string</td></tr><tr><td>  <b>visitedBy</b></td><td>实际回访人（员工id）</td><td>true</td><td>string</td></tr></tbody></table>

- **响应详情**:

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | boolean |
| msg | 响应消息 | string |

**响应示例**:

```JavaScript
{
        "code": 10000,
        "data": true,
        "msg": "操作成功"
}
```



## 快速回访（直接新增一条已回访的回访数据）

- **请求详情：（需要tpos鉴权）**

**接口地址**:`/api/v1/tpos/visit/quick-complete-visit`

**请求方式**:`POST`

**请求示例**:

```JSON
{
    "customerId": "ac33f779074c42479d8e116be7276cb6",  // 客户id
    "visitedBy": "915928121d976dbd6579ab98be6f5d9c", // 计划回访人/实际回访人
    "planContentVos": [
        {
            "response": "很满意", //回访结果
            "type": "1", //回访类型
            "visitType": "40" //回访方式
        }
    ]
}
```



**请求参数**:

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>  customerId</td><td>企微客户id</td><td>true</td><td>string</td></tr><tr><td>      visitedBy</td><td>计划回访人/实际回访人</td><td>true</td><td>string</td></tr><tr><td>  planContentVos</td><td>回访内容对象</td><td>true</td><td>array</td></tr><tr><td>    response</td><td>快速回访-回访结果</td><td>true</td><td>string</td></tr><tr><td>            visitType</td><td>回访方式<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>true</td><td>string</td></tr><tr><td>    type</td><td>回访类型<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>true</td><td>string</td></tr><tr><td>  tenantId</td><td>门店id（默认是客户的建档门店）</td><td>false</td><td>string</td></tr></tbody></table>

- **响应详情**:



**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | boolean |  |
| msg | 响应消息 | string |  |

**响应示例**:

```JavaScript
{
        "code": 10000,
        "data": true,
        "msg": "操作成功"
}
```

# 报备(`preparation`)

## [新增报备](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#CyNbd8sttosLUcxqcZtcEAYRndn)

- 请求URL（需要tpos鉴权）

`/api/v1/tpos/preparation/add`      `PSOT`

- 参数说明

<table><colgroup><col/><col/><col/><col/><col/></colgroup><thead><tr><th>字段</th><th>是否必填</th><th>类型</th><th>说明</th><th>备注</th></tr></thead><tbody><tr><td>tenantId</td><td>是</td><td>String</td><td>门店id</td><td></td></tr><tr><td>toTenantId</td><td>否</td><td>String</td><td>报备到的门店id<br/>（集团/区域报备）</td><td>可以是当前门店，或者当前门店的下级门店</td></tr><tr><td>customerName</td><td>否</td><td>String</td><td>客户姓名</td><td rowspan="2">如果客户id为空，则客户姓名和客户电话不能为空，在报备的同时会根据姓名和电话进行建档，对应睿美云的普通报备功能</td></tr><tr><td>phoneNumber</td><td>否</td><td>String</td><td>客户电话</td></tr><tr><td>customerId</td><td>否</td><td>String</td><td>客户id</td><td>如果客户姓名和客户电话为空，则客户id不能为空，报备就会变成目标报备，对应睿美云的目标报备功能</td></tr><tr><td>sex</td><td>否</td><td>Integer</td><td>性别</td><td>男1；女2</td></tr><tr><td>wechat</td><td>否</td><td>String</td><td>微信号</td><td></td></tr><tr><td><grid><column width-ratio="0.500000"><p>projectInfo</p></column><column width-ratio="0.500000"><p></p></column></grid></td><td>是</td><td>Array</td><td>报备项目</td><td>数组</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>projectId</p></column></grid></td><td>是</td><td>String</td><td>项目id/项目分类id</td><td>接口会根据preType对应的类型，验证对应的数据</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>preType</p></column></grid></td><td>是</td><td>String</td><td>项目类型,1:具体项目；0：项目分类</td><td></td></tr><tr><td>preUserId</td><td>否</td><td>String</td><td>报备人id</td><td>对应睿美云的员工id，和报备人姓名必须要有其中一个值，且对应的睿美云员工是在职未禁用的有效账号</td></tr><tr><td>preUserName</td><td>否</td><td>String</td><td>报备人姓名</td><td>对应睿美云的员工姓名，和报备人id必须要有其中一个值，且对应的睿美云员工是在职未禁用的有效账号</td></tr><tr><td>deptId</td><td>否</td><td>String</td><td>部门id</td><td>对应睿美云的部门id，和部门名称必须要有其中一个值，且必须是有效的部门</td></tr><tr><td>deptName</td><td>否</td><td>String</td><td>部门名称</td><td>对应睿美云的部门名称，和部门id必须要有其中一个值，且必须是有效的部门</td></tr><tr><td>preTypeId</td><td>是</td><td>String</td><td>来源类型<br/>0:运营媒体<br/>1:市场渠道<br/>2:老带新<br/>3:其他<br/>4:员工<br/>5:自然到院6:SCRM-新客户7:SCRM-老带新</td><td>报备的来源类型，传对应的数字<br/>如果是5或者6，则preChannelTypeId，<br/>preChannelId和otherRemark三个字段不用传数据</td></tr><tr><td>preChannelTypeId</td><td>否</td><td>String</td><td>运营媒体或者市场渠道的具体来源分类</td><td>如果preTypeId的值是0或者1；则必须需要传对应的来源分类id，比如preTypeId=0，则preChannelTypeId应该是运营媒体的分类id</td></tr><tr><td>preChannelId</td><td>否</td><td>String</td><td>具体来源id；<br/>比如：<br/>市场渠道id，<br/>运营媒体id，<br/>老带新的老客人id，<br/>员工id</td><td>如果preTypeId的值是0或者1；并且对应的来源有具体的来源（不止是分类），则需要传具体的来源id；<br/>如果preTypeId=2或者7，则preChannelId必须是睿美云里面已经存在的客户id（老客户id）,preChannelTypeId则会空就行；<br/>如果preTypeId=4，则preChannelId必须是睿美云里面有效的员工id</td></tr><tr><td>otherRemark</td><td>否</td><td>String</td><td>其他类型的说明</td><td>如果preTypeId=3，则可以把对应的说明放这个字段</td></tr><tr><td>remark</td><td>否</td><td>String</td><td>报备备注</td><td></td></tr></tbody></table>

- 返回结果

```JSON
{
    "msg": "操作成功",
    "code": 10000,
    "data": "358249418165583874"   // 报备成功后的报备id
}
```

![图片展示的是睿美云开放接口报备新增报备的POST请求界面。请求地址为http://localhost:8080/api/v1/tpos/preparation/add，Body选择JSON格式。请求体内容为JSON格式，包含projectInfo、phoneNumber、preUsageId、tenantId、deptId、preTypeId和customerName等字段，如preType为1，projectId为“0884f4115d3648b5b9b1b6affc0d308e”等。下方返回结果为操作成功，code为10000，data为“358249418165683874”。该图片与文档中新增报备的接口请求及返回结果内容对应。](https://feishu.cn/file/WdYwb6G3ToralHxT43Bc4ptWn2g)

## [查询报备](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#U42pdP9n5oP5BixPbvOcUVuvnef)

- 请求URL（需要tpos鉴权）

`/api/v1/tpos/preparation/get-preparation`     `POST`

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |
| customerName | 否 | string | 客户姓名/电话 |  |
| vipNum | 否 | string | 会员编号 |  |
| preUserName | 否 | string | 报备人姓名 |  |
| preStartDate | 否 | date | 报备开始时间 |  |
| preEndDate | 否 | date | 报备结束时间 |  |

- 返回结果

```json
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": [
        {
            "id": "355755994803863554",       //报备id
            "createDate": "2025-04-22 16:47:19",         //创建时间
            "updateDate": "2025-04-22 16:47:19"  //修改时间
            "customerId": "134c8b3c41b549e3ac1af55dcd7d10b5",     //客户id
            "phone": "15895236214",               //客户电话
            "customerName": "张三",           //客户姓名
            "vipNum": "035749",            //会员号
            "weiXin": "微信",       //微信
            "customerTypeName": "初诊",             //客户类型；初诊，复诊，老客人，其他，空
            "customerType": 0,   //客户类型标识；0：初诊，1：复诊，2：老客人，3：其他，-1：空
            "projects": [  //报备项目
                {
                    "projectName": "BOTOX全面部除皱（眉间+鼻背+鱼尾纹+额纹+下颌缘）"
                }
            ],
            "preUserId": "08b8466bbf028d4ea5003ed7a6804f4b",   //报备人id
            "preUserName": "于壹叁1",   //报备人姓名
            "preDeptId": "01e47b7104654c7499a5191debdc38a7",      //报备部门id
            "deptName": "采购部",   //报备部门
            "endDate": "2024-10-24",   //报备过期时间
            "remark": "报备备注",  //客户来源是市场渠道的渠道id
            "labels": [       //业绩标签
                {
                     "name":"标签名称",   //标签名称
                     "id": "01b8da659577802a9170d072c7cd48a5",  //标签id
                     "typeId":"01b8da659577802a9170d072c7cd48a5"  //标签分类id
                }
            ],
            "firstTreatDate": "2024-04-16 06:33:37",  //首次到院时间
            "latestArriveDate": "2024-04-29 06:20:45",         //最近到院时间
            "comeDate": "2024-04-24 00:00:00",   //预计到院日期
            "latestVisitedDate": "2024-06-04 06:21:58",            //最近回访时间
            "stateName": "待审核",      //报备状态，待审核，已通过，已拒绝，已失效
            "ifRecordName": "未建档",           //是否已建档
            "ifComeName": "否",                  //是否来院
            "costFlag": false,             //是否消费
            "latestCostDate": null,           //最近消费日期
            "payPropName": "再消费",           //消费性质
            "costAmount": 1465.00,            //消费总金额
            "dutyName": "安i十7",              //咨询师
            "preTypeName": "运营媒体",          //来源类型
            "preTypeId": "0",        //客户来源类型标识；0:运营媒体,1:市场渠道,2:老带新;3:其他,4:员工;5:自然到院;6:SCRM-新客户;7:SCRM-老带新
            "preTypeAll": "运营媒体/电商平台/三方转诊/直白",        //客户来源完整路径名称
            "preOtherRemark": null,            //渠道其他类型备注信息
            "preOldUserId": null,   //客户来源是老带新的老客人id
            "preOldUserName": null,           //客户来源是老带新的老客人名称
            "preChannelId": null,             //客户来源是市场渠道的渠道id
            "preChannelName": null,           //客户来源是市场渠道的渠道名称
            "preWebId": "01b8da659577802a9170d072c7cd48a5",          //客户来源是运营媒体具体渠道id
            "preWebName": "直白",   //客户来源是运营媒体具体渠道名称
            "preWebPid": "894056a27a26211fa8f0ae471a0e23f5",      //客户来源是运营媒体渠道对应的分类id
            "sourceTypeDetailAll": "01b8da659577802a9170d072c7cd48a5",  //每种客户来源对应的具体的id
            "toTenant":"1", // 分配归属门店id
            "toTenantName":"门店1" // 分配归属门店名称
        }
```

## [编辑客户报备人和报备部门（报备转交）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#LPMTdKqG0oFBAhxFRuncYXpYnNg)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/customer/update-customer-preparation-info     POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 否 | string | 客户id（与报备id二传一） | 修改客户最新关联的报备信息 |
| preparationId | 否 | string | 报备id（与客户id二传一） | 修改报备数据id |
| departmentId | 否 | string | 修改的报备部门id |  |
| userId | 否 | string | 修改的报备人id |  |
| updateReception | 否 | Boolean | 是否更新接待数据 | 默认是false。true表示同步会将选择客户的所有接待时关联的报备人更新为新报备人 |
| updateVisit | 否 | Boolean | 是否同步更新报备回访计划 | 默认是false。true表示更新客户所以待回访的报备后回访的计划回访人为新的报备人 |

- 请求示例

![图片展示的是Postman中更新报备信息的API请求界面。请求方法为POST，URL为/api/v1/tpos/customer/update-customer-preparation-info。Body部分以JSON格式发送数据，包含preparationId、userId、departmentId、updateReception、updateVisit等字段。响应状态码为200 OK，返回数据中code为10000，msg为“操作成功”。该图片与文档中更新报备信息的API请求示例内容对应，直观呈现了请求与响应的具体情况。](https://feishu.cn/file/TqJGboxxhomMQOxwPihczzqQnLd)

**响应示例**:

```JavaScript
{
        "code": 10000,
        "data": true,
        "msg": "操作成功"
}
```

# 员工（user）

## [员工查询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Khfhdv9VBoPHvyxKZJwcGkeKn9g)

- 请求URL（需要tpos鉴权）

**`/api/``v1/tpos/user/get-page`    `GET`**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| name | 否 | string | 员工姓名 |  |
| phone | 否 | string | 员工电话 |  |
| page | 否 | int | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数量 | 默认为：20，最大为：500 |
| tenantId | 是 | string | 要查询的门店id |  |
| roleId | 否 | string | 岗位id |  |
| deptId | 否 | string | 部门id |  |

![图片展示的是员工查询接口的Postman测试界面。左侧参数栏中，name和phone参数被勾选，name值为空，phone值为15。右侧响应体区域显示了接口返回的JSON数据，包含code、data等字段，其中data字段下有countId、current、maxLimit等信息，还包含records数组，记录了员工的相关信息，如id、account、address等。该图片与文档中员工查询接口的请求URL及参数说明内容相关，直观呈现了接口调用时的参数设置及返回结果。](https://feishu.cn/file/Lc82byUYnoaBCPx6Hv3cdwlCnNL)

- 返回结果

```JSON
{
    "code": 10001,
    "data": {
        "pages": 1,
        "records": [
            {
                "id": "03a88f8614ca0ef0f9695eb2d8190b44",    //    员工id
                "idCard": "",                    //    身份证号    
                "jobStatus": false,              //    false表示在职，true表示离职
                "entryDate": 1654444800000,      //    入职日期
                "leaveDate": null,               //    离职日期
                "name": "林一",                  //    姓名
                "namePy": "linyi",              //    姓名拼音
                "phone": "15985222222",          //    电话
                "sex": 1,                        //    性别（1：男 2：女）
                "status": false,                 //    false表示在职，true表示离职
                "catTenant": "[\"85\"]",         //    可切换的门店id
                "userNo": "100001",              //    工号
                "weChatPhone": "15985222222",    //    企微电话 ，
                "roleId":""，                    //    岗位id
                "roleName":""，                  //    岗位名称   
                "deptId":""，                    //    部门id
                "deptName":""                   //    部门名称   
            }
        ],
        "size": 20,
        "total": 1        //    数据总数
    },
    "msg": "成功获取数据，数据非空"
}
```

## [获取部门树](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#NAkndYp13oHOt3xWphMch2OPn0g)

- **请求URL**

 **/api/v1/tpos/basic/dept-tree GET**

![图片展示的是员工查询接口中获取部门树的Postman测试界面。请求方式为GET，URL为127.0.0.1:60005/api/v1/tpos/basic/dept-tree?tenantId=1。参数部分仅tenantId为必填项，值为1。返回结果以JSON格式呈现，包含code、data等字段，data字段下有id、name、medicalFlag、children等信息，如id为“928ada89a294d5faa56ecdf9827a”的部门，name为“事业发展战略”，medicalFlag为true，children字段下有id、name等信息。](https://feishu.cn/file/WCfVbG1txohf0Ux5uc7c6IPdn0c)

- 参数说明



| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |

- **返回结果**

```JSON
{
    "code": 10000,
    "data": [
        {
            "children": [],                              //    子部门
            "id": "020ada859a294dfaa66fcdf9827a2c25",    //    数据id
            "medicalFlag": true,                         //    是否医疗部门
            "name": "事业发展部"                          //    部门名称
        },
        {
            "children": [
                {
                    "children": [],
                    "id": "179fba004dd24b7cb7e70cd49cdca6d3",
                    "medicalFlag": true,
                    "name": "集团部"
                },
                {
                    "children": [],
                    "id": "1963160c39d64307b8aa0d2a3ab3bfdc",
                    "medicalFlag": true,
                    "name": "系统部"
                }
            ],
            "id": "4aa72138c9564ed09ea537cea4c12213",
            "medicalFlag": true,
            "name": "重庆分公司"
        }
    ],
    "msg": "操作成功"
}       
```

## [分页获取岗位信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Tov4dI4KjoUnpxxhn4Lcz4l4nRg)

- 请求URL（需要tpos鉴权）

/api/v1/tpos/role/getRoleListV2  GET

![图片展示的是睿美云开放接口中员工（user）分页获取岗位信息的接口测试界面。请求方式为GET，URL为http://localhost:8080/api/v1/tpos/role/getRoleListV2，参数包括tenantId、name、page、size等。返回结果中，code为180001，data为空，msg显示“或未获取数据 - 数据为空”。该图片与文档中介绍的员工分页获取岗位信息接口相关，直观呈现了接口请求与响应情况。](https://feishu.cn/file/WYSObhWD7o7NtdxKejOcFlSdnZd)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 否 | string | 岗位id |  |
| name | 否 | string | 岗位名称 |  |
| tenantId | 否 | string | 门店id |  |
| page | 否 | int | 当前页 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |

说明：三个参数是 并且的关系

返回结果

```JSON
{
    "code": 10001,
    "data": [
          {
                "createBy": "1",                //创建人id
                "createDate": 1616944575000,    //创建时间戳
                "delFlag": false,                //删除状态,true:删除，false：正常
                "groupInfoId": "",               //集团下发角色对应的id
                "id": "0830f5ddf9140d3dfbfebfdbb061f089",
                "name": "网电主管",               //角色名称
                "num": null,                      //序号
                "pid": "",                        //父角色id
                "roleType": 0,                    //0：门店角色，1：集团门店角色，2：集团角色
                "status": 1,                       //0：门店角色，1启用，2禁用
                "tenantId": "1",                    //门店id
                "tips": "",                        //岗位提示
                "updateBy": "1",                    //修改人id
                "updateDate": 1629450332000        //修改时间戳
            }
        ]
    },
    "msg": "成功获取数据，数据非空"
}
```

# 卡券（coupon）

## [客户卡券查询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#AUNFdLvQ9oKuOuxFLaEcHq6HnDX)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/coupon/customer-coupon-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| page | 否 | string | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | string | 每页数量 | 默认为：20，最大为：500 |



![图片展示的是一个API测试工具界面，用于查询客户卡券信息。请求URL为http://192.168.2.133:60005/api/v1/tpos/coupon/customer-coupon-page，需tpos鉴权。参数包括customerId、page、size、state，其中customerId为必填，page默认1，size默认20，state可选。界面显示了1条记录，包含billingId、cardType、consumeAmount、orderId、orderTag、realUseRule、realUseRuleTag、realUseRuleValue、state、userId等字段信息。该图片与文档中客户卡券查询接口的参数说明及返回结果内容相关，直观呈现了接口调用及返回数据情况。](https://feishu.cn/file/Oju2bFEd5ojbT0xx4VjcB9M4n9b)

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "pages": 1,
        "records": [            
            {
                "title": "测试优惠券",              //    卡券名称
                "startDate": 1700150400000,        //    有效期开始时间（时间戳）
                "expireTime": 1701273600000,       //    有效期结束时间（时间戳）
                "state": 1,                        //    卡券状态 -1.已核销 1.未使用   2.已使用   3.已过期    4.已作废  5.已赠送   6.已失效
                "donorFlag": false,                //    是否可转赠
                
            }
        ],
        "size": 20,
        "total": 1        //    数据总数
    },
    "msg": "成功获取数据，数据非空"
}
```

## [客户卡券查询（](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#ZgThdqpP8oZDXWxFyW1cmcp5ndf)[返回结果与客户资产的优惠券数据对齐](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#ZgThdqpP8oZDXWxFyW1cmcp5ndf)[）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#ZgThdqpP8oZDXWxFyW1cmcp5ndf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/coupon/customer-coupon-list   GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
|  state | 否 | int | 状态 | 空值：所有；  <br/>1：未使用； 2：已使用；  <br/>3：已失效； 4：已赠送；  <br/>-1：已核销； |
| page | 否 | string | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | string | 每页数量 | 默认为：20，最大为：500 |

![图片展示的是睿美云开放接口中卡券（coupon）客户卡券查询（/api/v1/tpos/coupon/customer-coupon-list GET）的API请求示例。请求URL为http://api.rumeiyun.com/api/v1/tpos/coupon/customer-coupon-list，参数包括customerId、state、page、size等。返回结果JSON格式中显示了code、count、data等字段，其中data包含多个“items”，每个“items”包含如“billingId”“cardCode”“cardCodeText”等信息，还显示了“pages”等字段。该图片与文档中介绍的卡券客户卡券查询API请求及返回结果内容相关。](https://feishu.cn/file/Aru5bB7T6ohcY4xojMIc9d13njg)

- 返回结果

```SQL
{
    "code": 10000,
    "data": {
        "pages": 1,
        "records": [            
            {
                "cardType":1,                      //    代金券类型（1代金券，2折扣卷，3体验卷）
                "title": "测试优惠券",              //    卡券名称
                "subtitle":"优惠券副标题",          //    优惠券副标题
                "cardGiveOutId":"0177362503",      //    卡券码
                "receiveTime":1721629664000,       //    领取时间
                "startDate": 1700150400000,        //    有效期开始时间（时间戳）
                "expireTime": 1701273600000,       //    有效期结束时间（时间戳）
                "state": 1,                        //    卡券状态 -1.已核销 1.未使用   2.已使用   3.已过期    4.已作废  5.已赠送   6.已失效
                "donorFlag": false,                //    是否可转赠
                "useTime":1701273600000,           //    使用时间
                "orderNo":"PT202408120011",        //    关联订单号
                "receiver":"",                     //    赠送对象
                "giftDate":1701273600000,          //    赠送时间
                "consumeAmount":100,               //    消费金额满多少(元)
                "upperLimit":50,                   //    优惠金额上限（元）
                "deductionAmount":30,              //    抵扣金额（元）
                "discount":5,                       //   折扣率（折）
                "receiveFlag":0,                   //    是否领取（0表示未领取，1表示已领取）
                "receiveFromDesc":"系统发送",       //    卡券领取来源
                "giveOutDetailRemark":"",          //    发放详情备注
            }
        ],
        "size": 20,
        "total": 1        //    数据总数
    },
    "msg": "成功获取数据，数据非空"
}
```

## [使用卡券](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#QCpSdPe3doplwcxGkbXcgyXhnld)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/coupon/use-coupon   POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| cardGiveOutId | 是 | string | 卡券id |  |
| remark | 否 | string | 备注信息 |  |
| tenantId | 是 | string | 使用门店id |  |

![图片展示的是使用卡券接口的POST请求及返回结果界面。在Body部分，输入了“cardGiveOutId”和“tenantId”两个参数，分别为“6fa8abff7f8a480e96d94f122ebdf2ef”和“6”。返回结果中，code为10000，data为true，msg为“操作成功”，表明卡券使用操作成功。该图片与文档中介绍的卡券使用接口请求相关，直观呈现了请求参数及成功返回结果。](https://feishu.cn/file/BNu0bNGPtogKAPxqcWGc2Dwmnkg)

- 返回结果

> 除此之外，全是失败请求

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

## [分页获取卡券信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#QHGMdsJcEo3hAyxDEuTcSN6snNf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/coupon/coupon-page    GET**

- 参数说明

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| tenantId | 查询门店 | query | true | string |
| cardType | 卡券类型 | query | false | integer(int32) |
| title | 卡券标题  （模糊查询） | query | false | string |
| useFlag | 状态-是否启用 | query | false | boolean |
| page | 默认为：1，最小为：1 | query | false | integer(int32) |
| size | 默认为：20，最大为：500 | query | false | integer(int32) |

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | 查询卡券信息 |  |
|   current | 当前页 | integer(int64) |  |
|   pages | 总页数 | integer(int64) |  |
|   records |  | array | 卡券信息集合 |
|     applyPartTypes | 支持分类项目/物料/套餐/次卡/年卡(0/1/2/3/4) | string |  |
|     applyProjectShow | 适用项目显示 | string |  |
|     applyProjectType | 适用项目类型【1全部适用，2指定范围适用，3指定范围不适用，4部分适用，5部分不适应】 | integer |  |
|     cardDetail | 卡券描述 | string |  |
|     cardType | 卡劵类型【1代金券，2折扣券，3体验券】 | integer |  |
|     code | 编码 | string |  |
|     consumeAmount | 消费金额满多少可用 | number |  |
|     deductionAmount | 可抵扣金额 | number |  |
|     discount | 折扣率 | number |  |
|     list | 支持项目集合 | array | 支持项目集合 |
|       id | 数据Id | string |  |
|       cardId | 卡劵ID | string |  |
|       projectId | 项目/物料/套餐/次卡/年卡ID | string |  |
|       projectName | 项目/物料/套餐/次卡/年卡名称 | string |  |
|       type | 项目/物料/套餐/次卡/年卡类型【1项目，2分类】 | integer |  |
|       useType | 适用类型(项目/物料/套餐/次卡/年卡(0/2/4/6/8)) | integer |  |
|     projectNameShow | 项目名称显示 | string |  |
|     subtitle | 副标题 | string |  |
|     title | 标题 | string |  |
|     upperLimit | 优惠金额上限 | number |  |
|     useCardRangeType | 卡券使用范围:0-全部,1-仅线上,2仅线下 | integer |  |
|     useFlag | 是否启用【true启用，false禁用】 | boolean |  |
|     useRule | 规则 | string |  |
|   size | 查询数量 | integer(int64) |  |
|   total | 总数量 | integer(int64) |  |
| msg | 响应消息 | string |  |

**响应示例**:

```JavaScript
{
        "code": 10000,
        "data": {
                "current": 0,
                "pages": 0,
                "records": [
                        {
                                "applyPartTypes": "[0, 2, 3]",
                                "applyProjectShow": "",
                                "applyProjectType": 0,
                                "cardDetail": "",
                                "cardEffectiveRes": {
                                        "cardId": "",
                                        "effective": 0,
                                        "effectiveTimeType": 0,
                                        "endDate": "",
                                        "expireRemind": 0,
                                        "startDate": "",
                                        "takeEffect": 0
                                },
                                "cardType": 0,
                                "code": "",
                                "consumeAmount": 0,
                                "deductionAmount": 0,
                                "discount": 0,
                                "list": [
                                        {
                                                "cardId": "",
                                                "id": "",
                                                "projectId": "",
                                                "projectName": "",
                                                "type": 0,
                                                "useType": 0
                                        }
                                ],
                                "projectNameShow": "",
                                "subtitle": "",
                                "title": "",
                                "upperLimit": 0,
                                "useCardRangeType": 0,
                                "useFlag": true,
                                "useRule": ""
                        }
                ],
                "size": 0,
                "total": 0
        },
        "msg": ""
}
```



## [发送卡券](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#PG5xdB0hToooP0xEzezcCOcnnBd)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/coupon/send-coupon   POST**

- 参数说明



**请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| acceptMethod | *[1.立即到账  2.设定日期发送]* |  | true | integer(int32) |  |
| cards | 发送卡券集合 |  | false | array |  |
|        amount | 发送卡券数量 |  | false | integer |  |
|        cardId | 发送卡券id |  | false | string |  |
| remark | 发送卡券备注(最大200个字符) |  | false | string |  |
| destinationJson | 发送给客户id |  | true | 对象转换成json字符串 |  |
|       peopleId | 客户id |  | true | array |  |
| sendTime | 设置发送时间 （精确到分钟）  <br/>当acceptMethod是2时不能为空 |  | false | string(date-time) |  |
| expireRemind | 到期前多少天提醒 |  | false | integer(int32) |  |
| startDate | 有效开始日期 |  | true | string(date-time) |  |
| endDate | 有效结束日期 |  | true | string(date-time) |  |
| donorFlag | 是否可以转赠 |  | true | boolean |  |
| batchName | 发放批次名称 |  | false | string |  |
| tenantId | 发送门店id |  | true | string |  |

请求实例

```JSON
{
    "acceptMethod": 2,
    "sendTime": "2024-05-22 13:40",
    "startDate": "2024-05-14 00:00:00",
    "endDate": "2024-05-26 23:59:59",
    "donorFlag": true,
    "expireRemind": 2,
    "destinationJson": "{\"peopleId\": [\"0001e3d7aa0b4cf3afd67a4918196e82\"]}",
    "remark": "请问",
    "cards": [
        {
            "cardId": "185785081007177733",
            "amount": 1
        },
        {
            "cardId": "181062894488649728",
            "amount": 1
        }
    ]
}
```

- **返回结果**

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | object |  |
| msg | 响应消息 | string |  |

**响应示例**:

```JavaScript
{
        "code": 10000,
        "data": {},
        "msg": ""
}
```

## [卡券赠送（小程序分享）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#HeqtdAUlKoqKmnxjRaVcUzCXnOg)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/coupon/gift-coupon    POST**

- 参数说明

![图片展示的是一个API接口测试工具界面，当前处于Body标签页。界面中选中“raw”选项，下方显示JSON格式的参数内容。参数包括“cardId”为“1e63c2efe13a4adfa991edca485b6132”和“tenantId”为“9”。该图片与文档中卡券接口相关，具体是卡券赠送（小程序分享）接口的参数示例，展示了接口所需传递的“cardId”和“tenantId”参数值。](https://feishu.cn/file/PpGTbFM76omqMrxQwtPcAWtGnXd)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| cardId | 是 | string | 客户卡券数据id |  |
| tenantId | 是 | string | 门店id |  |

- 返回结果

```json
{
    "code": 10000,
    "data": true,    
    "msg": "操作成功"
}
```

## [领取卡券（小程序分享）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#TGE1dzxhfoXYjAx92yecfD1Pnzh)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/coupon/receive-coupon    POST**

- 参数说明

![图片展示的是睿美云开放接口中领取卡券（小程序分享）接口的请求参数设置界面。在Body选项卡下，参数类型选择raw，参数内容为JSON格式，包含“cardId”“customerId”“tenantId”三个字段，其值分别为“1e63c2efe13a4adfa991edca485b6132”“c101ae946dfc423386ece3b41979952a”“9”。该图片与上下文紧密相关，直观呈现了接口请求时所需填写的参数内容，帮助开发者正确设置参数进行接口调用。](https://feishu.cn/file/YQgHbCVXro9XEMxoKcMcF7gSndc)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| cardId | 是 | string | 客户卡券数据id |  |
| customerId | 是 | string | 领取人id | 客户id |
| tenantId | 是 | string | 门店id |  |

- 返回结果

```json
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

# 营销（marketing）

## [线上预约-名片管理](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Eawpdg20uoyVWYxtrzRchrFZn1b)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/marketing/appoint-card-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| currentTenantId | 是 | string | 要查询的门店id数据 |  |
| enableFlag | 否 | boolean | 是否启用 | true表示启用 |
| page | 否 | int | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数量 | 默认为：20，最大为：500 |

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "countId": "",
        "current": 1,
        "maxLimit": null,
        "optimizeCountSql": true,
        "orders": [],
        "pages": 17,
        "records": [
            {
                //    个人介绍的富文本
                "expertInfo": "<p>整形外科主任医师.换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试换行测试</p><p/><p>爱好广泛</p><ul><li>外科主任</li><li>协会常委</li></ul>",
                "goodField": "徐氏全鼻，眼部年轻化手术",    //   擅长领域 
                "id": "168688081971445788",                //    数据id
                //    照片json
                "photoUrl": "{\"path\":\"https://test.hospital.realmerit.com.cn/api/file//system/81d98b84d02abfa3a65a08f927d96637/scrm/20231123/062c51791bc74e16bf332e12bca84410.png?tenantId=1&secret=d2BmXf23vbNJgGL21kojrw==\",\"size\":2456,\"thumbnailPath\":\"https://test.hospital.realmerit.com.cn/api/file///system/81d98b84d02abfa3a65a08f927d96637/scrm/20231123/062c51791bc74e16bf332e12bca84410.png_150x150.png?tenantId=1&secret=bGm2D+vp1rDTwhcyADDrRg==\"}",
                //    岗位
                "post": "医生",
                //    头衔
                "title": "创始人 整形外科专家",
                //    名称
                "userName": "杨烯"
            }
        ],
        "searchCount": true,
        "size": 1,
        "total": 17
    },
    "msg": "操作成功"
}
```

## [内容管理-图文消息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#RT80dqDwEoJox5xiaJ4cqecEndF)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/marketing/graphic-message-list    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| currentTenantId | 是 | string | 要查询的门店id数据 |  |
| type | 否 | string | 类型 | 可选参数（直接传中文）：优惠活动，整形科普，其他 |

- 返回结果

```JSON
{
    "code": 10000,
    "data": [
        {
            //    视频地址
            "description": "<p><br/></p><div class=\"media-wrap video-wrap\"><video class=\"media-wrap video-wrap\" controls=\"\" id=\"1700719076276_4\" poster=\"http://test.system.realmerit.com.cn/static/4.71.0-beta.24/app.html\" src=\"https://test.hospital.realmerit.com.cn/api/file/system/81d98b84d02abfa3a65a08f927d96637/scrm/20231123/4513927e4d244303861d622ab1e54d35.mp4\" title=\"QQ录屏20231123135750.mp4\"/></div><p><br/></p>",
            //    数据id
            "id": "a63cc49af06143c3bd0f44c6ec1b6ce1",
            //    封面图片
            "photoUrl": "https://test.hospital.realmerit.com.cn/api/file/system/81d98b84d02abfa3a65a08f927d96637/marketingMgt/20231123/8ac59afe62f74e57919d4233d8add9b6.png"
        }
    ],
    "msg": "操作成功"
}
```



# **积分（integral）**

## [**获取客户积分**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#doxcnnyo7P0riQwdvF0xxd2uJbc)

- **请求URL**

`/api/``v1``/tpos/integral/getCusIntegral` **GET**

- **请求参数**

 **application/x-www-form-urlencoded**

| 参数名 | 类型 | 必须 | 描述 |
|-|-|-|-|
| customerId | string | 是 | 客户id |

- **返回结果**

```JSON
{
        "code":"int",
        "msg":"string",
        "data":{
                "openId":"string //openId",
                "unionId":"string //unionId",
                "customerId":"string //客户id",
                "points":"int //剩余可用积分"
        }
}
```

 

---

## [**获取客户积分/成长值**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#doxcnejpCloQyWc0wtAfJwcmgpe)[**分页信息**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#doxcnejpCloQyWc0wtAfJwcmgpe)

- **请求URL（需要tpos鉴权）**

**/api/v1/tpos/integral/score-record-page    GET**

- **请求参数** 

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| customerId | 客户id | **true** | string |
| scoreFlag | true：查询积分  <br/>false：查询成长值 | **true** | boolean |
| startTime | 记录的开始时间 | false | string(date-time) |
| endTime | 记录的结束时间 | false | string(date-time) |
| tenantIds | 要查询的门店id，多个用逗号隔开，不传视为看所有门店的数据 | false | string |
| page | 默认为：1，最小为：1 | false | integer(int32) |
| size | 默认为：20，最大为：500 | false | integer(int32) |

- **返回结果**

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOfScoreRecordRes | IPageOfScoreRecordRes |
|   current | 当前页 | integer(int64) |  |
|   pages | 总页数 | integer(int64) |  |
|   records |  | array | ScoreRecordRes |
|             id | 数据id | string |  |
|     changeReason | 变更原因 | string |  |
|     createDate | 变更时间 | string |  |
|     optionType | false 获赠积分  <br/>true 使用积分 | boolean |  |
|     points | 积分（成长值）数量 | integer |  |
|     remark | 备注 | string |  |
|     taskName | 任务名称 | string |  |
|     tenantId | 门店id | string |  |
|     tenantName | 门店名称 | string |  |
|   size | 每页数据量 | integer(int64) |  |
|   total | 总记录数 | integer(int64) |  |
| msg | 响应消息 | string |  |

 

---

## **编辑客户积分**

> 积分可能会影响实际业务【抵扣，提现等】，调用请慎重，请与睿美云工作人员沟通实际使用场景，获取接口详细信息

## 4.查询会员升级信息

- **请求URL（需要tpos鉴权）**

**/api/v1/tpos/integral/query-customer-growth-upgrade    POST**

- 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| customerId | 客户id | true | string |
| tenantId | 门店id | true | string |

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "memberKeepNeedMoney": 3000.00,  //保级还需缴费xxx元（维持当前会员等级）
        "memberNextLevelNeedMoney": 6000.00,  //距离下一等级还需缴费xxx元
        "memberValidityDate": "2025-09-19",  //当前会员等级有效期至【年月日】
        "memberValiditySubDays": 16  //会员有效期剩余xxx天
    },
    "msg": "操作成功"
}
```

# **订单（order）**

## [**获取订单信息列表**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#doxcnHhyR2MJyRFvUaG7ungjW2d)

- **请求URL（需要tpos鉴权）**

**/api/v1/tpos/order/billing-page    GET**

- **请求参数**

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| billingNo | 订单号 | false | string |
| choiceValidity | 是否选择有效的列表 | false | boolean |
| customerId | 客户id | false | string |
| customerPhone | 客户电话 | false | string |
| endCreateDate | 创建结束时间 | false | string |
| endUpdateDate | 更新结束时间 | false | string |
| **id** | **订单id** | **false** | **string** |
| page | 默认为：1，最小为：1 | false | integer(int32) |
| size | 默认为：20，最大为：500 | false | integer(int32) |
| startCreateDate | 创建开始时间 | false | string |
| startUpdateDate | 更新开始时间 | false | string |
| status | 订单状态 | false | integer(int32)  <br/>见顶部  <br/>BillingStatusEnum枚举值 |
| tenantId | 门店ID | true | string |

- **返回结果**

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | 订单通用数据结构 | 订单通用数据结构 |
|   current |  | integer(int64) | 当前页 |
|   pages |  | integer(int64) | 页码总数 |
|   records |  | array | 对外推送，订单通用数据结构 |
|     billingItemList | 开单项信息 | array | 三方推送_订单子项信息 |
|       billingItemName | 开单项名称 | string |  |
|       billingItemType | 订单项类型,可用值:PROJECT,PACKAGE,GOODS_INFO,PACKAGE_PROJECT,DRUG,COUPON | string |  |
|       billingSourceConfigName | 开单来源 | string |  |
|       childBillingItems | 子项 | array | 三方推送_订单子项信息 |
|       departmentId | 科室id | string |  |
|       departmentName | 科室名称 | string |  |
|       discount | 折扣 | number |  |
|       discountDetailPrice | 折扣金额 | number |  |
|       doctorId | 医生id | string |  |
|       doctorName | 医生名称 | string |  |
|       id | 数据id | string |  |
|       itemDataId | 订单项对应的数据id | string | 项目id或套餐id或商品id |
|       numberOfTime | 数量 | integer |  |
|       totalPrice | 总价 | number |  |
|       unitPrice | 单价 | number |  |
|                   receivedMoney | *已收中实收的金额（包括定金、储值）* | number |  |
|                   alreadyRefundMoney | *已退总金额(不包括虚拟金)* | number |  |
|                   alreadyReceivedMoney | *实际消费金额(已收中实收的金额-已退总金额)* | number |  |
|     billingNo | 订单号 | string |  |
|     billingUserId | 开单人id | string |  |
|     billingUserName | 开单人姓名 | string |  |
|     createDate | 开单时间 | string |  |
|     currentExclusiveServerId | 当前专属客服id | string |  |
|     currentExclusiveServerName | 当前专属客服姓名 | string |  |
|     currentExclusiveServerPhone | 专属客服手机 | string |  |
|     customerId | 客户id | string |  |
|     customerName | 客户姓名 | string |  |
|     dataSource | 订单来源,可用值:CLIENT,WX,APP,YZ,WM,SO_YANG,MIRAGE,YZMY,EQUITY_CARD,SCRM_GROUP_PURCHASING | string |  |
|     dataSourceDes | 订单来源描述 | string |  |
|     dealSourceId | 客户成交来源id（市场渠道id） | string |  |
|     dealSourceName | 客户成交来源名称（市场渠道名称） | string |  |
|     id | 订单id | string |  |
|     mallOrderTrackingDTO | 收货信息 | 对外推送_收货信息 | 对外推送_收货信息 |
|       id | 数据id | string |  |
|       takeTypeCode | 收货方式code(数据字典) | string |  |
|       takeTypeName | 收货方式名称(数据字典) | string |  |
|     paymentList | 费用单信息 | array | 对外推送_费用单信息 |
|       approvalStatus | 审批状态,可用值:WAIT_APPROVAL,APPROVAL,PASS,REFUSE,SEAT,ERROR,DELAY_REFUSE,AUTO_REFUSE | string |  |
|       approvalStatusMessage | 审批状态中文 | string |  |
|       billingExplain | 费用单备注 | string |  |
|       createDate | 创建时间 | string |  |
|       id | 数据id | string | 费用单id |
|       payBillingUserName | 费用单开单人姓名 | string |  |
|       payMark | 缴费类型,可用值:PAYMENT,REFUND,TRANSFER_PROJECT,DEPOSIT_PAYMENT,DEPOSIT_REFUND,BALANCE_RECHARGE,BALANCE_REFUND,TRANSFER_REFUND,EQUITY_PAYMENT,EQUITY_REFUND | string |  |
|       payMarkMessage | 缴费类型中文 | string |  |
|       paymentNo | 缴费单单号 | string |  |
|       shouldPayMoney | 本次收费金额 | number |  |
|       shouldRefundMoney | 应退金额 | number |  |
|       status | 缴费单状态,可用值:WAIT_HANDLE,HANDLE,CANCEL,PAUSE | string |  |
|       statusMessage | 缴费单状态中文 | string |  |
|     remark | 开单说明 | string |  |
|     roleManagerInfoList | 当前岗位负责人 | array | RoleManagerInfo |
|       customerId | 客户id | string |  |
|       id | 数据Id | string |  |
|       roleId | 岗位id | string |  |
|       roleManagerId | 配置负责岗位id | string |  |
|       roleName | 岗位名称 | string |  |
|       userId | 负责用户id | string |  |
|       userName | 负责用户姓名 | string |  |
|       userPhoneNumber | 负责用户手机号 | string |  |
|     status | 订单状态,可用值:WAIT_PAID,PAID,CANCEL,PART_PAID,PAUSE,REVOKE,DISABLED,REFUND | string |  |
|     statusDes | 具体的订单状态 | string |  |
|     sysAssistantList | 协助开单人 | array | 对外推送，系统协助人（协助开单人通用数据结构） |
|       assistantId | 协助人id | string |  |
|       assistantName | 协助人名称 | string |  |
|       id | 本身数据id | string |  |
|     tenantId | 开单门店id | string |  |
|     tenantName | 开单门店名称 | string |  |
|     totalPrice | 总价 | number |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

`v1/tpos/customer/customer-search`

---

## [**获取费用单详细信息**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#V2hldw2bQoxxdXx3jqBcz7p1ncd)

- **请求URL（需要tpos鉴权）**

**/api/v1/tpos/order/payment-detail    GET**

- **请求参数**

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
| paymentId | 费用单id | false | string |

![图片展示的是睿美云开放接口中订单（order）获取费用单详细信息的接口调用示例。在Postman中，请求方式为GET，URL为127.0.0.1:60005/api/v1/tpos/order/payment-detail?paymentId=7af438e5b55b4f57863ca5c0233ebed1，参数paymentId为费用单id。返回结果中，code为10000，data包含支付方式、支付金额、支付状态等信息，如支付方式为“扫码（微信）”，支付金额为2000元，支付状态为“HANDLE”。该图片直观呈现了接口调用及返回结果情况。](https://feishu.cn/file/HghabzZZ9oCXdix4Eb7cTqgmnAf)

- **返回结果**

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>类型</td><td>schema</td></tr><tr><td>code</td><td>响应结果</td><td>integer(int32)</td><td>integer(int32)</td></tr><tr><td>data</td><td>结果内容</td><td>三方对接：费用单详细信息DTO</td><td>三方对接：费用单详细信息DTO</td></tr><tr><td>  historyPayWay</td><td>历史支付信息</td><td>array</td><td>PaymentModePayWayRes</td></tr><tr><td>    billingSourceConfigId</td><td></td><td>string</td><td>开单来源id</td></tr><tr><td>    billingSourceConfigName</td><td></td><td>string</td><td>开单来源名称</td></tr><tr><td>    billingSourcePayFlag</td><td></td><td>boolean</td><td>是否是开单来源已付款</td></tr><tr><td>    id</td><td>数据Id</td><td>string</td><td></td></tr><tr><td>    onlinePayFlag</td><td>是否是在线支付</td><td>boolean</td><td></td></tr><tr><td>    ourSerialNo</td><td></td><td>string</td><td></td></tr><tr><td>    payDeviceCode</td><td>支付设备值</td><td>string</td><td></td></tr><tr><td>    payDeviceName</td><td>支付设备名称</td><td>string</td><td></td></tr><tr><td>    payMode</td><td>支付方式</td><td>string</td><td></td></tr><tr><td>    payModeName</td><td>支付方式名称</td><td>string</td><td></td></tr><tr><td>    payMoney</td><td>支付金额</td><td>number</td><td></td></tr><tr><td>    payShapeCode</td><td>支付形式值</td><td>string</td><td></td></tr><tr><td>    payShapeName</td><td>支付形式描述</td><td>string</td><td></td></tr><tr><td>    payStatus</td><td>可用值:WAIT_PAID,PAID,WAIT_REFUND,REFUND,WAIT_UNDO,UNDO,FAIL_PAID,FAIL_REFUND,FAIL_UNDO</td><td>string</td><td>支付状态</td></tr><tr><td>    payStatusMessage</td><td></td><td>string</td><td>支付状态描述</td></tr><tr><td>    payWayJson</td><td></td><td>array</td><td>MapOfstringAndobject</td></tr><tr><td>      additionalProperty1</td><td></td><td>MapOfstringAndobject</td><td>MapOfstringAndobject</td></tr><tr><td>    remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>    sourceId</td><td></td><td>string</td><td>数据来源关联业务id</td></tr><tr><td>    sourcePayWayId</td><td></td><td>string</td><td>退款数据的来源id</td></tr><tr><td>    sourceType</td><td>可用值:<br/>PAYMENT（费用单）,<br/>SPEED_PAY（极速收款）</td><td>string</td><td>数据来源类型</td></tr><tr><td>    terminalSerialNo</td><td></td><td>string</td><td>终端交易流水号(仅支付宝、微信)</td></tr><tr><td>    transactionNo</td><td>交易号（在线支付时第三方流水号，线下无）</td><td>string</td><td>交易号（在线支付时第三方流水号，线下无）</td></tr><tr><td>  payDetail</td><td>支付方式</td><td>object</td><td></td></tr><tr><td>        payWay</td><td>实收/实退</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>支付方式名称(微信/现金等)</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            depositInfo</td><td>定金抵扣（不算实收，算预收款抵扣）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            balanceInfo</td><td>储值抵扣（不算实收，payMode等于"储值"时算预收款抵扣，payMode等于"赠送储值"时算虚拟金抵扣）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            equityInfo</td><td>权益卡本金抵扣（不算实收，算预收款抵扣）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            cardInfo</td><td>优惠券抵扣（不算实收，算虚拟金抵扣）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            otherVirtualInfo</td><td>自定义虚拟金抵扣（不算实收，算虚拟金抵扣）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            scoreInfo</td><td>积分抵扣（不算实收，算虚拟金抵扣）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            equityGivenInfo</td><td>权益卡赠送金抵扣（不算实收，算虚拟金抵扣）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            intoDepositInfo</td><td>退款退入的定金（不算实退，算退入预收款）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            intoBalanceInfo</td><td>退款退入的储值（不算实退，算退入预收款）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>            intoBillingEquityCardInfo</td><td>退款退入的权益卡本金（不算实退，算退入预收款）</td><td>array</td><td></td></tr><tr><td>                        payMode</td><td>名称</td><td>string</td><td></td></tr><tr><td>                        payMoney</td><td>金额</td><td>number</td><td></td></tr><tr><td>                        remark</td><td>备注</td><td>string</td><td></td></tr><tr><td>  payment</td><td>费用单信息</td><td>对外推送_费用单信息</td><td>对外推送_费用单信息</td></tr><tr><td>    approvalStatus</td><td>审批状态,可用值:WAIT_APPROVAL,APPROVAL,PASS,REFUSE,SEAT,ERROR,DELAY_REFUSE,AUTO_REFUSE</td><td>string</td><td></td></tr><tr><td>    approvalStatusMessage</td><td>审批状态中文</td><td>string</td><td></td></tr><tr><td>    billingExplain</td><td>费用单备注</td><td>string</td><td></td></tr><tr><td>    createDate</td><td>创建时间</td><td>string</td><td></td></tr><tr><td>    id</td><td>数据id</td><td>string</td><td></td></tr><tr><td>    payBillingUserName</td><td>费用单开单人姓名</td><td>string</td><td></td></tr><tr><td>    payMark</td><td>缴费类型,可用值:PAYMENT,REFUND,TRANSFER_PROJECT,DEPOSIT_PAYMENT,DEPOSIT_REFUND,BALANCE_RECHARGE,BALANCE_REFUND,TRANSFER_REFUND,EQUITY_PAYMENT,EQUITY_REFUND</td><td>string</td><td></td></tr><tr><td>    payMarkMessage</td><td>缴费类型中文</td><td>string</td><td></td></tr><tr><td>    paymentNo</td><td>缴费单单号</td><td>string</td><td></td></tr><tr><td>    shouldPayMoney</td><td>本次收费金额</td><td>number</td><td></td></tr><tr><td>    shouldRefundMoney</td><td>应退金额</td><td>number</td><td></td></tr><tr><td>    status</td><td>缴费单状态,可用值:WAIT_HANDLE,HANDLE,CANCEL,PAUSE</td><td>string</td><td></td></tr><tr><td>    statusMessage</td><td>缴费单状态中文</td><td>string</td><td></td></tr><tr><td>  paymentItem</td><td>费用单子项信息</td><td>三方对接-费用单子项DTO</td><td>三方对接-费用单子项DTO</td></tr><tr><td>    billingSourceConfigId</td><td>开单来源id</td><td>string</td><td></td></tr><tr><td>    billingSourceConfigName</td><td>开单来源名称</td><td>string</td><td></td></tr><tr><td>    departmentId</td><td>计划治疗科室id</td><td>string</td><td></td></tr><tr><td>    departmentName</td><td>计划治疗科室名称</td><td>string</td><td></td></tr><tr><td>    discountPrice</td><td>折扣金额</td><td>number</td><td></td></tr><tr><td>    doctorId</td><td>医生id</td><td>string</td><td></td></tr><tr><td>    doctorName</td><td>医生名称</td><td>string</td><td></td></tr><tr><td>    id</td><td>数据id</td><td>string</td><td></td></tr><tr><td>    minusInfo</td><td>子项列表-欠费项</td><td>array</td><td>三方对接-费用单子项DTO</td></tr><tr><td colspan="4"><b>minusInfo</b>内部的结构即<b>paymentItem的结构</b></td></tr><tr><td>    minusTotalPrice</td><td>小计（负值）</td><td>number</td><td></td></tr><tr><td>    numberOfTime</td><td>数量</td><td>number</td><td></td></tr><tr><td>    packagePackages</td><td>子项列表</td><td>array</td><td>三方对接-费用单子项DTO</td></tr><tr><td>    packageProjectList</td><td>子项列表-项目</td><td>array</td><td>三方对接-费用单子项DTO</td></tr><tr><td>    paymentItemName</td><td>子项名称</td><td>string</td><td></td></tr><tr><td>    plusInfo</td><td>子项列表-收费项</td><td>array</td><td>三方对接-费用单子项DTO</td></tr><tr><td colspan="4" rowspan="2"><b>plusInfo</b>内部的结构即<b>paymentItem的结构</b></td></tr><tr></tr><tr><td>    status</td><td>状态code</td><td>integer</td><td></td></tr><tr><td>    statusMessage</td><td>状态-中文</td><td>string</td><td></td></tr><tr><td>    thisChargePrice</td><td>本次收费金额</td><td>number</td><td></td></tr><tr><td>    todayTreatFlag</td><td>是否今日治疗,true：是，false：否</td><td>boolean</td><td></td></tr><tr><td>    totalPrice</td><td>总价</td><td>number</td><td></td></tr><tr><td>    uncollectedPrice</td><td>未缴费金额</td><td>number</td><td></td></tr><tr><td>    unitPrice</td><td>单价</td><td>number</td><td></td></tr><tr><td>    paymentItemMarkOrigin</td><td>费用项类型-code</td><td>string</td><td></td></tr><tr><td>    paymentItemMarkOriginMessage</td><td>费用项类型-中文</td><td>string</td><td></td></tr><tr><td>    itemDataId</td><td>订单项原数据id</td><td>string</td><td>项目id或套餐id或商品id或者活动id</td></tr><tr><td>msg</td><td>响应消息</td><td>string</td><td></td></tr></tbody></table>



---

## [**开单**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#V6xOdaE3Bow1H0x19uVcQgF9ncv)

> 当前仅支持，**项目，商品，套餐，年卡，次卡**的开单，如果需要同时生成已收费的费用单，请务必保证费用单不是欠费状态
> 
> 套餐子项只需要选中的子项
> 
> 套餐子项的开单价需要根据套餐的开单价分摊，需要处理在参数里面，包括套餐嵌套的子套餐下的子项开单价

- 请求URL（需要tpos鉴权）

 **/api/v1/tpos/order/add-billing-review    POST**

- 参数说明

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><b>字段</b></td><td><b>是否必填</b></td><td><b>类型</b></td><td><b>说明</b></td><td><b>备注</b></td></tr><tr><td>tenantId</td><td>是</td><td>string</td><td>门店id</td><td></td></tr><tr><td>uId</td><td>是</td><td>string</td><td>重复提交判断</td><td>请自行生成uuid，去掉横杠,最长32位</td></tr><tr><td><b>billing</b></td><td><b>是</b></td><td></td><td></td><td></td></tr><tr><td>  +customerId</td><td>是</td><td>string</td><td>客户id</td><td></td></tr><tr><td>  +billingUserId</td><td>否</td><td>string</td><td>开单人id</td><td>不确定的就传1</td></tr><tr><td>  +dataSource</td><td>否</td><td>string</td><td>开单来源</td><td>不传就视为院内开单<br/>WX：系统小程序<br/>......（有其他需要再补充）</td></tr><tr><td><b>billingProjects</b></td><td></td><td><b>array</b></td><td><b>开单项目</b></td><td></td></tr><tr><td>  +id</td><td>是</td><td>string</td><td>开单项id</td><td>需自行指定，建议32位UUID，这个id是一个主键id，不能重复，去掉横杠,最长32位</td></tr><tr><td>  +projectId</td><td>是</td><td>string</td><td>项目id</td><td></td></tr><tr><td>  +projectName</td><td>是</td><td>string</td><td>项目名称（必填）</td><td>项目名称（开单需要记录当时的项目名称）</td></tr><tr><td>  +discount</td><td>否</td><td>int</td><td>折扣</td><td>打折的折扣仅做记录，如果不传，则不会显示数据，不打折的都建议传10</td></tr><tr><td>  +numberOfTime</td><td>是</td><td>int</td><td>购买次数</td><td></td></tr><tr><td>  +orderOriginalPrice</td><td>是</td><td>decimal</td><td>项目原价</td><td></td></tr><tr><td>  +totalPrice</td><td>是</td><td>decimal</td><td>这个开单项的总价</td><td></td></tr><tr><td><b>billingGoodsInfoList</b></td><td></td><td><b>array</b></td><td><b>开单商品</b></td><td></td></tr><tr><td>  +id</td><td>是</td><td>string</td><td>开单项id</td><td>需自行指定，建议32位UUID，去掉横杠,最长32位</td></tr><tr><td>  +materialId</td><td>是</td><td>string</td><td>商品id</td><td></td></tr><tr><td>  +materialName</td><td>是</td><td>string</td><td>商品名称（必填）</td><td>商品名称（开单需要记录当时的商品名称）</td></tr><tr><td>  +specification</td><td>是</td><td>string</td><td>商品规格</td><td></td></tr><tr><td>  +unitOriginalPrice</td><td>是</td><td>decimal</td><td>商品原价</td><td></td></tr><tr><td>  +orderOriginalPrice</td><td>是</td><td>decimal</td><td>商品开单价</td><td></td></tr><tr><td>  +numberOfTime</td><td>是</td><td>int</td><td>购买次数</td><td></td></tr><tr><td>  +unitCode</td><td>是</td><td>string</td><td>单位（值）</td><td rowspan="2">例：1/支</td></tr><tr><td>  +unitName</td><td>是</td><td>string</td><td>单位（名称）</td></tr><tr><td>  +totalPrice</td><td>是</td><td>decimal</td><td>这个开单项的总价</td><td></td></tr><tr><td>  +drugFlag</td><td>否</td><td>bool</td><td>是否是药品</td><td>true代表是药品，不传默认视为false</td></tr><tr><td>  +discount</td><td>否</td><td>decimal</td><td>折扣</td><td>打折的折扣仅做记录，如果不传，则不会显示数据，不打折的都建议传10</td></tr><tr><td>  +warehouseId</td><td>是</td><td>string</td><td>物料所在仓库id</td><td>不清楚的就传空字符串就行</td></tr><tr><td><b>otherBillingItemList</b></td><td></td><td></td><td><b>开单年卡/次卡</b></td><td></td></tr><tr><td>+id</td><td>是</td><td>string</td><td>开单项id</td><td>需自行指定，建议 32 位 UUID，去掉横杠，最长 32 位</td></tr><tr><td>+billingItemName</td><td>是</td><td>string</td><td>年卡名称/次卡名称</td><td></td></tr><tr><td>+billingItemType</td><td>是</td><td>int</td><td>类型</td><td>直接默认成1</td></tr><tr><td>+billingItemTypeCategory</td><td>是</td><td>int</td><td>类型</td><td>3：年卡，4：次卡</td></tr><tr><td>+itemDataId</td><td>是</td><td>string</td><td>年卡/次卡的基础数据id</td><td></td></tr><tr><td>+numberOfTime</td><td>是</td><td>int</td><td>数量</td><td>直接默认成1，只支持1</td></tr><tr><td>+unitPrice</td><td>是</td><td>decimal</td><td>单价</td><td></td></tr><tr><td>+totalPrice</td><td>是</td><td>decimal</td><td>开单价</td><td></td></tr><tr><td>+childBillingItemList</td><td>是</td><td>array</td><td>年卡子项/次卡子项</td><td>结构同 <code>billingProjects</code></td></tr><tr><td><b>billingPackageList</b></td><td></td><td></td><td><b>开单套餐</b></td><td></td></tr><tr><td>+billingPackage</td><td>是</td><td>object</td><td>套餐信息</td><td></td></tr><tr><td>    +id</td><td>是</td><td>string</td><td>套餐开单项 id</td><td>需自行指定，建议 32 位 UUID，去掉横杠，最长 32 位</td></tr><tr><td>    +packageId</td><td>是</td><td>string</td><td>套餐 id</td><td>原套餐的唯一标识</td></tr><tr><td>    +packageName</td><td>是</td><td>string</td><td>套餐名称</td><td>开单时的套餐名称</td></tr><tr><td>    +discount</td><td>否</td><td>decimal</td><td>套餐折扣</td><td>不打折建议传 10</td></tr><tr><td>    +orderOriginalPrice</td><td>是</td><td>decimal</td><td>套餐原价</td><td>套餐未打折前的总金额</td></tr><tr><td>    +totalPrice</td><td>是</td><td>decimal</td><td>套餐开单总价</td><td>套餐实际应收金额</td></tr><tr><td><code>+billingPackageProjects</code></td><td>否</td><td>array</td><td>套餐内项目列表</td><td>结构同 <code>billingProjects</code></td></tr><tr><td><code>+billingPackageGoods</code></td><td>否</td><td>array</td><td>套餐内商品列表</td><td>结构同 <code>billingGoodsInfoList</code></td></tr><tr><td><code>+billingPackagePackages</code></td><td>否</td><td>array</td><td>嵌套子套餐列表</td><td>结构同 <code>billingPackageList</code>，支持套餐嵌套餐</td></tr><tr><td><code>+billingPackageAnnualCards</code></td><td>否</td><td>array</td><td>套餐内年卡列表</td><td>结构同 <code>otherBillingItemList</code></td></tr><tr><td><code>+billingPackageTimeCards</code></td><td>否</td><td>array</td><td>套餐内次卡列表</td><td>结构同 <code>otherBillingItemList</code></td></tr><tr><td><b>payment</b></td><td></td><td></td><td><b>费用单信息</b></td><td></td></tr><tr><td>  +shouldPayMoney</td><td>是</td><td>decimal</td><td>本次要收取的金额</td><td></td></tr><tr><td>  +dataSource</td><td>否</td><td>string</td><td>开单来源</td><td>不传就视为院内开单<br/>WX：系统小程序<br/>......（有其他需要再补充）</td></tr><tr><td>  +billingExplain</td><td>否</td><td>string</td><td>费用单备注</td><td></td></tr><tr><td><b>paymentItemList</b></td><td></td><td><b>array</b></td><td><b>费用单详细信息</b></td><td></td></tr><tr><td>  +selectFlag</td><td>是</td><td>bool</td><td>是否是选中状态</td><td>true-选中，表示本次收费了这个开单项</td></tr><tr><td>  +dataId</td><td>是</td><td>string</td><td>订单项id</td><td>上面定义个各个【开单项id】</td></tr><tr><td>  +thisChargePrice</td><td>是</td><td>decimal</td><td>本次收费金额</td><td></td></tr><tr><td colspan="5"><b>参数（batchPayFeeReq）会自动生成已缴费的费用单（请务必保证费用单收到的钱就是各个开单项总价之和）</b><br/>注：开单和收费是两个动作，有可能收费会失败（内部错误，传参错误，金额验证不通过），此时订单数据不会回滚</td></tr><tr><td><b>batchPayFeeReq</b></td><td></td><td></td><td><b>收费方式</b></td><td></td></tr><tr><td>  +actualRecordedTime</td><td>是</td><td>time</td><td>实际入账时间</td><td>格式yyyy-MM-dd HH:mm:ss<br/>（2023-09-13 09:00:00）</td></tr><tr><td>  +thirdOrderId</td><td>否</td><td>string</td><td>三方订单id</td><td>有抵扣方式时该字段不能为空（该字段主要是为了查询之前的预抵扣信息与当前收银做关联）</td></tr><tr><td><b>  +payWay</b></td><td><b>是</b></td><td><b>array</b></td><td><b>支付方式</b></td><td></td></tr><tr><td>      +payMode</td><td>是</td><td>string</td><td>具体支付方式</td><td>根据数据字典-支付方式的属性值来传</td></tr><tr><td>      +payMoney</td><td>是</td><td>decimal</td><td>支付金额</td><td></td></tr><tr><td>      +remark</td><td>否</td><td>string</td><td>具体支付方式备注</td><td></td></tr><tr><td><b>  +scoreReq</b></td><td></td><td></td><td><b>积分抵扣信息</b></td><td></td></tr><tr><td>    +scoreMoney</td><td>是</td><td>decimal</td><td>积分抵扣金额</td><td rowspan="2">例：scoreMoney = 10.5，scoreNum =21<br/>则表示：用21个积分抵扣了10.5元</td></tr><tr><td>    +scoreNum</td><td>是</td><td>int</td><td>积分抵扣数量</td></tr><tr><td>    +onlyRecordFlag</td><td>否</td><td>bool</td><td>这次的抵扣是否只做记录</td><td>有些平台需要开单时扣减积分，有些平台在开单前就已经扣减积分了。<br/>所以需不需要扣减由三方自行决定。这个参数传true，则表示这次操作不会真实扣减积分，只会有抵扣记录</td></tr><tr><td><b>  +balanceReqList</b></td><td><b>否</b></td><td><b>array</b></td><td>储值抵扣请求参数</td><td></td></tr><tr><td vertical-align="middle">    +givenBalance</td><td vertical-align="middle"></td><td vertical-align="middle">decimal</td><td vertical-align="middle">赠送金抵扣金额</td><td rowspan="2">储值抵扣，赠送金抵扣，都会做余额校验，并且扣款成功后，会自动生成抵扣记录，示例参数：<br/>此时表示：扣51元赠送余额，同时扣49元储值余额<br/> "balanceReqList": [<br/>            {<br/>                "givenBalance": 51,<br/>                "balance": 49<br/>            }<br/>  ]</td></tr><tr><td vertical-align="middle">    +balance</td><td vertical-align="middle"></td><td vertical-align="middle">decimal</td><td vertical-align="middle">储值抵扣金额</td></tr><tr><td><b>  +limitBalanceReq</b></td><td><b>否</b></td><td><b>object</b></td><td>限定储值抵扣请求参数</td><td></td></tr><tr><td vertical-align="middle">    +givenBalance</td><td vertical-align="middle"></td><td vertical-align="middle">decimal</td><td vertical-align="middle">限定储值赠送金抵扣金额</td><td rowspan="2">储值抵扣，赠送金抵扣，都会做余额校验，并且扣款成功后，会自动生成抵扣记录，示例参数：<br/>此时表示：扣51元赠送余额，同时扣49元储值余额<br/> "limitBalanceReq":  {<br/>                "givenBalance": 51,<br/>                "balance": 49<br/>            }</td></tr><tr><td vertical-align="middle">    +balance</td><td vertical-align="middle"></td><td vertical-align="middle">decimal</td><td vertical-align="middle">限定储值抵扣金额</td></tr><tr><td><b>  +depositReqList</b></td><td><b>否</b></td><td><b>array</b></td><td>定金抵扣请求参数</td><td></td></tr><tr><td vertical-align="middle">    +depositId</td><td vertical-align="middle">是</td><td vertical-align="middle">string</td><td vertical-align="middle">定金id</td><td></td></tr><tr><td vertical-align="middle">    +name</td><td vertical-align="middle">是</td><td vertical-align="middle">string</td><td vertical-align="middle">定金项名称</td><td></td></tr><tr><td>    +deductMoney</td><td>是</td><td>decimal</td><td>抵扣金额</td><td></td></tr><tr><td><b>  +equityCardReqList</b></td><td><b>否</b></td><td><b>array</b></td><td>权益卡本金抵扣请求参数</td><td></td></tr><tr><td vertical-align="middle">    +cardId</td><td vertical-align="middle">是</td><td vertical-align="middle">string</td><td vertical-align="middle">客户权益卡数据id</td><td></td></tr><tr><td vertical-align="middle">    +name</td><td vertical-align="middle">是</td><td vertical-align="middle">string</td><td vertical-align="middle">权益卡名称</td><td></td></tr><tr><td>    +deductMoney</td><td>是</td><td>decimal</td><td>抵扣金额</td><td></td></tr><tr><td><b>  +equityCardGivenReqList</b></td><td><b>否</b></td><td><b>array</b></td><td>权益卡赠送金抵扣请求参数</td><td></td></tr><tr><td vertical-align="middle">    +cardId</td><td vertical-align="middle">是</td><td vertical-align="middle">string</td><td vertical-align="middle">权益卡订单id</td><td></td></tr><tr><td vertical-align="middle">    +name</td><td vertical-align="middle">是</td><td vertical-align="middle">string</td><td vertical-align="middle">权益卡名称</td><td></td></tr><tr><td>    +deductMoney</td><td>是</td><td>decimal</td><td>抵扣金额</td><td></td></tr><tr><td><b>  +cardReqList</b></td><td><b>否</b></td><td><b>array</b></td><td>优惠券抵扣请求参数</td><td></td></tr><tr><td vertical-align="middle">    +cardId</td><td vertical-align="middle">是</td><td vertical-align="middle">string</td><td vertical-align="middle">客户优惠券数据id</td><td></td></tr><tr><td vertical-align="middle">    +title</td><td vertical-align="middle">是</td><td vertical-align="middle">string</td><td vertical-align="middle">优惠券名称</td><td></td></tr><tr><td>    +cardType</td><td>是</td><td>int</td><td>优惠券类型（1代金券，2折扣券，3体验券）</td><td></td></tr><tr><td>    +deductMoney</td><td>是</td><td>decimal</td><td>抵扣金额</td><td></td></tr></tbody></table>

- 示例：

```JSON
{
    "tenantId": "1",
    "billing": {
        "customerId": "1339024af9404ff1a7f882c8b037b509",
        "billingUserId": "1",
        "dataSource": "WX"
    },
    "billingProjects": [
        {
            "id": "142987337838624791",
            "projectId": "b98447ebff3c42d7b9112db24ea94e55",
            "projectName": "测试项目",
            "discount": 6.6,
            "numberOfTime": 3,
            "orderOriginalPrice": "120",
            "totalPrice": 240
        }
    ],
    "billingGoodsInfoList": [
        {
            "id": "142987337838625862",
            "materialId": "2078840a889640e1ac973f025ef869f3",
            "materialName": "测试商品",
            "specification": "153",
            "unitOriginalPrice": 60,
            "orderOriginalPrice": 60,
            "numberOfTime": 2,
            "unitCode": "1",
            "unitName": "支",
            "totalPrice": 120,
            "drugFlag": false,
            "discount": 10,
            "warehouseId": ""
        }
    ],
    "otherBillingItemList": [
      {
        "billingItemName": "法国（其他来源限制一天）",
        "billingItemType": 1,
        "billingItemTypeCategory": 3,
        "departmentId": "",
        "departmentName": "",
        "discount": 10,
        "doctorId": "",
        "doctorName": "",
        "id": "90060082aae3499994c348803f4d582b",
        "itemDataId": "553baa83ec474fbb17868073411f9578",
        "numberOfTime": 1,
        "totalPrice": 720,
        "unitPrice": 720,
        "childBillingItemList": [
          {
            "id": "8f316a269bb84091ab4ef1fdc5a629ba",
            "billingItemType": 0,
            "billingItemTypeCategory": 3,
            "packageProjectId": "4ef6213cdfa86ddc68a5d5f5186ebe57",
            "itemDataId": "913da62deadf44a787c7a679c53829ba",
            "billingItemName": "分潜伏期",
            "departmentId": null,
            "doctorId": null,
            "unitPrice": 100,
            "totalPrice": 200,
            "numberOfTime": 2,
            "remark": null
          }
        ]
      }
    ],
    "billingPackageList": [
      {
        "billingPackage": {
          "id": "373b217a160a473c8c666236ae20d24c",
          "packageId": "175606772390690843",
          "packageName": "门店信息套餐嵌套餐20231212",
          "discount": 10,
          "orderOriginalPrice": 4145,
          "totalPrice": 4145
        },
        "billingPackageProjects": [
          {
            "id": "53dfea819eb243349d8851e6c70e5fa7",
            "packageProjectId": "175606772457799696",
            "projectId": "26ea34539bd942ba8b373ef96a21b5b0",
            "projectName": "门店新增项目20231207",
            "departmentId": "111894219936759808",
            "doctorName": null,
            "departmentName": "夫妇",
            "doctorId": null,
            "selectFlag": true,
            "totalPrice": 888,
            "remark": null,
            "numberOfTime": 1
          }
        ],
        "billingPackageGoods": [
          {
            "id": "d2e3fe2f8f6649cbab16ff0995882627",
            "billingItemName": "物料下发",
            "itemDataId": "247289801370239237",
            "unitPrice": 15,
            "numberOfTime": 1,
            "selectFlag": true,
            "totalPrice": 15,
            "departmentId": "",
            "departmentName": "",
            "doctorId": null,
            "doctorName": null,
            "unitCode": "1",
            "unitName": "支",
            "unitOriginalPrice": 0,
            "specification": "1",
            "packageProjectId": "382241521019125766"
          }
        ],
        "billingPackagePackages": [
          {
            "billingPackage": {
              "id": "3194210f888e4e949a3d62d7025b4b25",
              "packageId": "173826517799796742",
              "packageProjectId": "175606772457799967",
              "packageName": "门店新增套餐20231207",
              "packageTypeName": "整形套餐",
              "discount": 10,
              "orderOriginalPrice": 2254,
              "totalPrice": 2254,
              "selectFlag": true
            },
            "billingPackageProjects": [
              {
                "id": "cb88090a3c27421ca5cc6fc97bcb3dbb",
                "packageProjectId": "175606772457800732",
                "projectId": "e4110e7fe6e743ff9db6a34629eff3aa",
                "projectName": "（集团）巴黎人",
                "departmentId": "",
                "doctorName": null,
                "departmentName": "",
                "doctorId": null,
                "selectFlag": true,
                "totalPrice": 200,
                "remark": null,
                "numberOfTime": 1
              }
            ],
            "billingPackageGoods": []
          }
        ],
        "billingPackageAnnualCards": [
          {
            "selectFlag": true,
            "billingItemName": "吃饭饭",
            "departmentId": null,
            "departmentName": null,
            "discount": 10,
            "doctorId": null,
            "doctorName": null,
            "id": "8197e7ed53694700a30fdade9ed4e101",
            "itemDataId": "e4bb00e21c408832e1343320e4285f27",
            "packageProjectId": "175606772457801475",
            "totalPrice": 203,
            "unitPrice": 203,
            "childBillingItemList": [
              {
                "id": "b37385071fe54f28ae7074968e389091",
                "packageProjectId": "175606772457801751",
                "itemDataId": "eae78d079d3f44ab9c41ad55975c7815",
                "billingItemName": "消费项目哈哈1",
                "departmentId": "341514b58b534a518880d2da82b406f0",
                "departmentName": "集团整形科",
                "doctorId": null,
                "doctorName": null,
                "unitPrice": 1,
                "totalPrice": 0,
                "numberOfTime": 1,
                "remark": null
              }
            ]
          }
        ],
        "billingPackageTimeCards": [
          {
            "selectFlag": true,
            "billingItemName": "集团下发20231123",
            "departmentId": null,
            "departmentName": null,
            "discount": 10,
            "doctorId": null,
            "doctorName": null,
            "id": "9d4d454122204ba990632bdeac38adfe",
            "itemDataId": "7d5c39ae2b5544f7fc234f1b85524f58",
            "packageProjectId": "175606772977893894",
            "totalPrice": 800,
            "unitPrice": 800,
            "childBillingItemList": [
              {
                "id": "7d46d98eab6242969f7d92cc122b3d27",
                "packageProjectId": "175606772977894175",
                "itemDataId": "74dde656518c432d8330b9c89abb1cc7",
                "billingItemName": "（集团）红温兰博",
                "departmentId": "",
                "departmentName": "",
                "doctorId": null,
                "doctorName": null,
                "unitPrice": 700,
                "totalPrice": 0,
                "numberOfTime": 10,
                "remark": null
              }
            ]
          }
        ]
      }
    ],
    "payment": {
        "shouldPayMoney": 360
    },
    "paymentItemList": [
        {
            "selectFlag": true,
            "dataId": "142987337838624791",
            "thisChargePrice": 240
        },
        {
            "selectFlag": true,
            "dataId": "142987337838625862",
            "thisChargePrice": 120
        }
    ],
    "batchPayFeeReq": {
        "actualRecordedTime": "2023-09-13 11:10:12",
        "payWay": [
            {
                "payMode": "WECHAT",
                "payMoney": 20
            },
            {
                "payMode": "DEFAULT_MINIPARAM_WECHAT",
                "payMoney": 220
            }
        ],
        "scoreReq": {
            "scoreMoney": 20,
            "scoreNum": 20,
            "onlyRecordFlag": true
        },
        "balanceReqList": [
            {
                "givenBalance": 51,
                "balance": 49
            }
        ]
    },
    "uId": "1546254854856963217" 
}
```

- **返回结果**

code是10000表示成功，其他全视为失败，失败会在msg放置失败消息

data会返回开单的订单号

```JSON
{
    "code": 10000,
    "data": {
        "billingId": "订单id",
        "billingNo": "订单号",
        "paymentId": "费用单id",
        "payment": {   //费用单
        
        },
        "newBillingItems":[{  // 订单项参数信息
            
        }],
        "todayTreatResList":[{  //今日治疗信息
            
        }],
        "payFailFlag": true, //收费是否成功
        "payFailMsg": "支付失败的原因",
        "exception": {}  // Exception对象信息
    },
    "msg": "操作成功"
}
```

## [可操作的订单项](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#OFXUdkgZZoJd95xTCaPcRce6nyd)

> 订单内部变化场景非常多，所以如果有等待提示"*不要频繁操作同一个客户，请稍后再操作*"
> 
> 就必须要等院内业务完成后再请求。

- 请求URL（需要tpos鉴权）

 **/api/v1/tpos/order/enable-billing    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| billingId | 是 | string | 订单id |  |
| mark | 是 | int | 操作类型 | （0-退款，1-转赠，2-转项） |

![图片展示的是订单（order）相关接口的GET请求示例。请求URL为127.0.0.1:60005/api/v1/tpos/order/enable-billing，需tpos鉴权。参数包括billingId（订单id，必填）和mark（操作类型，0为退款，1为转赠，2为转项，必填）。响应状态码200，返回结果中包含code、data等信息，billingItems下有billingItemId、finishFlag、treatScoreMoney等字段，如billingItemId为“bf2a1246eccd4ceeb93e536b860f5d499”，finishFlag为false等。](https://feishu.cn/file/HoDrbeAEBo8KCDx59TMc1kYhngh)

- **返回结果**

> 系统中有单项，套餐，年卡，次卡
> 
> 单项的开单次数是numberOfTime，剩余次数是residueNum
> 
> 年卡的剩余次数无意义，年卡是无限的
> 
> 次卡的剩余次数在次卡本身上，他的子项剩余次数也是无意义的

```JSON
{
    "code": 10000,
    "data": {
        "residualTotalPrice": 130.00                    //    可退款总额
        "billingItems": [
            {
                "id": "e443f39f18a649b1bd7995f7062c060e",        //    订单项id
                "billingItemName": "集团下发治疗",                //    订单项名称
                "typeName": "普通次卡",                           //    所在分类名称
                "billingItemTypeCategory": 4,                    //    订单项分类 0：单项 1：套餐 2：活动 3：年卡 4：次卡 5：权益卡
                "billingItemType": 1,                            //    订单项类型 0：项目 1：分类本身 2：商品 3：套餐项目（仅套餐在用）4：药品 5：卡券
                "canSelect": true,                               //    是否可选择
                "unitPrice": 130.00                              //    单价
                "totalPrice": 130.00,                            //    总价
                "numberOfTime": 1,                               //    开单次数，年卡的次数是无限的，次卡的次数在次卡本身上
                "residueNum": 6,                                 //    剩余数量，年卡的剩余次数是无限的，次卡的剩余次数在次卡本身上
                "childBillingItems": [                           //    子项
                    {
                        "id": "54139f3057e140c1a2c05aec5d24a05d",
                        "billingItemName": "项目A",
                        "typeName": "新建分类",
                        "billingItemTypeCategory": 4,
                        "billingItemType": 0,
                        "unitPrice": 10.00,
                        "totalPrice": 130.00,
                        "alreadyRefundMoney":"0.00"         //    已退款的金额
                        "numberOfTime": 6,
                        "residueNum": 1               
                    },
                    {
                        "id": "869b7d136c5242519ce87dfd07a12997",
                        "billingItemName": "项目B",
                        "typeName": "新建分类",
                        "billingItemTypeCategory": 4,
                        "billingItemType": 0，
                        "unitPrice": 20.00
                        "totalPrice": 20,
                        "numberOfTime": 6,
                        "residueNum": 1,
                    },
                    {
                        "id": "e490dd79a97a4f52acafecc744ee49aa",
                        "billingItemName": "项目C",
                        "typeName": "新建分类",
                        "billingItemTypeCategory": 4,
                        "billingItemType": 0，
                        "unitPrice": 100.00,
                        "totalPrice": 100,
                        "numberOfTime": 6,
                        "residueNum": 1
                    }
                ]
            }
        ],
    },
    "msg": "操作成功"
}
```



## [订单退款](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#MaN4dYVLVoeHoMxezgUczibLnGh)

> 调用此接口视为普通退款（生成普通退款费用单）
> 
> 接口并不会自动完成审批（如果配置了审批权限），并不会自动处理退款费用单。
> 
> 审批（如果配置了审批权限）和退款费用单的处理，需要院内员工在系统上操作。
> 
> 订单内部变化场景非常多，所以如果有等待提示"*不要频繁操作同一个客户，请稍后再操作*"
> 
> 就必须要等院内业务完成后再请求。

- 请求URL（需要tpos鉴权）

 **/api/v1/tpos/order/refund    POST**

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| **billingRecord** |  |  | **退款单信息** |  |
|   +billingId | 是 | string | 订单id |  |
| **oldBillingItems** |  | **array** | **退款单信息** |  |
|   +billingItemId | 是 | string | 订单项id |  |
|   +deductPayMoney | 是 | decimal | 实际退款金额 |  |
|   +shouldUserPrice | 是 | decimal | 订单可以操作的钱 |  |
|   +usePrice | 是 | decimal | 实际退的钱 |  |
|   +useCount | 是 | int | 退款数量 |  |
|   **+childBillingRecordItem** |  | **array** | **子项信息（子项记录）** |  |
|       +billingItemId | 是 | string | 订单项id |  |
|       +shouldUserPrice | 是 | decimal | 可以操作的钱 |  |
|       +usePrice | 是 | decimal | 实际退的钱 |  |
|       +useCount | 是 | int | 退款数量 |  |
|   **+billingPackagePackages** |  | **array** | **子项信息（套餐中的套餐）** |  |
|       +billingItemId | 是 | string | 订单项id |  |
|       +shouldUserPrice | 是 | decimal | 可以操作的钱 |  |
|       +usePrice | 是 | decimal | 实际退的钱 |  |
|       +useCount | 是 | int | 退款数量 |  |
|       +childBillingRecordItem |  | array | 子项信息 |  |
|           +billingItemId | 是 | string | 订单项id |  |
|   **+billingPackageAnnualCards** |  | **array** | **子项信息（套餐中的年卡）** |  |
|       +billingItemId | 是 | string | 订单项id |  |
|       +shouldUserPrice | 是 | decimal | 可以操作的钱 |  |
|       +usePrice | 是 | decimal | 实际退的钱 |  |
|       +useCount | 是 | int | 退款数量 |  |
|       +childBillingRecordItem |  | array | 子项信息 |  |
|           +billingItemId | 是 | string | 订单项id |  |
|   **+billingPackageTimeCards** |  | **array** | **子项信息（套餐中的次卡）** |  |
|       +billingItemId | 是 | string | 订单项id |  |
|       +shouldUserPrice | 是 | decimal | 可以操作的钱 |  |
|       +usePrice | 是 | decimal | 实际退的钱 |  |
|       +useCount | 是 | int | 退款数量 |  |
|       +childBillingRecordItem |  | array | 子项信息 |  |
|           +billingItemId | 是 | string | 订单项id |  |
| finishRefundFlag | 否 | boolean | 是否需要完成收银 | true-完成收银，若无指定支付方式则以开单缴费支付方式原路退回 |
| payFeeReq | 否 |  | 退款支付信息 |  |
|   **+payWay** | **是** | **array** | **支付方式** |  |
|       +payMode | 是 | string | 具体支付方式 | 根据数据字典-支付方式的属性值来传 |
|       +payMoney | 是 | decimal | 支付金额 |  |

示例数据：

```JSON
{    
    "billingRecord": {
        "billingId": "2a138fa7efd84bd1931da6ccee97365a"
    },
    "oldBillingItems": [
        {
            "billingItemId": "6fe80620d0964ad892154dfd9f5100e8",
            "useCount": 1,
            "shouldUserPrice": 1280,
            "usePrice": 1270,
            "childBillingRecordItem": [
                {
                    "billingItemId": "bda1ece42e5547c88b228f0e58746260",
                    "useCount": 6,
                    "shouldUserPrice": 1280,
                    "usePrice": 1270
                }
            ],
            "billingPackagePackages": [
                {
                    "billingItemId": "a5891565e23e4b23bb762844d861036e",
                    "useCount": 1,
                    "shouldUserPrice": 170,
                    "usePrice": 160,
                    "childBillingRecordItem": [
                        {
                            "billingItemId": "ef4c18cacdc5413eaaa335b8c426205d",
                            "shouldUserPrice": 170,
                            "useCount": 1,
                            "usePrice": 160
                        }
                    ]
                }
            ],
            "billingPackageAnnualCards": [
                {
                    "billingItemId": "2d7f7a0912504e948a523198aae41b4a",
                    "useCount": 1,
                    "shouldUserPrice": 100.01,
                    "usePrice": 100.01,
                    "childBillingRecordItem": [
                        {
                            "billingItemId": "57315ab00b7341729922077984480968"
                        },
                        {
                            "billingItemId": "6b9e70d088574e279ebba6af818a3d91"
                        }
                    ]
                }
            ],
            "billingPackageTimeCards": [
                {
                    "billingItemId": "ea3b40397c924b1691de98ba52591a48",
                    "shouldUserPrice": 273,
                    "usePrice": 272,
                    "useCount":1,
                    "childBillingRecordItem": [
                        {
                            "billingItemId": "18ac5c655acd4381bfddb69c169093e2"
                        },
                        {
                            "billingItemId": "63dc13deeceb43108df990c29336f4ed"
                        },
                        {
                            "billingItemId": "d0f79b70dbde42ae99060e2908c8372e"
                        }
                    ]
                }
            ]
        }
    ]
}
```

- **返回结果**

> code是10000表示成功，其他全视为失败，失败会在msg放置失败消息

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

## [小程序-赠送项目（分享）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#IcigdN2LxoVjRfxFp3Qc2tCXnIc)

- 请求URL

**/api/v1/scrm/giftReceive/gift/project   POST**

- 参数说明

![图片展示的是睿美云开放接口中订单（order）相关接口的请求参数示例。在“Body”选项卡下，参数类型为“raw”，内容为JSON格式，包含“oldBillingId”“oldBillingProjectId”“giftRecordId”“sourceBillingRecordId”等字段，其中“giftRecordId”字段值为“56123c77d3e38280f1ac809df5142eba”，“sourceBillingRecordId”字段值为空。该图片与文档中订单接口参数说明部分对应，直观呈现了接口请求参数的具体内容。](https://feishu.cn/file/MiODb5OlDoDyUTxnHAvcC36PnLe)

![这是一个API请求的Body内容示例，对应睿美云开放接口中小程序分享赠送项目的POST请求。该请求的Body为JSON格式，其中标注了请求必填的两个核心字段，分别是oldBillingId（值为"4299e993313a4a18a34d81b06a7a6ae2"）和giftRecordId（值为"123c77d3e8280f1ac809df5142ebae"），还包含可选的套餐相关信息，比如oldBillingPackageProjectInfo对象及其内的oldBillingPackageId、oldBillingPackageProId等字段，可用于小程序分享赠送项目的接口传参。](https://feishu.cn/file/Apo2b2g0no9CYexmX9acrlOonfE)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| oldBillingId | 是 | string | 原始订单id |  |
| oldBillingProjectId | 否 | string | 订单项id |  |
| oldBillingPackageProjectInfo | 否 | object | 套餐项信息 |  |
| oldBillingPackageId | 否 | string | 套餐项id |  |
| sourceBillingRecordId | 否 | string | 关联的转项记录id |  |
| oldBillingPackageProId | 否 | string | 订单项id |  |
| giftRecordId | 是 | string | 赠送单id | 微信分享不支持异步获取这个ID，所以ID改由小程序端生成，后端通过这个ID生成待领取的赠送记录 |
| sourceBillingRecordId | 否 | string | 关联的转项记录id |  |

- **返回结果**

```JSON
{
  "msg": "成功",
  "code": 10000,
  "data": "c77d3e38280f1ac809df5142ebaeed14"    //赠送单id
}
```

## [小程序-领取赠送项目](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#W7lpd4CdCoZ1zTxpqaVc4SG2nIg)

- 请求URL

 **/api/v1/scrm/giftReceive/receive/project    GET**

- 参数说明

![图片展示的是接口测试工具中“/api/v1/scrm/giftReceive/receive/project GET”接口的参数设置界面。在“Query Params”标签下，有两个参数被选中，分别是“Key”和“giftRecordId”，其对应的Value分别为“123c77d3e38280f1ac809df5142ebaee”和“123c77d3e38280f1ac809df5142ebaee”。该图片与文档中“小程序-领取赠送项目”接口的参数说明部分对应，直观呈现了接口调用时所需参数的具体设置情况。](https://feishu.cn/file/Yv7qbxXQ4oWu7JxFmAScV5eWnGe)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| giftRecordId | 是 | string | 待领取的赠送单id |  |

- 返回结果

```JSON
{
  "msg": "领取成功",
  "code": 10001,
  "data": null
}
```

## [小程序-项目转赠（小程序分享）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#UWDkdoBbTosMr9xG4nLcgoz6nWb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/gift-project    POST**

- 参数说明

![图片展示的是睿美云开放接口中订单（order）小程序-项目转赠（小程序分享）的Body部分。在Body中，以raw形式提交了JSON数据，包含giftRecordId、customerId、oldBillingProjectId和scrmOperateTenant四个字段，其值分别为“78cd08ce094e11f089ba0242ac110002”等。该图片与文档中请求URL（需tpos鉴权）及参数说明的内容相关，直观呈现了Body部分的参数结构和值，是接口调用时参数提交的示例。](https://feishu.cn/file/DNS1bBLZtoQ97fxyYfwcV2unnhh)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| giftRecordId | 否 | string | 赠送单id | 长度不能超过32位。因为微信分享不支持异步获取这个ID，所以ID改由小程序端生成，后端通过这个ID生成待领取的赠送记录。如果不传值，则由接口生成并返回 |
| customerId | 是 | string | 客户id |  |
| oldBillingProjectId | 是 | string | 订单项id |  |
| scrmOperateTenant | 是 | string | 门店id |  |

- 返回结果

```JSON
{
  "msg": "操作成功",
  "code": 10000,
  "data": "c77d3e38280f1ac809df5142ebaeed14"    //赠送单id
}
```

## [小程序-领取赠送项目（小程序分享）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Tk13dCuNgosG8CxQBQGclfIGnXe)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/receive-project    POST**

- 参数说明

![图片展示的是一个API接口请求的Body部分，请求方式为POST，URL为/api/v1/tpos/order/receive-project。Body内容为JSON格式，包含三个字段：customerId（客户id，值为“c101ae946dfc423386ece3b41979952a”）、tenantId（门店id，值为“1”）、giftRecordId（待领取的赠送单id，值为“78cd08ce094e11f089ba0242ac110002”）。该图片与文档中“小程序-领取赠送项目（小程序分享）”接口请求相关，展示了接口请求参数的具体内容。](https://feishu.cn/file/WJPnbTwsCotJ4Sxn6QCcfPMonmc)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| tenantId | 是 | string | 门店id |  |
| giftRecordId | 是 | string | 待领取的赠送单id |  |

- 返回结果

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

## [**获取客户权益卡**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#FzpLd8Vd5oJERUxUKQ9ciWgFn9f)[**列表**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#FzpLd8Vd5oJERUxUKQ9ciWgFn9f)

- 请求URL（需要tpos鉴权）

 **/api/v1/tpos/order/billing-equity-card-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| page | 否 | int | 页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |
| choiceValidity | 否 | bool | 是否要查询有效的权益卡 | true: 有效的权益卡  <br/>false或者不传，全部的权益卡 |

![图片展示的是睿美云开放接口中获取客户权益卡的请求及返回结果界面。请求URL为192.168.2.133:60000/api/v1/tpos/order/billing-equity-card-page，参数包括customerId、page、size等。返回结果中，code为10000，data部分显示了billingEquityCardId、billingEquity、billingEq、billingEq等信息，其中billingEquityCardId为“868e4d7389f79e6ca9291a6de496d07868”，billingEq为“两期免息”，billingEqId为“1217e6c78ed74ac45d464b9917ca9c6d7”。该图片与文档中获取客户权益卡的请求及返回结果内容对应。](https://feishu.cn/file/ZbmTbdJutoQ3QAxmlA4clwAynWg)

- **返回结果**

```JSON
{
    "code": 10000,
    "data": {
        "current": 1,
        "pages": 1,
        "records": [
            {
                "billingEquityCardId": "865b6178079d4ca39291a66a95dd7050",    //    权益卡id
                "cardGivenMoney": 40.00,                                //    权益卡赠送金额
                "cardMoney": 30.00,                                     //    权益卡本金
                "cardName": "有期限的权益卡",                            //    权益卡名称
                "customerId": "217e6c170ef74acf84bf4b9917ca9687",        //    客户id
                "operatorId": "81d98b84d02abfa3a65a08f927d96637",        //    开单人id
                "operatorName": "lf管理员",                              //    开单人姓名
                "paymentInfo": "[{\"id\": \"8274e1a066744ed7af740aed160ad1ac\", \"name\": \"JF20230316145344327\"}]",    //    费用单信息
                "recordNo": "QY20230830155159810",                    //    权益卡号
                "subCardGivenMoney": 0.00,                            //    还有多少赠送金额可用
                "subCardMoney": 0.00,                                 //    还有多少金额可用
                "tenantId": "1",                                      //    门店id
                "tenantName": "门店1",                                //    门店名称
                "validPeriodText": "2023-08-23~2023-09-22",            //    有效期（日）
                "validityEndDate": "2023-09-22 23:59:59",            //    有效期开始时间
                "validityStartDate": "2023-08-23 00:00:00"            //    有效期结束时间，
                "flowList":[{
                     "status": "WAIT_HANDLE",        //    状态 WAIT_HANDLE：待处理，HANDLE（已处理），CANCEL(已作废)，PAUSE(挂起)
                     "sourceType": "DEDUCTION",      //    明细来源 BILLING（开单），DEDUCTION（抵扣），REFUND(退款)
                     "tenantId": "1",                //    门店id
                     "tenantName": "门店1",          //    门店名称
                     "createDate": 1668566872000,    //    操作时间
                     "cardGivenMoney": 40.00,        //    权益卡赠送金额
                     "cardMoney": 30.00,             //    权益卡本金
                     "operatorId": "81d98b84d02abfa3a65a08f927d96637",       //    操作人id
                     "operatorName": "lf管理员",                              //    操作人姓名
                     "paymentInfo": "[{\"id\": \"8274e1a066744ed7af740aed160ad1ac\", \"name\": \"JF20230316145344327\"}]" //    所属费用单信息
                 }]
            }
        ],
        "size": 20,
        "total": 6
    },
    "msg": "操作成功"
}
```

## 添加储值记录

> 储值记录涉及到实际金额，调用请慎重，请与睿美云工作人员沟通实际使用场景，获取接口详细信息

## 添加储值抵扣记录

> 储值记录涉及到实际金额，调用请慎重，请与睿美云工作人员沟通实际使用场景，获取接口详细信息



## [储值充值记录](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#HpJvdQA0xo0ZTNxAU0VcH9d9nCh)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/balance-recharge-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 否 | string | 客户id |  |
| phoneNumber | 否 | string | 客户电话号码 | 因为不同客户可能使用相同的电话号码，如果查询到多个客户，则随机选择第一个客户进行查询，所以强烈建议使用客户id进行查询 |
| page | 否 | int | 当前页 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOf三方：储值记录DTO | IPageOf三方：储值记录DTO |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | 三方：储值记录DTO |
|     createDate | 开单时间 | string |  |
|     fromCustomerName | 转赠客户 | string |  |
|     fromCustomerPhone | 转赠客户手机号 | string |  |
|     givenMoney | 赠送金额 | number |  |
|     id | 数据id | string |  |
|     operatorId | 开单人id | string |  |
|     operatorName | 开单人姓名 | string |  |
|     paymentId | 费用单id | string |  |
|     paymentNo | 费用单号 | string |  |
|             chargeTime | 缴费时间 | string |  |
|     rechargeMoney | 充值金额 | number |  |
|     rechargeNo | 充值单号 | string |  |
|     rechargeType | 充值类型 | integer |  |
|     rechargeTypeDesc | 充值类型描述 | string |  |
|     remark | 备注 | string |  |
|     status | 状态 | integer |  |
|     statusDesc | 状态描述 | string |  |
|     tenantId | 门店id | string |  |
|     tenantName | 门店名称 | string |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## [储值抵扣记录](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#V2R9drrYJopXzqxCG7ecAbCGnEj)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/balance-deduction-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| page | 否 | int | 页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOf三方：储值抵扣记录DTO | IPageOf三方：储值抵扣记录DTO |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | 三方：储值抵扣记录DTO |
|     deductionMoney | 抵扣金额 | number |  |
|     givenFlag | 是否是赠送金额  true：是，false：否 | boolean |  |
|     id | 数据id | string |  |
|     operatorId | 抵扣人id | string |  |
|     operatorName | 抵扣人姓名 | string |  |
|     paymentInfo | 费用单信息 (json) | string |  |
|     tenantId | 门店id | string |  |
|     tenantName | 门店名称 | string |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## [储值退款记录](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#IBpmdxVqhoePfRxBRs9clugenNh)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/balance-refund-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| page | 否 | int | 当前页 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOf三方：储值退款记录DTO | IPageOf三方：储值退款记录DTO |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | 三方：储值退款记录DTO |
|     createDate | 退款时间 | string |  |
|     id | 数据id | string |  |
|     operatorId | 退款人id | string |  |
|     operatorName | 退款人姓名 | string |  |
|     paymentId | 费用单id | string |  |
|     paymentNo | 费用单号 | string |  |
|     refundGivenMoney | 扣除赠送 | number |  |
|     refundMoney | 退款金额 | number |  |
|     refundNo | 退款单号 | string |  |
|     refundType | 退款类型描述 | string |  |
|     refundTypeOrigin | 退款类型 | integer |  |
|     remark | 备注 | string |  |
|     status | 状态 | integer |  |
|     statusDesc | 退款状态描述 | string |  |
|     tenantId | 门店id | string |  |
|     tenantName | 门店名称 | string |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## [储值转赠记录](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#ZFh0dI8OuocKaHxGzG7c9sfUnJg)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/balance-transfer-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| page | 否 | int | 当前页 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOf三方：转赠记录DTO | IPageOf三方：转赠记录DTO |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | 三方：转赠记录DTO |
|     balanceTransferNo | 转赠记录号 | string |  |
|     createDate | 转赠时间 | string |  |
|     givenMoney | 赠送金额 | number |  |
|     id | 数据id | string |  |
|     operatorId | 转赠操作人id | string |  |
|     operatorName | 转赠操作人姓名 | string |  |
|     rechargeNo | 转赠充值单号 | string |  |
|     refundNo | 转赠退款单号 | string |  |
|     remark | 备注说明 | string |  |
|     status | 状态(0-未转赠 1-已转赠 2-已作废 3-已撤销) | integer |  |
|     tenantId | 门店id | string |  |
|     tenantName | 门店名称 | string |  |
|     toCustomerId | 受赠客户id | string |  |
|     toCustomerName | 受赠客户名称 | string |  |
|     toCustomerPhone | 受赠客户手机号 | string |  |
|     transferMoney | 赠送金额 | number |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## [获取积分兑换订单信息列表](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#EHqxdL4ZLotE54xu8mJcR2Wvn1e)

- 请求URL（需要tpos鉴权）

 **/api/v1/tpos/order/integral-mall-exchange-page    GET**

- 参数说明

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| tenantIdList | 要查询的门店id，多个用逗号隔开 | query |  | string |
| customerId | 客户id | query |  | string |
| exchangeStartTime | 兑换时间-开始时间 | query |  | date-time |
| exchangeEndTime | 兑换时间-结束时间 | query |  | date-time |
| page | 默认为：1，最小为：1 | query |  | integer(int32) |
| size | 默认为：20，最大为：500 | query |  | integer(int32) |

![图片展示的是Postman工具中获取积分兑换订单信息列表的请求界面。请求方法为GET，URL为http://192.168.2.133:60005/api/v1/tpos/order/integral-mall-exchange-page。参数部分，tenantIdList为1,2，customerId为b99a1a46aa7748dbd9aa17d6d9d25a098，exchangeStartTime为2023-12-01 00:00:00，exchangeEndTime为2023-12-29 23:59:59，page为1，size为10。右侧响应结果中，tenantId为1，code为10000，data中包含countId、current、maxList、orders、total等信息，pages为1，records中显示了订单相关数据。](https://feishu.cn/file/ZRjMbF1e8ofLvlxM1CJcZZTunLh)

- **返回结果**

```JSON
{
    "code": 10000,
    "data": {
        "current": 1,
        "pages": 1,
        "records": [
            {
                "customerId": "b99a1a46aa7748db9aa17dd69d25a098",    //    客户id
                "name": "黄雪杰",                                    //    客户姓名
                "phoneNumber": "[{\"isp\": \"电信\", \"area\": \"1\", \"city\": \"眉山\", \"prov\": \"四川\", \"ismain\": true, \"phoneNumber\": \"17381755957\"}]",
                "itemId": 1,                            //    0：礼品，1：优惠券
                "giftName": "测试领取-优惠券",            //    礼品名称
                "integralExchangeNum": 1,               //    积分兑换值(单价)
                "exchangeNum": 5,                       //    兑换数量
                "createDate": "2023-12-19 14:58:52",    //    兑换时间
                "useNum": null,                         //    使用数量
                "refundNum": 5,                         //    退款数量
                "refundTime": "2023-12-19 14:59:43",    //    退款时间
                "exchangeOrderNum": "JF20231219145856905",    //    兑换单号
                "trackingType": 2,                            //    0：无，1：到店自提，2：快递到家
                "deliverAddress": "北京市东城区xxx小区",        //    收货人地址
                "deliverCustomerName": "【游客】王旺",          //    收货人姓名
                "deliverPhoneNumber": "13000001111",           //    收货人电话
                "exchangeStatus": 3,                // 0：未领取，1：已领取，2：退款审核中，3：已退回，4：部分退款，5：出库中，6：未领取-部分退款
                "trackingStatus": 2,                // 0：待发货，1：待收货，2：已完成
                "id": "de3102fb25304df89923c6616ccfde23",       //    数据id
                "tenantId": "1",                                //    门店id
                "tenantName": "门店1"                           //    门店名称
            }
        ],
        "size": 10,
        "total": 1
    },
    "msg": "操作成功"
}
```

## 对接三方小程序开单

- 请求URL（需要tpos鉴权）

**POST /api/v1/tpos/order/add-order-external**

- 参数说明

<sheet sheet-id="Bibxep" token="shtcnTKOlDjgLChPQvGBfiOv2Eg"></sheet>

- 注意事项

储值抵扣，储值赠送抵扣，积分抵扣 都只支持一个 OrderItemPayRequest 对象

- 返回结果

code是10000表示成功，其他全视为失败，失败会在msg放置失败消息

data会返回开单的订单号

- 请求示例：

请求参数：

```json
{
    "tenantId": "1",
    "orderTime": "2025-03-31 08:00:00",
    "payTime": "2025-03-31 08:00:00",
    "customerId": "279f5b07f69749a29736c857abd1d7c0",
    "transactionNo": "106",
    "orderPrice": 6223.42,
    "discountPrice": 0,
    "payPrice": 6223.42,
    "orderRemark": "velit qui Duis",
    "orderVerifyCode": "7489465",
    "integralRatio": 20,
    "items": [
        {
            "thirdOrderItemId":"uid1",
            "itemOrderType": "BILLING",
            "type": "PROJECT",
            "dataId": "347692090710294532",
            "name": "不治疗项目",
            "originUnitPrice": 1000,
            "unitPrice": 500,
            "num": 2,
            "orderItemPrice": 2000,
            "orderItemDiscountPrice": 1000,
            "orderItemPayPrice": 1000,
        },
        {
                    "thirdOrderItemId":"uid2Q",
            "itemOrderType": "BILLING",
            "type": "PROJECT",
            "dataId": "310065629354786820",
            "name": "水光光-AD",
            "originUnitPrice": 200,
            "unitPrice": 200,
            "num": 1,
            "orderItemPrice": 200,
            "orderItemDiscountPrice": 0,
            "orderItemPayPrice": 200,
        },
        {
                    "thirdOrderItemId":"uid3",
            "itemOrderType": "BILLING",
            "type": "YEAR_CARD",
            "dataId": "ea9ea39f09a705b365ae5ab9c0575241",
            "name": "规范",
            "originUnitPrice": 100.01,
            "unitPrice": 100.01,
            "num": 1,
            "orderItemPrice": 100.01,
            "orderItemDiscountPrice": 0,
            "orderItemPayPrice": 100.01,
            "subItems": [
                {
                            "thirdOrderItemId":"uid4",
                    "itemUniqueId": "206366147669393409",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "cf1752dc18fb4467832a9db2f3377c0f",
                    "name": "分潜伏期",
                    "originUnitPrice": 100,
                    "unitPrice": 100,
                    "num": 1,
                    "orderItemPrice": 100,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 100,
                },
                {
                            "thirdOrderItemId":"uid5",
                    "itemUniqueId": "206366147669393666",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "f3023c0182fb423484278a8e56afa765",
                    "name": "一分项目",
                    "originUnitPrice": 0.01,
                    "unitPrice": 0.01,
                    "num": 1,
                    "orderItemPrice": 0.01,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 0.01,
                },
            ]
        },
        {
                    "thirdOrderItemId":"uid6",
            "itemOrderType": "BILLING",
            "type": "TIME_CARD",
            "dataId": "264072075818303490",
            "name": "次卡日志",
            "originUnitPrice": 4700,
            "unitPrice": 4700,
            "num": 1,
            "orderItemPrice": 4700,
            "orderItemDiscountPrice": 0,
            "orderItemPayPrice": 4700,
            "subItems": [
                {
                            "thirdOrderItemId":"uid7",
                    "itemUniqueId": "270152345935937541",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "257827290480640001",
                    "name": "保妥适-max",
                    "originUnitPrice": 600,
                    "unitPrice": 600,
                    "num": 1,
                    "orderItemPrice": 600,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 600,
                },
                {
                            "thirdOrderItemId":"uid8",
                    "itemUniqueId": "270152345935937797",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "257896522862034950",
                    "name": "肉毒素-项目-0001",
                    "originUnitPrice": 4000,
                    "unitPrice": 4000,
                    "num": 1,
                    "orderItemPrice": 4000,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 4000,
                },
                {
                            "thirdOrderItemId":"uid9",
                    "itemUniqueId": "270152345935938051",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "257829715895648261",
                    "name": "保妥适-max-001",
                    "originUnitPrice": 100,
                    "unitPrice": 100,
                    "num": 1,
                    "orderItemPrice": 100,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 100,
                },
            ]
        },
        {
                    "thirdOrderItemId":"uid10",
            "itemOrderType": "BILLING",
            "type": "PACKAGES",
            "dataId": "285728816804921349",
            "name": "会员套餐不要动",
            "originUnitPrice": 223.41,
            "unitPrice": 223.41,
            "num": 1,
            "orderItemPrice": 223.41,
            "orderItemDiscountPrice": 0,
            "orderItemPayPrice": 223.41,
            "subItems": [
                {
                            "thirdOrderItemId":"uid11",
                    "itemUniqueId": "285728816955916289",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "269879089358176257",
                    "name": "测试很多次哈哈哈",
                    "originUnitPrice": 0.6,
                    "unitPrice": 0.6,
                    "num": 1,
                    "orderItemPrice": 0.6,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 0.6,
                },
                {
                            "thirdOrderItemId":"uid12",
                    "itemUniqueId": "285821479998717956",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "269875843822518273",
                    "name": "测试商城管理Casablanca",
                    "originUnitPrice": 0.6,
                    "unitPrice": 0.6,
                    "num": 1,
                    "orderItemPrice": 0.6,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 0.6,
                },
                {
                            "thirdOrderItemId":"uid163",
                    "itemUniqueId": "348470352415817730",
                    "itemOrderType": "BILLING",
                    "type": "PACKAGES",
                    "dataId": "285728816804921349",
                    "name": "会员套餐不要动",
                    "originUnitPrice": 223.41,
                    "unitPrice": 1.2,
                    "num": 1,
                    "orderItemPrice": 1.2,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 1.2,
                    "subItems": [
                        {
                                    "thirdOrderItemId":"uid14",
                            "itemUniqueId": "348470352436789248",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "269879089358176257",
                            "name": "测试很多次哈哈哈",
                            "originUnitPrice": 0.6,
                            "unitPrice": 0.6,
                            "num": 1,
                            "orderItemPrice": 0.6,
                            "orderItemDiscountPrice": 0,
                            "orderItemPayPrice": 0.6,
                        },
                        {
                                    "thirdOrderItemId":"uid15",
                            "itemUniqueId": "348470352436789504",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "269875843822518273",
                            "name": "测试商城管理Casablanca",
                            "originUnitPrice": 0.6,
                            "unitPrice": 0.6,
                            "num": 1,
                            "orderItemPrice": 0.6,
                            "orderItemDiscountPrice": 0,
                            "orderItemPayPrice": 0.6,
                        }
                    ]
                },
                {
                            "thirdOrderItemId":"uid16",
                    "itemUniqueId": "348470352436789761",
                    "itemOrderType": "BILLING",
                    "type": "YEAR_CARD",
                    "dataId": "c31c91807b1c730e1d9c4c64fc370eb7",
                    "name": "20000",
                    "originUnitPrice": 210.01,
                    "unitPrice": 210.01,
                    "num": 1,
                    "orderItemPrice": 210.01,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 210.01,
                    "subItems": [
                        {
                                    "thirdOrderItemId":"uid17",
                            "itemUniqueId": "348470352436790021",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "f3023c0182fb423484278a8e56afa765",
                            "name": "一分项目",
                            "originUnitPrice": 0.01,
                            "unitPrice": 0.01,
                            "num": 1,
                            "orderItemPrice": 0.01,
                            "orderItemDiscountPrice": 0,
                            "orderItemPayPrice": 0.01,
                        },
                        {
                                    "thirdOrderItemId":"uid18",
                            "itemUniqueId": "348470352436790274",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "4079931ed2c44a25a0325fbe1a433992",
                            "name": "爱少女风1爱少女风1爱少女风1爱少女风1爱少女风1爱少女风1爱少女风1爱少女风1vv",
                            "originUnitPrice": 210,
                            "unitPrice": 210,
                            "num": 1,
                            "orderItemPrice": 210,
                            "orderItemDiscountPrice": 0,
                            "orderItemPayPrice": 210,
                        }
                    ]
                },
                {
                            "thirdOrderItemId":"uid20",
                    "itemUniqueId": "348470352436790528",
                    "itemOrderType": "BILLING",
                    "type": "TIME_CARD",
                    "dataId": "256444712196505600",
                    "name": "不可转赠03",
                    "originUnitPrice": 11,
                    "unitPrice": 11,
                    "num": 1,
                    "orderItemPrice": 11,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 11,
                    "subItems": [
                        {
                                    "thirdOrderItemId":"uid21",
                            "itemUniqueId": "348470352436790788",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "251349420140920834",
                            "name": "种草项目",
                            "originUnitPrice": 1,
                            "unitPrice": 1,
                            "num": 2,
                            "orderItemPrice": 2,
                            "orderItemDiscountPrice": 1,
                            "orderItemPayPrice": 1,
                        },
                        {
                                    "thirdOrderItemId":"uid22",
                            "itemUniqueId": "348470352436791046",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "248807782193561604",
                            "name": "AD钙项目",
                            "originUnitPrice": 10,
                            "unitPrice": 10,
                            "num": 2,
                            "orderItemPrice": 20,
                            "orderItemDiscountPrice": 10,
                            "orderItemPayPrice": 10,
                        }
                    ]
                },
            ]
        },
    ],
    "payItems": [
        {
            "amount": 1,
            "payWayId": "virtual_card_pay_id",
            "payWayName": "卡券",
            "sameAmountValue": 20,
            "payWayDetailType": "VIRTUAL_CARD_PAY"
        },
        {
            "amount": 20,
            "payWayId": "其他虚拟金",
            "payWayName": "其他虚拟金",
            "payWayDetailType": "VIRTUAL_OTHER_PAY"
        },
        {
            "amount": 7.45,
            "payWayId": "储值",
            "payWayName": "储值",
            "payWayDetailType": "ACTUAL_BALANCE_PAY"
        },
        {
            "amount": 2.55,
            "payWayId": "储值赠送",
            "payWayName": "储值赠送",
            "payWayDetailType": "VIRTUAL_BALANCE_GIVE_PAY"
        },
        {
            "amount": 10,
            "payWayId": "8b0de8636243466998078ca29593d1e4",
            "payWayName": "定金",
            "payWayDetailType": "ACTUAL_DEPOSIT_PAY"
        },
        {
            "amount": 10,
            "payWayId": "9cbe4bbdbe8d434389b7f6a316d625e0",
            "payWayName": "权益卡本金",
            "payWayDetailType": "ACTUAL_EQUITY_PAY"
        },
        {
            "amount": 6162.42,
            "payWayId": "ALIPAY",
            "payWayName": "支付宝",
            "payWayDetailType": "ACTUAL_OTHER_PAY"
        },
        {
            "amount": 10,
            "payWayId": "WECHAT",
            "payWayName": "微信",
            "payWayDetailType": "ACTUAL_OTHER_PAY"
        }
    ]
}
```

返回参数：

```json
{
    "code": 10000,
    "data": {
        "orderId": "350323538491604998"
    },
    "msg": "操作成功"
}
```

## 对接三方小程序退款 

退款（全部退和部分退），部分退不用给开单的参数，红色字段必传

- 请求URL（需要tpos鉴权）

**POST /api/v1/tpos/order/refund-order-external**

- 参数说明

<sheet sheet-id="QhqFOC" token="shtcnTKOlDjgLChPQvGBfiOv2Eg"></sheet>

- 返回结果

code是10000表示成功，其他全视为失败，失败会在msg放置失败消息

data：如果是部分退，会返回一个新的订单id

- 请求示例：

请求参数：

```json
{
    "transactionNo": "106",
    "refundStatus": "FULL_REFUND"
    "tenantId": "1",
    "orderTime": "2025-03-31 08:00:00",
    "payTime": "2025-03-31 08:00:00",
    "customerId": "279f5b07f69749a29736c857abd1d7c0",
 
    "orderPrice": 6223.42,
    "discountPrice": 0,
    "payPrice": 6223.42,
    "orderRemark": "velit qui Duis",
    "orderVerifyCode": "7489465",
    "integralRatio": 20,
    "items": [
        {
            "itemOrderType": "BILLING",
            "type": "PROJECT",
            "dataId": "347692090710294532",
            "name": "不治疗项目",
            "originUnitPrice": 1000,
            "unitPrice": 500,
            "num": 2,
            "orderItemPrice": 2000,
            "orderItemDiscountPrice": 1000,
            "orderItemPayPrice": 1000,
        },
        {
            "itemOrderType": "BILLING",
            "type": "PROJECT",
            "dataId": "310065629354786820",
            "name": "水光光-AD",
            "originUnitPrice": 200,
            "unitPrice": 200,
            "num": 1,
            "orderItemPrice": 200,
            "orderItemDiscountPrice": 0,
            "orderItemPayPrice": 200,
        },
        {
            "itemOrderType": "BILLING",
            "type": "YEAR_CARD",
            "dataId": "ea9ea39f09a705b365ae5ab9c0575241",
            "name": "规范",
            "originUnitPrice": 100.01,
            "unitPrice": 100.01,
            "num": 1,
            "orderItemPrice": 100.01,
            "orderItemDiscountPrice": 0,
            "orderItemPayPrice": 100.01,
            "subItems": [
                {
                    "itemUniqueId": "206366147669393409",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "cf1752dc18fb4467832a9db2f3377c0f",
                    "name": "分潜伏期",
                    "originUnitPrice": 100,
                    "unitPrice": 100,
                    "num": 1,
                    "orderItemPrice": 100,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 100,
                },
                {
                    "itemUniqueId": "206366147669393666",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "f3023c0182fb423484278a8e56afa765",
                    "name": "一分项目",
                    "originUnitPrice": 0.01,
                    "unitPrice": 0.01,
                    "num": 1,
                    "orderItemPrice": 0.01,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 0.01,
                },
            ]
        },
        {
            "itemOrderType": "BILLING",
            "type": "TIME_CARD",
            "dataId": "264072075818303490",
            "name": "次卡日志",
            "originUnitPrice": 4700,
            "unitPrice": 4700,
            "num": 1,
            "orderItemPrice": 4700,
            "orderItemDiscountPrice": 0,
            "orderItemPayPrice": 4700,
            "subItems": [
                {
                    "itemUniqueId": "270152345935937541",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "257827290480640001",
                    "name": "保妥适-max",
                    "originUnitPrice": 600,
                    "unitPrice": 600,
                    "num": 1,
                    "orderItemPrice": 600,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 600,
                },
                {
                    "itemUniqueId": "270152345935937797",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "257896522862034950",
                    "name": "肉毒素-项目-0001",
                    "originUnitPrice": 4000,
                    "unitPrice": 4000,
                    "num": 1,
                    "orderItemPrice": 4000,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 4000,
                },
                {
                    "itemUniqueId": "270152345935938051",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "257829715895648261",
                    "name": "保妥适-max-001",
                    "originUnitPrice": 100,
                    "unitPrice": 100,
                    "num": 1,
                    "orderItemPrice": 100,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 100,
                },
            ]
        },
        {
            "itemOrderType": "BILLING",
            "type": "PACKAGES",
            "dataId": "285728816804921349",
            "name": "会员套餐不要动",
            "originUnitPrice": 223.41,
            "unitPrice": 223.41,
            "num": 1,
            "orderItemPrice": 223.41,
            "orderItemDiscountPrice": 0,
            "orderItemPayPrice": 223.41,
            "subItems": [
                {
                    "itemUniqueId": "285728816955916289",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "269879089358176257",
                    "name": "测试很多次哈哈哈",
                    "originUnitPrice": 0.6,
                    "unitPrice": 0.6,
                    "num": 1,
                    "orderItemPrice": 0.6,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 0.6,
                },
                {
                    "itemUniqueId": "285821479998717956",
                    "itemOrderType": "BILLING",
                    "type": "PROJECT",
                    "dataId": "269875843822518273",
                    "name": "测试商城管理Casablanca",
                    "originUnitPrice": 0.6,
                    "unitPrice": 0.6,
                    "num": 1,
                    "orderItemPrice": 0.6,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 0.6,
                },
                {
                    "itemUniqueId": "348470352415817730",
                    "itemOrderType": "BILLING",
                    "type": "PACKAGES",
                    "dataId": "285728816804921349",
                    "name": "会员套餐不要动",
                    "originUnitPrice": 223.41,
                    "unitPrice": 1.2,
                    "num": 1,
                    "orderItemPrice": 1.2,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 1.2,
                    "subItems": [
                        {
                            "itemUniqueId": "348470352436789248",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "269879089358176257",
                            "name": "测试很多次哈哈哈",
                            "originUnitPrice": 0.6,
                            "unitPrice": 0.6,
                            "num": 1,
                            "orderItemPrice": 0.6,
                            "orderItemDiscountPrice": 0,
                            "orderItemPayPrice": 0.6,
                        },
                        {
                            "itemUniqueId": "348470352436789504",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "269875843822518273",
                            "name": "测试商城管理Casablanca",
                            "originUnitPrice": 0.6,
                            "unitPrice": 0.6,
                            "num": 1,
                            "orderItemPrice": 0.6,
                            "orderItemDiscountPrice": 0,
                            "orderItemPayPrice": 0.6,
                        }
                    ]
                },
                {
                    "itemUniqueId": "348470352436789761",
                    "itemOrderType": "BILLING",
                    "type": "YEAR_CARD",
                    "dataId": "c31c91807b1c730e1d9c4c64fc370eb7",
                    "name": "20000",
                    "originUnitPrice": 210.01,
                    "unitPrice": 210.01,
                    "num": 1,
                    "orderItemPrice": 210.01,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 210.01,
                    "subItems": [
                        {
                            "itemUniqueId": "348470352436790021",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "f3023c0182fb423484278a8e56afa765",
                            "name": "一分项目",
                            "originUnitPrice": 0.01,
                            "unitPrice": 0.01,
                            "num": 1,
                            "orderItemPrice": 0.01,
                            "orderItemDiscountPrice": 0,
                            "orderItemPayPrice": 0.01,
                        },
                        {
                            "itemUniqueId": "348470352436790274",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "4079931ed2c44a25a0325fbe1a433992",
                            "name": "爱少女风1爱少女风1爱少女风1爱少女风1爱少女风1爱少女风1爱少女风1爱少女风1vv",
                            "originUnitPrice": 210,
                            "unitPrice": 210,
                            "num": 1,
                            "orderItemPrice": 210,
                            "orderItemDiscountPrice": 0,
                            "orderItemPayPrice": 210,
                        }
                    ]
                },
                {
                    "itemUniqueId": "348470352436790528",
                    "itemOrderType": "BILLING",
                    "type": "TIME_CARD",
                    "dataId": "256444712196505600",
                    "name": "不可转赠03",
                    "originUnitPrice": 11,
                    "unitPrice": 11,
                    "num": 1,
                    "orderItemPrice": 11,
                    "orderItemDiscountPrice": 0,
                    "orderItemPayPrice": 11,
                    "subItems": [
                        {
                            "itemUniqueId": "348470352436790788",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "251349420140920834",
                            "name": "种草项目",
                            "originUnitPrice": 1,
                            "unitPrice": 1,
                            "num": 2,
                            "orderItemPrice": 2,
                            "orderItemDiscountPrice": 1,
                            "orderItemPayPrice": 1,
                        },
                        {
                            "itemUniqueId": "348470352436791046",
                            "itemOrderType": "BILLING",
                            "type": "PROJECT",
                            "dataId": "248807782193561604",
                            "name": "AD钙项目",
                            "originUnitPrice": 10,
                            "unitPrice": 10,
                            "num": 2,
                            "orderItemPrice": 20,
                            "orderItemDiscountPrice": 10,
                            "orderItemPayPrice": 10,
                        }
                    ]
                },
            ]
        },
    ],
    "payItems": [
        {
            "amount": 1,
            "payWayId": "virtual_card_pay_id",
            "payWayName": "卡券",
            "sameAmountValue": 20,
            "payWayDetailType": "VIRTUAL_CARD_PAY"
        },
        {
            "amount": 20,
            "payWayId": "其他虚拟金",
            "payWayName": "其他虚拟金",
            "payWayDetailType": "VIRTUAL_OTHER_PAY"
        },
        {
            "amount": 7.45,
            "payWayId": "储值",
            "payWayName": "储值",
            "payWayDetailType": "ACTUAL_BALANCE_PAY"
        },
        {
            "amount": 2.55,
            "payWayId": "储值赠送",
            "payWayName": "储值赠送",
            "payWayDetailType": "VIRTUAL_BALANCE_GIVE_PAY"
        },
        {
            "amount": 10,
            "payWayId": "8b0de8636243466998078ca29593d1e4",
            "payWayName": "定金",
            "payWayDetailType": "ACTUAL_DEPOSIT_PAY"
        },
        {
            "amount": 10,
            "payWayId": "9cbe4bbdbe8d434389b7f6a316d625e0",
            "payWayName": "权益卡本金",
            "payWayDetailType": "ACTUAL_EQUITY_PAY"
        },
        {
            "amount": 6162.42,
            "payWayId": "ALIPAY",
            "payWayName": "支付宝",
            "payWayDetailType": "ACTUAL_OTHER_PAY"
        },
        {
            "amount": 10,
            "payWayId": "WECHAT",
            "payWayName": "微信",
            "payWayDetailType": "ACTUAL_OTHER_PAY"
        }
    ]
}
```

返回参数：

```json
{
    "code": 10000,
    "data": {
        "orderId": "350323538491604998"
    },
    "msg": "操作成功"
}
```

## 对接三方小程序三方订单项退款 

（目前只支持三方订单的订单项全退（用于对接四川娇点），暂时没时间完善部分订单项退款和核销部分。）

- 请求URL（需要tpos鉴权）

**POST /api/v1/tpos/order/refund-order-external-item**

- 参数说明

<sheet sheet-id="cs2DIb" token="shtcnTKOlDjgLChPQvGBfiOv2Eg"></sheet>

- 返回结果

code是10000表示成功，其他全视为失败，失败会在msg放置失败消息

- 请求示例：

请求参数：

```json
{
    "tenantId": "1",
    "customerId": "279f5b07f69749a29736c857abd1d7c0",
    "transactionNo": "003",
    "remark": "测试订单项退款",
    "items": [
        {
            "thirdOrderItemId": "idt",
            "num": 1,
            "amount": 1000
        },
        {
            "thirdOrderItemId": "idt55",
            "num": 1,
            "amount": 100,
            "subItems": [
                {
                    "thirdOrderItemId": "idt56",
                    "num": 2,
                    "amount": 50,
                },
                {
                    "thirdOrderItemId": "idt57",
                    "num": 1,
                    "amount": 50,
                }
            ]
        }
    ],
    "applyTime": "2025-06-03 12:13:30",
    "actualOperationTime": "2025-06-03 00:12:12"
}
```

返回参数：

```json
{
    "code": 10000,
    "data": {
        "orderRecordId": "370935836683796486"
    },
    "msg": "操作成功"
}
```



## 查询客户订单消费记录

- 请求URL（需要tpos鉴权）

**接口地址**:**/api/v1/tpos/order/get-customer-billing-list    POST**

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
|   consumptionType |   <br/>*类别 0-项目  1-套餐 2-商品 3-药品 4-年卡 5-次卡* | false | integer |
|   customerId |  | true | string |
|   startTime | 开始时间 | false | string(date-time) |
|   endTime | 结束时间 | false | string(date-time) |
|   isGive | 仅赠送 | false | boolean |
|   performFlag | 仅业绩项目 | false | boolean |
|   page | 页码 | true | integer(int64) |
|   size | 每页数量 | true | integer(int64) |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | OrderPaymentPage | OrderPaymentPage |
|   current |  | integer(int64) | page(页码) |
|   records |  | array | 订单消费 |
|             nearOperateTenantName | 最近操作门店 | string |  |
|             tenantName | 开单门店 | string |  |
|             feeProp | 消费性质 | string |  |
|             consumptionTimeStr | 开单时间 | string |  |
|             consumptionTypeName | 类别名称 | string |  |
|             billingPropertyType | 门诊住院类型  <br/>（0-门诊订单，1-住院订单） | integer |  |
|             consumptionContent | 项目内容 | string |  |
|             remark | 开单项目备注 | string |  |
|             cardList | 卡券使用详情(是否使用卡券) | array |  |
|               cardName | 卡券名称 | string |  |
|               cardApplyReason | 发送卡券原因 | string |  |
|             typeRemarkFormBean | 状态 | string |  |
|             departmentName | 计划治疗科室 | string |  |
|             doctorName | 计划治疗医生 | string |  |
|             unitPrice | 单价 | number |  |
|             numberOfTime | 数量 | number |  |
|             numOfRestTime | 剩余数量 | number |  |
|             discount | 折扣 | number |  |
|             totalPrice | 开单总价 | number |  |
|             virtualGold | 虚拟金 | number |  |
|             receivedMoney | 实际消费 | number |  |
|             consumerCustomerTypeName | 消费时客户类型 | string |  |
|             courseDetailPrice | 补疗程 | number |  |
|             chargeTime | 收费日期 | long(时间戳) |  |
|             dealWithMoney | 订单金额（应付） | number |  |
|             alreadyMoney | 订单金额（已付） | number |  |
|             billingTotalRefundMoney | 退费 | number |  |
|             billingTotalDonationMoney | 转赠 | number |  |
|             billingTotalTransferMoney | 转项 | number |  |
|             dataSource | 订单来源  <br/>0：院内;  <br/>1：系统小程序;  <br/>2：app; | integer |  |
|             billingUserName | 订单开单人 | string |  |
|             sysAssistantList | 协助开单人 | array |  |
|               assistantId | 协助人id | string |  |
|               assistantName | 协助人姓名 | string |  |
|               mark |  第一（first），第二（second） | string |  |
|             billingRemark | 订单备注 | string |  |
|             labelList | 业绩标签 | array |  |
|               id | 标签id | string |  |
|               name | 标签名称 | string |  |
|   size |  | integer(int64) | 分页数量 |
|   total |  | integer(int64) | 总数 |
| msg | 响应消息 | string |  |

## 查询收银记录

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/get-cashierRecord-list    POST**

- 参数说明

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
|   current | *当前页* | true | integer |
|    limit | *每页显示条数* | true | integer |
|   customerInfo | *客人信息(电话或姓名)* |  | string |
| chargeType | *收费类型* |  | List<Integer> |
| payWay | *支付方式 枚举value* |  | List<String> |
| notInPayWay | *支付方式 - 不包含此列的支付方式查询  枚举value* |  | List<String> |
| chargeUserIds | *收费员ids* |  | List<String> |
| *billingUserIds* | *订单开单人ids* |  | List<String> |
| paymentNo | *费用单号 - 模糊匹配* |  | String |
| startTime | *收费开始时间* |  | yyyy-MM-dd HH:mm:ss |
| endTime | *收费结束时间* |  | yyyy-MM-dd HH:mm:ss |
| actualRecordedStartTime | *实际入账开始时间* |  | yyyy-MM-dd HH:mm:ss |
| actualRecordedEndTime | *实际入账结束时间* |  | yyyy-MM-dd HH:mm:ss |
| billingStartTime | *开单开始时间* |  | yyyy-MM-dd HH:mm:ss |
| billingEndTime | *开单结束时间* |  | yyyy-MM-dd HH:mm:ss |
|  |  |  |  |

- 返回结果



- 返回示例

```JSON
{
    "code": 10000,
    "data": {
        "result": [
            {
                "date": "2025-07-16",
                "paymentItemNames": "【项目】水光光-AD",
                "autoFlag": false,
                "billingId": "07eb194eeb084a2ab3097cac2db5d318",
                "originBillingUserId": "915928121d976dbd6579ab98be6f5d9c",
                "refundTotalNum": 398,
                "refundTotalAmount": -568865.56,
                "payWay": [
                    200.0,0
                ],
                "receptionId": "386521967542403072",
                "type": "订单收费",
                "4@@@!!!@@@定金": null,
                "8@@@!!!@@@儲值赠送": null,
                "preUserName": "测试茹",
                "24@@@!!!@@@权益卡儲值": null,
                "feeBillingUser": "明月（测试）",
                "serviceBillingUserId": "915928121d976dbd6579ab98be6f5d9c",
                "chargeTotalNum": 6486,
                "paymentId": "3e3af1555367404fb819582ac4dff1ef",
                "payMark": 0,
                "chargeUser": "明月（测试）",
                "invoiceNo": null,
                "cusTenantName": "门店1",
                "billingAssistantUser": "",
                "cashRefundTotalAmount": -46822.51,
                "autoFlagDesc": "手动",
                "payWayJson": [
                    {
                        "payMoney": 200.0,
                        "payMode": "test",
                        "payModeName": "test"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "JTXFDFS",
                        "payModeName": "集团下发的方式"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "企业微信",
                        "payModeName": "企业微信"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "WECHAT",
                        "payModeName": "微信"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "qudao",
                        "payModeName": "渠道"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "ALIPAY",
                        "payModeName": "支付宝"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "DEFAULT_MINIPARAM_WECHAT",
                        "payModeName": "微信小程序支付"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "UNIONPAY",
                        "payModeName": "银联"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "CASH",
                        "payModeName": "现金"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "A_LIJIANKANG",
                        "payModeName": "阿里健康"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "MEITUAN",
                        "payModeName": "美团/点评"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "DAZHONGDIANPING",
                        "payModeName": "大众点评"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "ZHONGGUOYINHANG",
                        "payModeName": "中国银行"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "BRUSHCARD",
                        "payModeName": "刷卡"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "PINXIXI",
                        "payModeName": "拼夕夕"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "YouZanPay",
                        "payModeName": "有贊支付"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "ARRCEN_PAY",
                        "payModeName": "九阵支付"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "weiMoOnlinePay",
                        "payModeName": "微盟智慧零售在线支付"
                    }
                ],
                "test": 200.0,
                "realBillingUserId": "915928121d976dbd6579ab98be6f5d9c",
                "dataSourceStr": "客户端",
                "chargeTime": 1752646852000,
                "actualRefundMoney": 0.00,
                "noCashRefundTotalAmount": -522043.05,
                "customerName": "王林化神",
                "paymentNo": "JF202507161420429470",
                "sourceType": 1,
                "16@@@!!!@@@积分": null,
                "dataSource": 0,
                "exclusiveServerName": "",
                "sourcePathName": "市場渠道/拍讯问题/动不了",
                "17@@@!!!@@@限定儲值": null,
                "sysAssistantList": null,
                "customerPhone": "784125",
                "total": 200.00,
                "7@@@!!!@@@儲值": null,
                "counselor": null,
                "billingType": 1,
                "customerId": "3607cbfdd6034b4ca2ee8d5905f10d85",
                "actualRecordedTime": 1752595200000,
                "brownSouthSystemSerialNumber": null,
                "9@@@!!!@@@卡券": null,
                "sysUserId": "",
                "shouldRefundMoney": 0.00,
                "totalNonActualReceive": 0,
                "cashChargeTotalAmount": 2657533.93,
                "noCashChargeTotalAmount": 8115420.82,
                "paymentRemark": null,
                "billingUser": "明月（测试）",
                "sex": "女",
                "billingTime": 1752646843000,
                "billingNo": "PT202507161420427560",
                "actualAndNonTotalAmount": 306053.60,
                "cusTenantId": "1",
                "25@@@!!!@@@权益卡赠送儲值": null,
                "cashierTotal": 200.00,
                "chargeTotalAmount": 10703437.75,
                "dateAndCustomerIdStr": "202507163607cbfdd6034b4ca2ee8d5905f10d85",
                "18@@@!!!@@@限定儲值赠送": null,
                "age": null,
                "vipNum": "153164",
                "isShared": true,
                "customer": "王林化神(784125)"
            },
            {
                "date": "2025-07-15",
                "paymentItemNames": "【项目】magic3",
                "autoFlag": false,
                "qudao": 10.0,
                "billingId": "b1423f159edd44fa9b109b67a79ce8bb",
                "originBillingUserId": "915928121d976dbd6579ab98be6f5d9c",
                "refundTotalNum": 398,
                "refundTotalAmount": -568865.56,
                "payWay": [
                    10.0,0
                ],
                "receptionId": "f92ed8ba91f7416aaec3f070b1594a6d",
                "type": "订单收费",
                "4@@@!!!@@@定金": null,
                "8@@@!!!@@@儲值赠送": null,
                "preUserName": "明月（测试）",
                "24@@@!!!@@@权益卡儲值": null,
                "feeBillingUser": "测试茹",
                "serviceBillingUserId": "915928121d976dbd6579ab98be6f5d9c",
                "chargeTotalNum": 6486,
                "paymentId": "26ea70a147dd4d819fcd3b21973cec35",
                "payMark": 0,
                "chargeUser": "测试茹",
                "invoiceNo": null,
                "cusTenantName": "门店1",
                "billingAssistantUser": "",
                "cashRefundTotalAmount": -46822.51,
                "autoFlagDesc": "手动",
                "payWayJson": [
                    {
                        "payMoney": 0,
                        "payMode": "test",
                        "payModeName": "test"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "JTXFDFS",
                        "payModeName": "集团下发的方式"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "企业微信",
                        "payModeName": "企业微信"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "WECHAT",
                        "payModeName": "微信"
                    },
                    {
                        "payMoney": 10.0,
                        "payMode": "qudao",
                        "payModeName": "渠道"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "ALIPAY",
                        "payModeName": "支付宝"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "DEFAULT_MINIPARAM_WECHAT",
                        "payModeName": "微信小程序支付"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "UNIONPAY",
                        "payModeName": "银联"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "CASH",
                        "payModeName": "现金"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "A_LIJIANKANG",
                        "payModeName": "阿里健康"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "MEITUAN",
                        "payModeName": "美团/点评"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "DAZHONGDIANPING",
                        "payModeName": "大众点评"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "ZHONGGUOYINHANG",
                        "payModeName": "中国银行"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "BRUSHCARD",
                        "payModeName": "刷卡"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "PINXIXI",
                        "payModeName": "拼夕夕"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "YouZanPay",
                        "payModeName": "有贊支付"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "ARRCEN_PAY",
                        "payModeName": "九阵支付"
                    },
                    {
                        "payMoney": 0,
                        "payMode": "weiMoOnlinePay",
                        "payModeName": "微盟智慧零售在线支付"
                    }
                ],
                "realBillingUserId": "915928121d976dbd6579ab98be6f5d9c",
                "dataSourceStr": "客户端",
                "chargeTime": 1752548950000,
                "actualRefundMoney": 0.00,
                "noCashRefundTotalAmount": -522043.05,
                "customerName": "测试报备22343",
                "paymentNo": "JF202507151109020040",
                "sourceType": 1,
                "16@@@!!!@@@积分": null,
                "dataSource": 0,
                "exclusiveServerName": "",
                "sourcePathName": "市場渠道/红盒/水岸东方",
                "17@@@!!!@@@限定儲值": null,
                "sysAssistantList": null,
                "customerPhone": "5124351435",
                "total": 10.00,
                "7@@@!!!@@@儲值": null,
                "counselor": "明月（测试）",
                "billingType": 1,
                "customerId": "351762824877309955",
                "actualRecordedTime": 1752508800000,
                "brownSouthSystemSerialNumber": null,
                "9@@@!!!@@@卡券": null,
                "sysUserId": "915928121d976dbd6579ab98be6f5d9c",
                "shouldRefundMoney": 0.00,
                "totalNonActualReceive": 0,
                "cashChargeTotalAmount": 2657533.93,
                "noCashChargeTotalAmount": 8115420.82,
                "paymentRemark": null,
                "billingUser": "明月（测试）",
                "sex": "女",
                "billingTime": 1752548899000,
                "billingNo": "PT202507151108193570",
                "actualAndNonTotalAmount": 306053.60,
                "cusTenantId": "1",
                "25@@@!!!@@@权益卡赠送儲值": null,
                "cashierTotal": 10.00,
                "chargeTotalAmount": 10703437.75,
                "dateAndCustomerIdStr": "20250715351762824877309955",
                "18@@@!!!@@@限定儲值赠送": null,
                "age": null,
                "vipNum": "153213",
                "isShared": true,
                "customer": "测试报备22343(5124351435)"
            }
        ],
        "virtualShowPayWays": [
            "4@@@!!!@@@定金",
            "7@@@!!!@@@儲值",
            "8@@@!!!@@@儲值赠送",
            "9@@@!!!@@@卡券",
            "15@@@!!!@@@chongzhi（）赠送",
            "15@@@!!!@@@九阵优惠",
            "15@@@!!!@@@值充赠送",
            "15@@@!!!@@@其他虚拟金",
            "15@@@!!!@@@微盟智慧零售积分抵扣",
            "15@@@!!!@@@测试",
            "15@@@!!!@@@测试类型",
            "15@@@!!!@@@美团",
            "16@@@!!!@@@积分",
            "17@@@!!!@@@限定儲值",
            "18@@@!!!@@@限定儲值赠送",
            "24@@@!!!@@@权益卡儲值",
            "25@@@!!!@@@权益卡赠送儲值"
        ],
        "total": 6884,
        "showPayWays": [
            "test",
            "JTXFDFS",
            "企业微信",
            "WECHAT",
            "qudao",
            "ALIPAY",
            "DEFAULT_MINIPARAM_WECHAT",
            "UNIONPAY",
            "CASH",
            "A_LIJIANKANG",
            "MEITUAN",
            "DAZHONGDIANPING",
            "ZHONGGUOYINHANG",
            "BRUSHCARD",
            "PINXIXI",
            "YouZanPay",
            "ARRCEN_PAY",
            "weiMoOnlinePay"
        ],
        "statisticsData": {
            "chargeTotalNum": 6486.0,
            "noCashChargeTotalAmount": 8115420.82,
            "refundTotalNum": 398.0,
            "chargeTotalAmount": 1.070343775E7,
            "refundTotalAmount": -568865.56,
            "noCashRefundTotalAmount": -522043.05,
            "actualAndNonTotalAmount": 11009491.35,
            "cashChargeTotalAmount": 2657533.93,
            "cashRefundTotalAmount": -46822.51
        },
        "totalVirtualPayWayMoney": {
            "4@@@!!!@@@定金": 0,
            "7@@@!!!@@@儲值": 0,
            "8@@@!!!@@@儲值赠送": 0,
            "9@@@!!!@@@卡券": 0,
            "15@@@!!!@@@chongzhi（）赠送": 0,
            "15@@@!!!@@@九阵优惠": 0,
            "15@@@!!!@@@值充赠送": 0,
            "15@@@!!!@@@其他虚拟金": 0,
            "15@@@!!!@@@微盟智慧零售积分抵扣": 0,
            "15@@@!!!@@@测试": 0,
            "15@@@!!!@@@测试类型": 0,
            "15@@@!!!@@@美团": 0,
            "16@@@!!!@@@积分": 0,
            "17@@@!!!@@@限定儲值": 0,
            "18@@@!!!@@@限定儲值赠送": 0,
            "24@@@!!!@@@权益卡儲值": 0,
            "25@@@!!!@@@权益卡赠送儲值": 0
        }
    },
    "msg": "操作成功"
}
```

## 收银时客户可用资产查询

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/get-customer-available-assets    POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| tenantId | 是 | string | 门店id |  |
| saleItemList | 是 | array | 收费项目 |  |
|     +id | 是 | string | 项目id/套餐id/商品id/年卡id/次卡id |  |
|     +projectDataType | 是 | int | 类型（0-项目，2-套餐，4-商品，6-年卡，8-次卡） |  |
|     +num | 是 | int | 数量 |  |
|     +totalPrice | 是 | decimal | 开单总价 |  |

- 返回结果

返回的可用卡券是线上订单可用的卡券

```JSON
{
    "code": 10000,
    "data": {
        "depositList": [  //可用定金
            {
                "id": "348daefb60214732bbc7709eef0eb3fd",//定金订单id
                "privateFlag": false, //是否是专用定金（true-专用定金）
                "subDepositAmount": 100,//保有金额（可用金额）
                "depositItemName": "多维全能光（面眼）",//定金项名称
                "projectIds": [  //定金适用范围的项目id数组
                    "457243502850342918" //项目id/套餐id/商品id/年卡id/次卡id
                ]
            }
        ],
        "balance": 100,  //储值本金余额
        "givenBalance": 10, //储值赠送余额
        "limitedBalance": 200, //限定储值本金余额
        "limitedGivenBalance": 20, //限定储值赠送余额
        "equityCardList": [ //可用权益卡
            {
                "id": "669bf83a89bd4f5fbc348e9bf4f4937b", //权益卡订单id
                "name": "桃花卡20241127", //权益卡名称
                "deductRule": 1, //抵扣规则（0-不限制，1-优先使用本金，2-按比例抵扣）
                "subMoney": 1000, //本金可用金额
                "subGivenMoney": 100, //赠送金额可用金额
                "disabledCardMoneyFlag": false, //本金是否禁用（true-禁用）
                "disabledCardMoneyTips": null, //本金禁用时的提示信息
                "disabledCardGivenMoneyFlag": true, //赠送金是否禁用（true-禁用）
                "disabledCardGivenMoneyTips": "该权益卡优先使用本金，本金还有剩余时，此权益卡的赠送金不可用" //赠送金禁用时的提示信息
            }
        ],
        "discountScore": 10, //x积分抵扣y元中的积分数量（例：discountScore = 10，discountMoney=1 则表示：10个积分抵扣1元）
        "discountMoney": 1, //x积分抵扣y元中的金额
        "scoreNum": 3580, //可用积分数量
        "discountRatio": 80, //积分最大抵扣比例（最大值100，例：订单金额为1000元，设置15%后，积分最多抵扣150元）
        "cardCouponList": [ //可用优惠券（这里只返回了线上订单可用的卡券）
            {
                "id": "488393799106560005",//客户卡券数据id
                "deductBillingMoney": 100, //抵扣的订单金额
                "activeStartDate": 1776873600000, //有效期起始时间
                "expireTime": 1780156800000, //有效期截止时间
                "title": "生日优惠券", //标题
                "cardType": 3, //卡券类型（1代金券，2折扣卷，3体验卷）
                "deductionAmount": null,//抵扣金额（卡券(代金券)定义的）
                "consumeAmount": null,//消费金额满多少可用(卡券定义的)
                "discount": null,//折扣率（卡券(折扣卷)定义的）
                "upperLimit": null,//优惠金额上限(卡券定义的)
                "applyProjectType": 1,//适用项目类型(1全部适用，2指定范围适用，3指定范围不适用，4部分适用，5部分不适应)
                "projectNameShow": "",//适用范围名称显示
                "useRule": "", //适用规则
                "tenantName": "门店9",//卡券所在门店名称
                "applyTenantName": "门店9",//适用门店
                "applyPartTypeList": [0,2],//部分适用/部分不适用(所有项目/商品/套餐/次卡/年卡(0/1/2/3/4))
                "allCustomerTypesAvailable": true, //否所有客户类型都可用(true-都可用)
                "applyCustomerTypeNamesDeserialized": ["初诊","复诊","老客人"] //允许使用的客户类型名称
            }
        ]
    },
    "msg": "操作成功"
}
```

## 客户资产抵扣

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/deduct-assets    POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| tenantId | 是 | string | 门店id |  |
| thirdOrderId | 是 | string | 三方订单id |  |
| payList | 是 | array | 抵扣信息 |  |
|     +paymentItemMark | 是 | int | 抵扣类型（4-定金，7-储值本金，8-储值赠送金，17-限定储值本金，18-限定储值赠送金，24-权益卡本金，25-权益卡赠送金，16-积分，9-优惠券） |  |
|     +businessId | 否 | string | 关联的客户资产数据id（定金/权益卡/优惠券时必填） |  |
|     +deductMoney | 是 | decimal | 抵扣金额 |  |
|     +deductScoreNum | 否 | int | 抵扣积分数量（积分时必填） |  |

- 返回结果

```Plain Text
{
    "code": 10000,
    "data": true, 
    "msg": "操作成功"
}
```

## 客户资产抵扣撤销接口

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/order/cancel-deduct-assets    POST**

- 参数说明

用于三方未核销订单（即未同步到睿美云的订单）整单退款

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| tenantId | 是 | string | 门店id |  |
| thirdOrderId | 是 | string | 三方订单id |  |

- 返回结果

```Plain Text
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

# 治疗（treat）

## [查询客户未治疗记录查询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#JCf3dw1txoRFvhxfsrgcvbzmn8b)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/untreated-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 否 | string | 客户id |  |
| phoneNumber | 否 | string | 客户电话号码 | 因为不同客户可能使用相同的电话号码，如果查询到多个客户，则随机选择第一个客户进行查询，所以强烈建议使用客户id进行查询 |
| billingTimeStart | 否 | datetime | 开单时间-开始时间 |  |
| billingTimeEnd | 否 | datetime | 开单时间-结束时间 |  |
| page | 否 | int | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数量 | 默认为：20，最大为：500 |

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 |  |  |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | TposTreatInfoDTO |
|     billFav | 开单优惠 | number |  |
|     billingDate | 开单日期 | string |  |
|     billingDepartmentId | 科室id | string |  |
|     billingDepartmentName | 科室名称 | string |  |
|     billingId | 订单id | string |  |
|             billingItemId | 订单项id | String |  |
|     billingProjectId | 项目id | string |  |
|     billingProjectName | 项目名称 | string |  |
|     billingTenantId | 所属门店id | string |  |
|     billingTenantName | 所属门店名称 | string |  |
|     billingUserId | 开单人id | string |  |
|     billingUserName | 开单人名称 | string |  |
|     dataSource | 订单来源 | string | 见顶部【订单来源枚举】  <br/>BillingDataSourceEnum |
|             treatPredefineId | 预治疗科室信息id | string |  |
|             itemDataId | 订单项目id | string |  |
|     doctorId | 医生id | string |  |
|     doctorName | 医生名称 | string |  |
|     downNum | 已治疗次数 | integer |  |
|     expiryDate | 有效期至 | string |  |
|     itemRemark | 开单项目备注 | string |  |
|     num | 总次数 | integer |  |
|             residueNum | 剩余次数 | integer |  |
|     owePrice | 欠费金额 | number |  |
|     paymentNo | 费用单号 | string |  |
|     projectAlias | 展示名称 | string |  |
|     sysAssistantList | 协助开单人 | array | 对外推送，系统协助人（协助开单人通用数据结构） |
|       assistantId | 协助人id | string |  |
|       assistantName | 协助人名称 | string |  |
|       id | 本身数据id | string |  |
|       mark | 协助人标志,first、second | string |  |
|     treatRemark | 备注 | string |  |
|     unitOrderPrice | 开单项的成交单价 | number |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |



## [查询客户已治疗记录查询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#ViR2d5bq2oHAAzxpNuFc9q6Znyb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/already-treated-page    GET**

- 参数说明

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><b>字段</b></td><td><b>是否必填</b></td><td><b>类型</b></td><td><b>说明</b></td><td><b>备注</b></td></tr><tr><td vertical-align="top">customerId</td><td vertical-align="top">否</td><td vertical-align="top">string</td><td vertical-align="top">客户id</td><td vertical-align="top">有客户Id则只用客户Id查询</td></tr><tr><td>phoneNumber</td><td>否</td><td>string</td><td>客户电话号码</td><td>没有客户id，只有传了电话号码，则通过电话号码查询客户，同时因为不同客户可能使用相同的电话号码，如果查询到多个客户，则随机选择第一个客户进行查询，所以强烈建议使用客户id进行查询</td></tr><tr><td vertical-align="top">treatTimeStart</td><td vertical-align="top">否</td><td vertical-align="top">datetime</td><td vertical-align="top">治疗时间-开始时间</td><td rowspan="2" vertical-align="top">如果客户Id和电话号码都没传，则开始和结束时间不能为空，用时间段查询</td></tr><tr><td vertical-align="top">treatTimeEnd</td><td vertical-align="top">否</td><td vertical-align="top">datetime</td><td vertical-align="top">治疗时间-结束时间</td></tr><tr><td vertical-align="top">page</td><td vertical-align="top">否</td><td vertical-align="top">int</td><td vertical-align="top">页码</td><td vertical-align="top">默认为：1，最小为：1</td></tr><tr><td vertical-align="top">size</td><td vertical-align="top">否</td><td vertical-align="top">int</td><td vertical-align="top">每页数量</td><td vertical-align="top">默认为：20，最大为：500</td></tr></tbody></table>

- 返回结果



| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 |  |  |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | TposTreatInfoDTO |
|     achievement | 已治疗 - 执行业绩 | number |  |
|     anesthesiaName | 麻醉方式描述 | string |  |
|     anesthesiaValue | 麻醉方式值 | string |  |
|     billFav | 开单优惠 | number |  |
|     billingDate | 开单日期 | string |  |
|     billingDepartmentId | 科室id | string |  |
|     billingDepartmentName | 科室名称 | string |  |
|     billingId | 订单id | string |  |
|             billingItemId | 订单项id | String |  |
|     billingItemTypeCategory | 订单项类型 | integer |  |
|     billingProjectId | 项目id | string |  |
|     billingProjectName | 项目名称 | string |  |
|     billingTenantId | 所属门店id | string |  |
|     billingTenantName | 所属门店名称 | string |  |
|     billingUserId | 开单人id | string |  |
|     billingUserName | 开单人名称 | string |  |
|     dataSource | 订单来源 | string | 见顶部【订单来源枚举】  <br/>BillingDataSourceEnum |
|     dealWith | 处置 | string |  |
|     deductRemark | 划扣说明 | string |  |
|     departmentId | 已治疗 - 科室id | string |  |
|     departmentName | 已治疗 - 科室名称 | string |  |
|     doctorId | 医生id | string | 计划治疗医生id |
|     doctorName | 医生名称 | string | 计划治疗医生名称 |
|     downNum | 已治疗次数 | integer |  |
|     expiryDate | 有效期至 | string |  |
|             id | *项目治疗记录id* | string |  |
|             itemDataId | 订单项目id | string |  |
|     itemRemark | 开单项目备注 | string |  |
|     num | 总次数 | integer |  |
|     otherDoctor | 已治疗 - 其他岗位信息 | array | 三方治疗，其他岗位信息DTO |
|       doctors | 处理人员名称 | string |  |
|       roleName | 岗位名称 | string |  |
|     owePrice | 欠费金额 | number |  |
|             packageBillingItemId | 上一级订单项id | string |  |
|             packageId | 套餐id | string |  |
|             packageName | 套餐名称 | string |  |
|     paymentNo | 费用单号 | string |  |
|     projectAlias | 展示名称 | string |  |
|     sysAssistantList | 协助开单人 | array | 对外推送，系统协助人（协助开单人通用数据结构） |
|       assistantId | 协助人id | string |  |
|       assistantName | 协助人名称 | string |  |
|       id | 本身数据id | string |  |
|       mark | 协助人标志,first、second | string |  |
|     tenantId | 已治疗，治疗门店id | string |  |
|     tenantName | 已治疗，治疗门店名称 | string |  |
|     treatContent | 治疗记录 | string |  |
|     treatCount | 已治疗 - 治疗次数 | integer |  |
|     treatDeviceList | 治疗设备参数 | array |  |
|       deviceCode | 设备名称（值） | string |  |
|       deviceName | 设备名称 | string |  |
|       parameterCode | 参数名（值） | string |  |
|       parameterName | 参数名（名称） | string |  |
|       unitCode | 单位（值） | string |  |
|       unitName | 单位（名称） | string |  |
|       actualValue | 值 | string |  |
|     treatParameter | 治疗参数 | string |  |
|     treatPosition | 已治疗 - 治疗部位 | string |  |
|             treatPredefineId | 预治疗科室信息id | string |  |
|             treatRecordId | 治疗记录id | string |  |
|     treatRemark | 治疗备注 | string |  |
|     treatmentNo | 已治疗 - 所属治疗单号 | string |  |
|     treatmentTime | 已治疗 - 治疗日期 | string |  |
|     unitOrderPrice | 开单项的成交单价 | number |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## [分页获取治疗数据](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#SYABdDaAmoaYjgxWNOHctzNinuv)



请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/treated-page-review   GET**

- 参数说明

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| customerId | 客户id | query | false | string |
| tenantId | 查询门店id | query | false | string |
| treatTimeEnd | 治疗时间-结束时间 | query | false | string(date-time) |
| treatTimeStart | 治疗时间-开始时间 | query | false | string(date-time) |
| deductFlag | 是否已划扣 | query | false | boolean |
| verifyFlag | 是否已核销 | query | false | boolean |
| page | 默认为：1，最小为：1 | query | false | integer(int32) |
| size | 默认为：20，最大为：500 | query | false | integer(int32) |

- 返回结果

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOf治疗记录 | IPageOf治疗记录 |
|   current | 当前页 | integer(int64) |  |
|   pages | 总页数 | integer(int64) |  |
|   records |  | array | 治疗记录 |
|     id | 治疗记录id | string |  |
|     customerId | 客户id | string |  |
|     customerName | 客户姓名 | string |  |
|     customerPhones | 客户电话信息 | array | 电话号码集合 |
|     deductFlag | 是否划扣 | boolean |  |
|     deductPostponeFlag | 划扣是否延期 | boolean |  |
|     deductRecordId | 划扣记录id | string |  |
|     deductRecordNo | 划扣记录号 | string |  |
|     deductTime | 划扣时间 | string |  |
|     deductUserName | 划扣用户姓名 | string |  |
|     projectList | 治疗项目信息 | array | 治疗项目信息 |
|       billingItemId |  | string |  |
|       billingItemName |  | string |  |
|       billingItemRemark |  | string |  |
|     signInfo | 签名信息 | string |  |
|     tenantId | 治疗门店 | string |  |
|     treatDeptId | 治疗部门id | string |  |
|     treatDeptName | 治疗部门名称 | string |  |
|     treatPostponeFlag | 治疗是否延期 | boolean |  |
|     treatRecordNo | 治疗记录号 | string |  |
|     treatmentTime | 就诊时间 | string |  |
|     verifyFlag | 是否核销 | boolean |  |
|     verifyPostponeFlag | 核销是否延期 | boolean |  |
|     verifyRecordNo | 核销记录单号 | string |  |
|     verifyStatus | 核销状态 | integer |  |
|     verifyTime | 核销时间 | string |  |
|     verifyUserName | 核销用户姓名 | string |  |
|   size | 每页的数量 | integer(int64) |  |
|   total | 总数 | integer(int64) |  |
| msg | 响应消息 | string |  |





**响应示例**:

```JavaScript
{
        "code": 10000,
        "data": {
                "current": 0,
                "pages": 0,
                "records": [
                        {
                                "customerId": "",
                                "customerName": "",
                                "customerPhones": [],
                                "deductFlag": true,
                                "deductPostponeFlag": true,
                                "deductRecordId": "",
                                "deductRecordNo": "",
                                "deductTime": "",
                                "deductUserName": "",
                                "id": "",
                                "projectList": [
                                        {
                                                "billingItemId": "",
                                                "billingItemName": "",
                                                "billingItemRemark": ""
                                        }
                                ],
                                "signInfo": "",
                                "tenantId": "",
                                "treatDeptId": "",
                                "treatDeptName": "",
                                "treatPostponeFlag": true,
                                "treatRecordNo": "",
                                "treatmentTime": "",
                                "verifyFlag": true,
                                "verifyPostponeFlag": true,
                                "verifyRecordNo": "",
                                "verifyStatus": 0,
                                "verifyTime": "",
                                "verifyUserName": ""
                        }
                ],
                "size": 0,
                "total": 0
        },
        "msg": ""
}
```







## [获取治疗时查询的手术间信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#RG4hd20fwokRQnxW8RHce4DinsO)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/get-operating-room-list    GET**

- 参数说明 

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| tenantId | 门店id | query | true | string |  |

- 返回结果

```JSON
{ 
"code": 10000,
    "data": [
        {
            "label": "UEX",
            "value": "af3569cd3f464b8b392f8778fd4fc961"
        },
        {
            "label": "UEXsdfa ",
            "value": "6984340a9fd0c632242a004e7089118e"
        },
        {
            "label": "SSD",
            "value": "166600f6b7fc5e54d08f577d8402d0d5"
        }
    ],
    "msg": "操作成功"
}
```

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | array |  |
|   label | label | string | 手术间名称 |
|   value | value | string | 手术间id |
| msg | 响应消息 | string |  |

## [获取治疗中和已治疗的数据](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#LmK2dKbIcojDVPxV0Ebc3WDPnAh)

数据场景：治疗详情中的数据

![图片展示了睿美云开放接口中治疗详情的数据获取界面。画面中以红色框突出显示了“已治疗(1)”部分，包含门类、项目、支付日期、支付金额、订单来源、治疗记录、治疗科室、主治疗人、参与人、治疗阶段、治疗记录、支付确认等信息。该图片与文档中获取治疗中和已治疗数据的上下文相关，直观呈现了获取已治疗数据时的展示样式，帮助理解数据获取后的呈现效果。](https://feishu.cn/file/G6QJbpowvoqOyBxkGq6cKmAcnxc)



- **请求URL（需要tpos鉴权）**

**/api/v1/tpos/treat/get-begin-treat-info    GET**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| billingItemId | 开单项id | query | true | string | 在获取已治疗和未治疗接口中获取 |

- 返回结果:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | array | 开始和已治疗数据 |
|   billingItemId | 订单项id | string |  |
|   deductFlag | 是否已划扣 | boolean |  |
|   tenantId | 所属门店Id | string |  |
|   tenantName | 所属门店 | string |  |
|   treatCount | 治疗次数 | integer(int32) |  |
|   treatProjectName | 治疗项目名称 | string |  |
|   treatRecordId | 治疗记录id | string |  |
|   verifyFlag | 是否已核销 | boolean |  |
|   verifyRecordId | 核销记录id | string |  |
|   verifyTime | 核销时间 | string |  |
| msg | 响应消息 | string |  |

**响应示例**:

```JSON
{
    "code": 10000,
    "data": [
        {
            "billingItemId": "",
            "deductFlag": true,
            "tenantId": "",
            "tenantName": "",
            "treatCount": 0,
            "treatProjectName": "",
            "treatRecordId": "",
            "updateDate": "",
            "verifyFlag": true,
            "verifyRecordId": "",
            "verifyTime": ""
        }
    ],
    "msg": "操作成功"
}
```



## [进行核销和划扣](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Q0ZvdVYvyo2KvGx4MjNc3eH0nFg)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/treat-deduct-verify    POST**

**接口描述：这个接口支持单独核销或划扣，也可以同时核销和划扣，只需要对应的deductFlag（划扣标识）和 verifyFlag（核销标识） 传true即可，取消核销或者划扣后，再次核销或者划扣还是调用这个接口**

- **请求参数**:

<table><colgroup><col/><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td></td><td>参数说明</td><td>请求类型</td><td>是否必须</td><td>数据类型</td><td>schema</td></tr><tr><td>deductAndVerifyPostDTO</td><td></td><td></td><td>body</td><td>true</td><td>核销划扣的请求参数</td><td>核销划扣的请求参数</td></tr><tr><td>  anesthesiaValue</td><td></td><td>麻醉code</td><td></td><td>false</td><td>string</td><td>通过查询字典数据获取 - <br/>code :anesthesia <br/>https://f1ufsuw9mx.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#SosIdyocSoEe8KxCf6tcnJJNnib</td></tr><tr><td>  dealWith</td><td></td><td>处置</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  deductDeptId</td><td></td><td>划扣科室id</td><td></td><td>false（当deductFlag是true，必填）</td><td>string</td><td></td></tr><tr><td>  deductRemark</td><td></td><td>划扣说明</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  deductUserId</td><td></td><td>划扣人id</td><td></td><td>false（当deductFlag是true，必填）</td><td>string</td><td></td></tr><tr><td>  deductUserName</td><td></td><td>划扣人姓名</td><td></td><td>false（当deductFlag是true，必填）</td><td>string</td><td></td></tr><tr><td>  injectionSiteVoList</td><td></td><td>治疗部位</td><td></td><td>false</td><td>array</td><td>InjectionSiteVo</td></tr><tr><td>    </td><td>value</td><td>字典对应的value</td><td></td><td>false</td><td>string</td><td>通过查询字典数据获取 - <br/>code :injectionSite<br/>https://f1ufsuw9mx.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#SosIdyocSoEe8KxCf6tcnJJNnib</td></tr><tr><td>  operateId</td><td></td><td>操作人id</td><td></td><td>true</td><td>string</td><td></td></tr><tr><td>  tenantId</td><td></td><td>治疗门店</td><td></td><td>true</td><td>string</td><td></td></tr><tr><td>  treatContent</td><td></td><td>治疗记录</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  treatDeptId</td><td></td><td>治疗科室id</td><td></td><td>true</td><td>string</td><td></td></tr><tr><td>  treatDeviceList</td><td></td><td>设备参数</td><td></td><td>false</td><td>array</td><td>治疗设备<br/>通过查询字典数据获取 - <br/>治疗设备名称<br/>code :treatDeviceName<br/>治疗设备参数<br/>code:treatDeviceParameter<br/>https://f1ufsuw9mx.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#SosIdyocSoEe8KxCf6tcnJJNnib</td></tr><tr><td>    </td><td>actualValue</td><td>值</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>deviceCode</td><td>设备名称（值）</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>deviceName</td><td>设备名称</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>id</td><td>数据Id</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>parameterCode</td><td>参数名（值）</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>   </td><td>parameterName</td><td>参数名（名称）</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>treatRecordId</td><td>治疗记录id</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>unitCode</td><td>单位（值）</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>unitName</td><td>单位（名称）</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  treatDoctorList</td><td></td><td>参与人</td><td></td><td>true</td><td>array</td><td>治疗参与人</td></tr><tr><td>    </td><td>doctorId</td><td>医生人id</td><td>用户id</td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>leadTreatFlag</td><td>是否是主导治疗</td><td></td><td>false</td><td>boolean</td><td></td></tr><tr><td>    </td><td>roleId</td><td>岗位id</td><td>医生和岗位需要对应<br/><b>假如岗位是”医生“，这个字段给空字符串：""</b></td><td>false</td><td>string</td><td><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite><br/>请从上面的接口获取配置的治疗岗位id（roleId）</td></tr><tr><td>    </td><td>roleName</td><td>岗位名称</td><td><b>假如岗位是”医生“，这个字段需要填写：”医生”，其他的岗位这个字段非必填</b></td><td>false</td><td>string</td><td></td></tr><tr><td>  treatParameter</td><td></td><td>治疗参数</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  deductFlag</td><td></td><td>是否划扣</td><td></td><td>true</td><td>boolean</td><td></td></tr><tr><td>  treatPredefineList</td><td></td><td>划扣信息</td><td>（当deductFlag是true，必填）</td><td>false</td><td>array</td><td>治疗划扣信息</td></tr><tr><td>    </td><td>billingItemId</td><td>订单项id</td><td>（当deductFlag是true，必填）</td><td>true</td><td>string</td><td></td></tr><tr><td>    </td><td>itemDataId</td><td>项目ID</td><td>（当deductFlag是true，必填）</td><td>true</td><td>string</td><td></td></tr><tr><td>    </td><td>treatCount</td><td>治疗次数</td><td>（当deductFlag是true，必填）</td><td>true</td><td>integer</td><td></td></tr><tr><td>    </td><td>treatPredefineId</td><td>治疗预计划科室信息id，<a href="https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#JCf3dw1txoRFvhxfsrgcvbzmn8b">通过接口获取值</a></td><td>（当deductFlag是true，必填）</td><td>true</td><td>string</td><td></td></tr><tr><td>treatRecordId</td><td></td><td>治疗记录id</td><td>当治疗已经开始治疗的数据时（取消划扣或者核销的数据），必填<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite><br/></td><td>false</td><td>string</td><td></td></tr><tr><td>   treatmentTime</td><td></td><td>治疗时间</td><td>（当deductFlag是true，必填）</td><td>false</td><td>string(date-time)<br/>yyyy-MM-dd HH:mm:ss</td><td></td></tr><tr><td> verifyDeptId</td><td></td><td>核销科室id</td><td>（当verifyFlag是true，必填）</td><td>false</td><td>string</td><td></td></tr><tr><td>  verifyFlag</td><td></td><td>是否核销</td><td></td><td>ture</td><td>boolean</td><td></td></tr><tr><td>  verifyMaterials</td><td></td><td>核销物品</td><td>（当verifyFlag是true，必填）</td><td>false</td><td>array</td><td>核销物料</td></tr><tr><td>    </td><td>materialId</td><td>物品id</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>    </td><td>materialUnit</td><td>划扣物品单位(值)</td><td></td><td>false</td><td>string</td><td>物料单位：通过调用字典接口获取。<br/>code:materialUnit<br/><br/>https://f1ufsuw9mx.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#SosIdyocSoEe8KxCf6tcnJJNnib</td></tr><tr><td>    </td><td>verifyNumber</td><td>核销数量</td><td></td><td>false</td><td>number</td><td></td></tr><tr><td>    </td><td>warehouseId</td><td>核销仓库id</td><td></td><td>false</td><td>string</td><td>通过调用</td></tr><tr><td>  verifyRemark</td><td></td><td>核销说明</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  verifyUserId</td><td></td><td>核销人id</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>  verifyUserName</td><td></td><td>核销人姓名</td><td></td><td>false</td><td>string</td><td></td></tr><tr><td>      assetPassword</td><td></td><td>资产变更密码</td><td></td><td>false</td><td>String</td><td></td></tr><tr><td>      assetChangeModeEnum</td><td></td><td>资产变更类型</td><td>当需要资产变更时，必传<br/>（"<em>SHORT_MESSAGE</em>":短信；<br/>"<em>APPLETS</em>"：小程序；<br/>"<em>PASSWORD</em>":密码）</td><td>false</td><td>String</td><td></td></tr><tr><td>      assetSmsCode</td><td></td><td>资产变更短信验证码</td><td></td><td>false</td><td>String</td><td></td></tr></tbody></table>

请求示例：

```JSON
{
    "treatmentTime": "2024-04-22 14:44:15",
    "injectionSiteVoList": [
        {
            "value": "0"
        },
        {
            "value": "1"
        }
    ],
    "dealWith": "接口3",
    "treatParameter": "接口2",
    "treatContent": "接口1",
    "verifyDeptId": "21de3d97e41551fed57cf96553978b23",
    "verifyUserId": "3183cbe2e1c64c1a25459e303d2b48e2",
    "verifyMaterials": [
        {
            "materialId": "211872640644677634",
            "verifyNumber": 1,
            "materialUnit": "82",
            "warehouseId": "211866598619742210"
        },
        {
            "materialId": "211872647917600768",
            "verifyNumber": 1,
            "materialUnit": "82",
            "warehouseId": "211866598619742210"
        }
    ],
    "deductRemark": "接口eqwe",
    "deductUserId": "3183cbe2e1c64c1a25459e303d2b48e2",
    "deductDeptId": "21de3d97e41551fed57cf96553978b23",
    "treatDeviceList": [
        {
            "deviceCode": "1",
            "deviceName": "萊西爾",
            "parameterCode": "0",
            "parameterName": "能量",
            "unitCode": "",
            "unitName": "",
            "actualValue": "测试",
            "key": 1
        }
    ],
    "treatPredefineList": [
        {
            "treatPredefineId": "95c3399eb24348d9970ffa6aac5806ad",
            "billingItemId": "8f9f396e934c4e3698123d55d94c0ce3",
            "itemDataId": "b6d1f5128b5f4da08433c2e126bd62c1",
            "treatCount": 1
        }
    ],
    "treatDoctorList": [
        {
            "roleName": "医生",
            "roleId": "",
            "doctorId": "5d28afbe69da47a8ad38534abd2033bc",
            "leadTreatFlag": true
        },
        {
            "roleId": "16ceefcd217e4684ab185664987386d9",
            "doctorId": "5233a6d1124eec029ba621060f7b4f7e",
            "leadTreatFlag": false
        }
    ],
    "treatDeptId": "211865618637389826",
    "anesthesiaValue": "0",
    "tenantId": "1",
    "operateId": "3183cbe2e1c64c1a25459e303d2b48e2",
    "assetPassword": "123456"
}
```





- **返回结果:**

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | 销划扣返回数据 | 销划扣返回数据 |
|   treatRecordId | 治疗记录id | string |  |
| msg | 响应消息 | string |  |

```JSON
{
    "code": 10000,
    "data": {
        "treatRecordId": ""
    },
    "msg": "操作成功"
}
```

## [取消划扣](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#DCGxddJfeot2b2xeIMLcWWGMnwj)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/cancel-deduct   POST**

- **请求参数:**

```JSON
{
    "operateId": "",
    "tenantId": "",
    "treatRecordId": ""
}
```

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td><td>备注</td></tr><tr><td>  operateId</td><td>操作人id</td><td>true</td><td>string</td><td></td></tr><tr><td>  tenantId</td><td>治疗门店id</td><td>true</td><td>string</td><td></td></tr><tr><td>  treatRecordId</td><td>治疗记录id</td><td>true</td><td>string</td><td><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite><br/>从这里获取治疗记录id</td></tr></tbody></table>

- **返回结果:**

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | boolean |
| msg | 响应消息 | string |

**响应示例**:

```JSON
{
        "code": 10000,
        "data": true,
        "msg": "操作成功"
}
```

## [取消核销](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#MEshdKzVzoqZHVxmUAFcXKDMnmf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/cancel-verify   POST**

- **请求参数:**

```JSON
{
    "operateId": "",
    "tenantId": "",
    "treatRecordId": "",
    "verifyRecordId": ""
}
```

**参数说明**:

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td><td>备注</td></tr><tr><td>  operateId</td><td>操作人id</td><td>true</td><td>string</td><td></td></tr><tr><td>  tenantId</td><td>治疗门店</td><td>true</td><td>string</td><td></td></tr><tr><td>  treatRecordId</td><td>治疗记录id</td><td>true</td><td>string</td><td><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite><br/>从这里获取治疗记录id</td></tr><tr><td>  verifyRecordId</td><td>划扣记录id</td><td>true</td><td>string</td><td><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite><br/>从这里获取划扣记录id</td></tr></tbody></table>

- **返回结果:**

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | boolean |
| msg | 响应消息 | string |

**响应示例**:

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

## [已治疗的核销和划扣详情信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#STSbdbfMHozgGZxdVGsckTqznae)

请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/get-treated-deduct-and-verify-detail  `GET`**

- **请求参数:**

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| tenantId | 治疗门店id | query | true | string |
| treatRecordId | 治疗记录id | query | true | string |

- **返回结果:**

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | 三方请求已治疗的划扣和核销信息 | 三方请求已治疗的划扣和核销信息 |
|   boneAgeReport | 骨龄报告 | string |  |
|   treatList | 治疗项目信息 | array | 治疗项目记录 |
|     billingId | 订单id | string |  |
|     billingItemId | 开单项目id | string |  |
|     billingItemName | 订单项目id | string |  |
|     billingNo | 订单号 | string |  |
|     billingTime | 开单时间 | string |  |
|     billingUserId | 开单人id | string |  |
|     billingUserName | 开单人姓名 | string |  |
|     canNotLimitDeduct | 是否可以无限划扣 | boolean |  |
|     crossHospitalFlag | 是否跨院治疗 | boolean |  |
|     customerId | 治疗客户id | string |  |
|     departmentId | 计划科室id | string |  |
|     departmentName | 计划科室名称 | string |  |
|     discountPrice | 开单优惠金额 | number |  |
|     doctorId | 计划医生id | string |  |
|     doctorName | 计划医生姓名 | string |  |
|     finishFlag | 是否完成治疗 | boolean |  |
|     freeFlag | 是否是赠送订单 | boolean |  |
|     itemDataId | 治疗项目id | string |  |
|     medicalRecordId | 病历id | string |  |
|     noCancelDeductCount | 未失效的已划扣数量 | integer |  |
|     noDeductVerifyCount | 未划扣已核销的数量 | integer |  |
|     numberOfTime | 开单总数 | integer |  |
|     orderVerifyTenant | 小程序订单核销门店id | string |  |
|     projectAlias | 项目别名 | string |  |
|     residueNoStartNum | 剩余未开始治疗数量(未失效的) | integer |  |
|     residueNum | 剩余数 | integer |  |
|     signInfo | 签名信息 | string |  |
|     totalNum | 总数 | integer |  |
|     totalPrice | 成交总价 | number |  |
|     treatCount | 治疗（划扣）次数 | integer |  |
|     treatPredefineId | 预治疗科室id | string |  |
|     treatRecordItemId | 治疗项id | string |  |
|     unitOrderPrice | 成交单价 | number |  |
|             arrearsFlag | 是否欠费 | boolean |  |
|             performanceMoney | 项目执行业绩 | number |  |
|   treatRecord | 治疗信息 | 治疗记录 | 治疗记录 |
|     anesthesiaName | 麻醉方式 | string |  |
|     anesthesiaValue | 麻醉方式对应值 | string |  |
|     customerId | 客户id | string |  |
|     customerName | 客户姓名 | string |  |
|     customerPhone | 客户电话 | string |  |
|     dealWith | 处置 | string |  |
|     deductDeptId | 划扣科室id | string |  |
|     deductDeptName | 划扣科室名称 | string |  |
|     deductFlag | 是否已划扣 | boolean |  |
|     deductRecordId | 划扣记录id | string |  |
|     deductRecordNo | 划扣记录号 | string |  |
|     deductRemark | 划扣说明 | string |  |
|     deductTime | 划扣时间 | string |  |
|     deductUserId | 划扣用户id | string |  |
|     deductUserName | 划扣用户姓名 | string |  |
|     deviceList | 设备参数 | array | 治疗设备 |
|       actualValue | 值 | string |  |
|       deviceCode | 设备对应字典code | string |  |
|       deviceName | 设备名称 | string |  |
|       id | 数据id | string |  |
|       parameterCode | 参数对应字典code | string |  |
|       parameterName | 参数名 | string |  |
|       treatRecordId | 治疗记录id | string |  |
|       unitCode | 单位对应字典code | string |  |
|       unitName | 单位 | string |  |
|     doctorList | 治疗医生 | array | 治疗医生 |
|       doctorInfo | 医生信息 | array | 医生id和姓名 |
|         id | 医生（员工）id | string |  |
|         name | 医生（员工）姓名 | string |  |
|       leadTreatFlag | 是否主导治疗 | boolean |  |
|       roleId | 治疗岗位id | string |  |
|       roleName | 治疗岗位名称 | string |  |
|     injectionSite | 注射/治疗部位 | array | InjectionSiteVo |
|       id | 部位code | string |  |
|       key | 部位code | string |  |
|       label | 部位名称 | string |  |
|       name | 部位名称 | string |  |
|       title | 部位名称 | string |  |
|       value | 部位code | string |  |
|     multipleFlag | 是否是连台治疗 | boolean |  |
|     signInfoDTOList | 签名信息 | array | 签名对象实体 |
|       signRoleEnum | 签名角色,可用值:CUSTOMER,DOCTOR | string |  |
|       url | 签名图片的相对路径 | string |  |
|     tenantId | 治疗门店 | string |  |
|     tenantName | 治疗门店名称 | string |  |
|     treatContent | 治疗记录 | string |  |
|     treatDeptId | 治疗部门id | string |  |
|     treatDeptName | 治疗部门名称 | string |  |
|     treatParameter | 治疗参数 | string |  |
|     treatRecordNo | 治疗记录号 | string |  |
|     treatmentTime | 就诊时间 | string |  |
|     verifyDeptId | 核销科室id | string |  |
|     verifyDeptName | 核销科室名称 | string |  |
|     verifyFlag | 是否已核销 | boolean |  |
|     verifyRecordId | 核销记录id | string |  |
|     verifyRecordList | 核销记录 | array | 核销记录 |
|       finishFlag | 是否已完成核销 | boolean |  |
|       id | 划扣记录id | string |  |
|       material | 划扣的物料信息 | array | 划扣物料信息 |
|             id | 物料划扣id | string |  |
|         materialId | 物料id | string |  |
|         materialName | 物料名称 | string |  |
|         materialUnit | 物料单位code | string |  |
|         materialUnitName | 物料单位名称 | string |  |
|         specification | 物料规格 | string |  |
|         verifyNumber | 核销数量 | string |  |
|         verifyRecordId | 核销记录id | string |  |
|         warehouseId | 核销仓库id | string |  |
|         warehouseName | 核销仓库名称 | string |  |
|       treatRecordId | 治疗记录id | string |  |
|       verifyDeptId | 核销科室id | string |  |
|       verifyDeptName | 核销科室名称 | string |  |
|       verifyRecordNo | 核销记录单号 | string |  |
|       verifyRemark | 核销备注 | string |  |
|       verifyTime | 核销时间 | string |  |
|       verifyUserId | 核销用户id | string |  |
|       verifyUserName | 核销用户姓名 | string |  |
|     verifyRecordNo | 核销记录单号 | string |  |
|     verifyRemark | 核销备注 | string |  |
|     verifyTime | 核销时间 | string |  |
|     verifyUserId | 核销用户id | string |  |
|     verifyUserName | 核销用户姓名 | string |  |
| msg | 响应消息 | string |  |

**响应示例**:

```JSON
{
    "code": 10000,
    "data": {
        "boneAgeReport": "",
        "connectVerficateAndDedutFlag": true,
        "treatList": [
            {
                "billingId": "",
                "billingItemId": "",
                "billingItemName": "",
                "billingItemTypeCategory": 0,
                "billingNo": "",
                "billingTime": "",
                "billingUserId": "",
                "billingUserName": "",
                "canNotLimitDeduct": true,
                "crossHospitalFlag": true,
                "customerId": "",
                "departmentId": "",
                "departmentName": "",
                "discountPrice": 0,
                "doctorId": "",
                "doctorName": "",
                "finishFlag": true,
                "freeFlag": true,
                "itemDataId": "",
                "medicalRecordId": "",
                "noCancelDeductCount": 0,
                "noDeductVerifyCount": 0,
                "numberOfTime": 0,
                "orderVerifyTenant": "",
                "projectAlias": "",
                "residueNoStartNum": 0,
                "residueNum": 0,
                "signInfo": "",
                "totalNum": 0,
                "totalPrice": 0,
                "treatCount": 0,
                "treatPredefineId": "",
                "treatRecordItemId": "",
                "unitOrderPrice": 0,
                "arrearsFlag": false
            }
        ],
        "treatRecord": {
            "anesthesiaName": "",
            "anesthesiaValue": "",
            "customerId": "",
            "customerName": "",
            "customerPhone": "",
            "dealWith": "",
            "deductDeptId": "",
            "deductDeptName": "",
            "deductFlag": false,
            "deductRecordId": "",
            "deductRecordNo": "",
            "deductRemark": "",
            "deductTime": "",
            "deductUserId": "",
            "deductUserName": "",
            "deviceList": [
                {
                    "actualValue": "",
                    "deviceCode": "",
                    "deviceName": "",
                    "id": "",
                    "parameterCode": "",
                    "parameterName": "",
                    "treatRecordId": "",
                    "unitCode": "",
                    "unitName": ""
                }
            ],
            "doctorList": [
                {
                    "doctorInfo": [
                        {
                            "id": "",
                            "name": ""
                        }
                    ],
                    "leadTreatFlag": true,
                    "roleId": "",
                    "roleName": ""
                }
            ],
            "id": [
                {
                    "id": "",
                    "key": "",
                    "label": "",
                    "name": "",
                    "title": "",
                    "value": ""
                }
            ],
            "multipleFlag": true,
            "signInfoDTOList": [
                {
                    "signRoleEnum": "",
                    "url": ""
                }
            ],
            "tenantId": "",
            "tenantName": "",
            "treatContent": "",
            "treatDeptId": "",
            "treatDeptName": "",
            "treatParameter": "",
            "treatRecordNo": "",
            "treatmentTime": "",
            "verifyDeptId": "",
            "verifyDeptName": "",
            "verifyFlag": true,
            "verifyRecordId": "",
            "verifyRecordList": [
                {
                    "finishFlag": true,
                    "id": "",
                    "material": [
                        {
                            "id": "",
                            "materialId": "",
                            "materialName": "",
                            "materialUnit": "",
                            "materialUnitName": "",
                            "specification": "",
                            "verifyNumber": "",
                            "verifyRecordId": "",
                            "warehouseId": "",
                            "warehouseName": ""
                        }
                    ],
                    "treatRecordId": "",
                    "verifyDeptId": "",
                    "verifyDeptName": "",
                    "verifyRecordNo": "",
                    "verifyRemark": "",
                    "verifyTime": "",
                    "verifyUserId": "",
                    "verifyUserName": ""
                }
            ],
            "verifyRecordNo": "",
            "verifyRemark": "",
            "verifyTime": "",
            "verifyUserId": "",
            "verifyUserName": ""
        }
    },
    "msg": "操作成功"
} 
```

## [获取所有的治疗岗位列表](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Ux0MdtGcIotSdUxD0xycSTbInZc)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/treat/get-treatment-roles   GET**

**接口描述**: 治疗划扣时选择参与治疗 医生的岗位信息

- **请求参数**

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 | schema |
|-|-|-|-|-|-|
| key | key | 关键字（名称）查询 | false | string |  |
| tenantId | tenantId | 查询门店id | true | string |  |

- **返回结果:**

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | array | 治疗中心 岗位配置 |
|   id | 配置id | string |  |
|   indexing | 排序 | integer(int32) |  |
|   name | 配置名称 | string |  |
|   remark | 配置备注 | string |  |
|   roleId | 岗位id | string |  |
|   stationFlag | 岗位性质 | integer(int32) |  |
|   stationFlagStr | 岗位性质描述 | string |  |
| msg | 响应消息 | string |  |





**响应示例**:

```JSON
{
    "code": 10000,
    "data": [
        {
            "id": "",
            "indexing": 0,
            "name": "",
            "remark": "",
            "roleId": "",
            "stationFlag": 0,
            "stationFlagStr": ""
        }
    ],
    "msg": "操作成功"
}
```

## [小程序-我的治疗](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#BdEndHCmeoW847xyxZqcj3Iencc)(旧版)

- 请求URL

**/api/v1/scrm/treatment/page   POST**

- 请求参数

![图片展示的是睿美云开放接口治疗（treat）中“小程序-我的治疗”接口的请求参数示例。在Postman中，Body部分选择raw，JSON格式下输入了参数值。参数包括current、size、customerId、purchaseType、startTime、endTime、treatmentTime、isGroup等，如current为1，size为10，customerId为特定字符串，purchaseType为BUY_IN_HOSPITAL等。该图片与文档中接口请求参数部分对应，直观呈现了参数的具体填写方式。](https://feishu.cn/file/NqEMbsqopoluvyxgGBHcD0Gwnud)

参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| current | 是 | long | 当前页数 | 从1开始 |
|    size | 是 | long | 每页显示条数 |  |
|    customerId | 是 | string | 客户id |  |
|    purchaseType | 否 | string | 购买方式 | BUY_IN_HOSPITAL：院内购买；  <br/>BUY_IN_NET：网络购买；  <br/>GIFTS_FROM_FRIEND：朋友赠送；  <br/>HC_MEMBER_CARD_GIFT：会员卡赠送；  <br/>HC_MEMBER_CARD_FRIEND_GIFT：亲友礼包赠送； |
|    startTime | 否 | date | 最近治疗日期（起始） | 格式：yyyy-MM-dd |
|    endTime | 否 | date | 最近治疗日期（截止） | 格式：yyyy-MM-dd |
|    treatmentTime | 是 | boolean | 是否是已治疗（true为已治疗列表，false为未治疗列表） |  |
| isGroup | 是 | boolean | 是否是集团版（true-集团，false-非集团） |  |

- 返回结果

```JSON
{
  "msg": "成功获取数据，数据非空",
  "code": 10001,
  "data": {
    "total": 4,    //总条数
    "records": [    //数据列表
      {
        "id":"",//数据id（已治疗非空，未治疗为空）
        "billingId":"0b20cdfdb38c4bfe81b6a8bd6bef1d09",    //订单id
        "oldBillingPackageId":"",    //所属套餐的订单项id
        "oldBillingPackageProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
        "oldBillingProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
        "treatPredefineId": "07bdf11733864fe09d0a814e582ce8af" //未治疗列表的数据id（当前消费项如果是非项目，则该字段为空）
        "billingItemId": "50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
        "billingItemType": "PACKAGE",    //订单项类型（PROJECT项目,PACKAGE分类本身(套餐/年卡/次卡本身),PACKAGE_PROJECT套餐项目）
        "billingItemTypeCategory": "ANNUAL_CARD",    //订单项所属类型（TOP_FLOOR单项，PACKAGE套餐，ANNUAL_CARD年卡，ONCE_CARD次卡，EXPERIENCE_CARD_CARD体验卡）
        "coverImage": "",    //商品封面路径
        "crossTreatTransferFlag": false,    //是否是跨院转诊（true-是跨院转诊）
        "purchaseType": "院内购买",    //购买形式  
        "donationFlag": true,    //是否可转赠（true-可转赠）
        "expireFlag": false,    //是否已过期（true-已过期）
        "mallGoodsFlag": false,    //是否是小程序订单（true-是小程序订单）
        "packageName": "",    //所属套餐/年卡/次卡名称
        "projectName": "规范",    //当前消费项名称
        "purchaseDate": 1733730911000,    //购买日期
        "recentTreatDate": 1733730936000,    //最近治疗日期
        "totalNum": 1,    //总次数
        "residueNum": 1,    //剩余次数
        "status": "PAID",    //订单状态（WAIT_PAID待缴费，PAID已缴清，PART_PAID欠费）
        "tenantName": "门店1",    //所属门店名称
        "treatCount": 1,    //治疗次数
        "treatmentDoctor": "[\"测试67\"]",    //已治疗的治疗医生/未治疗的最近治疗医生
        "validityStartDate": null,   //有效期开始时间
        "expireTime":null,    //过期时间
        "transferFlag":true,    //是否转赠
        "transferCustomerId": "323173219160817664",    //转赠客户id
        "transferCustomerName":"刘占林",    //转赠客户姓名
        "transferDate": 1739155807000,    //转赠时间
        "details": [    //套餐子项/年卡子项/次卡子项
          {
            "billingId":"0b20cdfdb38c4bfe81b6a8bd6bef1d09",    //订单id
            "oldBillingPackageId":"",    //所属套餐的订单项id
            "oldBillingPackageProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
            "oldBillingProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
            "billingItemId": "133c60556d77425d889d4746f04cea50",   //订单项id
            "billingItemType": "PROJECT",     //订单项类型（PROJECT项目,PACKAGE分类本身(套餐/年卡/次卡本身),PACKAGE_PROJECT套餐项目）
            "billingItemTypeCategory": "ANNUAL_CARD",    //订单项所属类型（TOP_FLOOR单项，PACKAGE套餐，ANNUAL_CARD年卡，ONCE_CARD次卡，EXPERIENCE_CARD_CARD体验卡）
            "crossTreatTransferFlag": false,    //是否是跨院转诊（true-是跨院转诊）
            "donationFlag": true,    //是否可转赠（true-可转赠）
            "expireFlag": false,   //是否已过期（true-已过期）
            "expireTime": null,   //过期时间
            "projectName": "一分项目",    //当前消费项名称
            "residueNum": 0,    //剩余次数
            "totalNum": 0,    //总次数
            "treatPredefineId": "07bdf11733864fe09d0a814e582ce8af" //未治疗列表的数据id
          }
        ]
      }
    ]
  }
}
```

## [小程序-我的治疗](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#SPgzdL6tZoSV1dxzNRXcjlUMn2c)（新版）

- 请求URL

**/api/v1/tpos/treat/scrmTreatList  POST**

- 请求参数

```json
{
  "current": 1,
  "size": 10,
  "customerid": "a7258949583e4e679b02a9fccd7317b3",
  "endTime": "2025-12-25",
  "startTime": "2024-11-01",
  "purchaseType":"BUY_IN_HOSPITAL",
  "tenantId":1,
  "treatFlag": false
}
```

参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| current | 是 | long | 当前页数 | 从1开始 |
|    size | 是 | long | 每页显示条数 |  |
|    customerId | 是 | string | 客户id |  |
|    purchaseType | 否 | string | 购买方式 | BUY_IN_HOSPITAL：院内购买；  <br/>BUY_IN_NET：网络购买；  <br/>GIFTS_FROM_FRIEND：朋友赠送；  <br/>HC_MEMBER_CARD_GIFT：会员卡赠送；  <br/>HC_MEMBER_CARD_FRIEND_GIFT：亲友礼包赠送； |
|    startTime | 否 | date | 最近治疗日期（起始） | 格式：yyyy-MM-dd |
|    endTime | 否 | date | 最近治疗日期（截止） | 格式：yyyy-MM-dd |
|    treatFlag | 是 | boolean | 是否是已治疗（true为已治疗列表，false为未治疗列表） |  |
| tenantId | 是 | string | 门店id |  |

- 返回结果

```JSON
{
  "msg": "成功获取数据，数据非空",
  "code": 10001,
  "data": {
    "total": 4,    //总条数
    "records": [    //数据列表
      {
        "id":"",//数据id（已治疗非空，未治疗为空）
        "billingId":"0b20cdfdb38c4bfe81b6a8bd6bef1d09",    //订单id
        "oldBillingPackageId":"",    //所属套餐的订单项id
        "oldBillingPackageProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
        "oldBillingProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
        "treatPredefineId": "07bdf11733864fe09d0a814e582ce8af" //未治疗列表的数据id（当前消费项如果是非项目，则该字段为空）
        "billingItemId": "50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
        "billingItemType": "PACKAGE",    //订单项类型（PROJECT项目,PACKAGE分类本身(套餐/年卡/次卡本身),PACKAGE_PROJECT套餐项目）
        "billingItemTypeCategory": "ANNUAL_CARD",    //订单项所属类型（TOP_FLOOR单项，PACKAGE套餐，ANNUAL_CARD年卡，ONCE_CARD次卡，EXPERIENCE_CARD_CARD体验卡）
        "coverImage": "",    //商品封面路径
        "crossTreatTransferFlag": false,    //是否是跨院转诊（true-是跨院转诊）
        "purchaseType": "院内购买",    //购买形式  
        "donationFlag": true,    //是否可转赠（true-可转赠）
        "expireFlag": false,    //是否已过期（true-已过期）
        "mallGoodsFlag": false,    //是否是小程序订单（true-是小程序订单）
        "packageName": "",    //所属套餐/年卡/次卡名称
        "projectName": "规范",    //当前消费项名称
        "purchaseDate": 1733730911000,    //购买日期
        "recentTreatDate": 1733730936000,    //最近治疗日期
        "totalNum": 1,    //总次数
        "residueNum": 1,    //剩余次数
        "status": "PAID",    //订单状态（WAIT_PAID待缴费，PAID已缴清，PART_PAID欠费）
        "tenantName": "门店1",    //所属门店名称
        "treatCount": 1,    //治疗次数
        "treatmentDoctor": "[\"测试67\"]",    //已治疗的治疗医生/未治疗的最近治疗医生
        "validityStartDate": null,   //有效期开始时间
        "expireTime":null,    //过期时间
        "transferFlag":true,    //是否转赠
        "transferCustomerId": "323173219160817664",    //转赠客户id
        "transferCustomerName":"刘占林",    //转赠客户姓名
        "transferDate": 1739155807000,    //转赠时间
        "details": [     //最多3级details   
          {
            "billingId":"0b20cdfdb38c4bfe81b6a8bd6bef1d09",    //订单id
            "oldBillingPackageId":"",    //所属套餐的订单项id
            "oldBillingPackageProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
            "oldBillingProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
            "billingItemId": "133c60556d77425d889d4746f04cea50",   //订单项id
            "billingItemType": "PROJECT",     //订单项类型（PROJECT项目,PACKAGE分类本身(套餐/年卡/次卡本身),PACKAGE_PROJECT套餐项目）
            "billingItemTypeCategory": "ANNUAL_CARD",    //订单项所属类型（TOP_FLOOR单项，PACKAGE套餐，ANNUAL_CARD年卡，ONCE_CARD次卡，EXPERIENCE_CARD_CARD体验卡）
            "crossTreatTransferFlag": false,    //是否是跨院转诊（true-是跨院转诊）
            "donationFlag": true,    //是否可转赠（true-可转赠）
            "expireFlag": false,   //是否已过期（true-已过期）
            "expireTime": null,   //过期时间
            "projectName": "一分项目",    //当前消费项名称
            "residueNum": 0,    //剩余次数
            "totalNum": 0,    //总次数
            "treatPredefineId": "07bdf11733864fe09d0a814e582ce8af" //未治疗列表的数据id,
            "details":[{ 
                 "billingId":"0b20cdfdb38c4bfe81b6a8bd6bef1d09",    //订单id
                "oldBillingPackageId":"",    //所属套餐的订单项id
                "oldBillingPackageProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
                "oldBillingProjectId":"50c5c6c8bbd34932947d8fe069efd1a3",    //订单项id
                "billingItemId": "133c60556d77425d889d4746f04cea50",   //订单项id
                "billingItemType": "PROJECT",     //订单项类型（PROJECT项目,PACKAGE分类本身(套餐/年卡/次卡本身),PACKAGE_PROJECT套餐项目）
                "billingItemTypeCategory": "ANNUAL_CARD",    //订单项所属类型（TOP_FLOOR单项，PACKAGE套餐，ANNUAL_CARD年卡，ONCE_CARD次卡，EXPERIENCE_CARD_CARD体验卡）
                "crossTreatTransferFlag": false,    //是否是跨院转诊（true-是跨院转诊）
                "donationFlag": true,    //是否可转赠（true-可转赠）
                "expireFlag": false,   //是否已过期（true-已过期）
                "expireTime": null,   //过期时间
                "projectName": "一分项目",    //当前消费项名称
                "residueNum": 0,    //剩余次数
                "totalNum": 0,    //总次数
                "treatPredefineId": "07bdf11733864fe09d0a814e582ce8af" //未治疗列表的数据id,
            }]
          }
        ]
      }
    ]
  }
}
```

## 所有的项目分类查询

- 请求URL

**/api/v1/tpos/basic/getProjectType   POST**

- 请求参数

<bitable table-id="tblGkNSQuTEnQ3vk" token="BYgabyXRia3oMbsiTtNczDwFnLf"></bitable>

- **返回结果**

<bitable table-id="tblDypIj7wu8ge3h" token="BYgabyXRia3oMbsiTtNczDwFnLf"></bitable>

## *项目或套餐搜索（需要门店）*

- 请求URL

**/api/v1/tpos/basic/getP/getProjectByType   POST**

- 请求参数

<bitable table-id="tbl5PGWtk6PUR2Zd" token="BYgabyXRia3oMbsiTtNczDwFnLf"></bitable>

- **返回结果**

<bitable table-id="tblf2xIERofBtT9p" token="BYgabyXRia3oMbsiTtNczDwFnLf"></bitable>

# **照片（photo）**

## [**外部七牛照片转存至**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#NwGOdSm6MoUWmcxAFnqc1EhZnWf)[**睿美云**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#NwGOdSm6MoUWmcxAFnqc1EhZnWf)

- 请求URL（需要tpos鉴权）

 **/api/v1/tpos/common/addPhoto    POST**

![图片展示的是睿美云开放接口中照片上传请求的JSON参数示例。在Body标签下，参数以JSON格式呈现，包含“photoInfoDTOList”数组，其中包含照片相关信息，如“path”为图片路径，“thumbnailPath”为缩略图路径，“comment”为备注，“photoTime”为拍照时间，“size”为文件大小，“name”为睿美云客户姓名，“phone”为客户手机号，“tenantId”为门店id，“remark”为拍照备注。该图片与文档中介绍的“照片（photo）”接口请求参数说明相呼应，直观呈现了参数内容。](https://feishu.cn/file/UgAhbsIfUoQceKxsDpIc8ScunWe)

- 参数说明

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><b>字段</b></td><td><b>是否必填</b></td><td><b>类型</b></td><td><b>说明</b></td><td><b>备注</b></td></tr><tr><td>photoInfoDTOList</td><td>是</td><td>array</td><td>该客户的照片路径列表</td><td>一次最多30张</td></tr><tr><td>   comment</td><td>否</td><td>string</td><td>照片备注</td><td></td></tr><tr><td>   lastModified</td><td>否</td><td>date-time</td><td>文件修改时间(yyyy-MM-dd HH:mm:ss)</td><td></td></tr><tr><td>   path</td><td>是</td><td>string</td><td>完整图片的相对路径</td><td>必须以 /neuron-outside_qiniu 开头</td></tr><tr><td>   size</td><td>否</td><td>string</td><td>文件大小（kb）</td><td></td></tr><tr><td>   thumbnailPath</td><td>否</td><td>string</td><td>缩略图路径，可以为空</td><td>必须以 /neuron-outside_qiniu 开头</td></tr><tr><td>   photoTime</td><td>否</td><td>date-time</td><td>拍照时间（yyyy-MM-dd HH:mm:ss）</td><td>箭头所指的时间<img name="image.png" alt="图片展示的是睿美云系统中“照片（photo）”页面的“已对比照片”部分。页面显示了2022年5月5日的照片，有“临时”和“门店二”两个标签。页面上方有“照片下载”“批量删除”“刷新”等操作按钮。图片中红色箭头指向“2022-05-05”日期，与上下文提到的“箭头所指的时间”相呼应，可能是在说明照片的拍摄时间。" mime="image/png" scale="1.000000" src="TMHIb7hLro9sDHxxANPc2cZOnvg"/></td></tr><tr><td>name</td><td>是</td><td>string</td><td>睿美云客户姓名</td><td></td></tr><tr><td>phone</td><td>是</td><td>string</td><td>睿美云客户手机号</td><td>优先使用手机号匹配，若多个客户手机号相同，再加上姓名匹配</td></tr><tr><td>remark</td><td>否</td><td>string</td><td>拍照备注</td><td></td></tr><tr><td>tenantId</td><td>是</td><td>string</td><td>睿美云门店id</td><td>测试的时候传1</td></tr></tbody></table>

- **返回结果**

除了这个结果之外，其他的全是错误信息或提示

```JSON
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": true
}
```

## [**外部照片路径转存至睿美云**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#C3DwdYSlSoVlRFx1eNscvEOAnHe)

- 请求URL（需要tpos鉴权）

 **`/api/v1/tpos/common/addPhotoOpen`       `POST`**

- 说明

这个接口只存储三方系统的图片访问地址，不存储图片文件

如果使用这个接口，则需要联系睿美云，把图片的访问地址（域名）添加到白名单中，以免睿美云在访问的时候把域名地址解析替换成睿美云的地址，导致无法访问

![图片展示的是睿美云开放接口中“照片（photo）”接口的POST请求示例。请求地址为https://test.hospital.realmerit.com.cn/api/v1/tpos/common/addPhotoOpen。Body部分以raw方式发送JSON数据，包含“name”“phone”“remark”“tenantId”等必填参数，以及“photoInfoDTOList”数组，其中包含“comment”“lastModified”“path”“thumbnailPath”“size”“photoTime”等字段，用于存储三方系统的图片访问地址等信息。该图片与文档中介绍此接口存储三方系统图片访问地址、需联系睿美云添加白名单等上下文内容相关。](https://feishu.cn/file/VKVEb5j9eoi2k6xzLNNcUUw5nPb)

- 参数说明

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><b>字段</b></td><td><b>是否必填</b></td><td><b>类型</b></td><td><b>说明</b></td><td><b>备注</b></td></tr><tr><td>photoInfoDTOList</td><td>是</td><td>array</td><td>该客户的照片路径列表</td><td>一次最多30张</td></tr><tr><td><grid><column width-ratio="0.300000"><p></p></column><column width-ratio="0.700000"><p>comment</p></column></grid></td><td>否</td><td>string</td><td>照片备注</td><td></td></tr><tr><td><grid><column width-ratio="0.300000"><p></p></column><column width-ratio="0.700000"><p> lastModified</p></column></grid></td><td>否</td><td>date-time</td><td>文件修改时间(yyyy-MM-dd HH:mm:ss)</td><td></td></tr><tr><td><grid><column width-ratio="0.300000"><p></p></column><column width-ratio="0.700000"><p> path</p></column></grid></td><td>是</td><td>string</td><td>完整图片访问路径</td><td rowspan="2">路径不能是那种需要验证权限，或者需要对路径进行加密等有限制的访问地址，因为是三方图片地址，睿美云无法做对应的验权的操作，只能是直接访问</td></tr><tr><td><grid><column width-ratio="0.300000"><p></p></column><column width-ratio="0.700000"><p> thumbnailPath</p></column></grid></td><td>否</td><td>string</td><td>缩略图路径，可以为空，为空则直接使用path的值进行赋值</td></tr><tr><td><grid><column width-ratio="0.300000"><p></p></column><column width-ratio="0.700000"><p> size</p></column></grid></td><td>否</td><td>string</td><td>文件大小（kb）</td><td></td></tr><tr><td><grid><column width-ratio="0.300000"><p></p></column><column width-ratio="0.700000"><p>photoTime</p></column></grid></td><td>否</td><td>date-time</td><td>拍照时间（yyyy-MM-dd HH:mm:ss）</td><td>箭头所指的时间<img name="image.png" alt="图片展示的是睿美云系统中“照片（photo）”页面的“已对比照片”部分。左侧显示“2022-05-05”日期，右侧列表中“2022-05-05”日期下有“备注：-”及一张照片缩略图，照片下方有“临时”和“门店二”标签。页面上方有“照片下载”“批量删除”“刷新”按钮。图片中红色箭头指向“2022-05-05”日期，与上下文提到的“箭头所指的时间”相呼应，用于指示照片拍摄时间。" mime="image/png" scale="1.000000" src="VHxsbsRupoCspsxXtfvcS7VTnhc"/></td></tr><tr><td>name</td><td>是</td><td>string</td><td>睿美云客户姓名</td><td></td></tr><tr><td>phone</td><td>是</td><td>string</td><td>睿美云客户手机号</td><td>优先使用手机号匹配，若多个客户手机号相同，再加上姓名匹配</td></tr><tr><td>remark</td><td>否</td><td>string</td><td>拍照备注</td><td></td></tr><tr><td>tenantId</td><td>是</td><td>string</td><td>睿美云门店id</td><td></td></tr></tbody></table>

- **返回结果**

除了这个结果之外，其他的全是错误信息或提示

```JSON
{
    "msg": "数据保存成功",
    "code": 10000,
    "data": true
}
```

## [上传照片到睿美云](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#K95MdKMCtoEBKLxcSt9cB7Binng)

说明：

这个接口是需要把图片文件上传到睿美云，由睿美云存储，如果图片量大，请联系医院或者睿美云，评估环境是否支持存储对应量的图片文件

请和接口：**`/api/v1/tpos/common/addPhotoOpen` 区分开**

- **请求URL（需要tpos鉴权）**

**`/api/v1/tpos/common/upload_customer_photo`          `POST`**

- **请求参数**

content-type: multipart/form-data

```JSON
{
    "customerId": "客户id"，
    "photoEnum": "影像类型（PHOTO_TYPE_ZERO：术前 ， PHOTO_TYPE_ONE：术后）"
    "file": "文件流数组（一次最多传30个照片）",
    "tenantId": "门店id" ，
    "photoTime": "拍照时间（yyyy-MM-dd HH:mm:ss）",
    "remark":"备注信息"  //添加专属备注信息可以用来区分图片来源，不填则默认：三方系统图片
}
```

- 返回结果

data只要是true，就视为成功

![图片展示的是睿美云皮肤检测类图片上传接口的Postman测试界面。请求方式为POST，URL为https://test.hospital.realmerit.com.cn/api/v1/tpos/yizhipai/uploadcustomerphoto。Body部分设置为form-data，有file、customerId、photoEnum、tenantId四个参数，其中file为必填，customerId、photoEnum、tenantId为选填。返回结果为JSON格式，显示“身份信息已经过期，请重新登陆！”，code为401。该图片与文档中皮肤检测类图片上传接口的测试操作相关，直观呈现了接口测试的具体参数设置情况。](https://feishu.cn/file/DdribAn4HoIOAlxVJAscF6Y6n1b)

## [**通过客户id分页查询照片信息**](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#CGM8du8MYoewOyxG6OqcQfMFnYK)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/common/photoPage    GET**

![图片展示的是通过客户id分页查询照片信息的接口请求界面。请求方式为GET，URL为http://www.stanislavssi.xyz/api/v1/tpos/common/photoPage，参数包括customerId、page、size，其中customerId为必填项，page和size可选，默认值分别为1和20。右侧返回结果JSON显示code为1000，data中包含current、pages、records等字段。该图片与文档中介绍的通过客户id分页查询照片信息接口请求相关，直观呈现了请求参数及返回结果。](https://feishu.cn/file/boxcnr4iwYW7DFRW5aDpRMhxCxb)



- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 睿美云客户id |  |
| page | 否 | string | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | string | 数据量 | 默认为：20，最大为：500 |

- **返回结果**

![图片展示的是睿美云开放接口中“通过客户id分页查询照片信息”接口的返回结果。JSON格式数据中包含code、data等字段，data字段下有count、current、maxLimit、notFirstPage、orders、pages、records等信息。records字段下记录了多条照片信息，包括customerId、id、lastModified、path、thread、token、thumbnailPath等，其中部分路径信息被模糊处理。该图片与文档中介绍的接口返回结果部分对应，直观呈现了接口返回的数据结构。](https://feishu.cn/file/CrwlbLFOioMlMTxIHD5cqneBnyd)



```JSON
{
    "code": 10000,            //    成功的code
    "data": {
        "current": 1,         //    当前页码
        "pages": 9,           //    一共有多少页
        "records": [
            {
                "customerId": "60503a87b6854dc5be1d6f3959a35d4d",    //    客户id
                "id": "1597072360490696705",              //    照片数据本身的id
                "lastModified": 1669605502000,            //    照片最后修改时间
                "path": "xxxxxxxxxxxxx",                  //    照片路径
                "pathQiNiuImageView":"xxxxxxxxxx",        //    如果是七牛照片，则提供七牛的缩略图
                "thumbnailPath":"xxxxxxxxxxxxx",          //    照片缩略图（如果是七牛照片，建议用上面的pathQiNiuImageView当缩略图）
                "tenantId": "1"                           //    该照片所属门店id
                "type":0                                  //照片类型(0-术前，1-术后)
            }
        ],
        "searchCount": false,         //    不用管
        "size": 1,                    //    传入参数的size    
        "total": 9                    //    总条数
    },
    "msg": "操作成功"
}
```

## [皮肤检测类图片上传](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf?chunked=false#L0Mnd1iGBoHCZ5xDwBDcG4D6n8g)

- 请求URL（需要tpos鉴权）

`/api/v1/tpos/skin_image/update_skin_file `            post

- **请求参数**

content-type: multipart/form-data

```JSON
{
    "customerId": "(必填)客户id，从客户查询接口获取",
    "files": "(必填)文件流数组（一次最多传30个照片）",
    "tenantId": "(必填)门店id",
    "uniqueUid": "(必填)本次拍摄的唯一id（三方平台的id）",
    "captureDate": "(必填)拍摄时间",
    "type": "(必填)平台类型，需要提前和睿美云沟通，需要睿美云在枚举（SkinLabelTypeEnum）里面添加对应的枚举",
    "projectIds": "[
        \"项目id,对应睿美云的项目id，从项目查询接口获取\",
        \"项目Id2\"
    ]",
    "dataJson": "{  //如果有其他信息也可以放进来,这是一个json字符串
        \"contents\": \"对图片的解析，可以是json字符串\",
        \"edition\": \"数据版本\",
        \"scannerId\": \"拍摄设备编号\",
        \"version\": \"拍摄设备数据版本\"
    }"
}
```

- 返会值

![图片展示的是皮肤检测类图片上传接口的Postman测试界面。请求URL为`http://localhost:8080/api/v1/tpos/skin_image/update_skin_file`，请求方式为POST。Body部分设置为form - data，有uniqueUId、files、projectIds、dataJson、captureDate、type等参数，其中files参数下有3个文件。返回结果为JSON格式，显示“code”为10000，“data”为null，“msg”为“上传成功”。该图片与文档中皮肤检测类图片上传接口的请求参数及返回结果内容对应，直观呈现了接口测试情况。](https://feishu.cn/file/JZK1bs33uofpXMxkEnXclYDFnBg)

# 基础（basic）

## **项目**

### [获取项目信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#MA4qd4GQeoYgyixIlWBcr8ASnmb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/project-page  GET**

![这张图片展示了睿美云获取项目信息接口的请求与响应内容，左侧是接口请求配置区，显示请求方式为GET，请求URL为对应项目查询地址，Query Params区域勾选了必填字段tenantId，还可见待选参数name、typeId、status；右侧是接口响应结果区域，返回格式为JSON，其中包含code、data、msg等字段，data内包含项目相关信息、项目分类编号、项目名称、项目状态、项目编码、项目创建时间、项目组信息以及操作提示消息。](https://feishu.cn/file/OJCAbZxVfoz6PWxQCFgcV5T8nGd)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |
| typeId | 否 | string | 项目分类id |  |
| name | 否 | string | 项目名称 |  |
| status | 否 | int | 状态 | 状态 0-禁用，1-在用，2-到期 |
| page | 否 | int | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数量 | 默认为：20，最大为：500 |

- 返回结果

```JSON
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "current": 1,           //    当前页
        "pages": 42,            //    可用总页数
        "records": [
             {
                "endDate": null,                             //    到期时间
                "id": "b759b156d99947fa94d47484be7d4f45",    //    数据id
                "name": "禁用测试",                           //    项目名称
                "price": 19999.00,                           //    价格
                "startDate": null,                           //    开始时间
                "status": 0,                                 //    状态
                "type": "a89d7c7997a72a27078b5bf16c0fb742"   //    分类id
            }
        ],
        "searchCount": false,
        "size": 2,              //    当前页大小
        "total": 84             //    总记录数
    }
}
```

### [获取项目分类树](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#L8YkdQuSwosiOMxSUDEcMsfKn29)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/project-type-tree    GET**

![这是一张接口测试工具的页面截图，对应文档中「获取项目分类树」的接口内容。该页面为GET请求的调试界面，请求地址为/api/v1/tpos/basic/project-type-tree，Query Params区域的tenantId参数被勾选，值为1，另一未勾选参数name的值为测试门店。右侧响应区域显示请求返回的JSON格式结果，包含code、codeText、children等字段，部分字段如isEdit、isValid等取值为false，其中value字段对应内容为“删除分类”，请求状态码为200 OK，耗时117ms。](https://feishu.cn/file/Jn0Qb8sQYoLRQPxuL0ncpdm2nGc)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": [{
                    "children": [{                                         //    子分类列表
                                "id": "96f519df42b740d8b9ecee71dfd65875",  //    分类id
                                "title": "儿牙矫正类1",                     //    分类名称
                            },
                            {
                                "id": "d468bc467dac4a8f9c5814b91b16a839",
                                "title": "儿牙矫正类2",
                            }
                    ],
                    "id": "015471e82d1e4f949690475505fdfb37",
                    "title": "整形外科",
                },
                {
                    "children": [],
                    "id": "26c937f751f84c52924073644a2a7051",
                    "title": "执行层",
                }
        ]
}
```

### [项目详情信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#SKU7dUZohoZncgxy4CBcNtoGnuh)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/project-detail      GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 项目id |  |

- 返回结果

![这张图片展示的是睿美云开放接口项目详情信息API（请求路径为/api/v1/tpos/basic/project-detail）的返回结果，呈现为结构化的JSON数据格式。返回数据包含多个层级的字段，涵盖项目名称、创建时间、更新时间、项目状态标识、项目编号、负责人、项目创建人、项目关联信息、项目时间范围等内容，部分字段带有示例值，其中一处橙色高亮标注的内容对应项目名称字段，整体为接口正常返回的项目详情数据内容。](https://feishu.cn/file/XAKfblBcxo3zjEx5JIfcfkDkncg)



```JSON
{
    "code": 10000,
    "data": {
        "allowDonationFlag": true,
        "allowedMemberLevelsList": [
            {
                "endScoreRange": null,
                "startScoreRange": null,
                "id": "5b46b642a8fc4606a14b71438c58e241",
                "memberLevelName": "高级VIP"
            }
        ],
        "anaeName": "局部麻醉",
        "anaesthesia": 1,
        "anestheticFee": 10.00,
        "billTotalPrice": 11.00,
        "billingSourceContentRes": [
            {
                "allowDonationFlag": true,
                "billTotalPrice": 11.00,
                "billingSourceEnum": "项目",
                "billingSourceType": 0,
                "channelRebateFlag": true,
                "configId": "998513f9cac6c99dc48cd8d56ae4a33e",
                "configName": "有赞美业",
                "defaultCount": 2,
                "discountStatus": true,
                "endDateStr": "2026-04-01",
                "exePerformanceStatisticsFlag": true,
                "exemptionFlag": true,
                "id": "c972da625d014d21854e6fb42a030719",
                "oneManualPrice": 1.00,
                "payExpiryDate": null,
                "performanceStatisticsFlag": true,
                "price": 111.00,
                "projectOrPackageId": "cdb0389f73f847238abf7c2294da394d",
                "sameProjectPayFlag": false,
                "sameProjectTreatFlag": false,
                "settlementPrice": null,
                "startDateStr": "2025-03-01",
                "status": true,
                "treatExpiryDate": 100
            }
        ],
        "canNotLimitDeduct": false,
        "channelRebateFlag": true,
        "comment": "项目介绍",
        "countryCode": "",
        "createDate": "2024-03-27 14:46:28",
        "dealFlag": true,
        "defaultCount": 2,
        "delFlag": false,
        "dept": "190832441441648644",
        "deptName": "240123新建的部门",
        "discountFlag": true,
        "ductFlag": true,
        "endDate": "2026-04-01",
        "exePerformanceStatisticsFlag": true,
        "exemptionFlag": true,
        "feeFlag": true,
        "id": "cdb0389f73f847238abf7c2294da394d",
        "injectedItem": "注射用玻璃酸酶",
        "injectedItemUnit": "支",
        "injectionFlag": true,
        "limitCustomerTypeValue": [
            {
                "label": "初诊",
                "value": "0"
            }
        ],
        "limitNum": 10,
        "manualConsemeType": "",
        "medicalInsuranceCode": "医保编码",
        "memberFlag": true,
        "memberPrice": 10.00,
        "name": "时不时地",
        "oneManualPrice": 1.00,
        "operationFlag": true,
        "partName": "部位",
        "payExpiryDate": null,
        "performanceStatisticsFlag": true,
        "price": 111.00,
        "projectAlias": "展示名称",
        "projectCostSingleTime": 100,
        "projectDuration": 15.0000,
        "projectNumber": "XM000337",
        "remainingDaysOfBilling": "",
        "saleConsumeType": "",
        "specialFlag": true,
        "startDate": "2025-03-01",
        "status": 1,
        "storageNum": 10,
        "tenantId": "1",
        "tenantName": "",
        "treatExpiryDate": 100,
        "treatFlag": true,
        "type": "69d53854788f449e9a6a0b74b870741b",
        "typeName": "集团下发的",
        "unitList": [
            {
                "uId": "支",
                "label": "支"
            }
        ],
        "updateDate": "2025-03-13 11:17:10"
    },
    "msg": "操作成功"
}
```

- 参数data说明

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><b>参数名称</b></td><td><b>参数说明</b></td><td><b>类型</b></td></tr><tr><td>id</td><td>项目id</td><td>string</td></tr><tr><td>createDate</td><td>创建时间(yyyy-MM-dd HH:mm:ss)</td><td>string</td></tr><tr><td>updateDate</td><td>修改时间(yyyy-MM-dd HH:mm:ss)</td><td>long</td></tr><tr><td>delFlag</td><td>删除状态(true:删除，false：正常)</td><td>boolean</td></tr><tr><td>tenantId</td><td>门店id</td><td>string</td></tr><tr><td>tenantName</td><td>所属门店</td><td>string</td></tr><tr><td>name</td><td>项目名称</td><td>string</td></tr><tr><td>projectAlias</td><td>项目别名</td><td>string</td></tr><tr><td>projectNumber</td><td>项目编码</td><td>string</td></tr><tr><td>type</td><td>分类id</td><td>string</td></tr><tr><td>typeName</td><td>分类名称</td><td>string</td></tr><tr><td>price</td><td>开单项目单价</td><td>double</td></tr><tr><td>discountFlag</td><td>是否优惠（false-否，true-是）</td><td>boolean</td></tr><tr><td>exemptionFlag</td><td>可否免单（false-否，true-是）</td><td>boolean</td></tr><tr><td>specialFlag</td><td>是否特色项目（false-否，true-是）</td><td>boolean</td></tr><tr><td>treatFlag</td><td>是否是治疗项目（false-否，true-是）</td><td>boolean</td></tr><tr><td>comment</td><td>项目描述</td><td>string</td></tr><tr><td>injectionFlag</td><td>是否为注射项目（false-否，true-是）</td><td>boolean</td></tr><tr><td>injectedItem</td><td>注射物品，注射项目（injectionFlag）为true时从物料选择</td><td>String</td></tr><tr><td>injectedItemUnit</td><td>注射物品默认单位,通过查询物品对应的单位选择</td><td>String</td></tr><tr><td>unitList</td><td>注射物品其它单位</td><td>数组</td></tr><tr><td>channelRebateFlag</td><td>是否参与渠道返佣</td><td>boolean</td></tr><tr><td>operationFlag</td><td>是否手术（false-否，true-是）</td><td>boolean</td></tr><tr><td>anaesthesia</td><td>麻醉方式</td><td>int</td></tr><tr><td>anaeName</td><td>麻醉方式名称</td><td>string</td></tr><tr><td>anestheticFee</td><td>麻醉费(金额)</td><td>double</td></tr><tr><td>startDate</td><td>项目开单有效期开始时间(yyyy-MM-dd)，如果为空则表示无限期</td><td>string</td></tr><tr><td>endDate</td><td>项目开单有效期结束时间（yyyy-MM-dd)，如果为空则表示无限期</td><td>string</td></tr><tr><td>status</td><td>是否禁用(0-禁用，1-在用，2-到期)</td><td>int</td></tr><tr><td>dept</td><td>部门id</td><td>string</td></tr><tr><td>deptName</td><td>部门名称</td><td>string</td></tr><tr><td>performanceStatisticsFlag</td><td>是否参与业绩统计</td><td>boolean</td></tr><tr><td>defaultCount</td><td>开单默认次数</td><td>int</td></tr><tr><td>payExpiryDate</td><td>缴费后项目有效期，单位天</td><td>int</td></tr><tr><td>treatExpiryDate</td><td>治疗后项目有效期，单位天</td><td>int</td></tr><tr><td>billTotalPrice</td><td>开单项目总价</td><td>double</td></tr><tr><td>partName</td><td>项目对应的部位</td><td>string</td></tr><tr><td>limitCustomerTypeValue</td><td>限购客户类型[{"value":"","label":""}]</td><td>array</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>value</p></column></grid></td><td>标识</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>label</p></column></grid></td><td>类型名称</td><td>string</td></tr><tr><td>limitNum</td><td>限购数量</td><td>int</td></tr><tr><td>storageNum</td><td>库存量</td><td>int</td></tr><tr><td>projectMarketEntities</td><td>项目营销信息</td><td>array</td></tr><tr><td>billingSourceContentRes</td><td>开单来源记录</td><td>array</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>id</p></column></grid></td><td>来单来源配置数据id</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>configId</p></column></grid></td><td>开单来源配置Id</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>configName</p></column></grid></td><td>开单来源配置名称</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>projectOrPackageId</p></column></grid></td><td>绑定的套餐或项目id</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>billingSourceEnum</p></column></grid></td><td>绑定的套餐/项目</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>performanceStatisticsFlag</p></column></grid></td><td>是否参与业绩统计</td><td>Boolean</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>startDateStr</p></column></grid></td><td>开始时间(项目/套餐开单有效期</td><td>String</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>endDateStr</p></column></grid></td><td>到期时间(项目/套餐开单有效期)</td><td>String</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>payExpiryDate</p></column></grid></td><td>缴费后项目/套餐有效期，单位天，空表示：无限期</td><td>int</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>sameProjectPayFlag</p></column></grid></td><td>是否同项目设置（缴费后套餐有效期）（套餐使用）</td><td>bool</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>treatExpiryDate</p></column></grid></td><td>治疗后项目/套餐有效期，单位天，空表示：无限期</td><td>int</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>sameProjectTreatFlag</p></column></grid></td><td>治疗后项目/套餐有效期，单位天</td><td>bool</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>price</p></column></grid></td><td>开单项目单价/套餐价</td><td>double</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>billTotalPrice</p></column></grid></td><td>开单项目总价/套餐总价</td><td>double</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>defaultCount</p></column></grid></td><td>项目开单默认次数</td><td>int</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>discountStatus</p></column></grid></td><td>是否可打折</td><td>bool</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>exemptionFlag</p></column></grid></td><td>是否可赠送</td><td>bool</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>status</p></column></grid></td><td>是否可用</td><td>bool</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>billingSourceType</p></column></grid></td><td>开单来源(0-运营媒体，1-市场渠道)</td><td>int</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>channelRebateFlag</p></column></grid></td><td>是否参与渠道返佣</td><td>bool</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>oneManualPrice</p></column></grid></td><td>单次手工费</td><td>double</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>settlementPrice</p></column></grid></td><td>结算价</td><td>double</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>exePerformanceStatisticsFlag</p></column></grid></td><td>是否参与计算执行业绩统计</td><td>bool</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>allowDonationFlag</p></column></grid></td><td>是否可转赠（true-可转赠）</td><td>bool</td></tr><tr><td>oneManualPrice</td><td>单次手工费</td><td>double</td></tr><tr><td>projectDuration</td><td>项目时长</td><td>double</td></tr><tr><td>saleConsumeType</td><td>销售/消耗业绩类别</td><td>string</td></tr><tr><td>manualConsemeType</td><td>手工消耗类别</td><td>string</td></tr><tr><td>projectCostSingleTime</td><td>项目成本（单次）</td><td>int</td></tr><tr><td>remainingDaysOfBilling</td><td>开单剩余天数</td><td>string</td></tr><tr><td>medicalInsuranceCode</td><td>医保编码</td><td>string</td></tr><tr><td>canNotLimitDeduct</td><td>是否可以无限划扣,false不能无限划扣</td><td>bool</td></tr><tr><td>exePerformanceStatisticsFlag</td><td>是否参与计算执行业绩统计</td><td>boolean</td></tr><tr><td>dealFlag</td><td>是否成交项目</td><td>boolean</td></tr><tr><td>feeFlag</td><td>是否消费项目</td><td>boolean</td></tr><tr><td>ductFlag</td><td>是否划扣项目</td><td>boolean</td></tr><tr><td>allowedMemberLevelsList</td><td>会员等级信息，允许指定会员等级的客户购买，为空则不限制</td><td>array</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>id</p></column></grid></td><td>会员等级ID</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>memberLevelName</p></column></grid></td><td>会员等级名称</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>startScoreRange</p></column></grid></td><td>起始等级积分</td><td>string</td></tr><tr><td><grid><column width-ratio="0.500000"><p></p></column><column width-ratio="0.500000"><p>endScoreRange</p></column></grid></td><td>结束等级积分</td><td>string</td></tr><tr><td>countryCode</td><td>国家编码</td><td>string</td></tr><tr><td>allowDonationFlag</td><td>是否可转赠（true-可转赠/false-不可转赠）</td><td>boolean</td></tr><tr><td>memberFlag</td><td>是否是会员项目</td><td>boolean</td></tr><tr><td>memberPrice</td><td>会员价(单价)</td><td>double</td></tr></tbody></table>



## **套餐**

### [获取套餐信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#KSa9d0mlGo28grx10TicOGrMnKb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/package-page  GET**

![图片展示的是睿美云开放接口基础（basic）中获取套餐信息的API调用界面。请求URL为192.168.2.133:60003/api/v1/tpos/basic/package-page，需tpos鉴权。参数部分，tenantId和name已勾选，tenantId值为1，name值为空。右侧返回结果以JSON格式呈现，包含code、data等字段，data下有count、current、maxSize、totalCount等信息，records字段下有套餐id、名称、价格、开始时间、结束时间、订单总价等详细数据。](https://feishu.cn/file/USEkbeyeQou5ekx3XJ9cQ3e0nJd)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |
| typeId | 否 | string | 项目分类id |  |
| name | 否 | string | 项目名称 |  |
| status | 否 | int | 状态 | 状态 0-禁用，1-在用，2-到期 |
| page | 否 | string | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | string | 每页数量 | 默认为：20，最大为：500 |

- 返回结果

```JSON
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "current": 1,           //    当前页
        "pages": 42,            //    可用总页数
        "records": [
             {
                "endDate": null,                             //    到期时间
                "id": "b759b156d99947fa94d47484be7d4f45",    //    数据id
                "name": "禁用测试",                           //    数据名称
                "packagePrice": 19999.00,                    //    套餐价
                "totalPrice": 100.00,                        //    总价（原价）
                "startDate": null,                           //    开始时间
                "type": "a89d7c7997a72a27078b5bf16c0fb742"   //    分类id
            }
        ],
        "searchCount": false,
        "size": 2,              //    当前页大小
        "total": 84             //    总记录数
    }
}
```

### [获取套餐分类树](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#OHITd4MJioQ4lyxPELVcu6venth)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/package-type-tree    GET**

![图片展示的是Postman工具中获取套餐分类树的API请求界面。请求URL为192.168.2.133:60003/api/v1/tpos/basic/package-type-tree，方法为GET。在Params标签下，tenantId值为1，name值为空。右侧Body区域显示了返回结果，包含code、data等字段，其中data字段下有id、name、type、typeNumber等信息，id为803a72a49f0ad85dcca38bca46dcca91fd，name为“基础套餐”，type为0。该图片与文档中获取套餐分类树API的上下文对应，直观呈现了API请求及返回结果。](https://feishu.cn/file/QbBHbTOwBo8vNlxXzLZcpmIIn5d)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | TRUE | string | 要查询的门店id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": [{
                    "children": [{                                         //    子分类列表
                                "id": "96f519df42b740d8b9ecee71dfd65875",  //    分类id
                                "title": "儿牙矫正类1",                     //    分类名称
                            },
                            {
                                "id": "d468bc467dac4a8f9c5814b91b16a839",
                                "title": "儿牙矫正类2",
                            }
                    ],
                    "id": "015471e82d1e4f949690475505fdfb37",
                    "title": "整形外科",
                },
                {
                    "children": [],
                    "id": "26c937f751f84c52924073644a2a7051",
                    "title": "执行层",
                }
        ]
}
```



### [套餐详情信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#O6kRd5RvNovvspxkA6uclqHRn67)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/package-detail    GET**

![图片展示的是睿美云开放接口基础（basic）中获取套餐详情信息的API请求界面。请求URL为192.168.2.133:60003/api/v1/tpos/basic/package - detail?tenantId=1&id=000b7e96c4941ed98270242ac110005 。在Params标签下，有tenantId和id两个必填参数，tenantId值为1，id值为000b7e96c4941ed98270242ac110005 。右侧Body区域显示返回结果为1。该图片与上下文紧密相关，直观呈现了获取套餐详情信息API请求时的参数设置情况。](https://feishu.cn/file/C0Dybnx4yoxpVhxiZNfc02Slnjb)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 套餐id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": {
            "name": "111",
            "packagePrice": 666.00,
            "packageProjectRelationVos":[{
                "projectId": "",             //    项目id
                "projectName": "",           //    项目名称
                "count": 1,                   //    数量
                "relationEnum": "PROJECT",    //    关联关系中文
                "relationEnumCode": 0,        //    关联关系code
                "childRelationList":[{        //    如果是年卡，次卡则有子项信息
                     "projectId": "",             //    项目id
                     "projectName": "",           //    项目名称
                }] 
            }]
        }
}
```

## 年卡

### [获取年卡信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#JzZmdktiiodoUixUbI2ch3qXnSU)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/annual-card-page  GET**

![这是睿美云开放接口年卡信息获取接口对应的请求调试示例图，展示了GET方法的请求信息：请求URL为/api/v1/tpos/basic/annual-card-page?tenantId=1，Query Params区域中，必填参数tenantId已勾选且值设为1，非必填参数name也已填写具体值“水光针10次”，右侧Body区域显示响应状态码为200 OK，当前按Pretty格式展示响应内容。](https://feishu.cn/file/PnTSbLuLXoGGg6xsF1EcS7eSn0g)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |
| typeId | 否 | string | 项目分类id |  |
| name | 否 | string | 项目名称 |  |
| status | 否 | int | 状态 | 状态 0-禁用，1-在用，2-到期 |
| page | 否 | int | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数量 | 默认为：20，最大为：500 |
| detailDataFlag | 否 | boolean | *得到详细数据标志，true\|需要* |  |

- 返回结果

```JSON
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "current": 1,           //    当前页
        "pages": 42,            //    可用总页数
        "records": [
             {
                "code": "",                                 //    年卡编号
                "disabledFlag": false,                      //    是否禁用
                "endDate": null,                            //    到期时间
                "id": "01bfaa998a7dd6cf84611b92e1d9302b",   //    数据id
                "name": "子年卡1",                           //    名称
                "showName": "",                             //    展示名称
                "startDate": null,                          //    开始时间
                "status": 1,                                //    状态
                "totalPrice": 100.00,                        //    售价
                "typeId": "2971f98c6ccbbf86d45db7870af470f1"    //    分类id
                "projectList":[
                    {
                      "id":"aasdfasf34557",//年卡子项唯一标识
                      "projectId":"sdfds",//年卡项目id
                    }
                ]
            }
        ],
        "searchCount": false,
        "size": 2,              //    当前页大小
        "total": 84             //    总记录数
    }
}
```

### [获取年卡分类树](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#DaQkdjjJaoGfboxTaWycfE54nph)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/annual-card-type-tree    GET**

![图片展示的是睿美云开放接口中年卡分类树的GET请求界面。请求URL为127.0.0.1:60000/api/v1/tpos/basic/annual-card-type-tree?tenantId=1，参数部分仅tenantId值为1，name和typeid为空。右侧返回结果部分显示“code”为0，“data”为{}。该图片与文档中获取年卡分类树的接口请求内容对应，直观呈现了请求参数设置及返回结果情况。](https://feishu.cn/file/QeSMbX1sOowfa5xx3DzcNXdNnDf)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | TRUE | string | 要查询的门店id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": [{
                    "children": [{                                         //    子分类列表
                                "id": "96f519df42b740d8b9ecee71dfd65875",  //    分类id
                                "title": "儿牙矫正类1",                     //    分类名称
                            },
                            {
                                "id": "d468bc467dac4a8f9c5814b91b16a839",
                                "title": "儿牙矫正类2",
                            }
                    ],
                    "id": "015471e82d1e4f949690475505fdfb37",
                    "title": "整形外科",
                },
                {
                    "children": [],
                    "id": "26c937f751f84c52924073644a2a7051",
                    "title": "执行层",
                }
        ]
}
```



- [年卡详情信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#YM8cdkNY5o6hVmxP6ZpcwSoVnrU)
- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/annual-card-detail    GET**

![图片展示的是睿美云开放接口中年卡详情信息的API调用界面。请求方式为GET，URL为127.0.0.1:60000/api/v1/tpos/basic/annual-card-detail?id=0094efb6fd86c02a03be4d430150b3d8 。在Query Params区域，id字段被勾选，其值为0094efb6fd86c02a03be4d430150b3d8 。右侧Body区域显示返回结果为1。该图片与文档中获取年卡详情的API请求内容相关，直观呈现了API调用时参数设置情况。](https://feishu.cn/file/HiEXbX2lJo72taxWEc7cJluEndc)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 套餐id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": {
            "name": "111",
            "totalPrice": 666.00,
            "projectList":[{
                "projectId": "",             //    项目id
                "projectName": "",           //    项目名称
                "count": 1                   //    数量
            }]
        }
}
```

## 次卡

### [获取次卡信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#V39nd73yAocRRFxP3xSciTNMnYe)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/time-card-page  GET**

![图片展示的是睿美云开放接口基础中次卡获取次卡信息的接口调用界面。请求方式为GET，URL为127.0.0.1:60000/api/v1/tpos/basic/time-card-page?tenantId=1。在Query Params区域，有tenantId、status、name、typeid等参数，其中tenantId值为1，status值为1，typeid值为e665acda...。右侧Body区域显示了返回结果，包含code、data等字段，data中包含countId、current、maxLimit等信息。该图片与上下文介绍的接口请求URL及参数说明相呼应，直观呈现了接口调用参数设置情况。](https://feishu.cn/file/SGsJbumaRo8gxhxq1PScMFZEn6c)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |
| typeId | 否 | string | 项目分类id |  |
| name | 否 | string | 项目名称 |  |
| status | 否 | int | 状态 | 状态 0-禁用，1-在用，2-到期 |
| page | 否 | int | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数量 | 默认为：20，最大为：500 |
| detailDataFlag | 否 | boolean | *得到详细数据标志，true\|需要* |  |

- 返回结果

```JSON
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "current": 1,           //    当前页
        "pages": 42,            //    可用总页数
        "records": [
             {
                "cardCode": "",                             //    编号
                "disabledFlag": false,                      //    是否禁用
                "endDate": null,                            //    到期时间
                "id": "01bfaa998a7dd6cf84611b92e1d9302b",   //    数据id
                "cardName": "子次卡1",                       //    名称
                "showName": "",                             //    展示名称
                "startDate": null,                          //    开始时间
                "cardStatus": "IN_USE",                     //    状态
                "statusName": "在用" ,                      //    状态中文名称  
                "totalPrice": 100.00,                        //    售价
                "typeId": "2971f98c6ccbbf86d45db7870af470f1"    //    分类id
                "projectList":[
                    {
                      "id":"aasdfasf34557",//次卡子项唯一标识
                      "projectId":"sdfasdfae"//次卡项目id
                    }
                ]
            }
        ],
        "searchCount": false,
        "size": 2,              //    当前页大小
        "total": 84             //    总记录数
    }
}
```

### [获取次卡分类树](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#NgnedDSlWoq3RSx8SpOc7ksFned)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/time-card-type-tree    GET**

![图片展示的是一个API接口请求配置界面。请求方式为GET，URL为127.0.0.1:60000/api/v1/tpos/basic/time-card-type-tree?tenantId=1。在Params标签下，有tenantId、status、name、typeId四个参数，其中tenantId和status已勾选，status值为1，name值为1231，typeId值为5ad43448...。该图片与文档中获取次卡分类树的API请求相关，直观呈现了请求参数的设置情况。](https://feishu.cn/file/BQoybJ4nQorocGxx2IRcmoHSnmc)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | TRUE | string | 要查询的门店id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": [{
                    "children": [{                                         //    子分类列表
                                "id": "96f519df42b740d8b9ecee71dfd65875",  //    分类id
                                "title": "儿牙矫正类1",                     //    分类名称
                            },
                            {
                                "id": "d468bc467dac4a8f9c5814b91b16a839",
                                "title": "儿牙矫正类2",
                            }
                    ],
                    "id": "015471e82d1e4f949690475505fdfb37",
                    "title": "整形外科",
                },
                {
                    "children": [],
                    "id": "26c937f751f84c52924073644a2a7051",
                    "title": "执行层",
                }
        ]
}
```

### [次卡详情信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#DayUdDE6oojHJtxePgwc1dgvnCb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/time-card-detail    GET**

![图片展示的是Postman工具中获取次卡详情信息的API请求界面。请求方式为GET，URL为127.0.0.1:60000/api/v1/tpos/basic/time-card-detail，带有id参数。参数部分显示了id、name、typeid三个参数，其中id参数已勾选且值为00d9375d6f629b3526948948b5091a8b，name和typeid参数未勾选。右侧Response区域显示了返回结果，包含id、name、typeid等字段信息。该图片与文档中获取次卡详情信息的API请求内容对应，直观呈现了请求参数设置情况。](https://feishu.cn/file/WNbgbnD4Bo8icox4km8c0IDRnMd)



- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 套餐id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": {
            "cardName": "111",
            "totalPrice": 666.00,
            "projectList":[{
                "projectId": "",             //    项目id
                "projectName": ""            //    项目名称
            }]
        }
}
```

## 物料

### [获取物料信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#GqzMdWRo1ohvwkx0u1qc0tTCnxI)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/material-page  GET**

![图片展示的是睿美云开放接口基础中获取物料信息的接口请求及返回结果界面。上方请求URL为192.168.2.133:60003/api/v1/tpos/basic/project-page?tenantId=1&name=测试有效，下方参数栏有tenantId、name、typeId、status等字段，其中tenantId和name已勾选。下方返回结果部分显示code为18990，data中包含code、count、current、maxList、total等信息，pages为1，records包含物料id、物料名称、物料价格、物料编码、物料开始时间、物料状态、物料类型等字段，total为1。](https://feishu.cn/file/GMihbJCN4oMWuHx3sNfcqX7SnOd)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |
| typeId | 否 | string | 项目分类id |  |
| name | 否 | string | 项目名称 |  |
| status | 否 | int | 状态 | 状态 0-禁用，1-在用 |
| page | 否 | int | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数量 | 默认为：20，最大为：500 |

- 返回结果

```JSON
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "current": 1,           //    当前页
        "pages": 42,            //    可用总页数
        "records": [
             {
                "anotherName": "",                            //    物料别名
                "disableFlag": false,                         //    是否禁用(true = 禁用)
                "drugFlag": false,                            //    是否医药物（true=是）
                "id": "9d6cdc30cb084d2b90abf72a2ccf9b96",    //    数据id
                "inventory": 1000.00,                        //    库存量
                "materialCode": "WL2023052276458",           //    编码
                "minUnit": "1",                              //    最小单位
                "name": "123123",                            //    物料名称
                "remark": "",                                //    备注
                "sellFlag": 0,                               //    是否销售（1= 销售）
                "sellingPrice": null,                        //    售价
                "specification": "123",                      //    规格
                "typeId": "13f90265360c65f5a36b2e8e9b143f72",    //    分类
                "unit": "1",                                  //    物品单位
                "typeName":"口服类"                            //物料分类名称
            }
        ],
        "searchCount": false,
        "size": 2,              //    当前页大小
        "total": 84             //    总记录数
    }
}
```

### [获取物料分类树](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#EUPDd52voo3Mqzx3B5ccwX41n3n)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/material-type-tree    GET**

![图片展示的是一个接口测试工具界面，用于获取物料分类树。请求方式为GET，URL为127.0.0.1:60000/api/v1/tpos/basic/material-type-tree?tenantId=1。在“Params”标签下，有tenantId、status、name、typId四个参数，其中tenantId值为1，status、name、typId为空。右侧Body区域显示了返回结果，包含“code”和“data”两个字段。该图片与文档中获取物料分类树的接口请求内容对应，直观呈现了参数设置及返回结果情况。](https://feishu.cn/file/I7D8blG9OojDK9x8wAXcgM2Pneu)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": [{
                    "children": [{                                         //    子分类列表
                                "id": "96f519df42b740d8b9ecee71dfd65875",  //    分类id
                                "title": "儿牙矫正类1",                     //    分类名称
                            },
                            {
                                "id": "d468bc467dac4a8f9c5814b91b16a839",
                                "title": "儿牙矫正类2",
                            }
                    ],
                    "id": "015471e82d1e4f949690475505fdfb37",
                    "title": "整形外科",
                },
                {
                    "children": [],
                    "id": "26c937f751f84c52924073644a2a7051",
                    "title": "执行层",
                }
        ]
}
```

### [物料详情](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#O1UJdEoYioEhdcxZQP0cJ47cn4c)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/material-detail       GET**

![图片展示了Postman中“物料详情”接口的请求参数设置界面。请求方式为GET，URL为http://localhost:8080/api/v1/tpos/basic/material-detail?id=000857db44914f5aa258569a8715812f 。参数部分，Key为id，Value为000857db44914f5aa258569a8715812f 。该图片与文档中“物料详情”接口的获取物料信息部分相关，直观呈现了接口请求时所需的关键参数设置情况。](https://feishu.cn/file/VxJtbLtUIo9QSZxa8eXc0NzDnuc)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 物料id |  |

- 返回结果

```json
{
    "code": 10000,
    "data": {
        "anotherName": "",                           //物料别名
        "disableFlag": false,                        //是否禁用(true = 禁用)
        "drugFlag": false,                           //是否医药物（true=是）
        "id": "000857db44914f5aa258569a8715812f",    //物料id
        "inventory": 0.00,                           //库存量
        "materialCode": "WL2023092606852",           //物料编码
        "materialUnitDTOList": [                     //物料单位换算
                {
                    "materialId": "物料Id",
                    "originUnit": "物料小单位字典",
                    "originUnitName": "物料小单位名称",
                    "originUnitScale": "物料大单位字典",
                    "changeUnit": "物料单位比例，10支(小单位)=1盒(大单位)",
                    "changeUnitName": "物料大单位名称"
                }
            ],                   
        "minUnit": "1",                              //最小单位
        "name": "测试物料下发10122111111111",         //物料名称
        "remark": "",                                //备注
        "sellFlag": 0,                               //是否销售（1= 销售）
        "sellingPrice": null,                        //售价
        "specification": "00-0",                      //规格
        "typeId": "4f6e53f70de240329461d14d3cfd9eac",  //物料分类id
        "typeName": "",                                //物料分类名称
        "unit": "1"                                    //物品单位
    },
    "msg": "操作成功"
}
```



## 会员权益

### [1.会员权益列表（会员等级](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#ZxTBdYFE6orGyzxpDXScQoO1nag)[）（弃用）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#ZxTBdYFE6orGyzxpDXScQoO1nag)

- **请求URL**

**/api/v1/tpos/basic/member-level-info        GET**

![图片展示的是睿美云开放接口中会员权益列表（会员等级）的GET请求参数设置界面。请求URL为127.0.0.1:60000/api/v1/tpos/basic/member-level-info?tenantId=1。参数部分，tenantId值为1，status、name、typelD等参数未勾选。该图片与文档中介绍会员权益列表（会员等级）接口的上下文对应，直观呈现了接口请求时需设置的参数信息。](https://feishu.cn/file/THOgbnHoKoCEKaxqCCIc0XwQnvW)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |

- **返回结果**

```JSON
{
        "code":"int",
        "msg":"string",
        "data":[
            {
                "endScoreRange": null,                       //    结束等级积分
                "feedbackDeny": "[0,1,2,7]",                 //    积分回馈率禁止来源 0：运营媒体，1：市场渠道，2和7：都是老带新（2是客户端定义的老带新，7是app老带新）
                "feedbackPower": 2.1,                        //    回馈倍率 - 积分回馈率
                "id": "0900f8ef42244b74a0dcbdd1096253e1",    //    数据id         
                "memberLevelName": "高级会员",                //    权益名称
                "specificDiscount": 5.5,                     //    支付折扣-具体折扣
                "startScoreRange": 5001                      //    起始等级积分
            },
            {
                "endScoreRange": 5000,
                "feedbackDeny": "[]",
                "feedbackPower": null,
                "id": "373fc875a9834f55a67f7e07b1e669b9",
                "memberLevelName": "普通会员",
                "specificDiscount": 3.00,
                "startScoreRange": 0
            }
            .....
        ]
}
```

### [2.会员权益列表（会员等级）（完整版）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Vhv1dbLONoVzLCxNiZJcUJJAnxe)

- **请求URL**

**/api/v1/tpos/basic/member-level-review        GET**

- 对应功能

![图片展示的是会员等级的会员权益配置界面。左侧有“会员等级”“会员任务”“会员规则”“权益配置”四个选项，当前选中“会员等级”。右侧显示会员卡权益配置，有“会员卡启用配置”和“会员卡权益配置”两个部分。会员卡权益配置中，从上至下依次为普通会员、一星、二星、三星，每个会员等级前都有皇冠图标，右侧标注“享受权益”。该图片与文档中会员权益列表（会员等级）功能对应，直观呈现了不同会员等级的权益配置情况。](https://feishu.cn/file/LO84bET4Noz128xmlaBcYOexn34)



![图片展示了睿美云开放接口中会员权益列表（会员等级）完整版的GET请求示例。请求URL为http://localhost:8080/api/v1/tpos/basic/member-level-review?tenantId=1，参数tenantId为必填项，类型为string。返回结果中包含“memberLevelName”“startScoreRange”等字段，如“memberLevelName”为“8080会员”等，还包含“memberLevelReviewDTOList”列表，其中包含“briefType”“equityBrief”“equityCode”等字段，如“briefType”为null等。该图片与文档中会员权益列表（会员等级）完整版的请求URL及参数说明对应，直观呈现了请求及返回结果。](https://feishu.cn/file/XShKboI5kozwKwxKpfTc8Gpcn9b)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |

- 返回结果

```json
{
    "code": 10000,
    "data": [
        {
            "endScoreRange": null,   //成长值范围结束值
            "id": "195551154208243713",       //会员等级id
            "memberLevelEquityDTOList": [
                {
                    "briefType": null,
                    "equityBrief": "积分回馈倍率",   //权益简介
                    "equityCount": 1.50,      //值，不同权益对应的含义值不同
                    "name": "积分回馈倍率",    // 权益名
                    "showName": "积分回馈倍率",   // 展示名称
                    "supplement": [  // 补充信息，不同权益补充说明不同
                        {
                            "name": "积分回馈率禁止来源",  //补充信息名称
                            "remark": "[0,1,2,7],0:运营媒体；1：市场渠道；2/7：老带新",  //补充信息备注
                            "value": "[]"   //补充信息值
                        }
                    ],
                    "useFlag": true   // 使用状态：true使用中，false未使用
                }
            ],
            "memberLevelName": "0205会员",  //会员等级名称
            "startScoreRange": 10000021     //成长值范围开始值
        }
    ],
    "msg": "操作成功"
}
```





### [3.会员权益的固定奖励](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#QZfBd37F6oCNznxStgZctpShnTd)

- 请求URL

**/api/v1/tpos/basic/member-task    GET**

- 对应功能

![图片展示的是睿美云开放接口中会员权益的会员任务页面。页面上方有“会员等级”“会员任务”“会员规则”“权益配置”四个选项卡，当前选中“会员任务”。会员任务部分有“有效消费1元”“有效消费1次”“完善个人信息”“完善我的兴趣”“线上首次消费”等任务选项，部分任务前有勾选框。下方有“赠送积分”“赠送成长值”“赠送时间配额”等设置项，可设置生日、倍数、假日倍数及时间配额等参数。该页面与文档中会员任务功能对应，呈现了任务设置相关内容。](https://feishu.cn/file/XIMobNo2hoNy7zxNxHHcrf6JnUf)

- 参数说明

![图片展示的是一个API测试工具界面中“Params”标签页下的参数设置区域。上方有“Params”“Authorization”“Headers (8)”“Body”“Scripts”“Settings”等标签。参数设置区域中，“Key”和“tenantId”两个参数被勾选，对应的Value分别为“1”和“1”，下方还有未被勾选的“Key”和“Value”字段。该图片与文档中“会员权益列表（会员等级）”的参数说明部分对应，直观呈现了参数设置情况。](https://feishu.cn/file/QGEObSKk9o9LbRxeFRDc3wtKnP4)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |

- 返回结果

```json
{
    "code": 10000,
    "data": {
        "costScoreType": 1,    //赠送类型（1：缴费时结算，2：消费时结算，3：划扣时结算）
        "task": [
            {
                "taskName": "有效到院1次",    //任务名称
                "taskFlag": 1,    //任务是否开启(0:未开启，1:已开启)
                "enjoyFeedbackPower": false,    //是否不享受【会员权益】积分回馈率(true:不享受，false:享受)
                "arrivalDates": [1,2],    //到院日期配置（整型数组。1：周一，2：周二，3：周三，4-周四，5-周五，6-周六，7-周天）
                "scoreCount": 0.00,    //赠送积分数量
                "description": "您每次到院后，可获取积分奖励",    //赠送积分描述
                "birthdayTimes": 1.00,    //积分生日倍数
                "expBirthdayRecognition": "WEEKS",    //生日赠送成长值时对生日范围的认定(DAYS:生日当天，WEEKS:生日当周，MONTHS:生日当月)
                "holidayTimes": 1.00,    //积分节日倍数
                "holidays": [{    //积分假日配置
                    "dateStart": 1705420800000,    //开始时间
                    "dateEnd": 1705507200000,   //结束时间
                    "name": "小年"    //名称
                }],    
                "expCount": 0.00,    //赠送成长值数量
                "expDescription": "您每次到院后，可获取成长值奖励",    //赠送成长值描述
                "expBirthdayTimes": 1.00,    //成长值生日倍数
                "scoreBirthdayRecognition": "MONTHS",    //生日赠送积分时对生日范围的认定(DAYS:生日当天，WEEKS:生日当周，MONTHS:生日当月)
                "expHolidayTimes": 1.00,    //成长值节日倍数
                "expHolidays": [{    //成长值假日配置
                    "dateStart": 1705420800000,    //开始时间
                    "dateEnd": 1705507200000,   //结束时间
                    "name": "小年"    //名称
                }]    
            }
        ]
    },
    "msg": "操作成功"
}
```

### [4.会员规则](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#LrjVdtSYwo7tNBxD8gRcVbY6n9b)

- 请求URL

`/api/v1/tpos/basic/member-rules`     `get`

- 对应功能

![图片展示的是睿美云开放接口中会员权益的会员规则页面。页面左侧有“会员等级”“会员任务”“会员权益”三个选项卡，当前选中“会员规则”。右侧是成长值配置，包含降级规则和换退规则。降级规则有“降级为降级到上一等级的”“最低成长值”“适用全部门店”选项，其中“连续365天未获得5000点成长值”被选中。换退规则有“退单不退成长值”“退单退款规则”“单笔退款后，再次下单不再属于单笔”“单笔退款后，再次下单依然属于单笔”选项，其中“退单退款规则”被选中。](https://feishu.cn/file/TONJbP06Vo0gmhxkP3KcEayNn5e)

- 参数说明

![图片展示的是会员规则接口的请求参数界面。请求方式为GET，URL为https://xxxxx/api/v1/tpos/basic/member-rules?tenantId=1。参数部分，Key和tenantId字段被勾选，Value分别为Key和1。该图片与文档中“会员规则”接口请求URL对应，直观呈现了接口请求时所需的关键参数配置情况。](https://feishu.cn/file/BvJrbTTk6o7jUlxGQeOcuOgnncb)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "integral": {   //积分规则
            "scoreClear": {      //积分清零规则
                "resetSetting": 4,//清零设置（1不清零，2自然年清零上一年积分，3自然年清零所有积分，4自定义清零时间）
                "clearScoreMonth": null,   //清空积分月，每年几月
                "resetTimeType": 1,        //清空积分时间类型（1：年 2：月 3：日）
                "resetTimeNum": 3,         //自定义清空积分时间数值，单位对应字段为resetTimeType
                "clearScoreDay": null,     //清空积分日，每年几月的几日
                "scoreClearMindDay": 6     //积分清空提前多少天提醒
            },
            "deduction": {           //积分抵扣规则
                "discountScore": 1,               //可抵扣金额对应的积分数额
                "discountFlag": true,             //是否可以抵扣
                "discountMoney": 1.00,            //积分抵扣对应的金额（元）
                "scrmOrderNotAllowed": false,     //小程序订单是否享受积分抵扣
                "discountRatio": 100.00           //积分一次性抵扣订单金额最大百分比
            },
            "refundScore": {   //退换规则
                "refundFirstScoreFlag": false,    //退换是否退积分
                "refundScoreFlag": true           //退换后是否首单送积分
            }
        },
        "growthValue": {     //成长值规则
            "downDay": {     //每天扣除成长值规则
                "downExtFlag": true,   //是否配置每天降低成长值
                "downExtCount": 10,    //每天降低的成长值数值
                "downExtDay": 10,      //连续多少天未登录降低成长值，则开始每天扣除对应成长值
                "downExtLine": 10,     //多少天未获得此成长值，则开始降低成长值
                "downExtLineDay":10    //对应天数未获得一定成长值，则开始降低成长值
            },
            "refundExt": {     //退换规则
                "refundExtFlag": false,   //退换是否退成长值
                "refundFirstExtFlag": false   //退换后再次下单，是否属于首单
            },
            "downRules": {   //降级规则
                "downLevelFlag": true,   //是否配置降级
                "downLevelType": 1,    //降低等级后新等级的成长值（1:最高成长值 2：最低成长值）
                "downLevelDay": 100,   //多少天未登录降级配置
                "downLevelExt": 100,   //多少天未获取到对应成长值降级配置
                "downLevelExtDay": 100,   //对应天数未获的一定成长值则进行降级处理
                "downLevelPayTimesNum": 10,   //连续多少天消费次数未满多少次
                "downLevelPayDaysNum": 10,    //连续消费次数未满多少次配置的多少天
                "payWayList": [0,1,2]      //连续多少天消费，包括有那些支付类型；0：实收消费；1：虚拟金支付；2：储值消费
            },
            "range": {   //会员等级计算范围
                "memberLevelScope": 5,      //会员等级计算范围数值
                "memberLevelDate": 2        //会员等级计算时间（1:年，2:月,3:日）
            },
            "protectionLevel": [    //会员等级保护规则
                {
                    "consumptionAmount": 10,        //累计消费金额  这个字段和consumptionNum互斥
                    "consumptionNum": 1,            //累计消费次数  这个字段和consumptionAmount互斥
                    "memberLevelId": "995d0ea0379249f1bc219f4f0abf5e3b",    //会员等级Id
                    "relation": 1,            //规则之间的关系（且：1/或：0）
                    "relegationFlag": true,          //是否配置了保级
                    "timeNum": 300,           //时间类型对应的值
                    "timeType": 1            //时间类型（1:年，2:月,3:日）
                }
            ]
        }
    },
    "msg": "操作成功"
}
```

## 供应商

### [获取供应商信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#LJ8edXin5o8m7DxlAwic3dBynEf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/supplier-page  GET**

![这张图片展示的是睿美云开放接口中“获取供应商信息”接口的实际请求与响应示例。左侧显示请求信息：请求方式为GET，请求路径为/api/v1/tpos/basic/supplier-page，Query Params中携带必填参数tenantId的值为1，满足该接口的鉴权与参数要求。右侧为响应结果，以JSON格式呈现，包含code、data等字段，data内又有current、totalizeCount等参数，且result中显示了如accruingPurchaseMoney、approveFlag等供应商相关的各类数据字段，对应了该接口返回供应商信息的功能。](https://feishu.cn/file/BoI1b6pWQoyaMaxL1hacLS3Onub)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 要查询的门店id |  |
| typeId | 否 | string | 供应商分类id |  |
| name | 否 | string | 供应商名称 |  |
| enableFlag | 否 | boolean | 是否启用 | true = 启用 |
| page | 否 | int | 当前页码 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数量 | 默认为：20，最大为：500 |

- 返回结果

```JSON
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "current": 1,           //    当前页
        "pages": 42,            //    可用总页数
        "records": [
             {
                "id": "b759b156d99947fa94d47484be7d4f45",    //    数据id
                "name": "夏季供应商内部",                     //    供应商名称
                "typeId": "9190d6b84b4b4a93947d404b2954e760",    //    分类id
                "typeText": "区域的分类1",                        //    分类名称
                "materialCount": "2",                        //    供应物料数
                "supplierContactId": "外部联系人1,外部联系人2",    //    联系人
                "createDate": 1694569977000,                //    创建时间
                "enableFlag": true                            //   是否启用 true是启用 
            }
        ],
        "searchCount": false,
        "size": 2,              //    当前页大小
        "total": 84             //    总记录数
    }
}
```

### [获取供应商分类树](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#FwPGdRBnXoQSWTxENmDcUIBanGf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/basic/supplier-type-tree    GET**

![图片展示的是睿美云开放接口获取供应商分类树的返回结果界面。上方显示请求URL为“127.0.0.1:60005/api/v1/tpos/basic/supplier-type-tree?tenantId=1”，下方参数栏中tenantId值为1。右侧Body区域以JSON格式呈现返回数据，包含“code”“data”等字段，其中“data”字段下有“canEdit”“children”等信息，如“children”字段下包含多个分类对象，每个对象有“canEdit”“children”等属性，部分属性值如“canEdit”为false，“children”为空数组。该图片与文档中获取供应商分类树接口的返回结果部分对应，直观呈现了接口返回数据情况。](https://feishu.cn/file/NPRob5Dezo927Ux7GJAc3mtcnNc)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |

- 返回结果

```JSON
{
        "msg": "成功获取数据，数据非空",
        "code": 10001,
        "data": [{
                    "children": [{                                         //    子分类列表
                                "id": "96f519df42b740d8b9ecee71dfd65875",  //    分类id
                                "title": "夏季供应商",                     //    分类名称
                            },
                            {
                                "id": "d468bc467dac4a8f9c5814b91b16a839",
                                "title": "冬季供应商",
                            }
                    ],
                    "id": "015471e82d1e4f949690475505fdfb37",
                    "title": "外部供应商",
                },
                {
                    "children": [],
                    "id": "26c937f751f84c52924073644a2a7051",
                    "title": "内部供应商",
                }
        ]
}
```



# 字典（sysdict）

## [通过字典类型和门店获取字典](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#WAWSdwqKeoKQysxEHpqc1oTHnVe)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/sysdict/dictlist    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| code | 是 | string | 字典code |  |
| tenantId | 是 | string | 门店id |  |

![图片展示的是睿美云开放接口中字典（sysdict）获取字典的API调用界面。请求URL为127.0.0.1:60000/api/v1/tpos/sysdict/dictlist，参数包括code、tenantId等。下方返回结果以JSON格式呈现，包含code、ext、name、num、old、status、value等字段，如code为10000，ext为“F7F038E”，name为“诊病”，num为1，old为“1”，status为1，value为“1”。该图片与文档中介绍的字典获取API请求及返回结果内容相关，直观呈现了API调用及返回数据情况。](https://feishu.cn/file/MVX8bzuOuohpd3xq4ITcss9lnxg)

- 返回结果

```JSON
{
    "code": 10000,
    "data": [
        {
            "code": "clinicType",        //    字典code
            "ext": "#79D38E",            //    额外扩展字段，各个领域定义不同
            "name": "咨询",              //    字典名称
            "num": 1,                    
            "pid": "0",
            "remark": "",
            "status": 1,                //    是否启用
            "value": "1"                //    属性值
        },
        {
            "code": "clinicType",
            "ext": "#222222",
            "name": "测试用",
            "num": 0,
            "pid": "0",
            "remark": "",
            "status": 1,
            "value": "11"
        }]
}
```

# 库存（inventory）

## 入库管理

### [入库管理分页数据](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Bi1gdtb4xocnbtxW73HcSg1Hn3d)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/inventory/storage-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |
| page | 否 | int | 当前页 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |
| materialName | 否 | string | 物料名称 |  |
| storageNumber | 否 | string | 入库单号 |  |
| sDate | 否 | string | 入库时间-开始日期 | yyyy-MM-dd |
| eDate | 否 | string | 入库时间-结束日期 | yyyy-MM-dd |

![这张图片展示的是睿美云开放接口“入库管理分页数据”的API测试界面，左侧是该GET接口的请求参数区域，已勾选并填充了必填的tenantId参数为RK2023，同时填充了非必填参数，包括page为1、size为2、materialName为“绿色棉布”、sDate为2023-11-01、eDate为2023-12-...。右侧是API返回的JSON格式结果，显示返回码为10000，成功请求的相关数据，包含分页信息、入库单相关配置字段以及具体的入库单状态“待审核”等内容，对应该接口的参数说明与返回结果内容。](https://feishu.cn/file/X5ohbTFMNoNA9fxoNTRcsszRnwd)

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "countId": "",
        "current": 1,
        "maxLimit": null,
        "optimizeCountSql": true,
        "orders": [],
        "pages": 1,
        "records": [
            {
                "id": "f88a24fcd7bc4016aaccfb11fda6c7ca",        //    入库单id
                "originCreateDate": 1678436713000,      //   创建时间
                "createDate": 1702280443000,            //   入库时间
                "storageNumber": "RK202311273903",      //    入库单号
                "storageSum": 9080.0000,
                "type": "1",                      //    入库类型
                "typeText": " 采购入库",            //    入库类型-中文
                "deptText": "集团",                //    部门id
                "warehouseId": "dfad47e789544aec36d0b95ffba2159b"    //    仓库id
                "warehouseText": "香克斯"                            //    仓库名称,
                "approvalStatus": 2,              //    审批状态
                "approvalStatusText": "已完成",    //    审批状态-中文
            }
        ],
        "searchCount": true,
        "size": 2,
        "total": 1
    },
    "msg": "操作成功"
}
```



### [入库详情数据](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#PsR5dgk4noPP7SxqMOucJb31nMd)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/inventory/storage-info    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 入库单id |  |

![图片展示的是睿美云开放接口中“入库管理”下的“入库详情数据”接口的请求与返回结果界面。左侧为Postman工具界面，显示GET请求，URL为/api/v1/tpos/inventory/storage-info?id=f88a24fcd7bc4016aaccfb11fda6c7ca，参数栏有id值。右侧为返回结果，以JSON格式呈现，包含code、data等字段，其中data字段下有allSuppliers、approvalFlag、approvalRecord等信息，还展示了审批记录详情，如审批人、审批结果、审批时间等。](https://feishu.cn/file/Xa7WbrKLpoSOJFxiKqwcTWc1nKc)

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "id": "f88a24fcd7bc4016aaccfb11fda6c7ca",    //    入库单id
        "storageNumber": "RK202303100301",          //    入库单号
        "warehouseId": "dfad47e789544aec36d0b95ffba2159b",    //    仓库id
        "warehouseText": "香克斯"                              //    仓库名称
        "departmentId": "1ff1c932d8e4484687abe9052b021966",    //    部门id
        "deptText": "护理部",                                  //    部门名称
        "responsibleId": "1",                                //    入库操作人id
        "responsibleText": "超级管理员",                      //    入库操作人名称
        "type": "1",                                        //    操作类型
        "typeText": "采购入库",                              //    操作类型-中文
        "createDate": 1678436713000,                        //    入库时间
        "storageMaterialResList": [
            {
                "materialCode": "WL296339",                        //    物料编码
                "materialId": "f65a868a0182e00e1a98d90f1224c7b6",    //    物料id
                "name": "物料M",                                    //    物料名称
                "storageAmount": 100.00,                            //    入库量
                "storageUnit": "支",                                //    入库单位
                "storageSum": 2000.0000,                            //    合计金额
                "supplierId": "128173894967230466"                //    供应商id
                "supplierText": "供应商张",                         //    供应商名称，
                "purchasePrice": 20.0000,                            //    实际进价
                "purchasePriceUnit": "4",                            //    实际进价单位（需要在unitList中匹配）
                "unitList": [                                        //    单位数据匹配
                    {
                        "label": "包",          //    展示名称
                        "uId": "5",             //    可以对应【purchasePriceUnit】字段
                    },
                    {
                        "label": "支",
                        "uId": "1"
                    },
                    {
                        "label": "箱",
                        "uId": "4"
                    },
                    {
                        "label": "发",
                        "uId": "8"
                    }
                ]
            }
        ]
    },
    "msg": "操作成功"
}
```



### [入库新增](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#IKZGdzKtEoaGm3xSqs0chVbjnBg)

- 请求URL（需要tpos鉴权）

/api/v1/tpos/inventory/storage-add

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |
| departmentId | 是 | string | 部门id |  |
| responsibleId | 是 | String | 操作人id |  |
| type | 是 | string | 入库类型 |  |
| tenantId | 是 | string | 门店id |  |
| remark | 是 | string | 备注 | 主表的备注 |
| warehouseId | 是 | string | 仓库id | 下面所有字段，都是子表请求参数 |
| remark | 是 | string | 备注 | 单个物料的备注 |
| purchasePrice | 是 | Bigdecimal | 进价 |  |
| purchasePriceUnit | 是 | string | 进价单位 |  |
| storageAmount | 是 | Bigdecimal | 入库数量 |  |
| storageUnit | 是 | string | 入库单位 |  |
| manufacturerId | 否 | string | 厂家id |  |
| supplierId | 否 | string | 供应商id |  |
| batchNumber | 否 | string | 批次号 |  |
| validityPeriod | 否 | string | 有效期 |  |
| materialId | 是 | string | 物料id |  |

【注】入库类型，需要调数据字典查询接口 code=storageType



- 请求参数示例

```JSON
{
    "departmentId": "9e950e33d7a6523412946352fc835368",
    "responsibleId": "5233a6d1124eec029ba621060f7b4f7e",
    "type": "1",
    "tenantId": "1",
    "storages": [
        {
            "warehouseId": "211866598619742210",
            "storageMaterialList": [
                {
                    "remark": "",
                    "purchasePrice": 50,
                    "purchasePriceUnit": "1",
                    "storageAmount": 20,
                    "storageUnit": "1",
                    "manufacturerId": "",
                    "supplierId": "125612282423017474",
                    "batchNumber": "1010",
                    "validityPeriod": "2028-04-12 23:59:59",
                    "materialId": "b2e7467d-a757-4c4d-9be6-0b4fe83"
                }
            ]
        }
    ],
    "remark":""
}
```

- 操作成功返回结果

```JSON
{
    "code": 10000,
    "data": {
        "id": "291885063346323456", //storage表的id
        "storageMaterialList": [
            { 
                "id": "291885099509612546" //storage_material表的id
            }
        ],
        "storageNumber": "RK202410283017" //入库单号
    },
    "msg": "操作成功"
}
```

- 操作失败返回结果

```JSON
{
    "msg": "仓库不存在",
    "code": 20002,
    "data": null
}

```

### [入库修正（需要tpos鉴权）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#VImOdXbiJoiuaVx4X0rcJExznte)

- 请求URL

/api/v1/tpos/inventory/storage-update

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 入库单id |  |
| userId | 是 | string | 修正人id |  |
| tenantId | 是 | string | 门店id |  |
| departmentId | 是 | string | 部门id |  |
| responsibleId | 是 | String | 入库操作人id |  |
| type | 是 | string | 入库类型 |  |
| tenantId | 是 | string | 门店id |  |
| remark | 否 | string | 备注 | 主表的备注 |
| warehouseId | 是 | string | 仓库id | 下面所有字段，都是子表请求参数 |
| remark | 否 | string | 备注 | 单个物料的备注 |
| purchasePrice | 是 | Bigdecimal | 进价 |  |
| purchasePriceUnit | 是 | string | 进价单位 |  |
| storageAmount | 是 | Bigdecimal | 入库数量 |  |
| storageUnit | 是 | string | 入库单位 |  |
| manufacturerId | 否 | string | 厂家id |  |
| supplierId | 否 | string | 供应商id |  |
| batchNumber | 否 | string | 批次号 |  |
| validityPeriod | 否 | string | 有效期 |  |
| materialId | 是 | string | 物料id |  |

- 请求参数示例

```JSON
{
    "id": "1dsdf46456s4dfsd54f6sd5f4s56f4sd5f4evry",
    "departmentId": "9e950e33d7a6523412946352fc835368",
    "responsibleId": "5233a6d1124eec029ba621060f7b4f7e",
    "type": "1",
    "userId":"12465454645646dfsf45645674re6r4wer56",
    "tenantId": "1",
    "storages": [
        {
            "warehouseId": "211866598619742210",
            "storageMaterialList": [
                {
                    "remark": "",
                    "purchasePrice": 50,
                    "purchasePriceUnit": "1",
                    "storageAmount": 20,
                    "storageUnit": "1",
                    "manufacturerId": "",
                    "supplierId": "125612282423017474",
                    "batchNumber": "1010",
                    "validityPeriod": "2028-04-12 23:59:59",
                    "materialId": "b2e7467d-a757-4c4d-9be6-0b4fe83"
                }
            ]
        }
    ],
    "remark":""
}
```

- 操作成功返回结果

```JSON
{
    "code": 10000,
    "data": {
        "id": "291885063346323456", //storage表的id
        "storageMaterialList": [
            { 
                "id": "291885099509612546" //storage_material表的id
            }
        ],
        "storageNumber": "RK202410283017" //入库单号
    },
    "msg": "操作成功"
}
```

- 操作失败返回结果

```JSON
{
    "msg": "入库单已作废，不支持修正",
    "code": 20002,
    "data": null
}

```

### [入库撤销（需要tpos鉴权）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Svq1dONZtop3pDxjwMsctwdFnhh)

- 请求URL

/api/v1/tpos/inventory/storage-undo

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
|      userId |  是 | String | 撤销人id |  |
| id | 是 | String | 入库单id |  |

- 请求参数示例

```JSON
{
    "id": "285437921001996290"
}
```

- 操作成功返回结果

```JSON
{
    "code": 10000,
    "data": null,
    "msg": "操作成功"
}
```

- 操作失败返回结果

```JSON
{
    "msg": "撤销将导致物料【药尘】库存量为负值，无法撤销",
    "code": 20002,
    "data": null
}

```



## 出库管理

### [分页获取仓库信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Ot8gdO3kkoVS9yxSoo0cES83nzf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/inventory/warehouse-page    GET**

![图片展示了睿美云开放接口中出库管理分页获取仓库信息的GET请求示例。请求URL为http://localhost:8080/api/v1/tpos/inventory/warehouse-page，需tpos鉴权。参数包括tenantId（必填，门店id）、page（可选，当前页，默认1，最小1）、size（可选，每页数据大小，默认20，最大500）。返回值示例中，code为10000，data包含仓库信息，如仓库id、名称、地址、默认标志等，还列出仓库管理员信息。该图片与上下文介绍的接口请求和参数说明紧密相关，直观呈现了接口调用情况。](https://feishu.cn/file/QvdGbUxjqoBTxoxkkeacxQnBn9f)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |
| page | 否 | int | 当前页 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |

- 返回值

```JSON
{
    "code": 10000,
    "data": [
        {
            "address": "",           //仓库地址
            "defaultFlag": false,    //是否默认仓库
            "departmentList": [  // 所属部门
                {
                    "id": "6f2da0369d94420d86ee8537a576c178",
                    "name": "皮肤美容"
                },
                {
                    "id": "d34fe485b8d54501abbbd46558e8a4a8",
                    "name": "注射美容"
                }
            ],
            "id": "01f0dd170ff6747eb7e2ca095aabb21c",
            "isSale": true,          //是否是销售仓库
            "managerList": [   // 仓库管理员
                {
                    "id": "d236f99ee0ec0dcb68bbaddc77821887",
                    "name": "施zf9"
                }
            ],
            "name": "赠品库",   //仓库名称
            "outFlag": false,    //出库是否默认
            "outInInventoryManagers": [
                 {
                    "createBy": "ba2b8cf5bb144a7eb0f6d1aabe55beba",
                    "createDate": 1717744698000,
                    "delFlag": false,
                    "id": "240131866185695235",
                    "tenantId": "1",
                    "updateBy": "ba2b8cf5bb144a7eb0f6d1aabe55beba",
                    "updateDate": 1717744698000,
                    "userId": "14ef74f9455cca79b98a105af0f8f486",  // 用户id
                    "userName": "k柒伍4",   //用户姓名
                    "warehouseId": "151734172463923226"  //仓库id
                }
             ],    // 仓库出入库管理员
            "outInInventoryManagersFlag": false,   // 仅出入库管理员可确认出入库 （打开为true）
            "status": true,    // 仓库是否可用
            "storageFlag": false,        //入库是否默认
            "tenantId": "1"   // 门店id
        }
    ],
    "msg": "操作成功"
}
```



### [出库管理分页数据](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#UEvTdEiwbotSc1xUXXscAvt1nHg)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/inventory/out-inventory-page       GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |
| page | 否 | int | 当前页 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |
| materialName | 否 | string | 物料名称 |  |
| outInventoryNumber | 否 | string | 出库单号 |  |
| sDate | 否 | string | 出库时申请间(开始日期) | yyyy-MM-dd |
| eDate | 否 | string | 出库时申请间(结束日期) | yyyy-MM-dd |
| finishStartDate | 否 | string | 出库完成时间(开始时间) | yyyy-MM-dd |
| finishEndDate | 否 | string | 出库完成时间(结束时间) | yyyy-MM-dd |

![图片展示的是Postman工具中“出库管理分页数据”接口的请求界面。请求URL为127.0.0.1:60005/api/v1/tpos/inventory/out-inventory-page，方法为GET。参数部分，page、size、sDate、eDate、materialName、outInventoryNumber、tenantId等字段均被勾选，且有具体值。响应结果部分，显示了操作成功返回的JSON数据，包含code、data、current、maxLimit、notInvalidateDetail、pages、records等字段，其中records字段下有出库单id、物料名称、物料编码、物料规格、物料单位、物料数量、物料单价、出库数量、出库金额、出库完成时间、出库单状态、出库单状态文本、审批状态、审批状态文本、审批记录、审批记录列表、审批设置、审批设置列表、审批设置名称、审批设置文本、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本列表、审批设置文本](https://feishu.cn/file/WrSSbHtbaoP3AAxuksycTlfBnqe)

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "current": 1,                        //    当前页
        "pages": 1,                          //    可用总页数
        "records": [
            {
                "createDate": 1701937119000,                //    出库申请时间
                "finishDate": 1701937119000,                //    出库完成时间
                "handleId": "5233a6d1124eec029ba621060f7b4f7e",   //    出库操作人id
                "handleName": "测试茹",                            //    出库操作人名称
                "id": "bebdde48455b42399fa830a160861669",        //    出库单id
                "outInventoryNumber": "CK202312078520",          //    出库单号
                "outBoundType": 3,                        //    出库类型
                "outBoundTypeText": "領用出庫",            //    出库类型名称
                "outSum": 10.0000,                        //    出库金额
                "recipientApplyNumber": "",                //    领用申请单号
                "recipientId": "5233a6d1124eec029ba621060f7b4f7e",         //    领用人id
                "recipientName": "测试茹",                        //    领用人名称
                "status": 1,                                     //    出库单状态
                "statusText": "已完成",                           //    出库单状态名称
                "warehouseManager": "lf",                                    //    仓库管理员名称
                "warehouseManagerId": "81d98b84d02abfa3a65a08f927d96637",     //    仓库管理员id
                "warehouseId": "dfad47e789544aec36d0b95ffba2159b",          //    仓库id
                "warehouseName": "香克斯"                                    //    仓库名称
            }
        ],
        "size": 10,                //    当前页大小
        "total": 1                //    总记录数
    },
    "msg": "操作成功"
}
```

### [出库详情数据](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#GMiJdSXHoouDJuxkzjIcpp31n2d)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/inventory/out-inventory-info    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 出库单id |  |

![这是睿美云开放接口出库详情数据接口的请求与响应截图，展示了该接口的交互信息。左侧是接口请求的Query Params区域，必填参数id已勾选，对应值为beb0be4845...；右侧是接口返回的JSON格式结果，code为10000代表操作成功，其中包含approvalFlag、approveValue等关键字段，还记录了审批相关信息，如审批人所属的““(集团)、UX（医疗）”等内容，以及resultMessage标注为“通过”。](https://feishu.cn/file/PuRUbdDdRoe5BaxmSvPcURr0nYd)

- 返回结果

实际返回结果里面在文档里面没有标注的字段，可以忽略

```JSON
{
    "code": 10000,
    "data": {
        "id": "bebdde48455b42399fa830a160861669",               //  数据id
        "outInventoryNumber": "CK202312078520",                 //  出库单号
        "warehouseId": "dfad47e789544aec36d0b95ffba2159b",      //  仓库id
        "warehouseName": "香克斯",                               //  仓库名称
        "handleId": "5233a6d1124eec029ba621060f7b4f7e",         //  出库操作人id
        "handleName": "测试茹",                                  //  出库操作人名称
        "createDate": 1701937119000,                    //    出库申请时间
        "finishDate": 1701937119000,                    //    出库完成时间
        "outBoundType": 3,                              //    出库类型
        "outBoundTypeText": "領用出庫",                  //    出库类型名称
        "deptId": "077ab6d9035640c8bd5b78d39adfa550",       //  领用部门id
        "deptName": "集团",                                  //  领用部门名称
        "recipientId": "5233a6d1124eec029ba621060f7b4f7e",  //  领用人id
        "recipientName": "测试茹",                           //  领用人名称
        "customerId": "eb19649cd6cb4784b09ac6fbd4caae12",   //  相关客户id
        "customerName": "测试王",                            //  相关客户名称
        "customerPhone": "18408234519",                     //  相关客户电话
        "outMaterialResList": [                             //  出库物料
            {
                "materialCode": "WL2019021944144",          //  物料编码
                "materialId": "5abc6954c539e9251fe9f759c9109704",   //  物料id
                "minUnitCode": "5",
                "name": "百洁擦棉（组）",                       //  物料名称
                "orderedInventoryVos": [],
                "outAmount": 1,                                 //  出库量
                "outUnit": "包",                                //  出库量的单位
                "outSum": 0.0000,                               //  合计（元）
                "outUnitCode": "5",
                "purchasePrice": 0.0000,                        //  进价
                "purchasePriceUnit": "5",                       //  进价单位（需要在unitList中匹配）
                "unitList": [
                    {
                        "label": "包",                          //  展示名称
                        "uId": "5"                              //  可以对应【purchasePriceUnit】字段
                    }
                ]
            }
        ]
    },
    "msg": "操作成功"
}
```

- 操作成功返回结果

```JSON
{
    "code": 10000,
    "data": null,
    "msg": "操作成功"
}
```

- 操作失败返回结果

```JSON
{
    "msg": "仓库不存在",
    "code": 20002,
    "data": null
}

```

### [出库新增](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#QELldOKxDo42U4x3ARhcmdFDnOb)

- 请求URL（需要tpos鉴权）

/api/v1/tpos/inventory/outInventory-add  POST

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| warehouseId | 是 | String | 仓库id |  |
| handleId | 是 | String | 出库人id |  |
| deptId | 否 | String | 领用（核销）部门id |  |
| recipientId | 否 | String | 领用（核销）人id |  |
| tenantId | 是 | String | 门店id | 出库门店 |
| outBoundType | 是 | int | 出库类型id | -1:"核销出库"  <br/>-2:"开单出库"  <br/>-3:"调拨出库"  <br/>-4:"盘亏出库"  <br/>-5:"兑换出库"  <br/>-6:"医嘱出库" |
| remark | 否 | String | 备注 | （主表备注） |
| outMaterialList | 是 |      array | 出库物料 |  |
|         inventoryId | 是 | String | 库存id |  |
|         outAmount | 是 | decimal | 出库数量 |  |
|         outUnit | 是 | String | 出库单位 |  |
|         remark | 否 | String | 备注 | （单位物料的备注） |
|         materialId | 是 | String | 物料id |  |

【注】其他出库类型，需要调数据字典查询接口 code=outboundType

- 请求参数示例

```JSON
{
    "warehouseId": "211866598619742210",
    "handleId": "5233a6d1124eec029ba621060f7b4f7e",
    "deptId": "077ab6d9035640c8bd5b78d39adfa550",
    "recipientId": "5233a6d1124eec029ba621060f7b4f7e",
    "tenantId": "1",
    "outBoundType": 3,
    "outMaterialList": [
        {
            "inventoryId": "256741564489924611",
            "outAmount": 1,
            "outUnit": "1",
            "remark": "",
            "materialId": "680783965203408786612a8f4e3e9195"
        }
    ]
}
```

- 操作成功返回结果

```JSON
{
    "code": 10000,
    "data": {
        "id": "291892183076700162",//out_inventory表id
        "outInventoryMaterialList": [
            {
                "id": "291892183823286272"//out_invnetory_material表id
            }
        ],
        "outInventoryNumber": "CK202410289957",//出库单号
    },
    "msg": "操作成功"
}
```

- 操作失败返回结果

```JSON
{
    "msg": "物料【水光针】出库量大于当前库存量，无法出库",
    "code": 20002,
    "data": null
}
```

### [出库修正（需要tpos鉴权）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#NItudwagmoXKfMxQMzFc3aU3n8e)

- 请求URL

/api/v1/tpos/inventory/outInventory-update

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | String | 出库单id |  |
| warehouseId | 是 | String | 仓库id |  |
| userId | 是 | String | 出库修正人id |  |
| handleId | 是 | String | 出库人id |  |
| deptId | 是 | String | 部门id |  |
| recipientId | 是 | String | 领用人id |  |
| tenantId | 是 | String | 门店id |  |
| outBoundType | 是 | String | 出库类型id |  |
| remark | 否 | String | 备注 | （主表备注） |
| inventoryId | 是 | String | 库存id | 下面的都是子表数据 |
| outAmount | 是 | Bigdecimal | 出库数量 |  |
| outUnit | 是 | String | 出库单位 |  |
| remark | 否 | String | 备注 | （单位物料的备注） |
| materialId | 是 | String | 物料id |  |

- 请求参数示例

```JSON
{   
    "id":"2118665914528742250",
    "warehouseId": "211866598619742210",
    "handleId": "5233a6d1124eec029ba621060f7b4f7e",
    "deptId": "077ab6d9035640c8bd5b78d39adfa550",
    "userId":"5233a6d1124eec029ba621060f7b4f7e",
    "recipientId": "5233a6d1124eec029ba621060f7b4f7e",
    "tenantId": "1",
    "outBoundType": "3",
    "outMaterialList": [
        {
            "inventoryId": "256741564489924611",
            "outAmount": 1,
            "outUnit": "1",
            "remark": "",
            "materialId": "680783965203408786612a8f4e3e9195"
        }
    ]
}
```

- 操作成功返回结果

```JSON
{
    "code": 10000,
    "data": {
        "id": "291892183076700162",//out_inventory表id
        "outInventoryMaterialList": [
            {
                "id": "291892183823286272"//out_invnetory_material表id
            }
        ],
        "outInventoryNumber": "CK202410289957",//出库单号
    },
    "msg": "操作成功"
}
```

- 操作失败返回结果

```JSON
{
    "msg": "仓库不存在",
    "code": 20002,
    "data": null
}

```





### [出库撤销（需要tpos鉴权）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#UnDcdLOTloWiuXx5qXZcQ9bJnnc)

- 请求URL

/api/v1/tpos/inventory/outInventory-undo

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | String | 出库单id |  |
| userId | 是 | String | 撤销人id |  |

- 请求参数示例

```JSON
{
    "userId": "125545674567464",
    "id": "286905093398200321"
}
```



- 操作成功返回结果

```JSON
{
    "code": 10000,
    "data": null,
    "msg": "操作成功"
}
```

- 操作失败返回结果

```JSON
{
    "msg": "仓库不存在",
    "code": 20002,
    "data": null
}

```



## 物料盘点

### [物料盘点分页数据](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#HtXbdiXltoMFB5xIGH4cLfxSnrc)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/inventory/check-inventory-page    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |
| page | 否 | int | 当前页 | 默认为：1，最小为：1 |
| size | 否 | int | 每页数据大小 | 默认为：20，最大为：500 |
| warehouseId | 否 | string | 盘点仓库id |  |
| status | 否 | string | 状态，多个用逗号隔开 | 0=盘点中，1=已完成,2=已作废 |
| createDateStart | 否 | string | 盘点创建时间-开始时间 | date-time |
| createDateStart | 否 | string | 盘点创建时间-结束时间 | date-time |

![图片展示的是睿美云开放接口中物料盘点分页数据的API调用及返回结果界面。左侧为API调用参数设置，包括tenantId、warehouseId、createDateStart、createDateEnd、status、page、size等参数，部分参数已勾选。右侧是返回结果，显示code为180006，data包含statusText、current、maxLimit、optimizeCountabl等字段，records中记录了盘点信息，如checkAmountSum、clean、createDate等，还显示了库存数据等。该图与文档中介绍的物料盘点分页数据API相关，直观呈现了API调用及返回结果情况。](https://feishu.cn/file/GRPbb1nEmoBOsBxtJegcE8SKndh)

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "current": 1,                        //    当前页
        "pages": 1,                          //    可用总页数
        "records": [
            {
                "id": "70fcd3d621ef4bbc98734c203b05d617",    //    数据id
                "inventorySum": 10.0000,                //    盘前货值
                "checkAmountSum": 9.0000,               //    盘后货值
                "deviationSum": -1.0000,                //    偏差货值
                "createDate": "2023-12-07 16:17:50",    //    创建时间
                "status": 1,                            //    状态：0=盘点中，1=已完成,2=已作废
                "statusText": "已完成",                  //    状态描述
                "updateBy": "测试茹",                    //    最后盘点人
                "updateId": "5233a6d1124eec029ba621060f7b4f7e",   //    最后盘点人id
                "updateDate": "2023-12-07 16:17:50",    //    最后盘点时间
                "warehouseId": "dfad47e789544aec36d0b95ffba2159b",    //  盘点仓库  
                "warehouseText": "香克斯"                             //   盘点仓库名称
            }
        ],
        "size": 10,                //    当前页大小
        "total": 1                //    总记录数
    },
    "msg": "操作成功"
}
```

### [物料盘点详情数据](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#ObgBdZNsfo1ZxTxXonWcraminYc)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/inventory/check-inventory-info    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |
| id | 是 | string | 数据id |  |

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "id": "6c1fbed2d1c749cd90b7c1c65c2b6cfc",        //    数据id
        "checkAmountSum": 100.0000,                      //    盘点物料价值
        "checkNumber": "PD202308220572",                 //    盘点单号
        "checkPeopleList": [                        
            {
                "name": "测试茹",                             //    盘点人
                "id": "5233a6d1124eec029ba621060f7b4f7e"     //    盘点人id
            }
        ],
        "checkRecordResList": [            {
                "name": "0822测试盘点",            //    物料名称
                "anotherName": "",                //    物料别名
                "batchNumber": "01",              //    批次
                "businessUnitId": "3",            //    业务单位 - code
                "businessUnitName": "盒",         //    业务单位 - 名称
                "checkAmount": 10.00,             //    盘点量
                "checkAmountList": [              //    可换算的单位列表
                    {
                        "label": "盒", 
                        "ratio": null,
                        "uId": "3",
                        "value": 10.00
                    },
                    {
                        "label": "支",
                        "ratio": null,
                        "uId": "1",
                        "value": 50.00
                    }
                ],
                "checkAmountSum": 100.0000,            //    盘后货值
                "checkPeople": "测试茹",                //    盘点人
                "checkUnit": "3",                      //    盘点单位 - code
                "checkUnitName": "盒",                 //    盘点单位 - 名称
                "deviation": -7.00,                    //    偏差
                "deviationValue": -70.0000,            //    偏差货值   
                "inventory": 17.00,                    //    该批次该物品的库量
                "inventoryId": "134990140790538240",   //    库存id
                "inventorySum": 170.0000,              //    库存货值
                "manufacturer": "成都市XXX有限公司",     //    生产厂家
                "materialCode": "WL2023082249427",     //    物料编码
                "materialId": "134989812330397952",    //    物料id
                "materialType": "顶级分类1/分类下2",     //    物料分类
                "specification": "古河",                //    规格
                "unitList": [                          //    编码code对应的单位换算（用uid匹配）
                    {
                        "label": "盒",
                        "ratio": 0.2000,
                        "uId": "3",
                        "value": 17.00
                    },
                    {
                        "label": "支",
                        "ratio": 1,
                        "uId": "1",
                        "value": 85.00
                    }
                ],
            }
        ],
        "createDate": 1692687720000,         //    创建时间
        "deviationSum": -70.0000,            //    偏差货值
        "inventorySum": 170.0000,            //    库存货值
        "status": 1,                         //    状态 - code
        "statusText": "已完成",               //    状态 - 名称
        "warehouseId": "dfad47e789544aec36d0b95ffba2159b",    //    盘点仓库id
        "warehouseText": "香克斯"                             //    盘点仓库名称
    },
    "msg": "操作成功"
}
```



# **预约（cusbespeak）**

## [新增预约](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#PEugdgOCWoIQOaxWo1VcrYNXnPf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/add      POST**

![图片展示的是睿美云开放接口中新增预约（cusbespeak）的POST请求示例。上方有“POST”标识及请求URL“/api/v1/tpos/cusbespeak/add”。下方是JSON格式的请求参数，包括customerId、bespeakProject、dataId、dataType、bespeakTypeValue等字段，如dataId为“00044150304406903150eefc0b30ae”。下方还显示了响应内容，code为20000，data包含“1e45954a43d044ea0033409840679a”，msg为“操作成功”。该图片与文档中新增预约接口的参数说明部分对应，直观呈现了接口请求示例。](https://feishu.cn/file/DhFYbJiu7o2Fk7xGSnjc1gHgnTf)

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| bespeakProject | 是 | array | 预约的项目/项目类型 |  |
|     +dataId | 是 | string | 项目/项目分类id |  |
|     +dataType | 是 | int | 项目：0  <br/>项目分类：1 |  |
| bespeakTypeValue | 是 | string | 就诊类型，需要参考机构的字典  <br/>（配置码：clinicType） | other代表：其他。不想参考字典的统一传other |
| bespeakUserId | 否 | string | 预约创建人 | *不传视为超级管理员* |
| startTime | 是 | string | yyyy-MM-dd HH:mm:ss |  |
| duration | 是 | int | 持续时间（分钟） | 最大值1440 |
| expertId | 是 | string | 预约专家id | 不给视为other（无指定医生） |
| tenantId | 是 | string | 门店id | 要预约的门店id |
| remark | 否 | string | 预约备注 |  |

- [注]

bespeakTypeValue需要调用接口字典，

code为clinicType

![图片展示的是睿美云开放接口中就诊类型配置界面。左侧为就诊类型配置菜单，右侧是数据详情区域，包含配置名、配置码等信息。关键内容是配置码“clinicType”下属性值列表，其中“咨询”属性值为1，颜色值为#9d8a6a，操作有编辑和新增；“治疗”属性值为2，颜色值为#77d2d2，操作同上；“复诊”属性值为3，颜色值为#a9bda，操作同上；“会诊”属性值为4，颜色值为#f0a591，操作同上；“其他”属性值为other，颜色值为#f0a5b9，操作同上。该图与上下文介绍的就诊类型配置相关，直观呈现了配置详情。](https://feishu.cn/file/boxcnoJJD9B6ugwOdcyFw3CS1af)



- 返回结果

> data会返回预约数据的id，错误信息会在msg中返回

```JSON
{
    "msg": "操作成功",
    "code": 10000,            // 只要是10000的，都是成功
    "data": "1e9554c43d8b4babb33c54b9840678a2"                    
}
```

## [修改预约](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#O2sCdkP8rog8LRxcWiXcVjKLncg)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/update    POST**

参数和新增预约一样，只不过需要多传一个预约id

![图片展示了睿美云开放接口中修改预约（cusbespeak）的POST请求界面。请求URL为/api/v1/tpos/cusbespeak/update，采用JSON(application/json)格式。请求参数部分，有“x-www-form-urlencoded”“form-data”“raw”三个选项，当前选中“raw”，下方显示JSON格式的预约信息，如bespeakId、customerName、duration等。响应内容显示“code: 10000”“data: true”“msg: '操作成功'”。该图片与文档中修改预约部分内容对应，直观呈现了请求参数及响应结果。](https://feishu.cn/file/FCFKbmvgwo4SR9xA3IWcvHW9nvd)

- 返回结果

> data会返回咨询的id，错误信息会在msg中返回

```JSON
{
      "code": 10000,     //只要是10000的，都是成功
      "data": true,    
      "msg": "操作成功"
}
```

## [确认预约](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#B7f2d0mdHo4BIJxhRyvcXLeSnYb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/confirm    PUT**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| bespeakId | 是 | string |  | 预约id |

![这是睿美云开放接口中确认预约接口的调用截图，展示了相关接口调用的Postman工具页面。页面显示该接口使用PUT请求，对应的请求地址包含预约ID参数，Query Params中必填的bespeakId参数值已填写，右侧Body区域返回的JSON结果显示code为10000，data为true，msg为“操作成功”，体现了预约确认操作的调用结果及参数传递情况。](https://feishu.cn/file/LDcnbzni7ofhH7xyoVQcje4mnZd)

- 返回结果

```JSON
{
      "code": 10000,     //只要是10000的，都是成功
      "data": true,    
      "msg": "操作成功"
}
```

## [取消预约](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#FUzTdB40FofVRSxx2dVc5rAFnqb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/cancel    PUT**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string |  | 预约id |
| reason | 是 | strng |  | 取消原因 |

![图片展示的是取消预约的API请求及返回结果界面。请求URL为192.168.2.133:60001/api/v1/tpos/cusbespeak/cancel，请求方式为PUT。Body部分显示参数为id: "1e9564c43d8b4abb33c54b984678a2"，reason: "取消了预约"。返回结果中，code为10000，data为true，msg为“操作成功”。该图片与文档中取消预约的API操作内容对应，直观呈现了请求与返回数据。](https://feishu.cn/file/HgSvbSz6rodV7RxPbugcy887nYb)

- 返回结果

```JSON
{
      "code": 10000,     //只要是10000的，都是成功
      "data": true,    
      "msg": "操作成功"
}
```

## [预约分页查询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#WvDfdIuzvogZrCxwGc8cRPtDnad)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/get-page    POST**

- 参数说明

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><b>字段</b></td><td><b>是否必填</b></td><td><b>类型</b></td><td><b>说明</b></td><td><b>备注</b></td></tr><tr><td>page</td><td>否</td><td>int</td><td>当前页码</td><td>默认为：1，最小为：1</td></tr><tr><td>size</td><td>否</td><td>int</td><td>每页数量</td><td>默认为：20，最大为：500</td></tr><tr><td>tenantId</td><td>是</td><td>string</td><td>要查询的门店数据id</td><td></td></tr><tr><td>customerId</td><td>否</td><td>strng</td><td>客户id</td><td>customerId,phoneNumber,expertId其中一个必传</td></tr><tr><td>phoneNumber</td><td>否</td><td>strng</td><td>客户电话号码</td><td>因为不同客户可能使用相同的电话号码，因此查询的数据会把这个电话的的客户的预约数据都查询出来，数据就不准确，所以建议使用客户id进行查询（customerId,phoneNumber,expertId其中一个必传）</td></tr><tr><td>expertId</td><td>否</td><td>Array[String]</td><td><em>专家id</em></td><td>字符串数组（customerId,phoneNumber,expertId其中一个必传）</td></tr><tr><td>startTime</td><td>否</td><td>date</td><td>预约开始时间</td><td rowspan="2">格式：yyyy-MM-dd HH:mm:ss，开始时间和结束时间必须同时有值，如果传了这两个时间条件，则不再验证客户id字段，如果没有传时间条件，则会验证客户id字段</td></tr><tr><td>endTime</td><td>否</td><td>date</td><td>预约结束时间</td></tr></tbody></table>

![图片展示的是睿美云开放接口中预约（cusbespeak）预约分页查询的接口调用示例。左侧为Postman界面，请求方式为GET，URL为192.168.2.133:600001/api/v1/tpos/cusbespeak/get-page?tenantId=2，Params栏有tenantId参数，其值为2。右侧为接口返回结果，显示了code、data等字段信息，其中data字段为空，pages字段为4，records字段包含预约项目等信息。该图片与文档中接口参数说明及返回结果部分对应，直观呈现了接口调用及返回数据情况。](https://feishu.cn/file/NT7KbvHLAoiRM4xgV97cs3WGnkd)

- 返回结果

```JSON
{
    "code": 10000,
    "data": {
        "current": 1,
        "records": [
            {
                "bespeakProject": "[{\"dataId\": \"c1fb644bc54311ec967d0242ac110002\", \"dataName\": \"费如\", \"dataType\": 1}, {\"dataId\": \"c1fb689fc54311ec967d0242ac110002\", \"dataName\": \"童防\", \"dataType\": 1}]",//预约项目
                "bespeakTypeName": "咨询",//就诊类型名称
                "bespeakTypeValue": "1",//就诊类型
                "bespeakUserId": "a415254841baa",//预约人id
                "bespeakUserName": "测试员工",//预约人
                "createDate": 1656299501000,//创建时间
                "customerId": "6e8114da0e3b4f1286761a850729c2a7",//客户id
                "customerName": "元8祥弘",//客户名称
                "startTime": "2022-06-27 10:30:00",//开始时间
                "endTime": "2022-06-27 10:45:00", //结束时间
                "expertId": "0f826edec6200d3f2f5c0c0d0ff9078d",//预约专家id
                "expertName": "测试专家", //预约专家名称
                "id": "0e475e962e7f460a99ae9e713e1be4e2",//预约数据id
                "inviteId": "a415254841baa",//邀约人id
                "inviteName": "测试员工", //邀约人
                "status":"ARRIVAL", //状态；UNCONFIRMED：预约；CONFIRMED：确认预约；ARRIVAL：到院；CANCEL：已取消
                "purpose":"预约备注"
            }
        ],
        "size": 20,
        "total": 10            //    总数
    },
    "msg": "操作成功"
}
```

## [获取可选择的预约医生](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#KIIYdUwAQosi8GxqoXfcwVG3nif)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/get-available-experts    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string |  | 门店id |

![图片展示的是睿美云开放接口中“预约（cusbespeak）”相关接口的API测试界面。左侧为请求参数设置区域，有Params、Auth、Headers等选项卡，当前选中Params，显示tenantId为11的参数。右侧为返回结果区域，显示HTTP状态码200 OK，响应时间为110 ms，响应体为JSON格式，包含code、data、msg等字段，data字段下有label和value，msg为“操作成功”。该图片与文档中获取可选择的预约医生接口的上下文相关，展示了接口请求与响应的示例。](https://feishu.cn/file/boxcnnpbQq8fdvbaUDWDX52Ishg)

- 返回结果

```JSON
{
    "code": 10000,
    "data": [
        {
            "sysUserName": "无指定医生", //医生名称
            "sysUserId": "other",       //医生id
            "maxAppointNum": 3          //最大可预约数
        }
    ],
    "msg": "操作成功"
}
```

## [查询预约专家排班](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#WAtodxQtuoeXT5xysgfc51wonEf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/get-available-experts-schedule Post**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| expertId | 是 | string |   | 专家id |
| tenantId | 是 | strng |   | 门店id |
| startTime |   | Date |   | 开始时间 |
| endTime |   | Date |   | 结束时间 |

**返回参数**

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| expertId | 是 | string |   | 专家id |
| name | 是 | strng |   | 班次名称 |
| startTime |   | Date |   | 开始时间 |
| endTime |   | Date |   | 结束时间 |
| time |   | String |   | 日期 |
| scheduleId |   | String |   | 班次id |

示例：

```JSON
{
    "code": 10000,
    "data": {
        "scheduleInfo": [
            {
                "scheduleInfoExpert": [
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#dc4c40",
                            "name": "234234",
                            "relationId": "166551936680591386",
                            "startTime": "08:00",
                            "time": "2023-11-17",
                            "endTime": "22:00",
                            "scheduleId": "5b8ac1d74a66d323de5ec7a8313f5c02"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#f7bd20",
                            "name": "555",
                            "relationId": "191149616706617346",
                            "startTime": "09:00",
                            "time": "2024-01-24",
                            "endTime": "12:00",
                            "scheduleId": "123111719823212544"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "191488723437748227",
                            "startTime": "09:00",
                            "time": "2024-01-25",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "191488730379321349",
                            "startTime": "09:00",
                            "time": "2024-01-26",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "192936888544264196",
                            "startTime": "09:00",
                            "time": "2024-01-29",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "区域删除普通",
                            "relationId": "192936915492667395",
                            "startTime": "10:30",
                            "time": "2024-01-30",
                            "endTime": "17:00",
                            "scheduleId": "500f808968ff4db4bb93843d849b1c96"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "213255689944956930",
                            "startTime": "09:00",
                            "time": "2024-03-25",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "213255691832393732",
                            "startTime": "09:00",
                            "time": "2024-03-26",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "213255698539085825",
                            "startTime": "09:00",
                            "time": "2024-03-27",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "213255699889651717",
                            "startTime": "09:00",
                            "time": "2024-03-28",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "213255702393651200",
                            "startTime": "09:00",
                            "time": "2024-03-29",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": "#a89bda",
                            "name": "加班",
                            "relationId": "213255705715539969",
                            "startTime": "09:00",
                            "time": "2024-03-30",
                            "endTime": "22:00",
                            "scheduleId": "0b529fe7eb539795e4af63ab565dd445"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": null,
                            "name": "小差的不见了",
                            "relationId": "247686704691937281",
                            "startTime": "10:00",
                            "time": "2024-06-28",
                            "endTime": "17:00",
                            "scheduleId": "52e1c44f3f845dd65e12c3b900ca7e37"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": null,
                            "name": "弄饭3214",
                            "relationId": "256354038210101252",
                            "startTime": "10:00",
                            "time": "2024-07-22",
                            "endTime": "19:30",
                            "scheduleId": "01fd772294364edab76d66c98a06e982"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": null,
                            "name": "弄饭3214",
                            "relationId": "256354042735755267",
                            "startTime": "10:00",
                            "time": "2024-07-23",
                            "endTime": "19:30",
                            "scheduleId": "01fd772294364edab76d66c98a06e982"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": null,
                            "name": "弄饭3214",
                            "relationId": "256354045600464897",
                            "startTime": "10:00",
                            "time": "2024-07-24",
                            "endTime": "19:30",
                            "scheduleId": "01fd772294364edab76d66c98a06e982"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": null,
                            "name": "弄饭3214",
                            "relationId": "256354050625241089",
                            "startTime": "10:00",
                            "time": "2024-07-26",
                            "endTime": "19:30",
                            "scheduleId": "01fd772294364edab76d66c98a06e982"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": null,
                            "name": "弄饭3214",
                            "relationId": "256354055360610308",
                            "startTime": "10:00",
                            "time": "2024-07-25",
                            "endTime": "19:30",
                            "scheduleId": "01fd772294364edab76d66c98a06e982"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": null,
                            "name": "弄饭3214",
                            "relationId": "256354058841882626",
                            "startTime": "10:00",
                            "time": "2024-07-27",
                            "endTime": "19:30",
                            "scheduleId": "01fd772294364edab76d66c98a06e982"
                        }
                    },
                    {
                        "schedule": {
                            "expertId": "other",
                            "color": null,
                            "name": "弄饭3214",
                            "relationId": "256354061270384642",
                            "startTime": "10:00",
                            "time": "2024-07-28",
                            "endTime": "19:30",
                            "scheduleId": "01fd772294364edab76d66c98a06e982"
                        }
                    }
                ],
                "indexing": 4,
                "id": "1",
                "label": "无指定医生",
                "depart": null,
                "value": "other"
            }
        ],
        "num": 61
    },
    "msg": "操作成功"
}
```

## [获取设备或者根据设备获取配置的手术间](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#SHHcdOhnpoiUk0xqYrzcktNQnMh)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/getEquipmentOrRoom Get**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| name | 否 | string |   | *设备名字* |
| type | 是 | int | *1：查询设备信息，0：查询手术间信息* | 标识 |
| equipmentId |  否 | string |   | *设备Id(查询手术间时需传)* |
| dateTime |  是 | Date |  *2024-12-26* | *时间* |
| tenantId | 是 | string |  | 门店id |

- **返回参数**

<bitable table-id="tblIrZvotqmfAIxV" token="BYgabyXRia3oMbsiTtNczDwFnLf"></bitable>

## 获取线上预约的名片管理

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/cusbespeak/getAppointCardList  POST请求**

- 参数说明

<sheet sheet-id="WMPvsU" token="shtcnTKOlDjgLChPQvGBfiOv2Eg"></sheet>

- **返回参数**
- 请求示例

```Plain Text
请求参数：
curl --location --request POST 'https://test.hospital.realmerit.com.cn/api/v1/tpos/cusbespeak/getAppointCardList' \
--data-raw '{
  "id": "", 
  "page": 1,
  "size": 20
}'

返回体：
{
    "code": 10000,
    "data": {
        "configTime": 10,
        "data": [
            {
                "afterCanBespeakHeaven": null,  //用户可以在多少天后预约，如果为null 则不限制多少天后预约（即随时预约）
                "appointConfigTimer": "[{\"disable\":false,\"status\":false,\"time\":\"09:00\"},{\"disable\":false,\"status\":false,\"time\":\"09:30\"},{\"disable\":false,\"status\":false,\"time\":\"10:00\"},{\"disable\":false,\"status\":false,\"time\":\"10:30\"},{\"disable\":false,\"status\":false,\"time\":\"11:00\"},{\"disable\":false,\"status\":false,\"time\":\"11:30\"},{\"disable\":false,\"status\":false,\"time\":\"12:00\"},{\"disable\":false,\"status\":false,\"time\":\"12:30\"},{\"disable\":false,\"status\":false,\"time\":\"13:00\"},{\"disable\":false,\"status\":false,\"time\":\"13:30\"},{\"disable\":false,\"status\":false,\"time\":\"14:00\"},{\"disable\":false,\"status\":false,\"time\":\"14:30\"},{\"disable\":false,\"status\":false,\"time\":\"15:00\"},{\"disable\":false,\"status\":false,\"time\":\"15:30\"},{\"disable\":false,\"status\":false,\"time\":\"16:00\"},{\"disable\":false,\"status\":false,\"time\":\"16:30\"},{\"disable\":false,\"status\":false,\"time\":\"17:00\"},{\"disable\":false,\"status\":false,\"time\":\"17:30\"},{\"disable\":false,\"status\":false,\"time\":\"18:00\"}]", //预约配置时间
                "appointFlag": false,  //是否预约
                "appointNums": 22,   //预约人数
                "appointRoleId": "", //线上预约岗位配置
                "appointShow": 0,  //小程序 显示预约数
                "appointments": 3,  //一个专家同一时间段 最大预约次数 默认3个 空代表无限制
                "beanVersion": "",
                "bespeakType": "[{\"code\": 0, \"name\": \"咨询\", \"limit\": -1, \"selectFlag\": true}, {\"code\": 1, \"name\": \"治疗\", \"limit\": -1, \"selectFlag\": false}, {\"code\": 2, \"name\": \"复查\", \"limit\": -1, \"selectFlag\": false}]",//可预约就诊类型 name-类型名 selectFlag-勾选标识(勾选-true 不勾选-false) limit-个数限制(-1表示无限制)
                "bespeakTypeVo": [
                    {
                        "code": 0,
                        "limit": -1,
                        "name": "咨询",
                        "selectFlag": true
                    },
                    {
                        "code": 1,
                        "limit": -1,
                        "name": "治疗",
                        "selectFlag": false
                    },
                    {
                        "code": 2,
                        "limit": -1,
                        "name": "复查",
                        "selectFlag": false
                    }
                ],
                "canEdit": true,
                "cateOrPro": "",  //分类或者项目id,name,isType(json) 0-项目 1-分类
                "cateOrProJsonList": [],  
                "cateOrPros": [],
                "consultant": "",
                "consultantId": "",
                "createBy": "1",
                "createDate": 1644848430000,
                "delFlag": false,
                "doctorFlag": true,  //是否是医生
                "effectDay": null,   //医生可预约最大时长
                "enableFlag": true, //是否启用
                "enterpriseWeChat": "",
                "exampleShow": false,  //是否案列展示
                "expertInfo": "<p>10101</p><div class=\"media-wrap image-wrap\"><img alt=\"图片2.bmp\" class=\"media-wrap image-wrap\" id=\"1656493267256_1\" src=\"https://uatphoto.realmerit.com.cn//neuron-qiniu/photos/E91ECEFA-F966-4763-875D-97A5E17418F8.bmp?e=1755246902&amp;token=MGZ_ZGHlQ_BUhuudnNb9ORYvesxLznfymWocviwq:E5y0wAorkQAKhg0J4y9CeWPmNas=\" title=\"图片2.bmp\"/></div><p/><p/>",//专家信息
                "forward": 1,//转发次数
                "goodField": "011010",//擅长领域
                "groupInfoId": "",
                "id": "a0b61369f8144d90b31da86524fd1bc4",
                "jobDescription": "",  //职位描述
                "maxAppointNum": 3, //最大预约数
                "microBlog": "",//个人微博
                "notCanDeleteFlag": true,
                "onlineConsultationFlag": false, //是否可以在线面诊
                "orderJingXuan": 0,  //小程序端精选排序
                "orderWx": 1,
                "orders": 0,
                "phone": "",
                "photoUrl": "{\"path\":\"https://uatphoto.realmerit.com.cn//neuron-qiniu/tenant1/photos/AF8264EE-77AA-4FC2-B7B0-E5FF790E0B9F.jpg?e=1755246902&token=MGZ_ZGHlQ_BUhuudnNb9ORYvesxLznfymWocviwq:wo5E1-WM8UzxiBOtu2WVqW1H9D4=\",\"size\":2015109,\"thumbnailPath\":\"https://uatphoto.realmerit.com.cn//neuron-qiniu/tenant1/photos/AF8264EE-77AA-4FC2-B7B0-E5FF790E0B9F.jpg?e=1755246902&token=MGZ_ZGHlQ_BUhuudnNb9ORYvesxLznfymWocviwq:wo5E1-WM8UzxiBOtu2WVqW1H9D4=\"}",//照片
                "post": "医生", //岗位名称
                "postId": "72c418f0eeab4c20b6afdb102b7d1c08", //岗位id
                "selected": false,//是否展示到精选
                "sysUserDeptDtos": [],
                "teletextFlag": false,//是否图文问诊
                "tenantId": "1",
                "tenantName": "门店1",
                "time": 30,//小程序配置的时间,默认30
                "title": "",//头衔(JSON)
                "totalFlag": false,
                "updateBy": "259690994490933248",
                "updateDate": 1754963814000,
                "userId": "other",
                "userName": "messages.appoint.appointment-card.no-appoint-doctor",
                "weChatFlag": false,//是否是企业微信用户
                "wechatId": "",
                "wxNo": ""
            }
        ],
        "total": 28
    },
    "msg": "messages.result.code.operation.success"
}
```

# **渠道（channel）**

## [整合渠道类型选择（建档，报备）](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#DeWGdUscgoKCeExGAZrcMTU2n0b)

- 请求URL

**/api/v1/tpos/channel/channelstypeinfo    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string |  | 门店id |
| channelType | 是 | int | 渠道类型 | 0: 运营媒体  <br/>1: 市场渠道 |

![图片展示的是Postman工具界面，用于测试获取渠道类型信息的接口。请求方式为GET，URL为{{ip}}/api/v1/tpos/channel/channeltypeinfo?channelType=1&tenantId=11。参数部分，channelType值为1，tenantId值为11。响应体显示接口成功，code为180000，data包含渠道类型信息，如id、label、openFlag等字段，其中id为846e5df44eeef7de8e080b081873ecce9，label为“超商”，openFlag为true等。该图片与文档中介绍的通过渠道类型获取渠道列表的接口测试内容相关。](https://feishu.cn/file/boxcnGmjLPXUyTFkKsHwxUY3VSf)



```JSON
{
    "code": 10000,
    "data": [
        {
            "children": [// 子渠道
                {
                    "id": "3b7ee7c1a614e5283f34e3832a78af3f",   
                    "title": "沃尔玛一层",      
                    "children": []                  
                }
            ],
            "id": "d124907929b51b6c4115388a202a560d", //    渠道id
            "title": "沃尔玛",//    渠道名称
        }
    ],
    "msg": "操作成功"
}
```



## [通过渠道类型获取渠道列表](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#VEqudKmWeoU0IMxS2FhcFuSTnGc)

- 请求URL

**/api/v1/tpos/channel/specificchannellist     GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string |  | 门店id |
| channelType | 是 | string |  | 0：运营媒体  <br/>1：市场渠道 |
| typeId | 是 | string |  | 渠道分类id |

![这张图片展示的是睿美云开放接口中“通过渠道类型获取渠道列表”的API请求响应界面。左侧是请求参数区域，显示请求方法为GET，请求地址为对应的接口路径，且已勾选必填字段tenantId、channelType、typeId，并填写了对应参数值。右侧为返回的JSON格式响应结果，呈现接口返回的相关数据内容，包含渠道相关的各类字段信息，整体用于展示该API的请求配置与返回数据的示例。](https://feishu.cn/file/boxcn1YcbqxmimBF2VEjBVT3sHf)



```JSON
{
    "code": 10000,
    "data": [
        {
            "label": "WeChat",// 渠道名称
            "value": "f641d3f9c134c4e6e0ad3ab75887b117"//渠道id
        }
    ],
    "msg": "操作成功"
}
```

## [查询渠道信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#U3CIdwR7joObF8ximzfcs97ineg)

- 请求URL

/api/v1/tpos/channel/getChannelPageInfo      Post

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** |
|-|-|-|-|
| id | 否 | 渠道id | 如果传了id，则只查询该id对应的渠道信息，其他参数则不起作用 |
| tenantId | 否 | 门店id | 传值和不传值，接口都会验证是否有权限查询对应门店的数据 |
| name | 否 | 渠道名称 |  |
| startCreateDate | 否 | 渠道创建开始时间 | 一般和endCreateDate配套使用 |
| endCreateDate | 否 | 渠道创建结束时间 | 一般和startCreateDate配套使用 |
| startUpdateDate | 否 | 渠道修改开始时间 | 一般和endUpdateDate配套使用 |
| endUpdateDate | 否 | 渠道修改结束时间 | 一般和startUpdateDate配套使用 |
| groupInfoId | 否 | 集团渠道id | 可以根据这个参数查询从集团下发的对应门店的渠道信息 |
| page | 否 | 分页页码 | 默认为1 |
| size | 否 | 每页条数 | 默认20，最大500 |

# 运营媒体（web）

## [查询运营媒体信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#EiBKdlhzso0vL9x9Voscrwg2nyd)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/channelWeb/getChannelWebPage-review    POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** |
|-|-|-|-|
| id | 否 | String | 运营媒体id |
| name | 否 | String | 运营媒体名称 |
| groupInfoId | 否 | String | 集团下发的id |
| tenantId | 否 | String | 门店id |

说明：参数为并且的关系，如果所有参数为空，则查询所有数据，请尽量精准查询

返回值：

```JSON
{
    "code": 10001,
    "data": [
        {
            "channelName": "柠檬儿",   //渠道名称
            "concat": "",               //联系人
            "createBy": "078946b880987c24bf0d273d8b6e10eb", //创建人
            "createDate": 1686460401000,           //创建时间戳
            "delFlag": false,                        //删除状态,true:删除，false：正常
            "groupInfoId": "a00c3922d20a45e9b804b08480bda001",   //数据复制于集团数据的业务id
            "id": "0022dd25f775428990d2f3f1f44ebb5a",
            "money": 0.0,             //缴费总额
            "phone": "",                //联系电话
            "registDate": null,        //注册时间
            "remark": "",                //备注
            "tenantId": "4",            //门店id
            "typeId": "ee2e2497829888081266af69bf4b0dac",   //渠道类型id
            "updateBy": "c1e4550f085cfd49ebbce6ba8e4982cd",   //修改人id
            "updateDate": 1686460267000,         //修改时间戳
            "userId": ""                         //渠道负责人id
        }
    ],
    "msg": "成功获取数据，数据非空"
}
```

# **接待（reception）**

> 新增接待划掉的参数本意是用于建档（如果传入的客户在系统中找不到档案，则会用这些参数去建档，建档这部分逻辑已暂停使用，因为建档比较耗时）

## [可用的接待分诊人列表](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#AtwXdjUFzo0dBux2ugpc9Nj2nXb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/reception/triagetouserlist    GET**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string | 门店id |  |

![这张图片展示的是睿美云开放接口中，“获取可用的接待分诊人列表”这一GET接口的请求与返回结果示例。在请求参数区域，明确标记了必填的tenantId字段，其值设置为1；返回结果区域的JSON数据里，code字段值为10000表示请求成功，data数组则返回了符合该接口的分诊人信息，每个分诊人数据包含roleName（角色名称）、userSerialId（用户序号）、sysUserName（系统用户名）三类内容，对应不同的员工身份，如“医生（修正）”“咨询师（全）”等。](https://feishu.cn/file/Ak9pbeY75onDGxxOmwac2gyqnOc)

- 返回结果

```JSON
{
    "code": 10000,
    "data": [
        {
            "roleName": "医生（修正） 总经办（修正） 皮肤医生",   //岗位名称
            "sysUserId": "213321293846544388",          // 用户id
            "sysUserName": "测试-小鹏"                   //用户名称
        },
        {
            "roleName": "医生（修正） 咨询师（全） 护士（修正）",
            "sysUserId": "200269154064793605",
            "sysUserName": "测试张"
        }
    ],
    "msg": "操作成功"
}
```

## [新增接待](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#BIAodWQscoggcqximqlczXPznqf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/reception/receptionadd    POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId |  | string |  | 客户id |
| receptionProject | 见机构配置 | array | 关联项目 | ProjectJsonEntity实体列表 |
| triageToUserId | 见机构配置 | string |  | 分诊（转到）的员工id |
| receiverId | 是 | string |  | 接待人id |
| receptionType | 是 | string |  | 就诊类型（查询字典：clinicType） |
| tenantId | 是 | string |  | 门店id |
| ~~customerParam~~ |  |  |  | ~~客户档案新增（编辑）的实体~~  <br/>~~如果customerId无值，则会用这里面的参数建档或匹配档案~~ |

![图片展示的是睿美云开放接口中“接待（reception）”新增接待的接口调用示例。请求方式为POST，URL为127.0.0.1:60001/api/v1/tpos/reception/receptionadd。Body部分以JSON格式提交参数，包括tenantId、receiverId、triageToUserId、sex、receptionType、customerParam、BusinessType、customerName、mainPhone、phoneNumber、sourceType、receptionProject等。返回结果为code 10000，data为true，msg为“操作成功”。该图片与文档中介绍的新增接待接口参数说明及返回结果内容相关，直观呈现了接口调用及返回数据情况。](https://feishu.cn/file/Qb26bQeNjoOWGBxB1gEcNzbbn9e)

- 返回结果

> 其余全视为错误，错误信息会在msg中返回

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

## [查询客户接待信息](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#QEKVdSENfoFYHrxASKZcrlqdnFc)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/reception/reception_cus    POST**

- 参数说明

<sheet sheet-id="vc87ZO" token="shtcnTKOlDjgLChPQvGBfiOv2Eg"></sheet>

![图片展示的是睿美云开放接口中“接待（reception）”模块下“查询客户接待信息”接口的POST请求示例。请求URL为http://localhost:8080/api/v1/tpos/reception/reception_cus，Body部分以JSON格式提交参数，包括customerId、startDate、endDate、tenantId、page、size等。返回结果中，code为18000，data包含客户信息，如arrivePurpose、assistReceiveId、assistReceiveName等，还显示了msg为“操作成功”。该图片与文档中接口参数说明及返回结果的上下文对应，直观呈现了接口调用示例。](https://feishu.cn/file/JEfBbpgAeoWUe0xSl86cm2WwnXb)

- 返回结果

```json
{
    "code": 10000,
    "data": [
        {
            "arrivePurpose": "",   // 来院目的
            "assistReceiverId": "",  //协助接待人id
            "assistReceiverName": "",  //协助接待人姓名
            "autoFlag": 1,     //是否自动生成 0否1是
            "createDate": "2024-07-27 06:42:09",  //创建时间
            "customerId": "00001718733c46b98056c01d30a4f019",   //客户id
            "customerName": "丁5肆1",    //客户姓名
            "deptId": "",      //就诊科室id
            "deptName": "",    //就诊科室名称
            "id": "0241ed0c612a4fa6a6cbde8f414ad248",   //接待id
            "phone": "1abbbb13050",  //客户电话
            "receiverId": "77e1ab1998354560a760b28080e0f5f8",   //接待人id
            "receiverName": "测试-贾",    //接待人姓名
            "receptionDate": "2024-07-27",   // 接待日期
            "receptionProject": [],  //关联项目,([{"dataId": "项目id", "dataName": "项目名称", "dataType": 0}]，dataType：0是项目，1是项目分类)
            "receptionTypeName": "其他",   // 接待类型
            "receptionTypeRemark": "",    //接待类型备注
            "remark": "",         //接待备注
            "tenantId": "1",      //接待门店id
            "tenantName": "门店1",   //接待门店名称
            "triageToUserId": "",   //分诊（转到）的用户id
            "triageToUserName": ""   // 分诊（转到）的用户姓名
        }
    ],
    "msg": "操作成功"
}
```



## [客户扫码签到初始化数据(小程序)](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#XB1EdcsOTooU0gx7GTHccpScnJT)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/reception/scrm-check-in-config    POST**

- 参数说明

![图片展示的是睿美云开放接口中“客户扫码签到初始化数据(小程序)”接口的请求参数设置界面。在Body选项卡下，参数类型选择“raw”，参数内容为JSON格式，包含“customerId”和“tenantId”两个字段，分别对应客户id和门店id，其中“customerId”值为“c101ae946dfc423386e6ce3b41979952a”，“tenantId”值为“1”。该图片与文档中介绍的接口参数说明部分对应，直观呈现了接口请求时所需填写的参数内容。](https://feishu.cn/file/SM0vbjsnmoOnhfxPoRwcv7SKntc)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| tenantId | 是 | string | 门店id |  |

- 返回结果

```JSON
{
  "code": 10000,
  "data": {
    "clinicType": [    //就诊类型
      {
        "ext": "#79D38E",    //就诊类型的颜色值
        "label": "咨询",    //就诊类型（名称）
        "value": "1"    //就诊类型（值）
      }
    ],
    "arrivePurpose": [    //到院目的
      {
        "id": "583055b830e782e3acfc9eada9272796",    //到院目的数据id
        "purpose": "瘦脸",    //到院目的
        "type": "1"    //对应的就诊类型（值）
      }
    ],
    "customerList": [    //客户信息(包括关联账户)
      {
        "age": 25,    //年龄
        "birthday": 946656000000,    //生日
        "enabledFlag": true,    //是否可选(true-可选)
        "id": "c101ae946dfc423386ece3b41979952a",    //客户id
        "idCardNumber": "",    //身份证号
        "name": "张月",    //客户姓名
        "phone": "18781979283",    //客户手机号
        "receptionFillInAddress": "",    //省市区
        "receptionFillInRegion": "",    //详细地址
        "selectFlag": true,    //是否默认选中（true-默认选中）
        "sex": "2",    //客户性别(1-男，2-女)
        "type": "2"    //客户类型（0：初诊；1：复诊；2：老客人；3：其他；-1：空）
      }
    ],
    "customizeFieldList": [    //自定义字段
      {
        "id": "340812398636040198",    //数据id
        "fieldName": "单选1",    //字段名称
        "textType": 0,    //文本类型（0-单选;1-多选;2-文本）
        "isFirst": false,    //是否首次到院（true-是）
        "isOnceMore": true,    //是否再次到院（true-是）
        "isRequired": true,    //是否必填（true-是）
        "maxSelectNum": null,    //当前至多可选的选项数量（文本类型为多选时）
        "num": 4,    //排序字段
        "configInfos": [    //配置的选项内容
          {
            "optionName": "是",    //选项名称
            "addDescription": true,    //是否添加描述(true-添加描述)
            "descriptionRequired": true,   //描述是否必填（true-描述必填）
            "descriptionContent": "如果有,请注明:____",    //描述文本内容
            "addRemark": true,    //是否添加备注(true-添加备注)
            "remarkRequired": true,    //备注是否必填（true-备注必填）
            "tagIds": ["000812398636040128"]    //关联企微标签id
          }
        ]
      }
    ],
    "fieldList": [    //签到的字段配置
      {
        "id": "d80f4eb4e7eb11ee8aca0242ac110002",    //数据id
        "fieldName": "姓名",    //字段名称
        "showName": "姓名1",    //展示名称
        "isFirst": true,    //是否首次到院（true-是）
        "isOnceMore": true,    //是否再次到院（true-是）
        "isRequired": true,    //是否必填（true-是）
        "num": 1,    //排序字段
        "value": "name"    //展示字段的value值
      }
    ],
    "receptionSignInConfig": {    //接待签到的相关配置
      "visitTypes": [    //可选就诊类型
        "1"    //就诊类型（值）
      ],
      "allProjectTypeJsonVoList": [    //配置的项目填写方式
        {
          "label": "1",    //对应的就诊类型（值）
          "value": "0"    //填写方式（0:手动填写;1:选择一级分类;2:选择二级分类;3:选择项目;4:选择客户未治疗项目;5:选择客户已治疗项目）
        }
      ],
      "cateOrProJsonVoList": [    //可选项目
        {
          "children": [], //子分类信息（结构与外层一致）
          "id": "1745cec6398942f8936ffa8f50da6f01", //项目id或项目分类id
          "label": "AD项目",    //项目名称或项目分类名称
          "level": null,    //层级（整型（从0开始），项目时为空，项目分类时不为空）
          "name": "AD项目",    //项目名称或项目分类名称
          "p_status": "1",    //父级状态(只有项目时候使用)
          "p_typeId": "7dcdd1b6feae43f6ba5a54a79fabb675",    //父级分类id(只有项目时候使用)
          "projectType": "project",    //项目类型（project：项目；type：项目分类）
          "showName": "AD项目",    //展示名称
          "type": "7dcdd1b6feae43f6ba5a54a79fabb675",    //父级分类id(只有项目时候使用)
          "value": "1745cec6398942f8936ffa8f50da6f01"    //项目id或项目分类id
        }
      ],
      "doctorTypeConfig": 1,    //医生信息-填写方式（0-手动填写，1-选择医生）
      "doctorJsonVoList": [    //可选医生
        {
          "id": "213368120469880838",    //医生id
          "label": "李含模",    //医生姓名
          "showName": "李含模"    //展示医生姓名
        }
      ],
      "id": "4eca6755ed9e11ee8aca0242ac110002"    //接待签到的相关配置的数据id
    }
  },
  "msg": "操作成功"
}
```

## [客户扫码签到(小程序)](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#NTP8dcklLoLyGoxkTcOcxKyEnVf)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/reception/scrm-check-in    POST**

- 参数说明

![图片展示的是睿美云开放接口接待（reception）中客户扫码签到（小程序）的请求参数示例。参数以JSON格式呈现，包含客户ID、访客类型配置、接待类型、接待类型名称、接待地点ID、接待地点名称、项目类型配置、项目名称、项目类型、咨询项目、咨询项目名称、医生类型配置、医生操作ID、医生姓名、是否有医疗史、历史内容、备注、客户来源、朋友电话、客户来访地图、租户ID等信息，部分字段有示例值。该图片与文档中请求URL及参数说明的内容相关，直观呈现了请求参数的具体结构与示例。](https://feishu.cn/file/IDuHbobRjo3B0SxJWtBcOd8HnAg)

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| visitTypeConfig | 是 | int | *就诊类型的填写方式*  | *0:手动填写;1:就诊类型* |
| receptionType | 是 | string | *就诊类型（值）* |  |
| receptionTypeName | 是 | string | *就诊类型（名称）* |  |
| arrivePurposeConfigId | 否 | array | *来院目的(id)* | 字符串数组 |
| arrivePurpose | 否 | array | *来院目的(名称)* | 字符串数组 |
| projectTypeConfig | 是 | string | *项目填写方式*  | *0:手动填写;1:选择* |
| projectName | 否 | string | 项目名称 | 手动填写的 |
| projectMap | 否 | array | 项目信息 | 选择的 |
|   +dataId | 是 | string | 项目id |  |
|   +dataName | 是 | string | 项目名称 |  |
|   +dataType | 是 | int | 类型 | *0:项目;1:项目分类* |
| consultProjectTypeConfig | 是 | string | 咨询项目填写方式 | *0:手动填写;1:选择* |
| consultProject | 否 | string | 咨询项目 | 手动填写的 |
| consultProjectMap | 否 | array | 咨询项目信息 | 选择的 |
|   +dataId | 是 | string | 项目id |  |
|   +dataName | 是 | string | 项目名称 |  |
|   +dataType | 是 | int | 类型 | *0:项目;1:项目分类* |
| doctorTypeConfig | 是 | int | 医生填写方式 | *0:手动填写;1:选择* |
| bespeakExpertId | 否 | string | 医生id | 医生填写方式如果是选择，该字段就需要有值 |
| bespeakExpertName | 否 | string | 医生姓名 |  |
| hasMedicalHistory | 否 | bool | 是否有病史 | true:有病史 |
| historyContent | 否 | string | *病史* |  |
| remark | 否 | string | 备注 |  |
| customerSource | 否 | int | *客户来源* | *0:自然到院;1:朋友介绍* |
| friendPhone | 否 | string | 朋友电话 |  |
| customFieldMap | 否 | map | *自定义字段* | key：*配置的自定义字段id；value：自定义字段值（对象数组,字段说明：selectContent-选择内容(勾选)；remark-输入框填写内容(备注)；description-输入框填写内容(描述)；inputContent-如果是文本输入框, 文本框输入内容）* |
| tenantId | 是 | string | 门店id |  |

- 返回结果

```json
{
    "code": 10000,
    "data": {
        "dupFlag": false,        //是否已经接待了（true-已经接待了）
        "receptionId": "346697267303940355"    //接待id
    },
    "msg": "操作成功"
}
```

# 咨询（consultation）

## [新增咨询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Q7mCdFlwMom4eZxtKu7cGnCwnLc)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/consultation/add    POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| userId | 是 | string |  | 咨询师id |
| handleRemark | 否 | string | 治疗方案 |  |
| customerRemark | 否 | string | 主诉 |  |
| customerId | 是 | string | 客户id |  |
| tenantId | 是 | string | 要操作的门店id | 接待人id |
| proIds |  | array |  | 就诊项目 |
|   +id | 否 | string | 项目id |  |
|   +name | 否 | string | 项目名称 |  |
| conPros |  | array |  | 咨询项目 |
|   +id | 否 | string | 项目id |  |
|   +name | 否 | string | 项目名称 |  |
| conProTypes |  | array |  | 咨询项目分类 |
|   +id | 否 | string | 项目id |  |
|   +name | 否 | string | 项目分类名称 |  |

![图片展示的是睿美云开放接口中新增咨询的POST请求示例。请求地址为192.168.2.133:60001/api/v1/tpos/consultation/add，Body部分以JSON格式提交参数，包括userId、handleRemark、customerId、tenantId、proIds、conPros、conProTypes等字段。返回结果中，code为100000，data为咨询id，msg为“操作成功”，且有Pretty、Raw、Preview、Visualize、JSON等显示选项。该图片与文档中新增咨询接口的请求和参数说明内容对应，直观呈现了接口调用示例。](https://feishu.cn/file/Tx9fbz0YIoLheExvB0Pc1LQZnlb)

- 返回结果

> data会返回咨询的id，错误信息会在msg中返回

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

## [修改咨询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#EKOid60jaokj6CxXXiPcy8EanKc)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/consultation/update    POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 咨询id |  |
| userId | 是 | string |  | 咨询师id |
| handleRemark | 否 | string | 治疗方案 |  |
| customerRemark | 否 | string | 主诉 |  |
| customerId | 是 | string | 客户id |  |
| tenantId | 是 | string | 要操作的门店id | 接待人id |
| proIds |  | array |  | 就诊项目 |
|   +id | 否 | string | 项目id |  |
|   +name | 否 | string | 项目名称 |  |
| conPros |  | array |  | 咨询项目 |
|   +id | 否 | string | 项目id |  |
|   +name | 否 | string | 项目名称 |  |
| conProTypes |  | array |  | 咨询项目分类 |
|   +id | 否 | string | 项目id |  |
|   +name | 否 | string | 项目分类名称 |  |

![图片展示的是睿美云开放接口中修改咨询的Postman测试界面。请求URL为192.168.133.60001/api/v1/tpos/consultation/update，方法为POST。Body部分以JSON格式呈现，包含userId、conProx、conProTypes、proIds等字段，如userId为“85d60b54d802abfa3a5a608f2927d9667”，conProx有“接待器”和“集团项目1”等。右侧返回结果中，code为100000，data包含咨询id，msg显示“操作成功”。该图片与文档中修改咨询接口的请求和参数说明紧密相关，直观呈现了接口调用及返回结果情况。](https://feishu.cn/file/NHDdbCz7Po635pxvfLEcViA2nff)

- 返回结果

> data会返回咨询的id，错误信息会在msg中返回

```JSON
{
    "code": 10000,
    "data": "5494adce62a54b68ba4f900be0256f67",
    "msg": "操作成功"
}
```





## 查询咨询

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/consultation/page  POST**

- **参数说明**

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>  customerId</td><td>客户</td><td>false</td><td>string</td></tr><tr><td>  customerKey</td><td>客户姓名或者电话</td><td>false</td><td>string</td></tr><tr><td>  startTime</td><td>开始时间</td><td>false</td><td>string(date-time)</td></tr><tr><td>  endTime</td><td>结束时间</td><td>false</td><td>string(date-time)</td></tr><tr><td>  userId</td><td>接诊咨询师</td><td>false</td><td>string</td></tr><tr><td>  page</td><td>分页参数（页码）</td><td>true</td><td>integer(int64)</td></tr><tr><td>  size</td><td>分页参数（每页数量）</td><td>true</td><td>integer(int64)</td></tr><tr><td>  tenantId</td><td>门店ID<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>true</td><td>string</td></tr></tbody></table>

**请求示例：**

![图片展示的是睿美云开放接口查询咨询的请求示例。左侧为Postman界面，请求方式为POST，URL为/api/v1/tpos/consultation/page，Body选择JSON格式，参数包括page、size、startTime、endTime、userId、customerId、customerKey、superId、tenantId等。右侧是请求后的返回结果，显示了code、countId、count、current、maxLimit、optimizeCountSql、tenantId、pages、records等参数，其中records下有1个item，还包含searchCount、size、total等信息，msg为“操作成功”。](https://feishu.cn/file/DrzSbrWr6oPCSIxc5Zwc1iEhnJd)

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 结果内容 | IPageOf三方新增咨询 |
|   current |  | integer(int64) |
|   pages |  | integer(int64) |
|   records |  | array |
|     id | id | string |
|     mainComplaint | 主诉 | string |
|     phoneNumber | 电话号码 | string |
|     customerId | 客户id | string |
|     customerName | 客户名称 | string |
|     assignedConsultantId | 归属咨询师id | string |
|     assignedConsultantName | 归属咨询师 | string |
|     conProjects | 就诊项目 | array |
|       id | 数据id | string |
|       name | 数据名称 | string |
|     consultationProjects | 咨询项目 | array |
|       id | 数据id | string |
|       name | 数据名称 | string |
|     consultationStatus | 咨询状态 | string |
|     consumptionStatus | 消费状态 | string |
|     customerType | 客户类型 | string |
|     dynamicFormSetting | 自定义表单 | string |
|     dynamicFormValue | 自定义表单值 | string |
|     receptionTime | 接待时间 | string |
|     receptionType | 来院类型 | string |
|     smartLabelList | 客户标签 | array |
|       id | 数据id | string |
|       name | 数据名称 | string |
|     treatmentPlan | 治疗方案 | string |
|     urgentFlag | 是否紧急客人 | boolean |
|     userId | 接诊咨询师id | string |
|     userName | 接诊咨询师 | string |
|     vipNum | 会员号 | string |
|     waitTime | 已等待时间 | integer |
|   size |  | integer(int64) |
|   total |  | integer(int64) |
| msg | 响应消息 | string |

**响应示例**:

```JSON
{
    "code": 10000,
    "data": {
        "current": 0,
        "pages": 0,
        "records": [
            {
                "assignedConsultantId": "",
                "assignedConsultantName": "",
                "conProjects": [
                    {
                        "id": "",
                        "name": ""
                    }
                ],
                "consultationProjects": [
                    {
                        "id": "",
                        "name": ""
                    }
                ],
                "consultationStatus": "",
                "consumptionStatus": "",
                "customerId": "",
                "customerName": "",
                "customerType": "",
                "dynamicFormSetting": "",
                "dynamicFormValue": "",
                "id": "",
                "mainComplaint": "",
                "phoneNumber": "",
                "receptionTime": "",
                "receptionType": "",
                "smartLabelList": [
                    {
                        "id": "",
                        "name": ""
                    }
                ],
                "treatmentPlan": "",
                "urgentFlag": true,
                "userId": "",
                "userName": "",
                "vipNum": "",
                "waitTime": 0
            }
        ],
        "size": 0,
        "total": 0
    },
    "msg": "操作成功"
}
```

# 面诊（assessment）

## 查询客户历史面诊

- 请求URL（需要tpos鉴权）

**接口地址: /api/v1/assessment/get-cus-assessment-page   POST**

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
|   customerId | 客户id | true | string |
|   searchKey | 表单查询关键字 | false | string |
|   endDate | 结束时间 | false | string(date-time) |
|   startTime | 开始时间 | false | string(date-time) |
|   size | 每页数量 | true | integer(int64) |
|   page | 页码 | true | string |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer(int32) | integer(int32) |
| data | 结果内容 | IPageOf客户面诊 | IPageOf客户面诊 |
|   current |  | integer(int64) |  |
|   pages |  | integer(int64) |  |
|   records |  | array | 客户面诊 |
|     assUserId | 面诊医生id | string |  |
|     assUserName | 面诊医生姓名 | string |  |
|     conUserId | 咨询师id | string |  |
|     conUserName | 咨询师姓名 | string |  |
|     customerName | 客户姓名 | string |  |
|     customerRemark | 客户主诉 | string |  |
|     feeFlagName | 消费状态 | string |  |
|     handleRemark | 病历诊断 | string |  |
|     id | 数据id | string |  |
|     payPropName | 消费性质 | string |  |
|     payStatus | 消费状态 | integer |  |
|     pros | 面诊项目 | string |  |
|     receptionType | 就诊类型 | string |  |
|     secondConfirmFlag | 面诊二次确认 | boolean |  |
|     startTime | 面诊开始时间 | string |  |
|     sureStatus | 确认状态 | integer |  |
|     tenantId | 门诊门店id | string |  |
|     tenantName | 门诊门店名称 | string |  |
|     undealRemark | 未成交原因 | string |  |
|   size |  | integer(int64) |  |
|   total |  | integer(int64) |  |
| msg | 响应消息 | string |  |

## 新增面诊

- 请求URL（需要tpos鉴权）

**接口地址**:**/api/v1/assessment/add-assessment  POST**

**请求示例：**

```JSON
{
    "operateDoctorId": "02b3f8365ee4e0b2de7b264c2ce1faee",
    "toUserId": "02b3f8365ee4e0b2de7b264c2ce1faee",
    "customerId": "489860652874072064",
    "arriveFlag": true,
    "tenantId": "1",
    "receptionType": "1",
    "treatmentPlan": "nihda132312d",
    "mainComplaint": " 我要吃3123",
    "undealType": "2",
    "undealRemark": "3123",
    "consultationProjectIds": [
        "00cd05fabe8e413ebba4dba0eec21968",
        "d02526506c013d9dbae7fda2b7d99081"
    ]
}
```

**请求参数：**

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>  customerId</td><td>客户id</td><td>true</td><td>string</td></tr><tr><td>  operateDoctorId</td><td>面诊医生</td><td>true</td><td>string</td></tr><tr><td>      receptionType</td><td>就诊类型<br/>查询字典：clinicType<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>true</td><td></td></tr><tr><td>  tenantId</td><td>面诊门店id</td><td>true</td><td>string</td></tr><tr><td>      arriveFlag</td><td>客户今日是否已到院</td><td>true</td><td>boolean</td></tr><tr><td>  toUserId</td><td>转咨询员工id（生成一条对应员工的咨询记录）</td><td>false</td><td>string</td></tr><tr><td colspan="4">就诊类型是（咨询）相关参数</td></tr><tr><td>  mainComplaint</td><td>客户主诉</td><td>true</td><td>string</td></tr><tr><td>  consultationProjectIds</td><td>就诊项目或者项目id集合</td><td>true</td><td>array</td></tr><tr><td>  treatmentPlan</td><td>治疗方案</td><td>true</td><td>string</td></tr><tr><td>  undealRemark</td><td>未成交原因</td><td>false</td><td>string</td></tr><tr><td>  undealType</td><td>未成交类型<br/>查询字典：undeal_type<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>false</td><td>string</td></tr><tr><td colspan="4">就诊类型是（治疗 复查 客诉 其他）相关参数</td></tr><tr><td>  consultationProjectIds</td><td>就诊项目或者项目id集合</td><td>true</td><td>array</td></tr><tr><td>  treatmentDoctorIds</td><td>治疗医生</td><td>false</td><td>array</td></tr><tr><td>      mainComplaint</td><td>内容</td><td>false</td><td>string</td></tr></tbody></table>

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 |
|-|-|-|
| code | 响应结果 | integer(int32) |
| data | 新增的面诊数据id | string |
| msg | 响应消息 | string |

**响应示例**:

```JSON
{
    "code": 10000,
    "data": "75b896c0ffab4a76979a63b448e823aa",
    "msg": "操作成功"
}
```



## 确认面诊

- 请求URL（需要tpos鉴权）

**接口地址**:   **/api/v1/assessment/confirm-assessment POST**



**请求示例**

```JSON
{
    "id": "75b896c0ffab4a76979a63b448e823aa"
}
```

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
|   id | 数据id | true | string |

- 返回结果

**响应示例**:

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```





## 更新面诊

- 请求URL（需要tpos鉴权）

**接口地址**:**/api/v1/assessment/update-assessment    POST**



**请求示例**:

```JSON
{
    "id": "75b896c0ffab4a76979a63b448e823aa",
    "operateDoctorId": "02b3f8365ee4e0b2de7b264c2ce1faee",
    "toUserId": "02b3f8365ee4e0b2de7b264c2ce1faee",
    "customerId": "489860652874072064",
    "arriveFlag": true,
    "tenantId": "1",
    "receptionType": "1",
    "treatmentPlan": "nihda132312d",
    "mainComplaint": " 我要吃3123",
    "undealType": "2",
    "undealRemark": "3123",
    "consultationProjectIds": [
        "00cd05fabe8e413ebba4dba0eec21968",
        "d02526506c013d9dbae7fda2b7d99081"
    ]
}
```

**请求参数**:

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>参数名称</td><td>参数说明</td><td>是否必须</td><td>数据类型</td></tr><tr><td>  id</td><td>数据id</td><td>true</td><td>string</td></tr><tr><td>  customerId</td><td>客户id</td><td>true</td><td>string</td></tr><tr><td>  operateDoctorId</td><td>面诊医生</td><td>true</td><td>string</td></tr><tr><td>      receptionType</td><td>就诊类型<br/>查询字典：clinicType<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>true</td><td></td></tr><tr><td>  tenantId</td><td>面诊门店id</td><td>true</td><td>string</td></tr><tr><td>      arriveFlag</td><td>客户今日是否已到院</td><td>true</td><td>boolean</td></tr><tr><td>  toUserId</td><td>转咨询员工id（生成一条对应员工的咨询记录）</td><td>false</td><td>string</td></tr><tr><td colspan="4">就诊类型是（咨询）相关参数</td></tr><tr><td>  mainComplaint</td><td>客户主诉</td><td>true</td><td>string</td></tr><tr><td>  consultationProjectIds</td><td>就诊项目或者项目id集合</td><td>true</td><td>array</td></tr><tr><td>  treatmentPlan</td><td>治疗方案</td><td>true</td><td>string</td></tr><tr><td>  undealRemark</td><td>未成交原因</td><td>false</td><td>string</td></tr><tr><td>  undealType</td><td>未成交类型<br/>查询字典：undeal_type<br/><cite doc-id="JVkQwr4eAisxvHkgv9TcOm45nsf" file-type="wiki" title="睿美云开放接口" type="doc"></cite></td><td>false</td><td>string</td></tr><tr><td colspan="4">就诊类型是（治疗 复查 客诉 其他）相关参数</td></tr><tr><td>  consultationProjectIds</td><td>就诊项目或者项目id集合</td><td>true</td><td>array</td></tr><tr><td>  treatmentDoctorIds</td><td>治疗医生</td><td>false</td><td>array</td></tr><tr><td>      mainComplaint</td><td>内容</td><td>false</td><td>string</td></tr></tbody></table>

- 返回结果

**响应示例**:

```JavaScript
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

# 病历（medical_record）

- 注：

接口中的病历夹id（dossierId），建议三方直接从病历夹配置中取

![图片展示的是睿美云开放接口中病历（medical_record）的页面。页面左侧有导航栏，其中“病历管理”选项被红色箭头指向突出显示。右侧是病历列表，显示了病历名称、病历夹id、病历类型、病历内容、创建人id、创建人名称、门店id等信息，部分病历名称被红色框线标注。页面右上角有“+添加病历”按钮。该图片与文档中新增病历接口的上下文相关，直观呈现了病历管理页面，辅助理解接口操作场景。](https://feishu.cn/file/Fkh7bU37Yowqrnxpx7octD1Unqx)



## [新增病历](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#TkH8dpxyzos1gIxzTvlcartpnWe)

> 调用此接口，视为遵循【**睿美云电子病历模版免责协议**】
> 
> 内部病历是富文本格式，所以为了格式好统一，请外部统一转换成图片，并转成base64编码

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/medical-record/add    POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string | 客户id |  |
| type | 是 | int | 病历类型 | 0：普通，1：初诊，2：复诊 |
| content | 是 | string | 病历内容 | 病历内容，只支持base64 |
| dossierId | 是 | string | 病历夹id |  |
| createBy | 是 | string | 病历创建人id |  |
| creatorName | 是 | string | 病历创建人名称 |  |
| tenantId | 是 | string | 门店id |  |

![这张图片展示了睿美云新增病历接口的请求示例，是一个POST请求，请求地址为/api/v1/tpos/medical-record/add。在请求的JSON参数中，包含customerId、type、content三个必填字段，其中type参数的值为0，对应普通病历；content字段为经过处理的base64编码内容，契合该接口要求外部将病历内容转换为base64编码的规则。](https://feishu.cn/file/UWu4be0VSoc0HLxZXEacMhUunTb)

- 返回结果

> data会返回病历的id，错误信息会在msg中返回

```JSON
{
    "code": 10000,
    "data": "148134343829618702",
    "msg": "操作成功"
}
```

## [修改病历](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#NMcXd7ijNoQyZ9xhXf5c5Mw4nrR)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/medical-record/update    POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 病历id |  |
| dossierId | 是 | string | 病历夹id |  |
| contentList | 是 | array |  | 病历内容，只会用第0个元素 |
|   +content | 是 | string | 病历内容 | base64格式字符串 |
|   +type | 是 | int | 病历类型 | 0：普通，1：初诊，2：复诊 |
|   +id | 是 | string | 病历id | 就是最外层的病历id |

![图片展示的是睿美云开放接口修改病历的POST请求界面。请求URL为192.168.2.133:60001/api/v1/tpos/medical-record/update，参数有id、dossierId、contentList等。contentList中包含type、id、content等字段，其中content为base64格式字符串。该图片与文档中修改病历的上下文对应，直观呈现了修改病历时所需填写的请求参数及内容格式，帮助开发者了解接口调用的具体参数配置。](https://feishu.cn/file/Le92bWSYto8xEqxejeBcnXa1nXb)

- 返回结果

> 成功只会有这一个返回结果，错误信息会在msg中返回

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

## [删除病历](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#H0o1d0VGNoHpz3xSR2acUEUYnMb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/medical-record/delete    DELETE**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| id | 是 | string | 病历id |  |

![图片展示的是删除病历的API请求界面。请求方式为DELETE，URL为192.168.2.133:60001/api/v1/tpos/medical-record/delete?id=148134343829618702。在Params标签下，有id参数，其值为148134343829618702。右侧返回结果为JSON格式，显示code为1，data为true，msg为“操作成功”。该图片与文档中删除病历的API请求内容对应，直观呈现了请求参数及返回结果。](https://feishu.cn/file/Axx7bugHSofoK4xVb81cQu37neR)

- 返回结果

> 成功只会有这一个返回结果，错误信息会在msg中返回

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```

# 文件（file）

> 文件的上传存储，取决于机构配置的是什么，现在支持七牛，本地
> 
> 上传参数的file是文件流，base64List的结构如下，传参需要转换成json

```JSON
[
    {
        "base64": "base64编码",
        "fileName": "文件名称"
    }
]
```

## [上传文件](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Pm4xdbQbyon2Z1xcFp8c6ZHOnSb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/file/upload    POST**

- 参数说明

> 用表单上传

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| customerId | 是 | string |  | 客户id |
| typeName | 是 | string | 文件夹名称 | 如果文件夹不存在  <br/>会自动创建对应文件夹 |
| tenantId | 是 | string |  | 门店id |
| file |  | file (array) |  | 文件数组 |
| base64List |  | string |  | 文件的base64形式，如果指定了file，则会忽略base64List的数据 |

![图片展示的是使用Postman进行文件上传的界面。请求URL为192.168.2.133:60005/api/v1/tpos/file/upload，方法为POST。Body部分以form-data方式设置参数，包括customerId、typeName、tenantId、file（两个文件hunting.jpg和1.pdf）以及base64List。右侧返回结果为JSON格式，显示code为10000，data为true，msg为“操作成功”。该图片与文档中文件上传存储相关，直观呈现了上传文件时参数设置及返回结果情况。](https://feishu.cn/file/HHgrbFpCao0hqKx3IzRclvDMnLe)

- 返回结果

> 其余全视为错误，错误信息会在msg中返回

```JSON
{
    "code": 10000,
    "data": true,
    "msg": "操作成功"
}
```



# 报表**（report）**

## [收银记录初始化](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#IsEedlXa6o5QANx9Nl9cpwtzndb)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/report/cashier-record-init    GET**

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| tenantId | 是 | string |  | 门店id |

- 返回结果

allVirtualPayWay：虚拟金支付方式，通常不算实收

payWayList： 实收支付方式

收银记录报表 **/api/v1/tpos/report/cashier-record-page**  的返回数据result中，每一项都有payWayJson

里面的

payMode表示支付方式：对应了payWayList的value值

payMoney表示实际金额

![图片展示了睿美云开放接口中“收银记录初始化”接口的请求参数Payload部分。其中，pay字段下的payJson列表中，有多个payMoney为0且payMode为“1231”的记录，如“payMoney: 0, payMode: “1231””等。此外，还有其他支付方式如“DEFAULT_MINIPARAM_WECHAT”等。该图片与文档中“收银记录初始化”接口的参数说明上下文对应，直观呈现了接口请求时的参数结构及部分支付方式信息。](https://feishu.cn/file/BXa7bNxrZoUUAQxa2iTc6Aonnah)



```JSON
{
    "msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "chargeList": [                            //    收费类型
            {
                "label": "订单收费",
                "value": "0"
            },
            {
                "label": "订单退费",
                "value": "1"
            }
        ],
        "allVirtualPayWay": [                                //    虚拟金支付方式，通常不算实收
            {
                "delFlag": false,
                "ext": "",
                "idList": [],
                "isEnable": false,
                "label": "定金",
                "order": 0,
                "projectFlag": false,
                "sourcePathName": "",
                "sourceTypeDetailType": "",
                "sourceTypeId": "",
                "tenantId": "",
                "type": null,
                "typeId": "",
                "value": "4@@@!!!@@@定金"    
            },
            {
                "delFlag": false,
                "ext": "",
                "idList": [],
                "isEnable": false,
                "label": "储值",
                "order": 0,
                "projectFlag": false,
                "sourcePathName": "",
                "sourceTypeDetailType": "",
                "sourceTypeId": "",
                "tenantId": "",
                "type": null,
                "typeId": "",
                "value": "7@@@!!!@@@储值"
            }
        ],
        "payWayList": [                                    //    实收支付方式
            {
                "delFlag": false,
                "ext": "",
                "idList": [],
                "isEnable": false,
                "label": "微信小进程",                     //    支付方式名称
                "order": 0,
                "projectFlag": false,
                "sourcePathName": "",
                "sourceTypeDetailType": "",
                "sourceTypeId": "",
                "tenantId": "",
                "type": null,
                "typeId": "",
                "value": "1231"                            //    支付方式的自定义code
            },
            {
                "delFlag": false,
                "ext": "",
                "idList": [],
                "isEnable": false,
                "label": "微信小进程支付测试",
                "order": 0,
                "projectFlag": false,
                "sourcePathName": "",
                "sourceTypeDetailType": "",
                "sourceTypeId": "",
                "tenantId": "",
                "type": null,
                "typeId": "",
                "value": "DEFAULT_MINIPARAM_WECHAT"
            },
            {
                "delFlag": false,
                "ext": "",
                "idList": [],
                "isEnable": false,
                "label": "有赞支付",
                "order": 0,
                "projectFlag": false,
                "sourcePathName": "",
                "sourceTypeDetailType": "",
                "sourceTypeId": "",
                "tenantId": "",
                "type": null,
                "typeId": "",
                "value": "YouZanPay"
            }
        ]
    }
}
```

## [收银记录](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#B2D5dPJn3oTZ8sxQJgLcNXEmnMg)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/report/cashier-record-page    POST**

- 参数说明

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><b>字段</b></td><td><b>是否必填</b></td><td><b>类型</b></td><td><b>说明</b></td><td><b>备注</b></td></tr><tr><td>customerInfo</td><td rowspan="3" vertical-align="middle">客户id和收费时间段二选一</td><td>string</td><td></td><td>传客户id</td></tr><tr><td>startTime</td><td>string</td><td>收费时间-开始时间</td><td>yyyy-MM-dd HH:mm:ss</td></tr><tr><td>endTime</td><td>string</td><td>收费时间-结束时间</td><td>yyyy-MM-dd HH:mm:ss</td></tr><tr><td>tenantId</td><td>是</td><td>string</td><td></td><td>门店id</td></tr><tr><td>current</td><td>是</td><td>string</td><td></td><td>当前页码</td></tr><tr><td>limit</td><td>是</td><td>string</td><td></td><td>每页数据量</td></tr><tr><td>chargeType</td><td>否</td><td>array</td><td>收银类型字符串数组</td><td>见PaymentTypeEnum枚举code</td></tr></tbody></table>

![图片展示的是使用Postman工具发送“/api/v1/tpos/report/cashier-record-page”请求的界面。请求方法为POST，URL为192.168.2.146:8885/api/v1/tpos/report/cashier-record-page。Body部分以JSON格式发送参数，包括startTime、endTime、tenantId、current、limit、chargeType等字段。返回结果部分显示了code、data、result等信息，其中result包含date、paymentItemsNum、autoFlag、billingID等字段，还展示了部分paymentItems的详细信息。该图片与文档中介绍的收银记录接口请求及返回结果内容相关，直观呈现了请求参数及返回数据情况。](https://feishu.cn/file/OEn9bSF8RoOhpJxbX7hc3jzkn5f)

- 返回结果

> 报表返回数据太多，此处按需列举返回字段

```JSON
{
    "code": 10000,
    "data": {
        "result": [
            {
                "customerId": "cd8e89e9e3414833a7a8a0b94fee0db0",      //  客户id
                "customerPhone": "1a058026778",                        //  客户姓名
                "type": "订单收费",                                     //  收银类型名称
                "payMark": 0,                                          //  收银类型（PaymentTypeEnum枚举）
                "paymentId": "a09137e5a5bc40b7ac8ef5a04840c46e",       //  费用单id
                "paymentNo": "JF20231214112924592",                    //  费用单号
                "chargeTime": 1702524602000,                           //  收费时间
                "total": 237.50,                                       //  实收合计
                "totalNonActualReceive":"0",                           //  非实收合计
                "billingId": "577628e625284cf0bd5790f61bf8f328",       //  订单id
                "billingNo": "PT20231213164102589",                    //  订单号
                "billingTime": 1703060940000,                          //  开单时间
                "chargeTime": 1703060954000,                           //  收银时间
                "paymentItemNames": "【项目】测试下发2，\r\n【项目】测试下发1，\r\n【商品】来个少点的，\r\n【药品】苯唑西林"    //  费用项
                "payWayJson":[{                                //    实收支付方式，和初始化接口的payWayList对应
                    "payMode": "YouZanPay"
                    "payMoney": 237.50
                  }]
            }
        ],
        "total": 1
    },
    "msg": "操作成功"
}
```

#  **企微聊天记录**

## [聊天记录查询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#KkGNdPk1Woq9xEx40Y5cNDQhnQf)

发送人和接收人强绑定，如果要查两人的对话，建议使用接口 /api/v1/tpos/wechat/message/cursorMessage

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/wechat/message/messageList POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| fromId | 非 | String |  | 发送人id |
| toId | 非 | String |  | 接收人id |
| roomId | 非 | String  |  | 群id |
| msgTimeStart | 非 | Date |  | 消息时间范围 |
| msgTimeEnd | 非 | Date |  | 消息时间范围 |
| toNickName | 非 | String |  | 接收人昵称 |
| cursor | 非 | Integer |  | 返回值中，前一次请求的nextCursor |
| size | 非 | Integer | 范围50-200，不传或不满足规则，默认50 | 单页数量 |

- 返回结果

```JSON
{
"msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "nextCursor": 224,   //分页的cursor
        "records": [
            {
                "fromUser": "a1c9a9e971edd8e12abd7e738358a0af",  //发送人id
                "fromUserName": "佳琪",  //发送人姓名
                "msgContent": "123123",  //消息内容
                "msgTime": 1587109338000,  //消息时间
                "msgType": "text",  //消息类型
                "roomId": "",   //群id
                "seq": 224,  //消息序号
                "toOne": "wm76rcDwAAcx0KAfjV-IQUDrrM-Y9IHA",  //toOne接受消息的一个企微id
                "toUserName": "未知用户",  //接收人姓名或群名称
                "toUserId": "xxxxxxxxxx"  //接收人id
            }
        ]
    }
}
```

    

## [聊天记录查询](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#KkGNdPk1Woq9xEx40Y5cNDQhnQf)

不分发送人接送人，查询私聊记录

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/wechat/message/cursorMessageInterList     POST**

- 参数说明

| **字段** | **是否必填** | **类型** | **说明** | **备注** |
|-|-|-|-|-|
| fromId | 非 | String | 私聊，发送人必须和接收人都传 | 发送人id |
|            fromIdType |        非 |              Sting |  |  发送人id类型（0：*默认，企微id，**1 系统员工**2 系统客户*  <br/>） |
| toId | 非 | String | 私聊，发送人必须和接收人都传 | 接收人id |
|             toIdType | 非 | int |  | 接收人id类型（0：*默认，企微id，**1 系统员工**2 系统客户*  <br/>） |
| roomId | 非 | String  |  | 群id |
| msgTimeStart | 非 | Date |  | 消息时间范围 |
| msgTimeEnd | 非 | Date |  | 消息时间范围 |
| toNickName | 非 | String |  | 接收人昵称 |
| cursor | 非 | Integer |  | 返回值中，前一次请求的nextCursor |
| size | 非 | Integer | 范围50-200，不传或不满足规则，默认50 | 单页数量 |
| descFlag | 否 | Boolean |  | 是否倒序 |

- 返回结果

```JSON
{
"msg": "成功获取数据，数据非空",
    "code": 10001,
    "data": {
        "nextCursor": 224,   //分页的cursor
        "records": [
            {
                "fromUser": "18312341234",  //发送人企微id
                "fromUserId": "7214a7a2b39e3d6c91168e4727f4e4f3", //发送人系统id
                "fromUserName": "佳琪",  //发送人姓名
                "msgContent": "123123",  //消息内容
                "msgTime": 1587109338000,  //消息时间
                "msgType": "text",  //消息类型
                "roomId": "",   //群id
                "seq": 224,  //消息序号
                "toOne": "wm76rcDwAAcx0KAfjV-IQUDrrM-Y9IHA",  //接收人企微id
                "toUserId": "278903936550174722", //接收人系统id
                "toUserName": "未知用户"  //接收人姓名或群名称
            }
        ]
    }
}
```

# 客户资产变更

## [客户资产变更列表](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#Ycijd4b3bo2fDnxGk1dcluEJnsc)

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/top/paymentAssetChange/paymentAssetChangeList   POST**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| customerId | 客户id |  |  | String |
| tenantId | 门店id |  |  | string |
| index | 开始页码 |  | true | integer(int32) |
| size | 每页条数 |  | true | integer(int32) |
| getTotalFlag | 是否获取总页数 |  |  | Boolean |
| status | 确认状态(0:*待确认,1:已确认*) |  |  | Integer |

- 返回结果

**响应参数**:

<bitable table-id="tblO9MsEIi7esec0" token="BYgabyXRia3oMbsiTtNczDwFnLf"></bitable>

## [得到资产变动记录](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#DVyWdprUboCQyTxaV7xcvYS5nhb)

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/top/paymentAssetChange/getOneRecord  GET**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| id | 变动记录Id |  | 必填 | String |

- 返回参数

<bitable table-id="tblBhVSrrgLRYjJ9" token="BYgabyXRia3oMbsiTtNczDwFnLf"></bitable>

## [确认资产变更](https://ruimeiyun.feishu.cn/wiki/JVkQwr4eAisxvHkgv9TcOm45nsf#J07RdcPeioHpDgxWlLLcHJTan2f)

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/top/paymentAssetChange/confirmAssetChange  POST**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| assetChangeRecordId | 资产变更 |  | 必填 | String |
| customerId | 客户id |  | 必填 | String |
| assetPassword | 用户密码 |  | 必填 | String |

# 问卷

## 1. 未填写的问卷列表

- 请求URL

**/api/v1/top/questionnaireCustomer/notYetList  POST**

- 请求参数

```Plain Text
{
    "customerId":"a7258949583e4e679b02a9fccd7317b3",
    "tenantId":"1"
}
```

- 请求参数说明

<bitable></bitable>

- 返回参数

```json
{
    "code": 10000,
    "data": [
        {
            "account": "lmk",
            "createBy": "915928121d976dbd6579ab98be6f5d9c",
            "createDate": 1706859427000,
            "customerId": "a7258949583e4e679b02a9fccd7317b3",
            "customerName": "",
            "dataJson": "",
            "delFlag": false,
            "fillDate": null,
            "fillFlag": false,
            "hospitalKey": "zxx_test",
            "id": "194475724910972934",
            "phone": "",
            "questionnaireId": "1519867428219895810",
            "questionnaireJson": "",
            "questionnaireName": "2312243",
            "questionnairePublishTime": "",
            "questionnaireStatus": null,
            "tenantId": "1",
            "totalScore": null,
            "updateBy": "915928121d976dbd6579ab98be6f5d9c",
            "updateDate": 1706859427000,
            "verificationKey": "aYlOL3BfWUD7TJ4f5l5CKdz7ynBN5AzRmUZGXQT5sJ8="
        }
    ],
    "msg": "操作成功"
}
```

- 返回参数说明

<bitable></bitable>

- 参数使用说明：

account，customerId，hospitalKey，questionnaireId，tenantId，verificationKey  
这些字段在调用静态页面时需要携带参数至静态页面

- 静态页面地址：
- WebView 加载 问卷详情页面 src 传

src = \`\${questionnaireUrl}?\${encodeURIComponent(

      \`id=xxx&tenantId=1&customerId=xxx&account=xxx&verificationKey=xxxx&detail=1&t=\${new Date().getTime()}\`

    )}\`

 

questionnaireUrl:问卷H5页面地址

测试环境:

[https://static.web.realmerit.com.cn/h5Form/test/build/index.html](https://static.web.realmerit.com.cn/h5Form/test/build/index.html)

Uat环境:

[https://static.web.realmerit.com.cn/h5Form/uat/build/index.html](https://static.web.realmerit.com.cn/h5Form/master/build/index.html)

正式环境:

https://static.web.realmerit.com.cn/h5Form/master/build/index.html

 

 

id 问卷id ，问卷列表返回取  questionnaireId这个字段

tenantId :门店id 问卷列表返回

account：账号 问卷列表返回

customerId：客户Id 问卷列表返回

verificationKey:验证秘钥  问卷列表返回

hospitalKey:机构代码 问卷列表返回

detail 问卷是否是已填写状态  已填写 传 1 未填写传 空， 可以根据问卷列表返回的fillFlag 判断，true 为已填写

 

t 当前时间， 刷新缓存用

## 获取客户的问卷记录

- 请求URL（需要tpos鉴权）

**接口地址**: **/api/v1/top/questionnaireCustomer/page  post**

- **请求参数**:

| 参数名称 | 参数说明 | 请求类型 | 是否必须 | 数据类型 |
|-|-|-|-|-|
| customerId | 客户id |  | 必填 | String |
| questionnaireStatus | 问卷状态  <br/>   *PENDING*(0, "待发布"),  <br/>   *LAUNCHED*(1, "已发布"),  <br/>   *REVOKE*(2, "已作废"),  <br/>   *SENDING*(3, "发布中"); |  | 否 | 数字 |
| page | 当前页（1开始） |  | 必填 | 数字 |
| size | 每页的数量 |  | 必填 | 数字 |

- 返回参数

<sheet sheet-id="oILuKq" token="shtcnTKOlDjgLChPQvGBfiOv2Eg"></sheet>

- 请求示例

请求

![图片展示的是一个API接口请求界面，用于查询客户问卷记录。界面中“Body”标签下，参数类型为json，参数内容为{ "customerId":"sdsd", "questionnaireStatus":0, "page":1, "size":20 }。该图片与文档中“获取客户的问卷记录”部分内容对应，是通过POST请求向/v1/top/questionnaireCustomer/page接口发送数据，以查询客户问卷记录的示例，展示了请求体中参数的具体填写方式。](https://feishu.cn/file/JGypbiKfIo3qXwxC5tucXAPnnBg)

响应值：

```SQL
{
    "code": 10000,
    "data": {
        "countId": "",
        "current": 1,
        "maxLimit": null,
        "optimizeCountSql": true,
        "orders": [],
        "pages": 1,
        "records": [
            {
                "createBy": "",
                "createDate": 1706859221000,
                "customerId": "00df10d51b8e4f6db79c2a83b7d9303e",
                "customerName": "杨7俊辉",
                "dataJson": "",
                "delFlag": false,
                "fillDate": null,
                "fillFlag": false,
                "id": "194474865367973888",
                "phone": "1a000257755",
                "questionnaireId": "1519863300001349633",
                "questionnaireJson": "{\"list\": [{\"id\": \"JZgL395jO\", \"pid\": \"\", \"label\": \"多行文本\", \"model\": \"textarea_JZgL395jO\", \"width\": \"100%\", \"componentType\": \"textarea\", \"formItemOptions\": {\"col\": {\"labelCol\": {}, \"wrapperCol\": {}}, \"rules\": [], \"labelWidth\": 100, \"diyLabelWidth\": false}, \"componentOptions\": {\"type\": \"text\", \"autoSize\": true, \"disabled\": false, \"placeholder\": \"请输入\"}}, {\"id\": \"wZTixnibW\", \"pid\": \"\", \"label\": \"单选框\", \"model\": \"radio_wZTixnibW\", \"width\": \"100%\", \"componentType\": \"radio\", \"formItemOptions\": {\"col\": {\"labelCol\": {}, \"wrapperCol\": {}}, \"rules\": [], \"labelWidth\": 100, \"diyLabelWidth\": false}, \"componentOptions\": {\"layout\": \"inline\", \"options\": [{\"key\": \"8xgeEZMdWt\", \"label\": \"label-1\", \"value\": \"value-KJf7sRYFau\"}, {\"key\": \"uVk9TNEhvF\", \"label\": \"label-2\", \"value\": \"value-9iRnGnkNIG\"}, {\"key\": \"lskNswkR9A\", \"label\": \"label-3\", \"value\": \"value-cMITZzwXBY\"}], \"disabled\": false, \"placeholder\": \"\"}}], \"config\": {\"size\": \"middle\", \"wdith\": \"100%\", \"layout\": \"horizontal\", \"labelAlign\": \"right\"}}",
                "questionnaireName": "规范问卷",
                "questionnairePublishTime": "2022-04-29 10:20:47",
                "questionnaireStatus": 1,
                "tenantId": "",
                "totalScore": null,
                "updateBy": "",
                "updateDate": null
            }
        ],
        "searchCount": false,
        "size": 20,
        "total": 9
    },
    "msg": "操作成功"
}
```

# 工牌

## 分页查询当天接待客户列表

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/smartworkcard/customerList  POST**

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
|-|-|-|-|
|   name | 名称 | false | string |
|   phone | 电话 | false | string |
|       tenantId | 门店id | true | string |
|   size | 每页数量，默认1 | false | integer |
|   page | 页码，默认20 | false | integer |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果 | integer |  |
| data | 结果内容 |  |  |
|   current | 当前页 | integer |  |
|   records | 客户列表 | array |  |
|     name | 姓名 | string |  |
|     phone | 电话 | string |  |
|     sex | 性别,1：男，2：女 | integer |  |
|     age | 年龄 | integer |  |
|     id | 客户id | string |  |
|             tenantId | 租户id | string |  |
|             receptionDate | 接待时间 | string |  |
|            consultationCount | 咨询次数 | integer |  |
|            projects | 就诊项目 | array | ["激光脱毛","瘦脸针"] |
|            consultantUserId | 咨询师id | string |  |
|            consultantUserName | 咨询师名称 | string |  |
|   size | 每页数量 | integer |  |
|   total | 总数 | integer |  |
| msg | 响应消息 | string |  |

## 质检点、客户标签、ASR转写结果推送(随行天使)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/smartworkcard/jellyCallback  POST**

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 类型 |
|-|-|-|-|
| id | 唯一id,同一个录音多次分析相同 | 否 | string |
| eventType | 事件类型，aivoice.visit.analyzed.summary | 是 | string |
| tenantId | 门店id | 是 | string |
| customerId | 客户id ，和客户电话选其一 | 否 | string |
| phone | 客户电话，和客户id选其一 | 否 | string |
| userId | 医生id | 是 | string |
| startTime | 录音开始时间 | 是 | string |
| endTime | 录音结束时间 | 是 | string |
| duration | 录音时长（毫秒） | 否 | integer |
| result | 命中质检点、标签 | 是 | array |
|     modelCategory | 类型，1质检点，2客户标签 | 是 | string |
|     dimensionName | 维度名称 | 是 | string |
|     speechName | 话术点名称 | 是 | string |
|     modelName | 模型名称 | 是 | string |
|         qualified | 是否命中 | 是 | boolean |
| audioAsrResult | asr转义分析结果 | 是 | array |
|            beginTime | 开始时间偏移量 | 否 | integer |
|            endTime | 结束时间偏移量 | 否 | integer |
|            text | 文本内容 | 是 | string |
|            role | 角色类型,-1：医生，0：客户 | 是 | integer |
| analyzeFieldResult | 自定义关联字段，需要和睿美云大模型字段配置三方字段名对应,字段内容可添加小标题，格式为[{"label":"客户档案","value":""},{"label":"护肤习惯","value":""}] | 否 | map |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果，!10000表示失败 | integer |  |
| data | 结果内容 | object |  |
| msg | 响应消息 | string |  |

## 质检点、客户标签、ASR转写结果推送，适用于工牌录音同步到睿美云(通用)

- 请求URL（需要tpos鉴权）

**/api/v1/tpos/smartworkcard/callback POST**

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 类型 |
|-|-|-|-|
| id | 唯一id,同一个录音多次分析相同 | 否 | string |
| eventType | 事件类型，aivoice.visit.analyzed.summary | 是 | string |
| platformType | 三方平台类型,对接时确认固定值 | 是 | string |
| tenantId | 门店id | 是 | string |
| recordId | 睿美云录音id | 否 | string |
| consultationId | 接待id | 否 | string |
| customerId | 客户id ，和客户电话选其一 | 否 | string |
| phone | 客户电话，和客户id选其一 | 否 | string |
| userId | 医生id | 是 | string |
| startTime | 录音开始时间 | 是 | string |
| endTime | 录音结束时间 | 是 | string |
| duration | 录音时长（毫秒） | 否 | integer |
| detail_url | 录音详情页地址 | 否 | string |
| result | 命中质检点、标签 | 是 | array |
|     modelCategory | 类型，1质检点，2客户标签 | 是 | string |
|     dimensionName | 维度名称 | 是 | string |
|     speechName | 话术点名称 | 是 | string |
|     modelName | 模型名称 | 是 | string |
|         qualified | 是否命中 | 是 | boolean |
| audioAsrResult | asr转义分析结果 | 是 | array |
|            beginTime | 开始时间偏移量 | 是 | integer |
|            endTime | 结束时间偏移量 | 是 | integer |
|            text | 文本内容 | 是 | string |
|            role | 角色类型,-1：医生，0：客户 | 是 | integer |
| analyzeFieldResult | 自定义关联字段，需要和睿美云大模型字段配置三方字段名对应,字段内容可添加小标题，格式为[{"label":"客户档案","value":""},{"label":"护肤习惯","value":""}] | 否 | map |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果，!10000表示失败 | integer |  |
| data | 结果内容 | object |  |
| msg | 响应消息 | string |  |

## 推送门店信息到三方

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 类型 |
|-|-|-|-|
| tenantId | 睿美云门店id | 是 | string |
| name | 门店名称 | 是 | string |
| thirdOrgId | 三方门店id | 否 | string |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果，!0表示失败 | integer |  |
| data | 结果内容 | object |  |
| msg | 响应消息 | string |  |

## 推送员工信息到三方

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 类型 |
|-|-|-|-|
| thirdOrgId | 三方门店id | 是 | string |
| tenantId | 睿美云门店id | 是 | string |
| userList | 员工信息 | 是 | array |
|            userId | 睿美云员工id | 是 | string |
|            phone | 电话 | 是 | string |
|            name | 名称 | 是 | string |
|            gender | 性别，1：男，2：女 | 否 | integer |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果，!0表示失败 | integer |  |
| data | 结果内容 | object |  |
| msg | 响应消息 | string |  |

## 开始录音(含硬件)

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 类型 |
|-|-|-|-|
| thirdOrgId | 三方门店id | 是 | string |
| tenantId | 睿美云门店id | 否 | string |
| userId | 医生id | 是 | string |
| userName | 医生名称 | 是 | string |
| phone | 医生电话 | 否 | string |
| recordId | 睿美云录音唯一标识 | 是 | string |
| visitCount | 来访次数 | 否 | integer |
| startTime | 开始时间（yyyy-MM-dd HH:mm:ss） | 是 | string |
| customerId | 客户id | 否 | string |
| customerName | 客户姓名 | 否 | string |
| customerPhone | 客户电话 | 否 | string |
| customerGender | 客户性别1：男，2：女 | 否 | integer |
| guestType | 客人类型，（初诊、复诊、老客人、其他） | 否 | string |
| guestPurpose | 到院目的 | 否 | string |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果，!0表示失败 | integer |  |
| data | 结果内容 | object |  |
| msg | 响应消息 | string |  |

## 结束录音(含硬件)

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 类型 |
|-|-|-|-|
| thirdOrgId | 三方门店id | 是 | string |
| tenantId | 睿美云门店id | 否 | string |
| userId | 医生id | 是 | string |
| userName | 医生名称 | 是 | string |
| phone | 医生电话 | 否 | string |
| recordId | 睿美云录音唯一标识 | 是 | string |
| endTime | 结束时间（yyyy-MM-dd HH:mm:ss） | 是 | string |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果，!0表示失败 | integer |  |
| data | 结果内容 | object |  |
| msg | 响应消息 | string |  |

## 更新录音客户信息

- 参数说明

**请求参数**:

| 参数名称 | 参数说明 | 是否必须 | 类型 |
|-|-|-|-|
| thirdOrgId | 三方门店id | 是 | string |
| tenantId | 睿美云门店id | 否 | string |
| recordId | 睿美云录音唯一标识 | 是 | string |
| customerId | 客户id | 否 | string |
| customerName | 客户姓名 | 否 | string |
| customerPhone | 客户电话 | 否 | string |
| customerGender | 客户性别1：男，2：女 | 否 | integer |
| guestType | 客人类型，（初诊、复诊、老客人、其他） | 否 | string |
| guestPurpose | 到院目的 | 否 | string |

- 返回结果

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
|-|-|-|-|
| code | 响应结果，!0表示失败 | integer |  |
| data | 结果内容 | object |  |
| msg | 响应消息 | string |  |

---

# 补遗（2026-09-16 数据之眼 · 实拉线上文档核对）

> 本地文档原缺 8 个接口。以下内容由 `lark-cli` 拉取飞书现行文档
> （`JVkQwr4eAisxvHkgv9TcOm45nsf`，431,353 字符 / 164 个路径）并逐项实调验证后补入。

## 本地缺失的 8 个接口（清单）

| 路径 | 说明 |
|---|---|
| `/api/v1/tpos/visit/obsolete-visit` | **作废回访**（详见下节·有坑） |
| `/api/v1/tpos/basic/get-can-buy-equity-card-list` | 可购买权益卡列表 |
| `/api/v1/tpos/basic/get-equity-card-detail` | 权益卡详情 |
| `/api/v1/tpos/consultation/acceptance-tool` | 接诊工具 |
| `/api/v1/tpos/customer/part-label-list` | 客户部分标签 |
| `/api/v1/tpos/order/add-balance-recharge` | 余额充值 |
| `/api/v1/tpos/order/add-billing-equity-card` | 开单-权益卡 |
| `/api/v1/tpos/order/add-deposit` | 定金 |

## 作废回访 obsolete-visit（⚠️ 当前不可用）

```
POST /api/v1/tpos/visit/obsolete-visit
请求示例: { "contentId": "538725851315831066", "obsoleteReason": "测试", "tenantId": "1" }
请求参数: contentId 回访id(非必填,string) / obsoleteReason 作废原因 / tenantId 门店id
响应示例: { "code": 10000, "data": true, "msg": "操作成功" }
```

**🔴 实测结论（2026-09-16）：该接口对本开放接口账号一律不可用。**

- 无论传什么 id（`planId` 待回访记录 / `planId` 已回访记录 / `planId` 已作废记录 /
  `customerId` / 文档自带样例 / 完全不传），**全部返回 `{"code":401,"msg":"没有找到您要的资源"}`**，
  错误码完全一致 → 不是"id 传错"，而是接口层面的问题。
- 同期 `get-visit-type` / `get-visit-page` 均 `code:10000` 正常 → **鉴权无问题**。
- **`contentId` 是孤儿字段**：全文检索 431KB 线上文档，`contentId`（忽略大小写）只出现 **2 次，
  且都在「作废回访」这一节内**（请求示例 + 参数表）。**没有任何其他接口会产出或消费它**，
  `get-visit-page` 的响应体（含 20 个文档未列出的隐藏字段）中也没有 `contentId`。
- 文档另一处截图明确记载 `code 401 = "身份信息已经过期，请重新登陆"` → **401 属"鉴权/资源范围"类，
  不是"记录不存在"**。推测：该接口未对开放接口账号开放，或文档参数名有误。

**替代方案（当前可用）**：用 `complete-visit` 把记录从「待回访」结清为「已回访」，
`visitType=44(其他)`，`response` 写明清理原因 → 效果等同"从队列清掉"，且可审计。
现成脚本：工作区 `void_0826_marketing.py`（默认 dry-run）。

## get-visit-page 文档三处不准（实测纠正）

1. **响应里的 `visitedFlag` 是 boolean，但请求筛选是数组字符串**：
   请求 `visitedFlag: ["1"待回访 / "2"已回访 / "3"作废]`（数组）；
   响应 `visitedFlag: true/false`。
2. **🔴 陷阱：作废（状态3）的记录在响应里也显示 `visitedFlag=false`**。
   因此**光看布尔值无法区分「待回访」与「已作废」**——要判断作废必须用请求筛选 `["3"]` 分桶拉取。
3. **响应实际字段远多于文档**。文档只列 20 个左右，实测还有：
   `typeId` `createBy` `createById` `planVisitTenantId` `delayFlag` `autoSendFlag`
   `chatIds` `aiPlanContent` `priorityScore` `visitPriority` `visitPriorityName`
   `visitEffect` `devPlanVisitResult` `customerType` `externalUserId`
   `addExternalUserFlag` `phoneNumber` `relatedSourceMaterialIdList`
   `relatedSourceMaterialList`。
   → 其中 `typeId`（数值型回访类型）、`createBy`（创建人）、`planVisitTenantId`（归属门店）
   在做筛选/归因时**必须用这三个**，文档里没有。
   ⚠️ 响应含 `phoneNumber`，按隐私铁律**不取不写**。

## get-visit-page 不支持按「执行人」筛选（实测）

依次测试 7 个参数名：`userId` / `userIds` / `visitedById` / `visitedBy` /
`visitedByIds` / `staffId` / `ownerId` —— 返回总量恒为 388，**全部被服务端忽略**。
→ 想按员工维度取回访，只能全量拉取后按 `userId`（计划回访人）或 `visitedBy`（实际回访人）本地分组。

## 🔴🔴 get-visit-page 两个会「算错」的坑（2026-09-16 实测，比筛选失效更危险）

### 坑1：`visitDateStart/End` 服务端筛选**不严格**，会漏出区间外记录
实测：以 `visitDateStart=2026-09-01, visitDateEnd=2026-09-16` 查询，服务端返回 **1,399** 条，
但其中 **只有 1,022 条** 的 `visitDate` 真的落在区间内；多出的 377 条是
`2026-08-26`（284 条）+ `2026-08-29`（93 条）——**全是 `delayFlag=True` 的超期记录**。
→ **统计前必须客户端二次校验 `visitDate`**，否则数字虚高约 37%。
（`visitedDateStart/End` 同理，也应校验 `visitedDate`。）

### 坑2：分页拉取失败会**静默截断**，让你得出错误结论
实测：同一查询 `total=1400 / pages=7`，某一页请求超时后循环 break，
**函数安静地返回了 1,021 条**——不报错、不告警。若不校验就会基于残缺数据下结论。
→ 正确做法：**单页失败重试 3 次**；仍失败则**显著告警并中止**，绝不用残缺数据出结论。
（本坑对 `total` 大于 1000 的查询尤其容易触发，因为页数多、总耗时接近超时线。）

### 坑3（附带）：`day` 字段恒为 `None`
实测 1,012 条治疗后回访计划的 `day` **全部为 None** → **无法用「第几天」判重**，
只能靠 `content` 内容文本（归一化去空白后比对）判重。按"同客户+同类型"粗判会把
D1/D3/D7 多节点误杀（实测误判 631 条，真实重复只有 98 条）。

## get-all-plan（开发计划）**不在开放接口中**
- `POST /api/v1/tpos/customer/get-all-plan` → `code 20002 请求方式不支持`
- `GET  同上` → `code 20004 缺少必要请求参数`
- 全文检索线上文档（431KB / 164 路径）**无此接口**
→ 需要"待开发项目/开发计划"数据时走 `POST /api/v1/tpos/consultation/page` 替代。

## consultation/page 使用要点（查询咨询）
- **必带 `tenantId`**（string），否则 `20002 门店id不能为空`
- **响应慢**：默认 15s 超时会失败，需 **≥40s**；必须缓存，不可逐客实时拉
- 高价值字段：`mainComplaint`（客户主诉）、`treatmentPlan`（治疗方案）、
  `conProjects`（咨询项目）、`consumptionStatus`（**未成交** ← 最精准的"有需求未转化"信号）、
  `consultationStatus`、`smartLabelList`、`customerType`、`receptionTime`、`userId/userName`（接诊人）
- ⚠️ 响应含 `phoneNumber`，按隐私铁律不取不写

## customer-by-id 高价值字段（160 字段中与经营相关的）
- **流失/活跃**：`activeStatus` + `activeStatusDesc`（如"深睡"）、`noVisitDay`（距上次到访天数）、
  `smartLabelCommonName`（智能标签，如"失效"）、`poolName`（如"失效顾客"）、`cusPoolTypeDesc`
- **治疗节奏**：`latestTreatDate`、`latestTreatProject`、`latestArriveDate`、`latestVisitedDate`、
  `firstRealTreatDate`、`treatTime`、`costTime`
- **价值**：`memberLevelName`（如"二星20000"）、`costAmount`、`costThisYear`、`integralTotal`、
  `balance`、`givenBalance`、`rfm`、`fScore/mScore/rScore`、`propensity`
- **归属**：`sysUserName` + `sysUserId`（当前归属）、`relatedConsul`（历史关联串）、
  `exclusiveServerName`、`roleManagerInfoList`、`wechatSysUserName`
- **意向**：`preProNames`（预约项目）、`preDeptName`、`preDate`
- ⚠️ 含 `mainPhone` / `phoneNumber` / `sysUserPhone` → **隐私，不取不写**
- ⚠️ 实测偶见 `name` 与 `customerName` 混淆填成员工名，展示以 `vipNum` + 主档 `name` 为准

## 回访类型 / 方式枚举（get-visit-type / get-visit-way-type 实拉）

类型：`1 治疗后回访`、`2 咨询未成交回访`、`3 成交未治疗回访`、`4 开发计划开始前回访`、
`5 开发计划失效前回访`、`6 企微标签回访`、`7 智慧标签回访`/`生日回访`、`8 新建客人`、
`9 注意事项提醒`/`试探性种草回访`、`10 集中种草回访`/`未上门回访`、`11 皮肤管理回访`/`疗程教育回访`、
`12 医美回访`/`生日前x天回访`、`13 VIP满意度调查`/`权益卡购买后`、`14 未消费回访`、
`30 沉睡客户回访`、`31 满意度调查回访`、`32 其他回访`、`61 报备后回访`、`62 报备未到院回访`、
`74 预约未到院`、`81 邀约回访`、`96 再次治疗提醒`、`97 客情维护`、`98 日常跟踪回访`
（注：同值重名是系统内多租户/多分类共存，实际以 value 为准）

方式：`40 电话`、`41 微信`、`42 现场`、`43 短信`、`44 其他`、`45 企业微信`

## 系统内回访待办规模（tenantId=1 实拉 2026-09-16）

| 桶 | 条数 |
|---|---|
| 待回访 `["1"]` | 95,108 |
| 已回访 `["2"]` | 559,782 |
| 作废 `["3"]` | 102,492 |

近期（8/26 起）两类记录的区隔方式：`typeId=81 邀约回访` + `visitDate=2026-08-26` = 营销群发遗留；
`typeId=1 治疗后回访` = 真实临床回访。**这个「按 typeId + 日期」的判据是区分噪音与真实任务的关键。**

---

## 补遗二（2026-09-16 下午 · 企微归属治理专项）

### 新增可用接口（线上文档有、此前未收录）

| 接口 | 方法 | 实测 | 说明 |
|---|---|---|---|
| `/api/v1/tpos/common/tenantList` | GET | ✅ `code:10000` | 门店清单。实测 `1=成都漾肤--凯德店` / `2=成都漾肤-双楠店` / `3=成都漾肤-远大店` |
| `/api/v1/tpos/customer/customer-qw-info` | GET | ✅ `code:10000` | 该客户**企微关系能否转移**。返回 `data.changeAllow`(bool) + `data.reason` |
| `/api/v1/tpos/customer/get-pool-info` | GET | ✅ `code:10000` | 可转移到的客户池列表 `data.commonPool[]`，含 `poolId/poolName/userId/userName` |
| `/api/v1/tpos/customer/transfer-pool` | POST | ⚠️ 契约完整，**未实测写入** | 客户池转移 + **企微关系转移** + **回访计划转移** |

`transfer-pool` 的 body：`customerId`(必填) / `poolId`(**必填**) / `sysUserId` / `syncVisitPlan`(必填, bool) /
`transferWxFlag` / `needApprovalFlag` / `reason` / `transTenantId`。
- `transferWxFlag=true` → 企微好友一起转（文档："只能是企微客户才能操作"，先用 `customer-qw-info` 判）
- `syncVisitPlan=true` → 回访计划一起转（⚠️ **非实时，每天凌晨 3:00 定时执行**）
- `poolId` 必填 → 只想换咨询师不想换池：用 `get-pool-info` 取当前池 id 原样传回
- `sysUserId` 传 **hex id**（`user/get-page` 的 `id`），不是短账号

### 文档未提及但极关键的字段（`customer-search`）

| 字段 | 说明 | 实测覆盖率 |
|---|---|---|
| `wechatSysuserId` | **企微好友持有者的睿美云员工账号**（稳定，与 `staff_push_config.json` 的 `userid` 同命名空间） | 33.1% |
| `wechatSysUserName` | 企微**昵称** —— ⚠️ **会漂移，不能用来判归属** | 33.1% |
| `namePy`（`user/get-page`） | 姓名拼音，可辅助核对账号归属；但**沿用旧账号的人对不上** | 100% |
| `tenantId` / `tenantName` | 客户建档门店 | 100% |
| `crossHospitalSysUserName` | 跨院咨询师 | **0%（不可用）** |
| `sysUserPhone` / `externalUserId` / `exclusiveStoreName` | — | **0%（不可用）** |

**四字段陷阱（必读）**：
1. `sysUserId` 是 32 位 hex，`wechatSysuserId` 是短账号 → **永不相等**，别直接比。
2. `wxBindFlag` **不是**"是否加了企微"（6,453 位有企微者中仅 1,942 位为 true）。
3. `wechatSysUserId` **≠** `namePy`：`ZhengYiQiu`=汪怡辰 / `meiling`=赵翊妗 / `xiaoyang`=潘婷 /
   `DaShiZi`=柳佩 / `WangMouMou`=王紫 / `alaso`=徐丽军，都是**沿用旧人的登录账号**。
4. `customer-search` **不带 `tenantId` = 全机构**。实测 全机构 28,107 / 凯德 19,519 / 双楠 926 / 远大 4,422。

### 分页硬限

`customer-search` 用 `page` 翻到**第 21 页即 `code:20002`**（≈ 10,000 条上限）。
→ 超 1 万条改 **`lastCustomerId` 游标**（传上一批最后一条的 `id`，`page` 恒传 1）。实测 40 批拉完 19,519 条仅 47 秒。

### 归属错位问题的量化结论（漾肤凯德店）

- 全池 19,519 位：无企微 66.9% / **有企微但系统无归属 19.4%（3,784 位）** / 归属一致 9.3% / 归属错位 3.2%。
- 那 3,784 位的企微实际在谁手里：**74.6% 在自己人在职咨询师手里**（潘婷 1,404 / 赵翊妗 713 / 汪怡辰 708）。
- 回访卡实测（476 张）：执行人能直触 28.4% / 企微在别人 43.1% / 无企微 22.9% / 外部账号 5.3%。
- 按角色：咨询师 49.7% 可直触、皮肤管理师 19.5%、**兜底指派（轮询/离职账号）0%**。
