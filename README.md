# yangfu-superagent-bot

dsh-superagent 的工作仓库（沙箱）。

Agent 在这个仓库里为工单开分支、提 PR、发评论。仓库本身不放业务代码，
它只是 superagent 的作业面。

- 面板: http://127.0.0.1:3082
- 操作者: yangfu20171212-hue

## Skill 同步约定

`skills/ruimeiyun-openapi/` 是本地 WorkBuddy skill 的**只读镜像**，遵循「**skill 更新即同步**」：
本地真源任何变更（含新增、修改、删除、生成脚本重跑）都必须在同一次工作结束前推送到本目录，
不允许出现「本地已更新、GitHub 仍是旧版」；禁止直接在镜像里修改 skill 内容。

真源位置、触发判定、同步命令、推送前三道门控与红线见
[skills/ruimeiyun-openapi/SYNC.md](skills/ruimeiyun-openapi/SYNC.md)。
