---
name: before-and-after
description: Capture before/after images and local comparison Markdown as evidence
  for a local task. Never upload images or edit hosted PR/MR descriptions.
---

# Local before-and-after evidence

Use the installed `@vercel/before-and-after` CLI or the project's existing capture tool to capture the before and after states. Reuse existing images when they match the viewport, state, and source revisions. Do not switch another task's branch, stash user changes, or use a full-page capture unless requested.

Save images under `.factory/<feature>/evidence/`, or the supplied local evidence directory. For the CLI, use an explicit `--output` directory; use `--mobile` or `--tablet` when appropriate. Verify local application readiness and that each server belongs to this task. Source states and viewports must be comparable.

Do not use the CLI's `--markdown` flag: it uploads images. Write local Markdown yourself with relative image paths. Do not use upload endpoints, publish images, change PR/MR descriptions, or bypass a remote sign-in wall. Remote source/delivery requests go through `implement`.

Return the absolute paths to both images and the local comparison document. Missing baseline or capture access is a limitation to report, not permission to upload elsewhere or invent evidence.
