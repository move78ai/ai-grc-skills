# How To Use The Library

## Pick the right entry point
- Start with `umbrella/ai-grc-and-regulatory/` when the problem is still messy, multi-domain, or under-scoped.
- Start with a standalone skill when the workflow family is already clear.

## Work pattern
1. Read the skill `README.md` to confirm the folder is the right fit.
2. Use `SKILL.md` as the working instruction layer.
3. If the folder includes `references/`, `assets/`, or `scripts/`, use them as accelerators rather than as the only way to complete the task.
4. If a referenced helper file is not present, create the artifact directly from the workflow in `SKILL.md`.

## Source and packaged use
- The source repo is the canonical product.
- Release ZIPs are packaging outputs for distribution, not the authoritative place to edit a skill.
- Do not treat a packaged ZIP as the master copy if the source repo has moved on.
