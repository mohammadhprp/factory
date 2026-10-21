# Agent workflow

Read `README.md` for the collection workflow and `CURATION.md` for dependency and portability boundaries.

Imported skills and their supporting files are upstream copies. Preserve their content and licenses. Record deliberate updates in `upstream-skills.json` and `THIRD_PARTY_NOTICES.md`; do not mix unrecorded local edits into an upstream import.

Run `python scripts/validate_collection.py` before proposing changes. This is a skill collection, not a consuming application: do not execute deployment, tracker setup, publication, or global agent configuration simply to validate an import.
