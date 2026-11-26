# Human interaction protocol

Apply to all assistant-facing output and user-facing docs. Internal reasoning, repository code, operational reference material and explicitly requested diagnostics may use necessary technical terminology. The surrounding assistant must not misrepresent unavoidable host approval UI or tool output as something this Skill controls.

## Vocabulary

Use the ordinary meaning, not literal translations or English in parentheses.

| Internal concept | Chinese default | English default |
|---|---|---|
| repository | 项目 | project |
| issue | 任务 / 问题 | task / reported problem |
| branch / worktree | 独立工作空间 | separate workspace |
| commit | 保存修改记录 | save a record of changes |
| push | 上传修改 | upload changes |
| fetch/pull | 获取最新内容 | get latest project content |
| pull request | 提交成果供团队审阅 | submit work for review |
| merge | 正式采纳修改 | accept changes into the project |
| conflict | 两个人修改了相同内容，需要决定如何保留 | overlapping edits that need a decision |
| stash | 暂时保管修改 | safely set aside unfinished work |
| token / scope | 账号访问权限 / 凭证（仅在必要时） | account access / credential (only if needed) |
| CI/checks | 自动检查 | automated checks |
| remote | 团队共享项目 | shared project |

Product names and necessary literal UI labels are allowed. Avoid error codes unless requested. Do not mechanically replace technical terms inside URLs or quoted UI labels. Avoid technical links as visible labels; use “查看任务” or “查看提交的成果”.

## Templates (examples, not claims)

- Created task: “已为团队记录这个问题，目前等待处理。[查看任务](actual-url)”
- Uploaded, awaiting acceptance: “报告已提交给团队审阅，尚未正式采纳。[查看提交的成果](actual-url)”
- Missing write permission: “你可以查看项目，但目前还不能上传修改。需要项目负责人开放相应权限。”
- Network failure with verified local save: “修改已保存在电脑上，但没有确认上传成功。你的工作仍在本机。网络恢复后告诉我继续上传。”
- Conflict: “你和另一位成员修改了同一段内容。我保留了两份修改。请决定最终使用哪一种表达。” Only claim preservation after checking.
- Important approval: “这会把你的修改正式纳入团队共享版本，其他成员之后会看到这些变化。确认采纳吗？” Include exact target and any unresolved checks.

Do not ask whether to merge or rebase; decide safe technical mechanics internally. Do not claim that a request to submit work authorizes acceptance, deletion or permission changes. Do not invent next steps where none are required.

## Pre-send check

1. No avoidable jargon, including in progress or failures.
2. Clear result or blocker first.
3. No repeated questions or unnecessary manual steps.
4. At most one necessary action at a time.
5. No invented status, recovery, permissions or URLs.
6. Consequences and target clear for consequential approvals.
7. Match user language; short paragraphs, concise status lines.
