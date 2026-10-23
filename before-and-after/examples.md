# Local before-and-after examples

## Compare existing screenshots

**Request:** "Compare these two screenshots for the local task."

Check viewport, state, and revision, then format the images in the task's local
evidence directory using the installed formatter. Return the local media and
Markdown paths. Do not upload, post a comment, or edit a hosted description.

## Record a local preview

**Request:** "Show the new page on desktop and mobile."

Use the existing capture tool or version-matched agent-browser guidance. Reuse
valid baseline media; capture only missing states. Use after-only Preview output
for a net-new page, and accurately label the viewport and source revision.

## Update a comparison document

**Request:** "Replace the evidence section, but keep the rest of this report."

Read the current file, use `--body-file` with a separate candidate output, and
verify unchanged text outside the marked block before replacing the original.
Report malformed markers rather than rewriting the whole file. A separate
request to publish evidence must be routed through `implement`.
