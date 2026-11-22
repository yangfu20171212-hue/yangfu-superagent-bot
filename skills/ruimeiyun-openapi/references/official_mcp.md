# 睿美云官方 MCP 工具（调用通道说明）

> **来源**：飞书 wiki `SlVTwN3hUifY1IkWP54cGRv8nDh`《睿美云 MCP 工具》（分享链接 + 访问密码），
> 文档标注「11月20日修改」，抓取于 2026-11-22。
> **访问方式**：该链接为密码分享页，需在页面输入密码后解锁；本文件不记录密码、appKey 或任何凭证。
> **定位**：这是**睿美云官方 MCP（appKey 通道）**的配置说明，不是 TPOS REST 开放接口文档。
> REST 全量接口请看 `api_capability_map.md` / `ruimeiyun_api_full.md`；两条通道并存、互不替代。

## 1. 三种调用通道，别混

| 通道 | 认证方式 | 能力范围 | 本机状态 |
|---|---|---|---|
| **TPOS REST 直连**（`references/rmy_client.py`） | TPOS RSA 签名 4 个 Header | 178 个接口全文契约，可读可写、参数粒度最细 | ✅ 主力通道，客户明细必走这里 |
| **自带 stdio MCP `ruimei-tpos`**（`scripts/rmy_mcp_server.py`） | 内部封装同一套 TPOS 签名 | 6 个快捷工具 + `rmy_call` 通用透传 | 已在 `mcp.json` 注册，当前 disabled |
| **睿美云官方 MCP `rmy`** | `appKey`（Header），**权限继承睿美云账号** | **92 个函数**（90 工具 + 2 文档独有），含 3 个写工具；清单见 `official_mcp_functions.md` | ✅ 已启用 `type: streamable-http`（旧 SSE 实测 405，已弃用） |

🔴 已知限制（本机实测，见 `SKILL.md` 注意事项 6/11）：官方 MCP 的 6 个客户维度函数
（治疗/开单/回访/咨询/接待/开发计划）一律返回「没有查到…」，`getPageCustomerInfo` 分页不可靠。
**不要用官方 MCP 的「没查到」推断客户没有数据，客户明细一律走 REST 直连。**

## 2. 调用方式（文档原文配置）

文档给了两种等价的客户端配置写法，`url` 里的 `xxxx` 换成**你所在机构的域名**。

写法一（部分客户端直接以服务名为键）：

```json
{
  "睿美云": {
    "type": "streamable",
    "url": "https://xxxx/ai/neuron-mcp",
    "headers": {
      "appKey": "<在睿美云后台复制的 APP Key>"
    },
    "description": "睿美云MCP市场"
  }
}
```

写法二（`mcpServers` 包裹，Claude Desktop / Cursor / WorkBuddy 等通用）：

```json
{
  "mcpServers": {
    "睿美云": {
      "type": "streamable",
      "url": "https://xxxx/ai/neuron-mcp",
      "headers": {
        "appKey": "<在睿美云后台复制的 APP Key>"
      },
      "description": "睿美云MCP市场"
    }
  }
}
```

> 文档注释原文要点：
> - `url` 是「睿美云的 api 地址，可询问睿美云工作人员你所在机构的地址（域名）」；
> - `appKey` 是「密钥，在睿美云配置里面获取」；
> - **「MCP 是集成了睿美云的账号权限，比如你只有个人权限，则只能查询你自己的数据，和睿美云的权限一致」** —— 权限模型与 TPOS 的机构级账号不同，取不到数据先查账号权限，别急着改代码。

## 3. 两个关键取值方法

### 3.1 appKey 从哪拿
睿美云后台 **HCM → 基础配置 → 左侧「MCP智能体功能权限」**（在「系统配置」分组下，
与治疗通知配置、预设预警配置相邻）→ 右侧页签「MCP智能体功能权限」→ APP Key 列表 →
操作列**复制**图标。列表字段：APP Key / 所属员工 / 手机号 / 描述 / 创建人 / 创建时间 / 操作；
顶部可按「搜索对应员工」筛选。

### 3.2 MCP url 从哪拿（文档给的 4 步）
登录睿美云系统（最好用浏览器登录）：

1. 浏览器按 `F12`
2. 选择「网络」（Network）
3. 在睿美云上随便点一个**查询类**按钮
4. 选下面随便一个接口 → 看「标头」（Headers）→ 找 **Request URL 的域名部分**

文档截图示例：`https://cdyangfu.hospital.realmerit.com.cn/api/v1/tpos/...`，
红字标注「**只需域名部分，后面部分 MCP 地址会帮你拼的**」。

