# Repo Map

## Root
- `README.md`: public project overview and entry points
- `SKILLS-CATALOG.md`: fastest route to the right skill
- `CHANGELOG.md`: repository-level change history
- `CONTRIBUTING.md`: contribution and publishing rules
- `docs/`: operating notes for using and maintaining the library
- `umbrella/`: intake and routing layer
- `skills/`: standalone domain skills grouped by category

## Public skill-folder contract
Each public skill folder should expose:
- `SKILL.md`
- `README.md`
- `agents/openai.yaml`

Helper material such as `references/`, `assets/`, and `scripts/` is optional. If a folder does not ship those files yet, the instruction layer in `SKILL.md` remains the canonical source.
