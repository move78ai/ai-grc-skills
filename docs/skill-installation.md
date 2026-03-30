# Skill Installation

## Local use
- Browse to the skill folder you want.
- Use `SKILL.md` as the canonical instruction file.
- Keep `agents/openai.yaml` with the skill so agent loaders can resolve a clean display name and description.

## Packaging
- Package one standalone zip per skill folder.
- Package the umbrella controller separately.
- Do not include private drafts, PDFs, or temporary packaging files in release bundles.
