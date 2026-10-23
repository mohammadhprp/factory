---
name: before-and-after
description: Capture or reuse before/after screenshots and recordings, then format
  local comparison Markdown for a task. Never upload media or edit hosted PR/MR
  descriptions; requested external delivery belongs to implement.
license: PolyForm-Shield-1.0.0
---

# Local before-and-after evidence

Use `agent-browser` or the project's established capture tool. For agent-browser,
load `agent-browser skills get core --full` for version-matched navigation,
screenshots, recordings, and session behavior. Do not install or activate a tool
merely to import this skill. If capture is unavailable, reuse suitable images or
report the missing capability; do not invent evidence.

Reuse existing media when it matches the viewport, page state, and source
revision. Treat the current state as after only when task context establishes
that fact. Ask only if the baseline remains ambiguous. Do not switch another
task's branch, stash changes, or capture a full page unless requested. Verify
local readiness and that any server belongs to this task.

## Local output and formatting

Save media under `.factory/<feature>/evidence/`, or the supplied local evidence
directory. Resolve `SKILL_DIR` from the absolute directory containing this loaded
`SKILL.md`, never a source-checkout path or fixed harness directory. Resolve
`EVIDENCE_DIR` to the task's absolute local evidence directory and preserve
existing files unless replacement is approved.

The bundled Node.js formatter only reads local media and emits Markdown. It does
not capture, upload, or contact a service. It supports PNG, JPEG, GIF, WebP, MP4,
MOV, and WebM. Run it with the evidence directory as the working directory and
use relative media paths without whitespace:

```sh
node "$SKILL_DIR/scripts/format.mjs" \
  --before before.png --after after.png --label Desktop \
  > "$EVIDENCE_DIR/comparison.md"
```

Use `--after after.png` alone for a new preview. Repeat before/after pairs and
labels for multiple states. Local videos render on their own lines; test the
consumer's Markdown viewer rather than promising an embedded player.

To update an existing local document, use `--body-file` and a different output
file. Review the proposed change before replacing the original. The formatter
replaces only its `before-and-after:start/end` marker block, preserving bytes
outside it. Broken or duplicate markers are errors, not permission to rewrite
the surrounding document. Media must remain within the working directory.

Do not use the older capture CLI's `--markdown` flag: it uploads images. Do not
use attachment-list or hosted-video URL modes to initiate delivery from this
entrypoint. Do not call upload endpoints, publish media, edit PR/MR descriptions,
or bypass a remote sign-in wall. Explicit external source or delivery requests
go through `implement`; existing delivery adapters remain there.

Return the absolute paths to the available media and local comparison document.
Record the source revision, viewport, and state represented by each capture.
Missing baseline or capture access is a limitation to report, not permission to
upload elsewhere or invent evidence.

## Source

The formatter and capture guidance were synchronized from Stack's shared skill.
The pinned source hashes and Factory's local-only adaptations are recorded in
`upstream-skills.json` at the collection root. Those root files are provenance,
not runtime dependencies of the installed skill. The upstream PolyForm Shield
license is retained in `LICENSE` and is not replaced by another repository's license.
