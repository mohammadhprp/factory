# Local task states

Store `Status:` in each task file. These values are local states, not hosted labels:

| Status | Meaning |
| --- | --- |
| needs-triage | Not yet evaluated |
| needs-info | Required information is missing |
| ready-for-agent | Actionable and eligible once blockers are done |
| ready-for-human | Requires human judgment or unavailable capability |
| in-progress | Claimed and being implemented |
| blocked | Cannot proceed; record the release condition |
| done | Acceptance criteria verified with evidence |
| wontfix | Deliberately declined with a recorded reason |

Store `Category: bug` or `Category: enhancement` separately. Store `Owner: unclaimed` until a session claims the task. Never map these values to remote labels automatically.
