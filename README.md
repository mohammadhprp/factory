# Factory

A curated collection of upstream agent skills for software delivery across languages, frameworks, and platforms. This repository distributes instructions and supporting tools; it is not an autonomous execution service.

## Start here

Install only the skills needed for a project. The collection includes optional web, GitHub, GitLab, Docker, and agent-host integrations; none is a requirement for every project.

With the Skills CLI, select skills from this repository:

```sh
npx skills add mohammadhprp/factory --skill to-spec --skill to-tickets --skill implement-spec
```

Alternatively, copy the chosen skill directories into the consuming project's established skill directory, such as `.agents/skills/`. Copy each entire directory, including references, scripts, assets, and license. Keep companion skill names unchanged. Check the chosen host's support for frontmatter extensions and tool names before installation.

Read [CURATION.md](CURATION.md) for selection decisions, dependencies, compatibility limits, and the remaining infrastructure gaps. Exact imported revisions and file checksums live in [upstream-skills.json](upstream-skills.json). Licenses and attribution are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Suggested workflow

1. Configure the consuming project with `setup-matt-pocock-skills`. It supports GitHub, GitLab, local Markdown, and documenting another tracker. Do not run it merely to install this collection.
2. Explore relevant code and clarify decisions using `improve-codebase-architecture`, `codebase-design`, `domain-modeling`, and the existing `research` and `grilling` skills as appropriate. Small changes do not need every stage.
3. Use `to-spec` to capture agreed behavior, then `to-tickets` to produce verifiable slices with explicit dependencies.
4. Use `new-feature` for isolated editing tasks. For a connected task graph, `implement-spec` manages its own integration branch and task worktrees; do not independently apply competing branch rules.
5. Use `tdd` for behavior-focused implementation and `diagnosing-bugs` for reproducible failures.
6. Use `create-verification-skill` to establish a project-specific launch, drive, evidence, and cleanup workflow. Use `maintain-verification-skill` to keep it accurate. Use `verification-before-completion` before claiming success.
7. Use `code-review` for specification and standards alignment; the existing `review` skill produces structured review artifacts. Add `differential-review` or `sharp-edges` when security scope warrants them.
8. Prepare delivery with `deployment-pipeline-design` and `changelog-automation`. Use `incident-runbook-templates`, `postmortem-writing`, and `triage` to feed operational findings back into development.
9. Use `handoff` for session continuity and `retro` for improvements to the engineering environment. Use `skill-creator` for controlled skill evaluations and `benchmark-checklist` for credible performance measurements.

These are selectable workflows, not a rule to load every skill into every task. Follow the consuming project's instructions and the user's actual authorization.

## Added capabilities

| Area | Skills | Upstream |
| --- | --- | --- |
| Project configuration and intake | `setup-matt-pocock-skills`, `triage` | Matt Pocock |
| Specifications and task graphs | `to-spec`, `to-tickets`, `implement-spec` | Matt Pocock |
| Architecture and domain understanding | `codebase-design`, `domain-modeling`, `improve-codebase-architecture`, `prototype` | Matt Pocock |
| Behavior tests and debugging | `tdd`, `diagnosing-bugs`, `code-review` | Matt Pocock |
| Continuity and learning | `handoff`, `retro`, `writing-for-agents` | Matt Pocock |
| Project verification | `create-verification-skill`, `maintain-verification-skill` | pstack |
| Performance evidence | `benchmark-checklist` | pstack |
| Completion evidence | `verification-before-completion` | Superpowers |
| Security | `differential-review`, `sharp-edges` | Trail of Bits |
| Delivery and release preparation | `deployment-pipeline-design`, `changelog-automation` | wshobson/agents |
| Operations | `incident-runbook-templates`, `postmortem-writing` | wshobson/agents |
| Evaluation of LLM components | `llm-evaluation` | wshobson/agents |
| Optional interface quality | `wcag-audit-patterns` | wshobson/agents |
| Optional web design and testing | `frontend-design`, `webapp-testing` | Anthropic |
| Skill evaluation and maintenance | `skill-creator` | Anthropic |
| Skill supply-chain inspection | `skill-scanner` | Sentry |
| Optional checked-in product and technical specs | `write-product-spec`, `write-tech-spec` | Warp |

The existing 19 skills remain available. The Notion-specific `implement` workflow is an alternative for explicitly linked Notion tasks, rather than the general implementation entry point.

## Validate this collection

Python 3.12 and PyYAML are sufficient for the collection checks:

```sh
python -m pip install PyYAML==6.0.3
python scripts/validate_collection.py
```

Validation checks metadata, imported file integrity, licenses, local links in imported skill entry points, Python syntax, and the existing skill lock's referenced directories. It does not run project workloads, contact production services, or establish that a skill succeeds on every agent host.

To inspect one skill with the vendored scanner:

```sh
python skill-scanner/scripts/scan_skill.py ./to-spec
```

Scanner matches require review: security documentation intentionally contains attack examples. Do not equate a pattern match with a malicious skill or a clean scan with a security guarantee.

## Updating upstream imports

Select a new upstream commit, review the changed skill and its dependencies, and copy the complete selected directory. Retain its license. Update the matching entry and SHA-256 values in `upstream-skills.json`, then validate and open a PR. Do not silently modify imported skill bodies: make a deliberate fork with documented changes if adaptation becomes necessary.

The older `skills-lock.json` is retained for its existing Skills CLI provenance; `upstream-skills.json` tracks this curated import batch. These are distinct formats and are not interchangeable.
