# Skill Installation

## Use from source
- Open the target folder in the repo.
- Review `README.md` for fit and operating boundaries.
- Use `SKILL.md` directly when running the skill from source.

## Agent metadata
- `agents/openai.yaml` provides the public display name and short behavior summary for agent loaders.
- Keep the YAML description aligned with the skill README and frontmatter.

## Packaged distribution
- Release assets should mirror the source folder names.
- Build packaged ZIPs from the current source tree.
- Do not assume every source folder includes local helper scripts or templates; the instruction layer remains authoritative.
