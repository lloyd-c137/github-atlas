# Work and delivery

## Begin safely

Confirm repository and task. Inspect current branch, remote state, local changes and ignored/untracked files. Do not stash, reset, clean, overwrite or switch away from user work without understanding its ownership and preserving it. Fetching remote metadata is safe; integrating changes can alter files, so inspect first.

Follow repository instructions for branches and worktrees. Otherwise create or reuse an isolated branch/worktree tied to the task. Avoid working directly on a protected/shared branch. Read the relevant code or documents and acceptance checks before editing. Keep unrelated files out of the task.

## Deliver

When the user asks to deliver:

1. Review the diff and status. Confirm each file belongs to the task; look for accidental generated files, secrets, personal data, unrelated edits and work owned by others. Stop before upload if unsure about sensitive or unrelated content.
2. Run the repository's applicable checks. Report skipped, failing, pending and passing checks separately. Do not claim a test passed unless it ran and passed.
3. Make a concise, accurate save message and save the intended changes locally. Push only the task branch to the matching remote branch; never force-push. If the user directly asked to submit/deliver and permissions allow, proceed to open or update a PR under project conventions.
4. Link the PR to the Issue using repository conventions (for example “Fixes #N” only when merge should close that task). Request the appropriate reviewer when the user or repository rules identify one. Do not select a reviewer by guess.
5. Verify branch head, remote push, PR target/body/Issue link/reviewer request and latest checks from GitHub.
6. State separately what is local, uploaded, under review, and accepted. Leave merge and formal acceptance to the authorized human/project rule.

For a task involving an uploaded document or comment only, verify that exact artifact/link instead of creating a branch or PR.
