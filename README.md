# AI GRC Skills

A public, workflow-first library of AI governance, risk, compliance, assurance, supplier, transparency, and regulatory skills.

## What this repository is
This repo is built for operators who need working structures, not generic explainers. Each folder is meant to help a real team move from a vague governance question to a memo, register, plan, or decision package.

The library stays modular on purpose:
- `umbrella/ai-grc-and-regulatory/` is the intake and routing layer.
- `skills/<category>/<skill-name>/` folders are the actual working units.
- Standalone skills stay narrow enough to maintain and reuse without turning into a giant merged pack.

## Who this library is for
- CISOs and Chief Risk Officers
- legal, compliance, and audit teams
- AI governance, product-governance, and assurance leads
- procurement and supplier-risk operators
- product, platform, and security teams carrying regulated or high-impact AI workloads
- consultants and practitioners who need artifact-ready starting points

## Category model
- `frameworks`: Framework-led governance, classification, and crosswalk skills.
- `regulations`: Jurisdiction-specific screening, readiness, and compliance workflows.
- `agentic-and-security`: Agentic governance, hardening, threat modeling, and controls mapping.
- `inventory-and-suppliers`: Inventory, AIBOM, dependency, and third-party AI oversight workflows.
- `assurance-and-oversight`: TEVV, oversight, incident response, and executive reporting skills.
- `risk-and-landscape`: Risk classification, governance mapping, and broader landscape analysis.
- `transparency-and-provenance`: Content provenance, synthetic media transparency, and disclosure design.

## Start with the umbrella when
- the task is still messy or under-scoped
- several domains are involved at once
- you need one intake memo before routing work to narrower skills

If the task is already clear, skip the umbrella and go straight to the relevant skill folder.

## What each public skill folder should contain
- `SKILL.md`: the instruction layer
- `README.md`: the operator-facing overview
- `agents/openai.yaml`: the machine-readable display name and summary
- optional `references/`, `assets/`, and `scripts/` material when it is ready for public release

## Source vs packaged use
Use the source repo when you want to inspect or adapt the skill directly. Use release assets when you need packaged distribution artifacts. The source tree is the product; ZIP assets are a delivery format, not the canonical copy.

## Boundaries
- This library is implementation support, not legal advice.
- Crosswalks and mappings are decision aids, not claims of legal or standards equivalence.
- Public content should stay derivative and public-safe. Do not add raw standards text, private handoff files, or release ZIPs to the repo.

## Key entry points
- [Umbrella controller](umbrella/ai-grc-and-regulatory/)
- [Skills catalog](SKILLS-CATALOG.md)
- [How to use the library](docs/how-to-use-the-library.md)
- [Naming conventions](docs/naming-conventions.md)
- [Release policy](docs/release-policy.md)
