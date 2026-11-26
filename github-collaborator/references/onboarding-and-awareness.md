# Onboarding and project awareness

## First visit

1. Identify the exact repository and host. Inspect `git --version` and, if using GitHub CLI, `gh --version` and `gh auth status`. For connector use, retrieve the authenticated profile and repository metadata. Report the account name, never the token.
2. Verify repository access with a read request. Do not interpret an inaccessible private repo as nonexistent. If access is missing, give the user the repository's normal invite/access request link and let an owner grant it. Never seek credentials.
3. Reuse a local checkout if it belongs to that remote. Before changing it, inspect status, branch, remotes, and untracked files. If absent, clone into a safe, clearly named location; if the intended path is occupied, do not overwrite it.
4. Read root instructions and only applicable nested instructions, README, contribution guide, templates and task-specific docs. Respect actual project workflow over generic defaults.
5. Inspect current GitHub state relevant to the person's role: open/assigned Issues, active PRs and review requests, unresolved review comments, recent material changes and checks. Query Projects only if relevant and permitted; a missing scope is not evidence that there is no board.
6. Summarize: access/setup complete; role/work found; latest verifiable state; blockers; and one natural next action.

If Git or `gh` is missing, check the operating system and available installer/package manager. Do not install software without authorization when it changes the user's machine. Prefer Codex's connected GitHub tools if they suffice. Ask only for the human-only step (login, invite acceptance, organization SSO/approval) and do useful work that does not depend on it.

## Progress brief

Use direct evidence: Issue and PR state, timestamps, authors/assignees, review threads, check conclusions, commit summaries and project status. For “yesterday”, use the user's local date and repository timestamps; state the time window. Separate facts from inference. Say “I could not check” when a permission or tool blocked inspection. Show a short list of relevant links rather than raw logs.
