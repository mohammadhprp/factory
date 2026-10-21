---
name: new-feature
description: Isolate edits in a local Git worktree and task branch, preserving an
  existing task assignment. Requires no remote, fetch, hosted PR scope check, or service
  account.
---

# Isolate a local task

Read-only investigations need no worktree. Before edits, inspect `git worktree list`, `git status --short`, the current branch, and task assignment. Keep a verified checkout already assigned to this task. Preserve unrelated work.

1. Inspect local branches, worktrees, task notes, and uncommitted changes for overlapping work. Do not query hosted PRs/MRs or fetch a remote.
2. Honor an explicit base. Otherwise use the project's documented locally available base branch; when absent, use the current clean HEAD and state that choice. Never assume `origin/main` exists. Do not switch a dirty checkout or incorporate unrelated edits.
3. Choose a unique task branch and a worktree directory outside the checkout or in an established ignored worktree directory. Validate the branch name with `git check-ref-format --branch`. Never force an occupied path or branch.
4. Create the worktree with `git worktree add <path> -b <branch> <local-base>`. Verify its branch and base before editing. For a repository without a commit, use a dedicated local task branch in the existing checkout; explain that worktrees require a base commit. For a non-Git project, preserve its existing files and report that Git isolation is unavailable rather than initializing a repository without authorization.
5. Use the task's local state directory. Confirm required runtime versions and run only relevant setup. Documentation edits do not require an application toolchain.

Worktrees do not isolate ports or databases. Verify that processes and data belong to this task. Preserve worktrees with uncommitted work or evidence until the result is safely retained. Do not push, publish, merge into the default branch, or delete another task's branch. External source/delivery operations belong to `implement` only when requested.
