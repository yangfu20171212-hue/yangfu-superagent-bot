# ruimeiyun-openapi 同步约定

> 🔴 **唯一约定：skill 更新即同步。**
> 本地真源发生任何变更后，必须在同一次工作结束前把变更推送到本目录；
> 不允许出现「本地已更新、GitHub 仍是旧版」的状态。

本文件是**仓库侧文件**，由仓库直接维护，不参与 skill 内容覆盖。

---

## 1. 真源与镜像

| 角色 | 位置 | 说明 |
|---|---|---|
| **唯一真源** | `~/.workbuddy/skills/ruimeiyun-openapi/` | iCloud symlink，真身在 `shared-skills/sources/codex-custom/ruimeiyun-openapi/`，改动自动同步双机 |
| **只读镜像** | 本仓库 `skills/ruimeiyun-openapi/` | 供其他软件 clone / raw 拉取，**禁止直接在此修改 skill 内容** |
| 例外 | 本文件 `SYNC.md`、仓库根 `README.md` | 仓库侧文件，可直接维护 |

**直接改镜像的后果**：下次同步会被全量覆盖，且本地真源不知道这次改动 → 静默丢失。
发现镜像与真源不一致时，一律以真源为准重新覆盖，不要在仓库侧修补。

## 2. 什么算「skill 更新」

| 触发 | 是否需同步 |
|---|---|
| `SKILL.md` 内容变更 | ✅ 必须 |
| `references/` 下新增 / 修改 / 删除文档、客户端 | ✅ 必须 |
| `scripts/` 下新增 / 修改 / 删除脚本 | ✅ 必须 |
| 重跑 `build_capability_map.py` / `fetch_official_mcp_docs.py` 导致产物变化 | ✅ 必须 |
| 重新导出 `ruimeiyun_api_full.md`（官方文档更新后） | ✅ 必须 |
| 仅阅读文件、跑只读查询、临时文件、`__pycache__` | ❌ 不需要 |
| `~/.workbuddy/mcp.json`、`secrets/`、工作区记忆日志 | ❌ 不需要，且**永不入仓** |

删除和重命名同样算更新 —— 同步必须用 `--delete` 模式，不能只 `cp` 新增文件。

## 3. 责任与审批

- 执行者：WorkBuddy 助手；**外部平台写操作需李刚确认后推送**。
- 推送前必须展示 `git diff --cached --stat`，确认变更文件数与预期一致。
- 同步完成后回填下方「同步记录」，并在工作区记忆日志记一条。

## 4. 标准同步流程（可复制执行）

前提：本机 `gh` 已认证到 `yangfu20171212-hue` 且 scopes 含 `repo`。

```bash
SRC="$HOME/.workbuddy/skills/ruimeiyun-openapi"
SYNC=/tmp/rmy_skill_sync
DST="$SYNC/skills/ruimeiyun-openapi"
REPO=yangfu20171212-hue/yangfu-superagent-bot

git clone --depth 1 "https://github.com/$REPO.git" "$SYNC"

# 全量镜像覆盖：--delete 保证删除也能同步；SYNC.md 被排除，不会被覆盖
rsync -a --delete \
  --exclude '__pycache__' --exclude 'SYNC.md' \
  "$SRC/" "$DST/"

git -C "$SYNC" add -A
git -C "$SYNC" diff --cached --stat          # 人工核对
git -C "$SYNC" diff --cached --name-status   # 核对 A / M / D 是否符合预期
git -C "$SYNC" commit -m "chore: sync ruimeiyun-openapi skill (<本次变更摘要>)"
git -C "$SYNC" push origin main

# 推送后校验：远端 tree 的 size + blob sha 与本地逐文件一致
git -C "$SYNC" rev-parse HEAD
git -C "$SYNC" ls-remote origin refs/heads/main
```

> ⚠️ `--delete` 只作用于临时 clone 内的明确目标目录，禁止对个人目录使用。

## 5. 推送前三道门控（缺一不可）

1. **凭证扫描 0 命中**：appKey 真值、飞书分享密码、TPOS RSA 私钥（片段 + 全串）、真实客户姓名 / 订单号 / 长 id / 金额。
   注：`references/auth.md` 的 PEM 样式串是文档示例，不是密钥；精确凭证扫描命中数必须为 0。
2. **逐文件 SHA256 校验**：真源 ↔ 暂存区一致，字节数一致，异常 0。
3. **内容自洽**：`scripts/build_capability_map.py` 幂等可重跑；markdown 表格列数校验 0 异常；`SKILL.md` 的交叉引用文件均存在。

## 6. 红线

- 🔴 skill 目录内**永不写凭证**：appKey、分享密码、RSA 私钥、客户数据、`mcp.json`、`secrets/`。
- 🔴 本仓库为 **public**：完整第三方接口文档、生产域名、账号、生产实测记录均对外可见。新增内容前先判断是否可公开。
- 🔴 写入门控不变：57 个语义写接口零实测；官方 MCP 的 `markManualOrder` / `restoreWxByVipNums` / `unbindWxByVipNums` 绝不自动调用。
- 🔴 不用 GitHub MCP `push_files` 传全量内容（近 1MB 会整包读入上下文），走 git CLI。

## 7. 提交信息规范

```
chore: sync ruimeiyun-openapi skill (<本次变更摘要>)
docs:  update ruimeiyun-openapi sync convention        # 仅改本约定时
```

## 8. 同步记录

| 提交 | 内容 |
|---|---|
| `063f675` | 首次全量同步：14 个文件 / 978,274 字节（178 个 REST 接口能力地图 + 92 个官方 MCP 函数清单 + 生产只读实测报告） |
| 见 git history | 新增本同步约定，仓库根 README 挂入口 |

## 9. 其他软件调用入口

- 目录：`skills/ruimeiyun-openapi/`
- skill 加载入口：`SKILL.md`
- 任务反查接口：`references/api_capability_map.md`
- 机读函数契约：`references/official_mcp_functions.json`
- raw 直取：`https://raw.githubusercontent.com/yangfu20171212-hue/yangfu-superagent-bot/main/skills/ruimeiyun-openapi/SKILL.md`

---

_约定建立：2026-11-23 · 维护者：李刚 / WorkBuddy_
