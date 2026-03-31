---
name: financial-services-ai-risk-management-framework
description: "Sector-specific AI governance workflows for financial institutions, control mapping, evidence planning, and exam readiness."
---

# Financial Services AI Risk Management Framework

Use this skill to produce working financial-services AI governance artifacts, not generic summaries.






Default audience: Model-risk teams, operational-risk leads, compliance, internal audit, legal counsel, data governance, and executive reviewers in financial services.

Default style: Control-focused, evidence-backed, and explicit about regulated-institution ownership, exam readiness, and approval conditions.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the task type.
   - **Classify the institution or use case against adoption stages** → follow **Adoption-stage workflow**.
   - **Map a financial-services AI use case to control objectives** → follow **Control mapping workflow**.
   - **Run a maturity or current-state assessment** → use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Create a starter financial-services AI profile** → use `scripts/profile_builder.py` with the use-case profile template.
   - **Look up control or evidence ideas** → use `scripts/control_lookup.py`.
   - **Prepare executive, audit, or exam-readiness outputs** → follow **Evidence and review workflow**.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and proceed.
   If details are missing, infer the most likely financial-services context, label assumptions, and continue.

## Core operating rules

- Treat this framework as a sector-specific operationalization layer, not a replacement for enterprise risk, cybersecurity, privacy, model risk, or legal programs.
- Always identify the institution type, regulated activity, affected customer or market segment, and whether the AI influences consumer treatment, underwriting, fraud controls, sanctions, AML, trading, claims, collections, or operational resilience.
- Separate the object being assessed: enterprise AI program, business use case, model, third-party service, dataset, or decision workflow.
- Always identify the adoption stage before recommending the depth and sequencing of controls.
- Translate control needs into implementable artifacts: ownership, process steps, evidence, monitoring, and approval criteria.
- Distinguish between controls implemented in infrastructure or workflow and controls that exist only as policy statements.
- For regulated or consequential use cases, explicitly request evidence that could withstand internal audit, model-risk review, compliance review, or supervisory examination.
- When the user asks for a decision, conclude with one of: **proceed**, **proceed with conditions**, **hold pending remediation**, **restricted use only**, or **do not proceed**.
- Do not reproduce copyrighted source documents or gated downloads. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user requests another format, use this structure:

# [title]

## 1. executive summary
- institution or use-case scope
- adoption-stage view
- control posture
- decision recommendation
- top blockers or required conditions

## 2. business and regulatory context
- institution type and business process
- customer, market, or operational impact
- key risk and regulatory sensitivities
- third-party dependencies

## 3. control-objective posture
| area | control objective theme | current state | target state | owner |
|---|---|---|---|---|

## 4. evidence and assurance requirements
| artifact | why it is needed | owner | timing |
|---|---|---|---|

## 5. prioritized action plan
| priority | action | owner | due date | dependency |
|---|---|---|---|---|

## 6. decision and next review point
- approval status
- conditions or remediation gates
- monitoring and re-review cadence
- residual-risk notes

## Adoption-stage workflow

Use this when the user asks how advanced the institution is or what set of controls is proportionate.

1. Start from `assets/templates/ai-adoption-stage-questionnaire.csv`.
2. Classify the organization across a practical stage model using `references/adoption-stage-model.csv`.
3. Identify the use case and institutional footprint:
   - pilot / internal productivity
   - customer-facing support or marketing
   - decision support for employees
   - consequential or regulated decisions
   - enterprise-scale AI platform or multi-model environment
4. Match expectations for documentation, testing, monitoring, and oversight to the inferred stage.
5. Output a stage-based roadmap with near-term, medium-term, and advanced controls.

## Control mapping workflow

Use this when the user needs a mapping from financial-services AI use cases to control themes and implementation evidence.

1. Start from `assets/templates/fs-ai-use-case-profile.md`.
2. Use `references/control-objective-catalog.csv` and `references/financial-services-control-domains.csv`.
3. Identify the use case type, for example:
   - underwriting or pricing
   - fraud and AML
   - sanctions or surveillance
   - collections or servicing
   - customer support and communications
   - treasury, liquidity, or forecasting
   - cyber defense or operational resilience
4. Convert high-level control themes into concrete implementation artifacts.
5. If the user requests evidence or readiness, continue into the evidence and review workflow.

## Evidence and review workflow

Use this when the user asks for exam-readiness, internal audit support, model-risk evidence, or executive review materials.

1. Start from the templates in `assets/templates/`:
   - `control-implementation-register.csv`
   - `effective-evidence-checklist.csv`
   - `internal-review-pack.md`
   - `executive-decision-memo.md`
2. Use `references/effective-evidence-catalog.csv` to specify what evidence should exist for each control theme.
3. Tie every control to:
   - control owner
   - process or system location
   - validation or monitoring method
   - evidence artifact
   - review cadence
4. For gaps, assign remediation dates and accountable owners.
5. End with a decision and a named next review point.

## Gap-analysis workflow

Use this when the user wants a maturity score, remediation plan, or current-state assessment.

1. Copy `assets/templates/fs-ai-rmf-gap-questionnaire.csv` and fill `status`, `owner`, `evidence`, and `notes`.
2. Run:
   `python scripts/gap_analysis.py <input_csv>`
3. Convert the output into a decision-ready summary for the user’s audience:
   - ciso → resilience, security, supplier and operational dependency
   - chief risk officer → risk governance, materiality, residual risk, conditions to proceed
   - legal counsel → disclosures, governance evidence, consumer and documentation implications
   - model risk / audit → control ownership, validation independence, evidentiary sufficiency, review cadence

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter financial-services AI use-case profile
- `scripts/gap_analysis.py`
  - summarize a scored gap questionnaire into priorities and action items
- `scripts/control_lookup.py`
  - search the control, evidence, and adoption-stage libraries

## Resource map

### references/
- `implementation-workflows.md` → compact summary of repeatable workflows in this skill
- `how-the-skill-uses-the-sources.md` → explains source grounding and how to treat gated framework materials
- `publication-and-copyright-boundaries.md` → public-distribution safety note
- `adoption-stage-model.csv` → stage model and default expectations
- `financial-services-control-domains.csv` → domain clusters for financial-services AI governance
- `control-objective-catalog.csv` → derivative control-objective themes and implementation focus areas
- `effective-evidence-catalog.csv` → evidence types and what they demonstrate
- `review-and-decision-controls.csv` → internal review, committee, and decision controls
- `crosswalk-fs-ai-rmf.csv` → mapping to NIST AI RMF, NIST AI 600-1, ISO 42001, board reporting, supplier risk, and TEVV

### assets/templates/
- `fs-ai-use-case-profile.md`
- `fs-ai-rmf-gap-questionnaire.csv`
- `ai-adoption-stage-questionnaire.csv`
- `control-implementation-register.csv`
- `effective-evidence-checklist.csv`
- `review-and-decision-log.csv`
- `internal-review-pack.md`
- `executive-decision-memo.md`
- `residual-risk-acceptance-memo.md`
- `third-party-dependency-review.csv`
- `model-risk-and-ai-risk-mapping.csv`
- `board-summary-pack.md`

## Final checks before answering

Before finalizing a recommendation, check that the output answers these questions:
- what business process or financial-services use case is in scope?
- what adoption stage is the institution or use case in?
- which control themes are applicable now versus later?
- what evidence exists and what is missing?
- who owns implementation, review, and ongoing monitoring?
- what is the decision and what must happen before the next review?
