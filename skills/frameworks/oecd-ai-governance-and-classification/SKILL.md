---
name: oecd-ai-governance-and-classification
description: comprehensive workflow skill for classifying ai systems with the oecd framework, assessing governance needs across the ai lifecycle, and operationalizing the oecd ai principles into practical actions, evidence requests, inventory records, and executive-ready governance outputs. use when chatgpt needs to build or review an ai inventory, classify one system or portfolio slice, determine lifecycle-stage governance requirements, convert principle-level guidance into implementable controls, run a scored governance gap assessment, or prepare decision-ready outputs for risk, legal, compliance, audit, data governance, product, and executive stakeholders.
---

# OECD AI Governance and Classification

Use this skill to turn OECD AI classification, lifecycle, and principles material into working governance artifacts, not summaries.

Default audience: ciso, chief risk officer, legal counsel, compliance, audit, data governance, product governance, procurement, assurance, and executive oversight teams.

Default style: detailed, comprehensive, and actionable. Prefer decision-ready classifications, inventory records, governance checklists, owner assignments, evidence requests, and executive summaries over narrative explanation.

## Workflow decision tree

1. Determine the task type.
   - **Classify one AI system, model, agent, or use case using the OECD framework** -> use `scripts/profile_builder.py` with the classification profile template.
   - **Build or refine an AI inventory or registry record** -> follow **Inventory workflow**.
   - **Assess governance needs by lifecycle stage** -> follow **Lifecycle workflow**.
   - **Convert OECD AI Principles into concrete implementation actions and evidence** -> follow **Principles operationalization workflow**.
   - **Run a scored current-state or readiness assessment** -> use `scripts/gap_analysis.py` with the governance gap questionnaire template.
   - **Look up a classification dimension, lifecycle stage, principle, action, evidence type, or routing suggestion** -> use `scripts/oecd_lookup.py`.
   - **Prepare executive, legal, or residual-risk outputs** -> follow **Decision workflow**.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and continue.
   If deployment context, affected users, third-party dependence, or lifecycle stage is incomplete, infer the most likely operating environment, label assumptions, and proceed.

## Core operating rules

- Treat the OECD classification framework as the primary system-characterization lens in this skill.
- Treat the OECD AI system lifecycle as the primary sequencing lens in this skill.
- Treat the OECD AI Principles as the primary principle-to-action lens in this skill.
- Treat this skill as derivative operator guidance, not as an official OECD publication.
- Always separate the object being assessed: model, agent, application, workflow, dataset, supplier-provided service, or portfolio.
- Use classification before recommending governance depth. Do not jump straight to control advice.
- Convert principle-level guidance into owners, actions, evidence, monitoring, and decision outputs.
- Distinguish between controls that exist in policy and controls that exist in operating practice.
- Require evidence language. For every material recommendation, specify the artifact, log, review record, or evidence that would prove implementation.
- When the user asks for a decision, conclude with one of: **proceed**, **proceed with conditions**, **hold pending remediation**, **restricted use only**, or **do not proceed**.
- Keep outputs public-safe. Do not reproduce copyrighted or gated OECD source documents. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user asks for another structure, use this format:

# [title]

## 1. executive summary
- system or use-case scope
- oecd classification view
- lifecycle-stage governance posture
- principles most in scope
- decision recommendation
- top blockers or required conditions

## 2. system and governance context
- deployment pattern
- stakeholder and impact context
- third-party dependencies
- current lifecycle stage and change exposure

## 3. classification and lifecycle posture
| area | oecd dimension or stage | main finding | implication | owner |
|---|---|---|---|---|

## 4. actions and evidence requirements
| principle or issue | key action | evidence needed | owner | timing |
|---|---|---|---|---|

## 5. prioritized action plan
| priority | action | route | owner | due date |
|---|---|---|---|---|

## 6. residual risk and next review
- residual-risk position
- approval conditions
- next review point
- downstream skill handoff if needed

## Classification workflow

Use this when the user needs an OECD classification profile for one AI system, model, agent, or use case.

1. Start from `assets/templates/ai-system-classification-profile.csv`.
2. Run:
   `python scripts/profile_builder.py <input_csv> <output_dir>`
3. Review the generated outputs:
   - `classification_summary.md`
   - `classification_profile.csv`
4. Use:
   - `references/oecd-classification-dimensions.csv`
   - `references/system-impact-factors.csv`
   - `references/framework-next-steps.csv`
5. Populate:
   - `assets/templates/ai-inventory-record.csv`
   - `assets/templates/principles-operating-plan.csv`
6. If the system is consequential, high-impact, or supplier-dependent, route follow-on work into the relevant downstream skill using `references/framework-next-steps.csv`.

## Inventory workflow

Use this when the user needs an AI inventory or registry record.