即：`https://<机构域名>/ai/neuron-mcp`（`cdyangfu.hospital.realmerit.com.cn` 是成都武侯漾肤）。

## 4. 地址清单

| 用途 | 地址 |
|---|---|
| 正式环境 MCP（按机构域名拼） | `https://<机构域名>/ai/neuron-mcp` |
| 测试环境 MCP 地址（文档给出） | `https://p7bqujax.xiaomy.net/ai/neuron-mcp` |
| MCP 客户端调用测试地址（文档给出） | `https://demo.hospital.realmerit.com.cn/mcp/` |

## 5. 自省函数：`readQueryMcpDocs`（已实际调用）

文档原文：「MCP 里面有个函数返回了**所有查询类 MCP 函数的文档说明**」。

| 项目 | 实测结果（2026-11-22） |
|---|---|
| 工具名 | `readQueryMcpDocs`（入参为空对象 `{}`） |
| 调用方式 | `POST https://cdyangfu.hospital.realmerit.com.cn/ai/neuron-mcp`，JSON-RPC，返回 `application/json` |
| `tools/list` | **90 个工具** |
| `readQueryMcpDocs` | 返回 **47 组**返回值文档、覆盖 **86 个查询类函数**（66,813 字符） |
| 合并去重 | **92 个函数**（含 3 个写工具、1 个自省工具、2 个文档独有） |
| 协议版本 | `2025-11-25`，服务端 `neuron-mcp-server 0.0.1`，无需 session id |

🔴 返回示例里含**真实客户姓名、订单号、金额、客户 id** —— 固化时只保留**字段名**，
值全部丢弃，原始响应不落盘（见第 8 节）。

## 6. 全量函数清单（已回填）

产物由 `scripts/fetch_official_mcp_docs.py` 生成，可随时重跑刷新：

| 文件 | 用途 |
|---|---|
| `references/official_mcp_functions.md` | 人读：按 15 个业务域的函数速查表（函数名/说明/入参/视角/返回字段/状态）+ REST 对照表 |
| `references/official_mcp_functions.json` | 机读：92 个函数完整契约 + 47 组返回字段清单 |

关键结论：

- **3 个写工具** `markManualOrder`、`restoreWxByVipNums`、`unbindWxByVipNums`
  —— 🔴 绝不自动调用，需睿美云开通权限 + 李刚明确确认。
- `tools/list` 有、但返回值文档未覆盖：`getCustomerIdInfo`、`getSaleItemList`（查询类，可用但无返回结构说明）。
- 文档有、`tools/list` 未暴露：`getStatistics`、`getStatisticsByUserId`（统计类，疑似文档滞后）。
- 新增了一批 `...ByCustomerIdList` **批量版**函数 —— 均未实测，首次使用须用已知有数据的客户验证。
- ⚠️ `SKILL.md` 注意事项 6 仍有效：6 个客户维度函数一律返回「没有查到…」，**客户明细仍走 REST**。

## 7. ✅ 传输方式已验证并修正（2026-11-22）

| 验证项 | 结果 |
|---|---|
| `POST /ai/neuron-mcp` + JSON-RPC `initialize` | **200**，`application/json`，协议 `2025-11-25` |
| `GET /ai/neuron-mcp`（旧 SSE 建连） | **405** —— 服务端已不支持 SSE |
| 结论 | 官方新文档推荐的 streamable 方向正确；**旧 `transport: "sse"` 配置不可用** |

已将 `~/.workbuddy/mcp.json` 的 `rmy` 改为（appKey 为占位符，真值只在本地配置）：

```json
{
  "type": "streamable-http",
  "url": "https://cdyangfu.hospital.realmerit.com.cn/ai/neuron-mcp",
  "headers": { "appKey": "<本地 secret>", "summary": "0" },
  "timeout": 60,
  "disabled": false
}
```

- 改前备份：`~/.workbuddy/mcp.json.bak_20261122_232720`（原 SSE + disabled）。
- `type: "streamable-http"` 是 WorkBuddy 官方 connector 使用的字段名（已核对内置连接器模板）。
- ⚠️ 改配置**不会自动激活当前会话**：仍需在 WorkBuddy「连接器管理 → 自定义连接器」
  对 `rmy` 点「信任」。本次拉取函数清单走的是直连 HTTP，不依赖会话内工具。

## 8. 安全约定

- 分享密码、appKey、账号凭证**一律不写入本文件、不提交 git、不写进日志**；只走环境变量 / 本地 secret。
- 文档里的截图带有水印与真实后台数据，本文件只记录文字结论，不存图。
- 官方 MCP 的权限继承睿美云账号，最小权限原则：给 MCP 用的账号只开查询所需权限。
