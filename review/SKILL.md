---
name: review
description: Review local Git changes or a locally imported patch and produce local
  review.json and review.html artifacts. No remote fetching, hosted review submission,
  or account is required.
---

# Review Skill

## Generated files

Save artifacts under `.factory/<feature>/review/` in the consuming project, or the supplied persistent local output directory (`OUTPUT_DIR`). Reuse the active task directory; for a standalone review, derive a short review slug from the requested scope. Preserve existing reports unless replacement is requested. Return absolute paths.

Review the requested change and write the result to `$OUTPUT_DIR/review.json`. The review is
read-only: do not approve, request changes, comment, merge, push, or otherwise
modify remote repositories.

## Select the change source

Use the source explicitly named by the user. If it is not named, inspect the
current repository and ask when the target is ambiguous.

### Local changes

- Run `git status --short` and inspect staged and unstaged changes with
  `git diff`, `git diff --cached`, and the relevant branch comparison when
  needed.
- Review the working tree as it exists; do not checkout, reset, stash, or amend
  user changes.

### Imported change context

For a remote source, `implement` first imports the patch, source description, base/head identities, and needed check results into local files. Read those files here. A source URL is a citation only; do not resolve it or call a hosting CLI. If the local patch or necessary context is missing, report the limitation.

## Review process

1. Establish the change intent from the request, commit history, description,
   and diff. Focus findings on changed files and lines.
2. Read relevant repository guidance and contracts, including naming, testing,
   security, and performance standards when available.
3. Check correctness, edge cases, error handling, state transitions,
   compatibility, security, and meaningful performance risks.
4. Check maintainability, comments, and tests against the consuming
   repository's conventions. Treat changed comments and tests as review items.
5. Include only actionable findings. Put concerns about untouched code in the
   top-level body rather than attaching them to changed lines.
6. Classify findings as critical, important, suggestions, or nits. Do not block
   for speculative improvements or cosmetic preferences.

## Inline comments

Use inline comments only when the exact changed path, side, and line are
available in the reviewed diff. For annotated diffs, use `[OLD:n]` as `LEFT`,
`[NEW:n]` as `RIGHT`, and `[OLD:n,NEW:m]` as `RIGHT` line `m`. If an exact
location cannot be verified, put the finding in the top-level body.

Every inline comment must begin with one of:

- `🚨 [CRITICAL]`
- `⚠️ [IMPORTANT]`
- `💡 [SUGGESTION]`
- `🧹 [NIT]` (only with a concrete suggestion)

Keep comments concise, actionable, and limited to changed lines. Use a
`suggestion` block only when the replacement is exact and safe.

## Output contract

Write exactly one `$OUTPUT_DIR/review.json` with this shape:

```json
{
  "verdict": "APPROVE",
  "body": "## Overview\n...\n\n## Concerns\n...\n\nFound: 0 critical, 0 important, 0 suggestions\n\nApprove",
  "comments": []
}
```

- `verdict` is required and must be `APPROVE` or `REJECT`.
- `body` is required and must contain an overview, concerns, issue counts in
  the form `Found: X critical, Y important, Z suggestions`, and a final
  recommendation of `Approve`, `Approve with nits`, or `Request changes` that
  agrees with `verdict`.
- `comments` is required and must be an array. Use an empty array when no
  verified inline comment is appropriate.
- Paths are repository-relative. `side` and `start_side` are `LEFT` or
  `RIGHT`; `start_line` is used only for a multi-line range.

Before finishing, validate JSON and, when an annotated diff is available, run:

```sh
python3 .agents/skills/review/scripts/validate_review_json.py \
  --review-json "$OUTPUT_DIR/review.json" --diff "$OUTPUT_DIR/diff.txt"
```

If that path is unavailable, run the validator from this skill's `scripts/`
directory. Then render the review for human inspection:

```sh
python3 .agents/skills/review/scripts/render_review.py \
  --review-json "$OUTPUT_DIR/review.json" --output "$OUTPUT_DIR/review.html"
```

The renderer creates a self-contained Excalidraw-inspired dark HTML report.
Save any captured diff to `$OUTPUT_DIR/diff.txt` too. Set `OUTPUT_DIR` to the
expanded absolute skill output directory before these commands; create it before
writing and check existing outputs before invoking the renderer. The final
artifacts are `$OUTPUT_DIR/review.json` and `$OUTPUT_DIR/review.html`.