1. Start from:
   - `assets/templates/ai-inventory-record.csv`
   - `references/oecd-classification-dimensions.csv`
2. Record:
   - system name and owner
   - intended purpose and task
   - data and inputs
   - model and technical characteristics
   - output type and action scope
   - affected people and economic context
   - lifecycle stage
   - supplier, hosting, and dependency details
3. Use the classification output to decide whether the inventory record is sufficient or whether a deeper governance plan is needed.
4. If the user is inventorying a portfolio, repeat per system and aggregate in a separate register outside the skill if needed.

## Lifecycle workflow

Use this when the user asks what governance is needed at a particular lifecycle stage.

1. Start from:
   - `references/oecd-lifecycle-stages.csv`
   - `assets/templates/lifecycle-governance-checklist.csv`
2. Determine whether the system is in:
   - design, data, and modeling
   - verification and validation
   - deployment
   - operation and monitoring
3. For the current stage, specify:
   - required governance actions
   - required evidence
   - named owners
   - review cadence
   - stage-exit conditions
4. Distinguish between work that must happen now and work that belongs to a later stage.

## Principles operationalization workflow

Use this when the user asks how to turn OECD AI Principles into practical governance.

1. Start from:
   - `references/oecd-principles-to-actions.csv`
   - `references/oecd-principles-to-evidence.csv`
   - `assets/templates/principles-operating-plan.csv`
2. For each relevant principle, define:
   - why it applies in this context
   - concrete implementation actions
   - required operating evidence
   - owner and review cadence
3. Distinguish between:
   - policy statements
   - process controls
   - technical controls
   - user transparency or accountability actions
4. Note where a deeper downstream skill should take over.

## Gap-analysis workflow

Use this when the user wants a scored current-state assessment or remediation plan.

1. Copy `assets/templates/governance-gap-questionnaire.csv` and fill `score`, `owner`, `evidence`, and `notes`.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review and use:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `residual_risk_profile.csv`
4. Tailor the summary for the audience:
   - ciso -> accountability, safety, security, monitoring, and operational resilience
   - chief risk officer -> materiality, governance maturity, conditions to proceed, residual-risk posture
   - legal counsel -> documentation, accountability, transparency, human-rights and user-impact considerations
   - audit or assurance -> evidence sufficiency, control ownership, corrective actions, and review cadence

## Decision workflow

Use this when the user needs an executive, legal, or risk-acceptance output.

1. Start from:
   - `assets/templates/executive-governance-summary.md`
   - `assets/templates/residual-risk-note.md`
   - `assets/templates/review-and-decision-log.csv`
2. Tie each material issue to:
   - OECD classification dimensions
   - current lifecycle stage
   - relevant principles
   - current evidence status
   - missing action
   - owner and next review point
3. Use `references/system-impact-factors.csv` when the user wants a clear view of why governance depth should increase or stay proportionate.
4. End with a decision and a named next review point.

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter OECD classification profile and inventory starter for one AI-enabled system or use case
- `scripts/gap_analysis.py`
  - summarize a scored questionnaire into priorities and a residual-risk profile
- `scripts/oecd_lookup.py`
  - search dimensions, lifecycle stages, principles, actions, evidence types, and next-step routes

## Resource map

### references/
- `how-the-skill-uses-the-sources.md` -> explains source grounding and derivative-use boundaries
- `implementation-workflows.md` -> concise workflow and decision rules for repeat use
- `publication-and-copyright-boundaries.md` -> public-distribution safety note
- `oecd-classification-dimensions.csv` -> derivative OECD classification dimensions and practical usage notes
- `oecd-lifecycle-stages.csv` -> derivative lifecycle stages and governance interpretation notes
- `oecd-principles-to-actions.csv` -> derivative principle-to-action mapping
- `oecd-principles-to-evidence.csv` -> derivative principle-to-evidence mapping
- `system-impact-factors.csv` -> practical factors for determining governance depth
- `framework-next-steps.csv` -> where to route follow-on work into inventory, supplier risk, testing, provenance, incident, atlas, or mit workflows

### assets/templates/
- `ai-system-classification-profile.csv`
- `ai-inventory-record.csv`
- `lifecycle-governance-checklist.csv`
- `principles-operating-plan.csv`
- `governance-gap-questionnaire.csv`
- `executive-governance-summary.md`
- `residual-risk-note.md`
- `review-and-decision-log.csv`

## Final checks before answering

Before finalizing an output, check that it answers these questions:
- what AI-enabled system, workflow, or supplier capability is in scope?
- how does the system classify across the OECD dimensions?
- what lifecycle stage is the system in now?
- which OECD principles matter most in this context and why?
- what actions and evidence are needed now versus later?
- who owns implementation, review, and residual-risk acceptance?
- what is the decision and what must happen before the next review?
