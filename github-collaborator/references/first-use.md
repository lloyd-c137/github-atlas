# First use: state-based onboarding

Goal: enable a novice to contribute using conversation alone, with only unavoidable identity, permission, system approval and human decisions left to them. Do not assume this skill can install itself or that every Codex environment can access a shell, browser or local filesystem.

## Entry

If a target is already known, do not ask again. Otherwise ask for the project link (one question). Brief welcome: “我会帮你准备好工作环境。除了需要你本人完成的登录和授权，其他能处理的操作都由我完成。” Do not promise capabilities before inspecting them.

## Internal checks (not a user-facing technical checklist)

Inspect supported tools and permissions; installed dependencies and actual Skill availability where observable; authenticated GitHub identity and applicable credential path; target project and access; whether write access or a fork-based contribution path is available; existing local copy, remote identity, dirty/unpushed work, existing task workspaces; applicable team instructions and actual current tasks. Avoid reading unrelated files or exposing secrets. If environment cannot access local files, offer the supported collaboration path and distinguish it from local setup.

Re-evaluate each state after user action or a new conversation. Store no credentials. Use real account and project state as evidence. No persistent local metadata unless needed; never claim cross-device recovery of unuploaded work.

| Internal state | Behavior | User-visible result |
|---|---|---|
| Target ambiguous | Ask for one project link or choice among known candidates | “请把团队项目的链接发给我。” |
| Missing supported tools | Attempt approved installation only where supported; never use untrusted installers | One clear approval or shortest supported next action |
| No account | Provide verified official signup destination | Explain that the account identifies the member; ask them to register |
| Not authenticated | Start supported authentication flow; if browser is not opened, don't say it is | “请在打开的 GitHub 页面登录自己的账号。” |
| Wrong identity | Protect local work; explain identity mismatch; request account switch before writing | State the verified account and ask for correct account |
| Invite/access pending | Distinguish access, existence, invitation, and permissions when evidence allows | Explain what can be done now and what needs the owner; never assert 404 means no permission |
| Public read only | Verify whether contribution is possible without assuming membership | “可以查看项目，但还没有确认你能提交成果。” |
| Existing work | Inspect and preserve it; don't replace or silently switch project | State existing work is preserved only after verification |
| Ready for contribution | Verify actual usable path and applicable policy | Report account, project, readiness, real task or absence of tasks |
| Interrupted or offline | Record known result; re-check on resume; do not retry uncertain writes blindly | One concrete next action; no false success |

## Progress

Show only useful, verified states, e.g.:
- ✓ 已找到团队项目
- ✓ 工作环境已准备好
- → 需要你登录 GitHub

Do not present hypothetical success as fact. Do not show five pending technical steps if only one user action is needed. Recheck actual authentication after the user says they have logged in. Never request credentials or verification codes.

## Completion

A full local collaboration path requires verified identity, correct target, appropriate contribution access, usable local workspace, and relevant team rules checked. A read-only path must be labeled read-only. If rules cannot be read or permissions cannot be verified, say what remains unknown. Do not create a test issue, branch or PR merely to prove onboarding without authorization. Report current assigned work if available; otherwise say no assigned task was found or access is insufficient to check.

Example (only when verified):

“你已经可以参与开题手记项目的协作了。

目前没有分配给你的任务。你可以直接告诉我：
- 帮我看看团队最近做了什么。
- 帮我记录一个问题。
- 帮我提交这份报告。”

On resume, ask for the project link only if it cannot be determined from current context. Reuse safe existing setup. If multiple projects exist, don't silently choose. When switching accounts, verify the new actor and never reuse another actor's pending changes without authorization.
