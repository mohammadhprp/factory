# Agent workflow

Use this collection to deliver verified software changes across languages,
frameworks, and platforms. Select the workflow that fits the task, read its
skills, and carry the work through the requested outcome.

This file governs work in the factory repository. When applying these skills
to another project, read that project's instructions, architecture, and checks
first. Installing a skill directory does not install this root instruction
file or replace the consuming project's policies.

## Choose the scope

- For a review, explanation, research task, or plan, inspect and report. Create
  a branch only if the request leads to repository edits.
- For a small documentation change, use the assigned task branch and check
  the content, references, and examples. Runtime tests are unnecessary unless
  the change affects executable behavior.
- For a bug, reproduce the failure, trace its cause, implement the fix, and
  verify the affected behavior and relevant neighboring paths.
- For a feature, establish acceptance criteria and implementation boundaries.
  Use a written specification and task graph when the scope warrants them.
- For delivery, publish the requested PR/MR or release only within the user's
  authorization. A review or planning request does not imply publication.

## Workflow

1. **Understand.** Read applicable repository instructions, the task, relevant
   source, and existing tests. Identify the consumer-visible outcome,
   constraints, and verification commands. Discover the actual toolchain;
   never assume Node, Docker, a web UI, or a particular issue tracker.
2. **Scope.** State the intended change and material assumptions. Resolve
   decisions that block correct implementation; investigate facts yourself.
   Use `grilling` for decisions that need the user's judgment. Use `to-spec`
   and `to-tickets` for substantial work, rather than requiring them for every
   edit. Record genuine dependencies and work the unblocked tasks.
3. **Isolate.** Use `new-feature` before edits, preserving a checkout already
   assigned to this task. Check the branch, worktree, uncommitted changes, and
   overlapping open PRs/MRs. Keep each independent task off the default branch
   and out of another task's checkout.
4. **Build.** Follow the project's architecture and conventions. Use
   `codebase-design` and `domain-modeling` when interfaces or domain terms need
   work. Use `tdd` for behavior that benefits from regression coverage and
   `diagnosing-bugs` for failures. Make the smallest complete change that
   satisfies the task; avoid unrelated cleanup and speculative abstractions.
5. **Prove.** Run the relevant checks and inspect their results. Verify the
   requested behavior through its real interface where practical. Apply
   `verification-before-completion` before claiming success. A plausible
   implementation or an agent's review is not execution evidence.
6. **Review.** Inspect the final diff for correctness, scope, compatibility,
   security, and accidental data disclosure. Use `code-review` for standards
   and specification alignment, or `review` for a structured review artifact.
   Add a security pass when the changed surface warrants it. Fix actionable
   findings within scope and verify the resulting revision.
7. **Deliver.** When requested, commit the intended files and open or update
   the task's PR/MR against the verified target branch. Include the outcome,
   validation results, and remaining limitations. Inspect CI and investigate
   failures caused by the change. Report unrelated or unavailable checks
   accurately. End with the PR/MR URL and status.
8. **Hand off.** For unfinished or long-running work, record what is done,
   what is blocked, the current revision, evidence locations, and the next
   action. Use `handoff`; use `retro` when session evidence reveals a durable
   improvement to the environment or workflow.

## Skill routing

Read the selected skill's `SKILL.md` before applying it. Load supporting files
when that skill calls for them. Keep companion skills available, but do not
load the whole catalog for every task. Names below refer to sibling skill
directories; use the host's skill tool or read those files directly.

| Task | Use |
| --- | --- |
| Configure a project's tracker and domain docs | `setup-matt-pocock-skills` |
| Research external facts or challenge an unsettled decision | `research`, `grilling` |
| Capture agreed behavior and split substantial work | `to-spec`, then `to-tickets` |
| Implement a specification's task graph | `implement-spec`, with `tdd` and `code-review` |
| Implement an explicitly linked Notion task | `implement`; requires its documented Notion CLI access |
| Write checked-in product and technical specs | `write-product-spec`, `write-tech-spec` |
| Design interfaces, domain terms, or architectural changes | `codebase-design`, `domain-modeling`, `improve-codebase-architecture` |
| Make a concrete design experiment | `prototype` |
| Isolate edits and prepare Git commits | `new-feature`, `commit` |
| Reproduce and fix a bug | `diagnosing-bugs`, `tdd` |
| Establish or maintain real application verification | `create-verification-skill`, `maintain-verification-skill` |
| Check completion claims or performance measurements | `verification-before-completion`, `benchmark-checklist` |
| Review a change or assess merge risk | `code-review`, `review`, `merge-risk` |
| Inspect security-sensitive changes or dangerous defaults | `differential-review`, `sharp-edges` |
| Inspect a candidate skill before adoption | `skill-scanner` |
| Work with a repository or tracker | `gh`, `glab`, `jira-cli`, `triage` |
| Prepare a GitLab MR | `merge-request`, after resolving its branch and assignee defaults |
| Work with containers or Docker sandboxes | `docker` |
| Work on web interfaces or accessibility | `frontend-design`, `wcag-audit-patterns`, `agent-browser`, `webapp-testing` |
| Explain or demonstrate a change | `walkthrough`, `show-me`, `before-and-after` |
| Write project documentation | `docs-writer` |
| Review implementation complexity | `ponytail`, when selected for the task |
| Prepare delivery pipelines and release notes | `deployment-pipeline-design`, `changelog-automation` |
| Prepare incident response and follow-up | `incident-runbook-templates`, `postmortem-writing` |
| Evaluate LLM behavior or a skill's effectiveness | `llm-evaluation`, `skill-creator` |
| Discover an upstream capability | `find-skills` |
| Preserve session context or improve the environment | `handoff`, `retro`, `writing-for-agents` |

