---
name: triage
description: Evaluate local task files, reproduce reported behavior, and record category,
  status, brief, and blockers locally without using a hosted tracker.
disable-model-invocation: true
---

# Triage local tasks

Read `.factory/<feature>/tasks/*.md` or the local task path supplied by the user. No service configuration is needed. For an externally hosted report, `implement` first imports it as a local task. Triage never fetches, comments on, labels, or closes a remote record.

1. Read the task, prior notes, local specification, and relevant source. Search for an existing implementation and related local decisions before proposing duplicate work.
2. For a bug, reproduce the report through a real interface when practical. Record confirmed behavior, evidence, or the exact missing precondition. Do not confuse an inaccessible test environment with a verified result.
3. Recommend `Category: bug` or `Category: enhancement` and an appropriate local status. Ask for missing product decisions only when they block a reliable brief; use `grilling` and `domain-modeling` when needed.
4. Update the local file with the agreed outcome. Use `needs-info` for missing information, `ready-for-agent` for actionable work, `ready-for-human` for required judgment, or `wontfix` for an explicit rejection. Preserve the reasoning and acceptance criteria under `## Agent brief` and `## Notes`. Never mark work `done` merely because it has been triaged.
5. For a queue view, group local files by status, oldest first using recorded dates or filesystem timestamps. Show paths and blocking conditions. Do not query an external queue or notify a reporter.

Use [AGENT-BRIEF.md](AGENT-BRIEF.md) for brief quality and [OUT-OF-SCOPE.md](OUT-OF-SCOPE.md) for durable rejection notes, interpreted as local files. A local task is the authoritative record. Keep owner and dependency fields consistent with the local workflow.
