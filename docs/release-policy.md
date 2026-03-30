# Release Policy

## Source tree
- The repository stores normalized source material only.
- Release bundles are generated from the repo contents and published separately.

## Public-safe standard
- Keep only redistributable markdown, lightweight references, and agent metadata in source control.
- Exclude raw PDFs, session handoff notes, and internal-only packaging debris.

## Versioning
- Update `CHANGELOG.md` for each release candidate.
- Keep asset names stable so downstream installers can rely on predictable zip filenames.
