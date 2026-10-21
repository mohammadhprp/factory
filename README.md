# Factory

A curated collection of upstream agent skills for a local software factory,
across languages, frameworks, and platforms.

## Local by default

The full flow runs in your project:

`conversation → local spec → local tasks → local implementation → local verification → local review → local handoff`

No Jira, GitHub, GitLab, Notion, hosted tracker, or service account is required.
The files under `.factory/<feature>/` are the execution record. Source URLs
are citations, and local task status never automatically synchronizes outward.

| File or directory | Purpose |
| --- | --- |
| `spec.md` | Agreed behavior and scope |
| `tasks/NN-<slug>.md` | Task state, dependencies, owner, acceptance checks |
| `progress.md` | Current revision, decisions, blockers, next action |
| `evidence/` | Verification results and screenshots |
| `review/`, `walkthrough/` | Local review and explanation artifacts |
| `handoff.md` | Durable continuation context |
| `source.md` | Optional imported requirements with provenance |

Use an established local project convention instead when explicitly supplied.
Setup is optional; create only artifacts the task needs. For a local-only Git
repository, use an existing local base without fetching a remote.

## The external exception: implement

`implement` accepts a local task, conversation request, or an explicitly
supplied Jira, GitHub, GitLab, or Notion task. For an external source it reads
necessary requirements, records them in local `source.md`, and then follows
the same local workflow. It may use connected integrations or authenticated
provider CLIs. Missing external access blocks only an external source that
actually needs it, never local work.

Remote publication is optional and requires an explicit request. `implement`
is the only external workflow entrypoint and uses `gh`, `glab`, `jira-cli`,
and `merge-request` only as adapter references. Reading an external task does
not authorize creating a PR/MR, commenting, changing labels, or closing it.

## Choose the skills

| Work | Skills |
| --- | --- |
| Optional local conventions | `setup-matt-pocock-skills` |
| Understand requirements | `research`, `grilling`, `domain-modeling` |
| Specify and plan | `to-spec`, `to-tickets` |
| Implement locally | `implement-spec`, `implement`, `new-feature`, `tdd` |
| Diagnose failures | `diagnosing-bugs` |
| Architecture | `codebase-design`, `improve-codebase-architecture`, `prototype` |
| Verify | `create-verification-skill`, `maintain-verification-skill`, `verification-before-completion` |
| Review locally | `code-review`, `review`, `merge-risk`, `walkthrough` |
| Security | `differential-review`, `sharp-edges`, `skill-scanner` |
| Local visual evidence | `agent-browser`, `webapp-testing`, `before-and-after`, `show-me` |
| Optional interface design | `frontend-design`, `wcag-audit-patterns` |
| Delivery preparation | `deployment-pipeline-design`, `changelog-automation` |
| Operations methodology | `incident-runbook-templates`, `postmortem-writing`, `triage` |
| Evaluation and improvement | `benchmark-checklist`, `llm-evaluation`, `skill-creator`, `retro` |
| Continuity | `handoff` |

Read [AGENTS.md](AGENTS.md) for the full routing and execution rules, and
[CURATION.md](CURATION.md) for source choices and compatibility limits.
Optional platform-specific examples are not mandatory factory infrastructure.

## Install

Select the required skills with the Skills CLI, or copy their complete folders
into the consuming project's established skill directory:

```sh
npx skills add mohammadhprp/factory --skill to-spec --skill to-tickets --skill implement-spec
```

Include companions: `implement-spec` uses `tdd` and `code-review`; architecture
and TDD use `codebase-design`. Root instructions are not automatically copied
with installed skill directories, so the adapted entrypoints carry their own
local behavior. Use a host supporting the chosen tools and frontmatter.

## Sources and adaptations

The collection contains 52 skills, including 33 imports from established
upstreams. Original source revisions and hashes remain in
[upstream-skills.json](upstream-skills.json). Explicit local adaptations have
separate effective hashes and reasons; unchanged resources retain their
original hashes. [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) preserves
licenses and attribution. `skills-lock.json` is older Skills CLI provenance,
not the effective adaptation manifest.

## Validate

```sh
python -m pip install PyYAML==6.0.3
python scripts/validate_collection.py
python -m unittest discover -s tests -v
```

Validation checks metadata, import/adaptation integrity, licenses, links,
and syntax. Regression checks cover local workflow boundaries and offline
report generation. These checks do not prove model effectiveness or every
project runtime. Local validation runs without a service account. An optional
GitHub Actions job runs the same checks for this collection's review process;
CI and PR publication are not prerequisites for using the factory.
