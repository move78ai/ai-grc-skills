---
name: mit-ai-governance-mapping
description: "Operator-grade governance-mapping support for comparing laws, standards, frameworks, and guidance through a single coverage lens."
---

# MIT AI Governance Mapping

Use this skill to convert governance landscape questions into working mapping artifacts, not summaries.






Default audience: Policy leads, standards teams, legal counsel, governance operators, research teams, and executive stakeholders comparing governance material.

Default style: Mapping-first, portfolio-aware, and explicit about coverage gaps, blind spots, and next-step routing.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the task type.
   - **Classify one governance document** -> follow **Single-document mapping workflow**.
   - **Compare several laws, standards, or frameworks** -> follow **Multi-document comparison workflow**.
   - **Identify where governance coverage is weak or fragmented** -> follow **Governance-gap workflow**.
   - **Map governance by sector, actor, lifecycle, or legislative status** -> follow **Coverage-pattern workflow**.
   - **Prepare executive, policy, or research outputs** -> follow **Evidence and decision workflow**.
   - **Build a starter mapping profile from structured intake** -> use `scripts/profile_builder.py`.
   - **Run a scored mapping gap analysis** -> use `scripts/gap_analysis.py`.
   - **Look up governance dimensions, sectors, actors, or technical-scope terms** -> use `scripts/governance_lookup.py`.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and continue.
   If the user has not provided a document set, infer the most likely governance scope, label assumptions, and proceed.

## Core operating rules

- Treat the mit ai governance mapping project as a landscape-analysis layer, not a substitute for legal analysis or control implementation.
- Distinguish between **document coverage** and **real-world effectiveness**. A risk area can be frequently mentioned and still be poorly governed in practice.
- Distinguish between **single-document analysis** and **portfolio analysis**. Do not overgeneralize from one framework, law, or standard.
- Always separate the mapping dimensions:
  - risk-domain coverage
  - sectors covered
  - actor roles
  - lifecycle stages
  - legislative status
  - technical scope
  - jurisdiction and authority
- Treat LLM-derived classifications as indicative. Use them to prioritize follow-up analysis, not to claim definitive legal or policy truth.
- For executive outputs, convert mapping observations into concrete implications: blind spots, duplication, overconcentration, and next decisions.
- For portfolio work, highlight both **over-covered** areas and **under-covered** areas.
- When the user asks for a recommendation, conclude with one of: **proceed**, **proceed with conditions**, **hold pending deeper review**, or **research before decision**.
- Do not reproduce copyrighted source documents or bulk third-party datasets. Use derivative tables, summaries, and templates only.

## Default output structure

Unless the user requests another format, use this structure:

# [title]

## 1. executive summary
- scope reviewed
- main governance-coverage finding
- most material blind spots
- decision recommendation
- assumptions and limits

## 2. mapping scope
- document set or portfolio reviewed
- jurisdiction and authority mix
- technical scope
- lifecycle and actor focus
- sectors in scope

## 3. coverage findings
| dimension | current pattern | what it means | follow-up |
|---|---|---|---|

## 4. priority gaps and overlaps
| priority | gap or overlap | why it matters | owner | next step |
|---|---|---|---|---|

## 5. evidence and decision artifacts
| artifact | why it is needed | owner | timing |
|---|---|---|---|

## 6. decision and next review point
- approval or research status
- conditions or follow-up gates
- next review date or trigger
- residual uncertainty notes

## Single-document mapping workflow

Use this when the user wants to classify one law, standard, framework, guideline, or internal policy.

1. Start from `assets/templates/governance-document-intake.csv`.
2. Capture:
   - document title
   - jurisdiction
   - authority type
   - legislative status
   - technical scope
   - sectors mentioned
   - lifecycle stages covered
   - actors targeted, monitored, or enforced
   - primary risk-domain focus
3. Run `scripts/profile_builder.py` to generate a starter profile.
4. Convert the output into:
   - a concise mapping summary
   - a prioritized list of coverage strengths
   - a list of probable blind spots
5. If the user needs comparison or action routing, continue into the multi-document or evidence workflow.

## Multi-document comparison workflow

Use this when the user asks how two or more documents compare, overlap, or leave gaps.

