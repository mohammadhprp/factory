# Local task storage

Use `.factory/<feature>/` in the project, or an explicitly established local equivalent.

- `spec.md`: agreed behavior and scope.
- `tasks/NN-<slug>.md`: one task per independently verifiable slice.
- `progress.md`: current branch, base, decisions, blockers, and next action.
- `evidence/`: test output, screenshots, and other evidence.
- `review/`: local review inputs and reports.
- `walkthrough/`: optional change explanation.
- `handoff.md`: durable continuation notes.

Task fields: `Spec`, `Status`, `Owner`, `Blocked by`, acceptance criteria, and verification evidence. Use stable local IDs and relative paths. Add decisions under `## Notes`; do not post comments to a service.

Statuses: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `in-progress`, `blocked`, `done`, `wontfix`. A frontier task is ready-for-agent, unclaimed, and has only done blockers. Record a claim before work; a coordinator owns shared state updates. Missing dependencies and cycles block execution.

Files are the source of truth. Source URLs are citations only. External requirements must be imported by `implement`; no automatic two-way sync or remote status change follows a local edit.
