# Local agent briefs

Write the brief under `## Agent brief` in the local task file. Describe the current and desired behavior, domain interfaces, independently testable acceptance criteria, scope boundaries, and relevant local evidence. Keep statements durable across implementation changes. Do not post comments or create records on a service.

```markdown
## Agent brief
Category: bug
Summary: Repeated retries must not create duplicate work.

### Current behavior
Describe a reproduced failure and reference its local evidence.

### Desired behavior
State observable outcomes and error cases.

### Acceptance criteria
- [ ] Repeating the operation preserves one durable result.
- [ ] The regression check reproduces before the fix and passes afterward.

### Out of scope
List excluded behavior.
```

The task's Status, Owner, Blocked by, and Spec fields remain the source of execution state. Do not mark a brief complete until implementation has verified its acceptance criteria.
