# Contributing

## Core repository rules
- Keep the repo modular. Do not collapse several skills into one merged super-skill.
- Keep the umbrella skill as a router and intake layer, not as a replacement for child skills.
- Preserve public slugs and paths unless there is a real defect.
- Keep the repo public-safe. Do not add raw standards text, private session files, binaries, or release ZIPs.
- Keep `README.md`, `SKILL.md`, and `agents/openai.yaml` aligned when a skill changes.

## Skill-folder contract
Every public skill folder should expose:
- `SKILL.md`
- `README.md`
- `agents/openai.yaml`

Optional helper material such as `references/`, `assets/`, or `scripts/` should only be committed when it is ready for public release and safe to distribute.

## Copy and metadata standards
- Use blunt, operator-grade language.
- Prefer practical outputs over theory-heavy prose.
- Keep framework and law names capitalized consistently.
- Remove clipped sentences, scaffold filler, and unfinished marker text before committing.

## Release discipline
- Treat the source repo as the canonical product.
- Create release ZIPs from tagged source when needed, but do not commit those ZIPs into the repo.
- Update `CHANGELOG.md` with real repository changes, not generic scaffold notes.
