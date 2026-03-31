# Release Policy

## Canonical source
- The repository source tree is the canonical product.
- Release ZIPs are distribution artifacts generated from source.

## Public-safe packaging
- Only package public-safe material that is already approved for source control.
- Do not add raw standards text, private handoff files, PDFs, large binaries, or temporary packaging debris.

## Versioning
- Update `CHANGELOG.md` with meaningful repository changes.
- Keep asset names stable so downstream installation instructions stay valid.
- Package the umbrella router separately from standalone skills.
