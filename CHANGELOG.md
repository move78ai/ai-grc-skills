# Changelog

## Unreleased

### Changed
- Rewrote the root repository copy so the project reads like a live public library instead of an internal scaffold.
- Rebuilt the skills catalog and docs set around the current modular repo structure and source-versus-package model.
- Normalized every public skill README into a consistent operator-facing format with clearer inputs, outputs, and usage triggers.
- Aligned skill metadata by tightening `SKILL.md` frontmatter, adding consistent audience/style notes, and normalizing `agents/openai.yaml`.

### Notes
- The umbrella skill remains a router only.
- Public source boundaries remain in force: no raw standards text, private handoff files, or release ZIPs in the repo.