1. Create one intake row per document using `assets/templates/governance-document-intake.csv`.
2. Use `assets/templates/risk-domain-coverage-matrix.csv` and `assets/templates/sector-actor-lifecycle-map.csv` to normalize the comparison.
3. Compare on the following dimensions:
   - risk domains emphasized
   - sectors emphasized
   - actor allocation
   - lifecycle-stage focus
   - technical-scope assumptions
   - legal force or policy maturity
4. Separate:
   - duplicate coverage
   - complementary coverage
   - blind spots
   - unresolved contradictions or uncertainty
5. End with a decision-oriented summary: what to adopt, what to supplement, and what needs deeper review.

## Governance-gap workflow

Use this when the user wants to understand whether a governance portfolio is materially incomplete.

1. Start from `assets/templates/governance-mapping-gap-questionnaire.csv`.
2. Score the questionnaire with `score`, `evidence`, `owner`, and `notes`.
3. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
4. Convert the outputs into:
   - blind spots by risk domain
   - blind spots by sector or actor
   - weak legal-force / maturity areas
   - research and policy priorities
5. If the user is a program owner, tie each gap to the next relevant internal skill or workstream.

## Coverage-pattern workflow

Use this when the user wants to understand the landscape from one angle such as sectors, actors, lifecycle stages, technical scope, or legislative status.

1. Use the relevant reference tables in `references/`.
2. For each view, identify:
   - what appears heavily covered
   - what appears lightly covered
   - whether the pattern may be driven by corpus bias
   - what practical conclusions should or should not be drawn
3. Default output artifacts:
   - `assets/templates/jurisdiction-status-scan.csv`
   - `assets/templates/sector-actor-lifecycle-map.csv`
   - `assets/templates/governance-priority-log.csv`
4. Explicitly state that landscape concentration does not equal optimal governance allocation.

## Evidence and decision workflow

Use this when the user wants board, executive, policy, or research outputs.

1. Start from:
   - `assets/templates/executive-governance-gap-memo.md`
   - `assets/templates/review-and-decision-log.csv`
   - `assets/templates/governance-priority-log.csv`
2. Tie every finding to:
   - dimension assessed
   - implication
   - owner
   - decision or research next step
3. For executive audiences, emphasize:
   - material blind spots
   - overconcentration in a few governance themes
   - sector or actor blind spots
   - whether the portfolio is fit for purpose
4. For research or policy audiences, emphasize:
   - which dimensions need manual validation
   - where corpus limitations may distort the pattern
   - which document classes should be added next

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter governance mapping profile from structured document intake
- `scripts/gap_analysis.py`
  - summarize a scored governance-gap questionnaire into priorities and uncertainty notes
- `scripts/governance_lookup.py`
  - search governance dimensions, sector, actor, status, and technical-scope libraries

## Resource map

### references/
- `implementation-workflows.md` -> compact guide to the repeatable workflows in this skill
- `how-the-skill-uses-the-sources.md` -> source hierarchy and handling of MIT mapping outputs
- `publication-and-copyright-boundaries.md` -> public-package restrictions and derivative-use note
- `governance-dimensions.csv` -> core dimensions used in governance mapping
- `risk-domain-coverage-themes.csv` -> derivative risk-domain focus areas and interpretation rules
- `sector-taxonomy.csv` -> sector groups and what coverage patterns usually imply
- `actor-taxonomy.csv` -> proposer, target, enforcer, and monitor roles
- `lifecycle-stages.csv` -> oecd/nist lifecycle stages used in the public dashboards
- `legislative-status-categories.csv` -> hard law, soft law, and other framing
- `technical-scope-terms.csv` -> ai technical-scope tags and interpretation logic
- `framework-next-steps.csv` -> where to route follow-up work in the broader skill library

### assets/templates/
- `governance-document-intake.csv`
- `governance-mapping-gap-questionnaire.csv`
- `risk-domain-coverage-matrix.csv`
- `sector-actor-lifecycle-map.csv`
- `jurisdiction-status-scan.csv`
- `governance-priority-log.csv`
- `review-and-decision-log.csv`
- `executive-governance-gap-memo.md`
- `portfolio-coverage-summary.md`

## Final checks before answering

Before finalizing a recommendation, check that the output answers these questions:
- what documents or portfolio are being mapped?
- which mapping dimensions were actually assessed?
- what appears over-covered, under-covered, or ambiguous?
- where might corpus or classification bias distort the conclusion?
- what concrete next action follows from the mapping?
- what decision should the user take now versus after deeper review?
