# Curation and integration notes

Reviewed on 2026-10-21. Imports are pinned to the exact commits in `upstream-skills.json`; original source hashes are retained. The local workflow adaptations listed in the manifest override upstream defaults; unchanged resources remain exact copies.

## Selection method

Read candidate instructions and their bundled dependencies. Prefer concrete workflows, observable outputs, project discovery, established maintainers, compatible licenses, and limited overlap. Repository popularity was a supporting signal, not a substitute for content review. These are selected fits for this collection, not a universal benchmark ranking.

| Source reviewed | Selection and rationale |
| --- | --- |
| `mattpocock/skills` | Selected its connected engineering workflow, configuration templates, architecture vocabulary, debugging loop, and session handoff. Companion skills are included together. |
| `backnotprop/pstack` | Selected project verification generation and maintenance plus measurement discipline. These complement the current collection without importing pstack's whole operating mode. |
| `obra/superpowers` | Selected the focused completion-evidence skill. Its larger planning, debugging, worktree, and TDD suites overlap with the selected Matt workflow and existing skills. |
| `trailofbits/skills` | Selected evidence-based differential security review and dangerous-interface/default analysis. Kept all bundled reference material and CC BY-SA attribution. |
| `wshobson/agents` | Selected deployment, release-note, incident, accessibility, and LLM-evaluation guidance. These fill lifecycle areas absent from the two requested collections. Examples are conditional, not a mandatory production stack. |
| `anthropics/skills` | Selected skill evaluation tooling and optional web design/testing. Preserved per-skill licenses rather than assuming one license for the whole repository. |
| `getsentry/skills` | Selected skill inspection with a deterministic scanner and manual analysis guidance. Did not import its security-review skill: its instruction to exclude authenticated code paths is too broad for general authorization review. |
| `warpdotdev/common-skills` | Imported the missing `write-tech-spec` directory already referenced by the existing lock, plus its product-spec companion. These are optional, with Warp terminology retained and documented. |
| `skrrt-sh/skills` | Reviewed its release flow. Did not select it: it adds a second shipping-policy setup and host-specific scripts; selected pipeline and changelog guidance fits the existing tools with less duplication. |
| `anyshift-io/sre-skills` | Reviewed the current tree. Its available skills focus on AWS/Kubernetes investigations; selected incident methodology is a better general default. |

Not selected from pstack: `poteto-mode` and its broad principle suite overlap with `ponytail`; `how`, `why`, `architect`, `recall`, and `reflect` bring additional mode, model-runner, or companion dependencies. Do not import one of those entry points alone and assume the whole pstack runtime is present.

## Local workflow adaptations

The user requested that the complete factory flow operate locally, with only
`implement` integrating with externally supplied tasks or explicit delivery.
This requires deliberate adaptations of existing skills rather than importing
more skills. The source design and licenses remain attributed.

- Planning and setup write local `.factory/<feature>/` files without tracker
  accounts. Task state, ownership, dependencies, acceptance evidence, and
  handoff notes stay local.
- `implement` accepts local work and explicit Jira, GitHub, GitLab, or Notion
  sources, imports required context, then uses the same local execution flow.
- Reviews consume local diffs and imported context. Service-specific reference
  templates, the external spec resolver, and upload helpers live under
  `implement`. Adapter skills are manually invoked references for it only.
- Worktree setup uses local Git state without fetching or querying open PRs.
- Verification maintenance retains local edits and evidence. Reports and
  screenshots stay project-local; HTML walkthroughs load no CDN assets.
- Requested delivery, deployment, releases, and notifications require their
  own authorization through `implement`. Technical research, package sources,
  and testing application interfaces are separate from workflow state.

The manifest retains each original `files` hash and records `adaptations` with
an effective SHA-256 and reason. A null effective hash records a removal;
new paths are also explicit. Validation rejects unrecorded changes. Licenses
are never adapted. Supporting examples and host metadata follow the new
entrypoint behavior. This is a documented local fork of selected upstream
instructions, not an assertion that all imported files are unchanged.

Host-specific skill tools and subagents remain conditional. Local task-graph
execution supports a sequential fallback. The standalone differential review
uses its bundled context-building and adversarial methodology; optional native
Trail of Bits plugin agents are not installed by copying a skill directory.
Model evaluations may require a provider or host CLI; this does not require a
hosted task tracker.

## Import inspection

Ran the Sentry scanner over all 33 imports and inspected its high/critical matches. The notable matches were:

- `sharp-edges`: the checklist phrase about preventing security bypass, and Unicode joiners inside a Swift family-emoji example. These are ordinary security guidance and example text.
- `webapp-testing`: a loopback socket used for server readiness. The helper starts caller-supplied shell commands; use it only with trusted commands. Prefer `exec` for a simple server command so cleanup terminates the server itself rather than only its shell.
- `skill-creator`: the trigger evaluator writes a temporary command file under the selected project's `.claude/commands`, invokes the Claude CLI, and cleans it up. This is a real, documented configuration mutation, not a read-only validator. Do not run optimization merely to install the skill.
- `skill-scanner`: detection regexes and reference examples include injection strings, encoded attacks, and sensitive-path examples. They describe threats; they are not instructions to perform them.

The scanner is heuristic and does not recursively inspect every possible resource format. Metadata, checksums, entry-point relative links, and Python syntax are checked separately by `scripts/validate_collection.py`. No automatic hooks or package installation were added to activate the imported skills. Upload helpers are now restricted to explicit delivery under `implement`; the walkthrough renderer is offline.

## Remaining parts of a software factory

| Previously identified gap | Coverage added | What still requires a project or runtime |
| --- | --- | --- |
| Project discovery | Architecture exploration and verification generator | Persistent project profile and adapter registration |
| Specifications | `to-spec`, optional product/tech spec pair | Machine-readable requirement IDs and organization-specific contracts |
| Planning | `to-tickets`, `implement-spec` | Durable scheduling, atomic claims, retries, cancellation, and recovery |
| Independent verification | Review workflow, real-app verification, completion evidence | Protected acceptance checks and revision-bound evidence storage |
| Debugging | `diagnosing-bugs`, `tdd` | Target-specific reproducible environments and fixtures |
| Security | `differential-review`, `sharp-edges`, `skill-scanner` | Enforced credentials, network policy, sandbox boundaries, and audit records |
| Architecture | Domain and deep-module design skills | Project-specific contracts and accepted architecture decisions |
| Delivery | Pipeline and changelog guidance | Configured packaging, signing, migrations, promotion, and rollback execution |
| Operations | Runbooks, postmortems, triage | Monitoring integrations, service ownership, and incident access |
| Factory evaluation | Skill evaluation tooling and benchmark discipline | Representative task corpus, independent scoring, cost budgets, and regression thresholds |
| Interface quality | Optional design, browser tests, accessibility guidance | Native platform tooling and project-specific user journeys |
| Distribution and maintenance | Commit-pinned imports, licenses, integrity checks, CI | Host installation and deliberate upstream updates |

These remaining requirements are not solved by adding more Markdown. This PR imports existing capabilities and records those boundaries; it does not invent an orchestration service or claim autonomous factory readiness.
