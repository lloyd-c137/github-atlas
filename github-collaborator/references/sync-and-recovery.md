# Synchronization and recovery

## Sync

Inspect local branch/status, configured remote, ahead/behind relationship and latest remote commits before integration. Protect all local and untracked work. Fast-forward only when safe. If histories diverge, preserve the current state and explain the options in plain language; do not reset or discard local work. Resolve only mechanical conflicts where the intended result is unambiguous. Ask the human when competing edits affect meaning, design, behavior or ownership. Verify final files and branch state.

## Recover across sessions

Do not depend on prior chat memory. Rebuild context from current identity, repo instructions, local changes, branches and remotes, assigned/open Issues, open PRs, commits, review threads and checks. Search before creating anything. Match by task, branch, PR and linked Issue to avoid duplicate work. Confirm the intended task and existing output before continuing. If no copy exists locally or on GitHub, say that the work cannot be recovered; don't invent it.

For a mistaken change, inspect working tree, history and GitHub state first. Prefer a targeted reversible correction. Never rewrite shared history or delete a branch to “undo” work. For failed upload, check whether GitHub actually received the branch/PR before retrying; retry only the incomplete step.