### Resolve workflow conflicts before execution

- Choose one implementation entry point. The general path is `to-spec` →
  `to-tickets` → `implement-spec`. The existing `implement` is Notion-specific;
  its reference to `spec` is not an alias for `to-spec`.
- Use the task's explicit base and the consuming project's branch policy.
  Otherwise, use the remote's verified default branch. This factory's target
  is `main`. Do not inherit `develop` or an assignee from a generic example.
- `implement-spec` owns its integration branch and task worktrees. Do not
  apply a second branch-creation workflow to the same implementation.
- Resolve required setup and tool availability before starting the selected
  workflow. State a real blocker rather than inventing access or silently
  replacing a required integration.
- Native plugin agents, host-specific tool names, and optional external
  commands are not installed by copying skill files. See
  [CURATION.md](CURATION.md) for supported fallbacks and prerequisites.

## Verification and evidence

- For a bug, capture a failing check or reproducible observation before the
  fix, then repeat it afterward. If reproduction is blocked, state the limit.
- Check the actual interface: a CLI's output and exit status, an API's response
  and side effects, a library's public behavior, or the user's UI journey.
  Use the project's native tooling for mobile, desktop, or embedded work.
- Keep evidence tied to the tested revision and environment. Separate checks
  that passed, failed, were not run, or could not run.
- Do not weaken acceptance criteria, remove failing assertions, or mark an
  unreachable feature as verified to obtain a passing result. Change intended
  behavior only when the task establishes that change.
- Reuse screenshots, logs, and results when they still match the revision and
  conditions being reported. Recheck after changes that invalidate them.
- Keep tokens, personal data, and credentials out of logs and artifacts.
  Screenshot uploads can use public hosting; choose a suitable destination
  before uploading sensitive material.
- Run project verification generators against a real consuming application.
  Do not fabricate an application harness while maintaining this collection.

## Worktrees and collaboration

- Use one task branch and isolated checkout per independent editing task.
  Preserve an existing assignment when continuing the same task.
- Before editing shared files, inspect overlapping work. Coordinate when
  changes conflict in behavior or depend on unfinished work; independent
  changes can proceed in their own checkouts.
- Preserve user changes. Never reset, stash, discard, or commit another task's
  work to make your checkout convenient.
- Delegate only when the host supports it and the task benefits from separate
  ownership. Give each editor a clear scope and checkout. Keep dependencies
  and integration sequential where required; verify the combined result.
- Worktrees do not isolate ports, databases, credentials, or external services.
  Confirm that a running process and its data belong to this task. Stop only
  processes you started and preserve verification evidence during cleanup.
- Regenerate conflicting dependency lockfiles with the relevant package
  manager. Do not hand-merge them or change unrelated dependency versions.
- Keep the task checkout while its PR/MR is open. Never force-push the default
  branch; use a lease for an authorized history rewrite on your own branch.

## Maintaining this collection

Prefer established upstream skills over new local implementations. Review
the actual instructions, supporting tools, dependencies, licenses, and host
requirements before importing. Popularity alone is not a quality check.

Preserve imported skill bodies and bundled resources as exact upstream
copies. Keep complete directories and licenses. Record the source commit,
file checksums, and license in [upstream-skills.json](upstream-skills.json),
with attribution in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Make a
local adaptation only when explicitly required, and document it as a fork
rather than disguising it as an unchanged upstream copy.

For additions or deliberate upstream updates, review companion requirements
and overlapping entry points. Update [README.md](README.md) and
[CURATION.md](CURATION.md) when installation, routing, or compatibility changes.
Do not activate tracker setup, deployment, release publication, or global
agent configuration merely to validate an import.

## Checks in this repository

Run from the repository root with Python 3.12 and PyYAML available:

```sh
python scripts/validate_collection.py
```

The validator checks skill metadata, pinned imports, file and license
checksums, imported entry-point local links, Python syntax, shell syntax,
and the existing lock's referenced skill directories.

Also inspect the diff and check whitespace in the files you authored:

```sh
git diff --check
git diff --cached --check
```

Upstream copies can contain existing whitespace warnings. Preserve those
bytes and distinguish them from errors introduced in local integration files.
For documentation edits, check named skills and local links against the tree.
For executable helper changes, run an appropriate isolated smoke check after
reading the helper. A source checksum or syntax check does not prove runtime
behavior, model effectiveness, every platform, or a live external integration.

CI runs the collection validator through
[validate-skills.yml](.github/workflows/validate-skills.yml). Report its actual
status; do not describe a queued or unavailable run as passed.

## Writing and finishing

Write for the person reviewing the result. Use plain language, concrete
outcomes, and short explanations. Keep documentation, commit messages, and PR
descriptions consistent with the change. Avoid filler, invented measurements,
and implementation details that do not help the reader assess the result.

Before finishing a task that ships:

1. Confirm the diff contains only the requested change and necessary support.
2. Complete relevant verification and review the final revision.
3. Commit and publish to the verified task branch within the user's request.
4. Open or update the PR/MR with what changed, why, validation, and limitations.
5. Inspect available checks, address failures caused by the change, and report
   the result with the PR/MR URL. Leave merging to an explicit instruction.

If the work is blocked or partial, name what remains and what unblocks it.
Do not claim that skill coverage alone supplies durable orchestration,
protected acceptance checks, or enforced runtime permissions.
