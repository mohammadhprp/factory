---
name: implement-spec
description: Implement a local specification and its local task graph on an isolated
  integration branch. Track progress, verification, and completion in local files;
  no hosted tracker or remote publication.
disable-model-invocation: true
---

# Implement a local specification

Read `.factory/<feature>/spec.md` and `.factory/<feature>/tasks/*.md`, or the equivalent directory explicitly supplied by the user. Missing setup is not a blocker. If a specification or task graph is unnecessary for a small request, implement the requested change directly and record relevant evidence locally.

External task URLs and remote delivery belong to `implement`. This workflow consumes local requirements and finishes locally. Never fetch or mutate a hosted task, open a PR/MR, push, or mark a remote record complete.

## Process

1. Read the complete specification, acceptance criteria, dependencies, and existing progress. Validate that every dependency exists and the graph has no cycles. A task is eligible only when its status is `ready-for-agent`, its owner is `unclaimed`, and all blockers are `done`. Never reclaim done, wontfix, needs-info, or ready-for-human tasks. Resume an in-progress task only when its owner matches the verified current session assignment; do not steal stale-looking work. Move a blocked task back to ready-for-agent only after verifying its recorded release condition. Do not satisfy dependencies by silently changing their meaning.
2. Use the current verified task checkout or `new-feature` to create an integration branch from the explicit or locally discovered base. Record the base revision in `.factory/<feature>/progress.md`. No remote is required.
3. Claim an eligible task by writing `Owner: <session-or-agent>` and `Status: in-progress` before edits. A coordinator is the single writer for shared task state; subagents return results to it. For independent sessions, use an agreed exclusive local claim before proceeding. Never race two writers over the same task file.
4. Implement a verifiable slice using `tdd` where appropriate. When the host supports useful delegation, give each editor a separate worktree based on the integration revision and disjoint scope. Otherwise execute the same frontier sequentially. Never reset an occupied worktree or erase user work to change its base.
5. Verify the slice, integrate approved task commits locally when commits are authorized, and verify the combined result. Without commit authorization, work sequentially in the assigned checkout and leave changes uncommitted. Preserve evidence under `.factory/<feature>/evidence/` with the tested revision or working-tree state.
6. Record acceptance results and evidence paths in the task. Set `Status: done` only when its acceptance criteria pass. Set `blocked` with a precise release condition when work cannot continue. Release ownership after recording the result. Continue through the unblocked frontier.
7. Use `code-review` against the local base and specification, or `review` for a structured artifact. Resolve actionable findings and rerun affected checks. Update local task state only from verified results.
8. Write a concise outcome and remaining work to `progress.md`. Report the local branch, changed files, evidence, and incomplete tasks. Leave the result local. Keep worktrees containing uncommitted work or evidence; clean only task-owned disposable worktrees after their work is safely retained.
