---
name: handoff
description: Save durable continuation notes in the local task directory so another
  session can resume without a hosted tracker or temporary-directory dependency.
argument-hint: What will the next session be used for?
disable-model-invocation: true
---

# Local handoff

Write `.factory/<feature>/handoff.md`, or the explicitly supplied persistent local path. Reuse the active feature directory and preserve earlier handoffs when they still contain relevant decisions. Do not default to an OS temporary directory or create a remote page.

Record the user's goal, local spec/task paths, repository and branch, base and current revision, uncommitted changes, completed acceptance checks and evidence, blockers, ownership, and the next concrete action. Include suggested skills for the next session. Reference existing local artifacts instead of duplicating them. Redact credentials and personal data.

Check that the referenced files exist and remain available after cleanup. Report the absolute handoff path. A handoff is context, not permission to discard changes, take over another task, publish work, or close an external issue.
