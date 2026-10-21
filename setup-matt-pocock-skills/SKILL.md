---
name: setup-matt-pocock-skills
description: Configure local factory task storage and domain documentation for a repository.
  Uses local Markdown without hosted tracker setup, credentials, labels, or account
  access.
disable-model-invocation: true
---

# Set up the local workflow

Inspect the current repository, its instructions, existing `.factory/` state, glossary, and architecture decisions. Reuse established local paths when the project defines them. Otherwise use `.factory/<feature>/` for per-feature work. Do not inspect service accounts or configure an external tracker.

Setup is optional: `to-spec`, `to-tickets`, and `implement-spec` work without it. Create configuration lazily and never create sample tasks or empty project documents merely to satisfy this skill.

1. Read local `AGENTS.md` or `CLAUDE.md`, existing task conventions, `GLOSSARY.md` or `GLOSSARY-MAP.md`, and relevant ADRs.
2. If requested, write a short local workflow pointer to the established instruction file. Preserve surrounding content. Do not create a competing instruction file.
3. Write `docs/agents/issue-tracker.md` from [issue-tracker-local.md](issue-tracker-local.md), adapting only the actual local paths. Despite its compatibility filename, it describes files, not an external tracker.
4. When useful, write `docs/agents/triage-labels.md` from [triage-labels.md](triage-labels.md). These are local task status values, not service labels.
5. Write `docs/agents/domain.md` from [domain.md](domain.md) only when domain documentation guidance is requested or needed. Create glossary terms and ADRs lazily as decisions occur.
6. Report the changed local files and the selected conventions. Do not create issues, pages, labels, comments, remote settings, or synchronization jobs.

Remote source-task import is handled by `implement`, which copies necessary requirements into the local feature directory without moving the planning workflow to a service.
