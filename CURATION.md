# Curation and integration notes

Reviewed on 2026-10-21. Imports are pinned to the exact commits in `upstream-skills.json`; skill bodies and bundled resources are copied without edits.

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

## Dependency and workflow boundaries

| Workflow | Required companions or prerequisites |
| --- | --- |
| Matt engineering workflow | `setup-matt-pocock-skills` configures the consuming project's tracker and domain documents. `implement-spec` calls `tdd` and `code-review`; `tdd` and architecture work use `codebase-design`; architecture work also uses `grilling` and `domain-modeling`. All are present. |
| Retrospective | `retro` uses `writing-for-agents`, which is included. It suggests environment improvements; importing it does not authorize global configuration changes. |
| pstack verification | Generate a real project-local verification skill before invoking maintenance. Both generator and maintenance are included with the feature-map examples. This import does not generate a fictional verification skill for every possible project. |
| Differential security review | The standalone methodology contains a manual context-building fallback and a complete adversarial procedure. The upstream namespaced `audit-context-building` workflow and `differential-review:adversarial-modeler` agent are not registered by a skill-directory install. Use the bundled methodology/adversarial documents directly, or install the original Trail of Bits plugin for native dispatch. `issue-writer` is an optional external reporting integration, not an installed command. |
| Completion evidence | `verification-before-completion` is standalone. Installing it does not activate the whole Superpowers suite. |
| LLM evaluation | `llm-evaluation` supplies patterns for LLM features. Provider examples require the matching SDK and credentials. It is not an end-to-end factory benchmark. |
| Skill evaluation | Anthropic's `skill-creator` supplies graders, schemas, aggregation, and review tools. Some triggering/optimization commands require the Claude CLI and provider access. Basic validation and artifact inspection can run without them. |
| Skill scanner | Requires Python and PyYAML, or the documented `uv` workflow. Its findings are leads for manual review. |
| Optional web skills | `webapp-testing` requires Playwright and a working application/browser environment. `frontend-design` is a web specialty. Neither is a prerequisite for CLI, library, native, or embedded work. |
| Optional checked-in specs | Warp's two skills write `PRODUCT.md` and `TECH.md`. They retain Warp examples and optional references to upstream implementation workflows that are not included. Use the default Matt workflow for a connected, tracker-configurable implementation path. |

The existing `implement` still expects a Notion URL and CLI. Its reference to a skill named `spec` does not resolve to `to-spec` automatically. For general tasks, explicitly select `to-spec` → `to-tickets` → `implement-spec`; do not route an arbitrary task through the Notion-only entry point.

The existing `new-feature`, `implement`, and `merge-request` have different base-branch defaults. Existing `merge-request` also retains its fixed assignee. This import preserves those skills instead of silently rewriting their policies. Pick one workflow and apply the consuming project's branch and assignment policy before using its publishing commands.

## Portability and authorization

Skills are instructions consumed by an agent host. `Task`, `Skill`, `Workflow`, frontmatter extensions such as `disable-model-invocation`, and tool allowlists are host features, not portable executables. Use a compatible host; do not claim native plugin agents or hooks were installed by copying a directory. Parallel task-graph execution requires actual subagent support.

Keep operating-system commands and provider examples conditional on the target project. A deployment example using Kubernetes does not require Kubernetes for every project. A verification harness for a CLI will differ from a browser, mobile device, library, or firmware harness.

Loading or installing skills does not grant permission to publish releases, deploy, send messages, close issues, change production state, or edit global agent settings. Follow the user's request, host permissions, and consuming repository guidance. The factory collection is not a replacement for those controls.

## Import inspection

Ran the Sentry scanner over all 33 imports and inspected its high/critical matches. The notable matches were:

- `sharp-edges`: the checklist phrase about preventing security bypass, and Unicode joiners inside a Swift family-emoji example. These are ordinary security guidance and example text.
- `webapp-testing`: a loopback socket used for server readiness. The helper starts caller-supplied shell commands; use it only with trusted commands. Prefer `exec` for a simple server command so cleanup terminates the server itself rather than only its shell.
- `skill-creator`: the trigger evaluator writes a temporary command file under the selected project's `.claude/commands`, invokes the Claude CLI, and cleans it up. This is a real, documented configuration mutation, not a read-only validator. Do not run optimization merely to install the skill.
- `skill-scanner`: detection regexes and reference examples include injection strings, encoded attacks, and sensitive-path examples. They describe threats; they are not instructions to perform them.

The scanner is heuristic and does not recursively inspect every possible resource format. Metadata, checksums, entry-point relative links, and Python syntax are checked separately by `scripts/validate_collection.py`. No automatic hooks or package installation were added to activate the imported skills.

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
