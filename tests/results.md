# 实际测试报告

执行日期：2026-11-26（Asia/Singapore）

## 环境与证据边界

- Skill：本仓库 `github-collaborator/`。
- 本机：macOS；Git `2.50.1`；GitHub CLI `2.97.0`。
- GitHub CLI 已登录 `lloyd-c137`，`gh auth status` 显示 scopes：`gist`、`read:org`、`repo`、`workflow`。未读取或输出 token。
- Codex GitHub connector：本次会话可发现仓库、Issue、PR、评论、审阅、分支等工具；此文档不假定其他会话也有相同工具。
- 试点 `https://github.com/lloyd-c137/science-copy`：公开仓库，默认分支 `main`，当前账号 `ADMIN`；只读核对。README 和 `docs/team-onboarding.md` 鼓励成员直接用 Codex/WorkBuddy 协作，列出开发、部署、学生/教师反馈角色和审阅/复测交接。`docs/current-application-flow.md` 描述应用数据/审阅责任边界。

## 结果

| 范围 | 结果 | 实际证据 |
| --- | --- | --- |
| 开发前官方调研 | PASS | 核对 Agent Skills 规范、OpenAI Skills 文档、GitHub CLI 认证手册、GitHub 原生协作文档及 GitHub CLI 官方 `gh` Skill。链接见根 README。 |
| 本机 Git/gh 与登录检查 | PASS | `git --version`、`gh --version`、`gh auth status` 成功；不含凭证值。 |
| 试点仓库访问/只读项目检查 | PASS | 仓库可读取；默认分支 `main`，权限 `ADMIN`。根目录含 README、docs、proposal_app、skills。无 `AGENTS.md` 或 `CONTRIBUTING.md`。 |
| 试点 Issues / PRs | PASS | `gh issue list` 与 `gh pr list` 均返回空数组（当前可见范围）。未创建记录。 |
| 试点规则 / 自动检查 | PASS | Rulesets 列表为空；查询 `main` 保护返回 404“Branch not protected”；Actions workflows 列表为空。CODEOWNERS 不存在。 |
| 试点 Projects | BLOCKED | `gh project list --owner lloyd-c137` 拒绝访问：token 缺少 `read:project`。无法据此断定无 Project。未扩大授权。 |
| Skill 结构/元数据/本地引用 | PASS | `python3 scripts/validate_skill.py` 结果记录在本次交付验证中；标准库静态校验通过。 |
| 对 24 个正常/异常目标场景的行为覆盖 | NOT_TESTED | 已写入验收清单，但未在不同 Codex 会话逐条运行；不能把文档覆盖当成行为通过。 |
| GitHub 写入端到端（Issue→分支→PR→Review→Merge） | BLOCKED | 为遵守试点只读边界，未在真实项目写入；没有预设的独立测试仓库/测试账号。没有伪造端到端结果。 |
| UX 场景 U01–U23 | NOT_TESTED / BLOCKED | 完整逐项状态见下方。没有执行真实新手对话/安装流程，不将静态阅读或本轮实现冒充行为验证。 |
| Windows/Linux 安装与 Codex UI 发现 | NOT_TESTED | 按官方 Skill 目录约定提供说明；只在当前 macOS 文件/命令环境检查，没有其他平台实测证据。 |

## 试点观察

- 该项目已有自然语言 onboarding，适合验证非技术成员的测试反馈和教师协作场景。
- README 把开发/部署/测试角色和交接说明清楚。项目专属规则必须以其自身指南和实际设置为准。
- 目前查到仓库没有 Issue/PR 历史、无 branch ruleset/protection、无 Actions workflow、无 CODEOWNERS。GitHub Projects 状态未能读取。**这只是本次时间点和账号可见范围的观测。**
- 本任务不修改试点项目文件、设置或 GitHub 数据。

## 已知限制

- 这是指令型 Skill，行为成功依赖 Codex 能访问当前工作区、可用 GitHub connector 或本机 `gh`/`git`。Skill 本身不会安装程序、登录或授予账号权限。
- 某些连接器不覆盖 Projects、Actions、仓库设置或权限细节；用 `gh` 补充时也受 scopes 和组织策略限制。
- “Agent 能操作”不意味着“用户不用拥有权限”。GitHub 仍会执行真实账号的访问和审阅规则。
- 未进行多轮模型行为评测及写入型 GitHub E2E；请用 `tests/scenarios.md` 在隔离测试仓库和测试账号执行后补齐证据。
- GitHub CLI 安装方法会因操作系统、组织策略变化，安装指南不固定某一种包管理器。

## UX 验收逐项记录

验收表来自远端 `github-collaborator-ux/tests/ux-acceptance.md`。本轮真实执行了远端文件读取、仓库/API状态核验和本地打包/结构检查；并未启动 23 个独立的用户对话。因此对话行为不可标记 PASS。

| ID | 状态 | 证据/阻塞原因 |
| --- | --- | --- |
| U01 | BLOCKED | 当前桌面会话无法重启后验证技能发现；系统级用户目录未被本轮安装。 |
| U02 | PASS | 用户给出完整仓库 URL 后直接按该仓库检查，没有再次询问目标；本轮读取该 URL 的指定远端路径。 |
| U03 | NOT_TESTED | 未在无 GitHub 账号的隔离环境执行真实首次使用对话。 |
| U04 | NOT_TESTED | 当前 CLI 已登录；未登出真实账号，也未运行隔离未登录客户端。 |
| U05 | NOT_TESTED | 未配置第二个账号用于错误身份情境。 |
| U06 | PASS | 真实 Projects 权限错误被报告为无法检查，没有误报为“没有 Project”；未访问的私有仓库场景未测。 |
| U07 | PASS | 试点为公开仓库且实际权限为 ADMIN；报告区分公开可读和可贡献，不声称已做新手对话。 |
| U08 | NOT_TESTED | 未构造带用户修改的本地测试副本并观察真实恢复对话。 |
| U09 | NOT_TESTED | Git/gh 已安装；未在隔离系统中卸载依赖测试。 |
| U10 | NOT_TESTED | 未进行全新 Codex 对话的真实跨会话恢复。 |
| U11 | NOT_TESTED | 未注入网络中断/超时来观察实际对话。 |
| U12 | NOT_TESTED | 中文交互规则已集成，但尚无独立自然语言行为运行记录。 |
| U13 | NOT_TESTED | 英文交互规则已集成，但尚无独立自然语言行为运行记录。 |
| U14 | NOT_TESTED | 未执行术语解释边界对话。 |
| U15 | BLOCKED | 没有隔离 GitHub 测试仓库；试点按要求只读，因此未创建真实任务。 |
| U16 | BLOCKED | 没有隔离仓库验证上传/审阅；试点只读。 |
| U17 | NOT_TESTED | 未构造双人并行编辑测试并运行冲突恢复对话。 |
| U18 | NOT_TESTED | 安全规则静态检查通过；未在隔离环境发起正式采纳操作测试。 |
| U19 | NOT_TESTED | 未运行包含虚构秘密的提交拦截对话。 |
| U20 | NOT_TESTED | 未注入部分成功网络响应并观察用户回执。 |
| U21 | NOT_TESTED | 未执行无关任务负向触发评测。 |
| U22 | PASS | 本轮真实 Projects 调用因缺 `read:project` 失败，报告为 BLOCKED 且没有要求扩权或绕过。 |
| U23 | BLOCKED | 需要独立的新手参与者、隔离账号和测试仓库；当前没有这些测试条件。 |

这些 PASS 仅表示上述单项现场操作行为符合预期，不代表 Skill 已通过完整对话验收。要解除 U01、U03–05、U08–21、U23 的未测状态，需要用独立账号、可销毁的测试仓库及新手测试者执行场景并记录会话证据。
