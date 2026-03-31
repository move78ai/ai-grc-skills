---
name: owasp-agentic-ai-mapping-to-iso-42001
description: "Workflow-first mapping support that turns OWASP Agentic AI findings into ISO/IEC 42001 control, evidence, and remediation views."
---

# OWASP Agentic AI Mapping to ISO 42001

Use this skill to turn OWASP Agentic AI Top 10 findings into working ISO 42001 implementation artifacts.






Default audience: Security, governance, assurance, audit, and supplier-risk teams working through agentic AI findings against an ISO/IEC 42001 baseline.

Default style: Mapping-driven, evidence-aware, and explicit about what each finding means for control selection and remediation.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the task type.
   - **Map ASI findings to ISO 42001 clauses and Annex A controls** -> follow **Crosswalk workflow**.
   - **Assess one agentic use case and identify the most relevant ASI items and ISO controls** -> use `scripts/profile_builder.py` with the use-case profile template.
   - **Run a maturity or gap assessment** -> use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Look up a specific ASI item, ISO clause, control theme, evidence type, or action** -> use `scripts/crosswalk_lookup.py`.
   - **Prepare executive, audit, or residual-risk materials** -> follow **Evidence and decision workflow**.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and continue.
   If the use case, deployment pattern, or control maturity is unclear, infer the most likely agentic context, label assumptions, and proceed.

## Core operating rules

- Treat all OWASP-to-ISO mappings in this skill as derivative implementation guidance, not as official mappings published by ISO or OWASP.
- Use ISO 42001 clause and Annex A references to operationalize risk treatment, impact assessment, life-cycle control, monitoring, third-party governance, and documented information.
- Distinguish management-system requirements from technical safeguards. When a user asks for technical mitigations, translate them into governance artifacts, evidence, and accountable owners.
- Prefer primary mappings to clause 6.1.3, clause 6.1.4, clause 9.1, clause 9.2, clause 9.3, clause 10.2, and Annex A controls when the task is about threat response, assurance, or residual-risk approval.
- Use Annex A controls as the control-theme layer and management-system clauses as the governance-process layer.
- For agentic-security findings, always identify whether the main exposure sits in goal control, tool use, identity, supply chain, code execution, memory, inter-agent communication, cascading behavior, human oversight, or rogue autonomy.
- When the user requests a go or no-go view, conclude with one of: **proceed**, **proceed with conditions**, **hold pending remediation**, **restricted use only**, or **do not proceed**.
- Keep outputs public-safe. Do not reproduce copyrighted ISO text or long OWASP excerpts. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user asks for another format, use this structure:

# [title]

## 1. executive summary
- scope reviewed
- key asi findings in scope
- iso 42001 posture
- decision recommendation
- major blockers or required conditions

## 2. use case and threat context
- deployment pattern
- agent topology and autonomy
- tools, data, external systems, and suppliers
- applicable asi items and optional llm overlay

## 3. mapped iso 42001 control posture
| asi item | iso reference | control theme | current state | target state | owner |
|---|---|---|---|---|---|

## 4. evidence and assurance requirements
| artifact | why it is needed | mapped asi item | owner | timing |
|---|---|---|---|---|

## 5. prioritized implementation actions
| priority | action | mapped iso reference | owner | due date |
|---|---|---|---|---|

## 6. residual risk and next review
- residual-risk position
- approval conditions
- next review point
- monitoring or audit cadence

## Crosswalk workflow

Use this when the user needs a practical mapping from ASI findings to ISO 42001.

1. Start from `references/asi-to-iso42001-crosswalk.csv`.
2. Add context from `references/owasp-agentic-items.csv`, `references/iso42001-clause-guide.csv`, and `references/evidence-catalog.csv`.
3. Determine whether the user needs:
   - an as-is crosswalk table
   - a use-case-specific filtered mapping
   - a control tracker
   - an evidence request pack
   - an executive or residual-risk memo
4. If the user asks for optional model-layer coverage, add `references/asi-llm-overlay.csv`.
5. Convert the mapping into working artifacts from `assets/templates/`.

## Use-case profiling workflow

Use this when the user wants to know which ASI items and ISO controls matter most for one agentic deployment.

1. Start from `assets/templates/agentic-use-case-profile.csv`.
2. Run:
   `python scripts/profile_builder.py <input_csv> <output_dir>`
3. Review the generated outputs:
   - `starter_profile.md`
   - `recommended_crosswalk.csv`
4. Use the result to populate `mapped-control-tracker.csv` and `implementation-action-plan.csv`.
5. If the use case is multi-agent, high-autonomy, high-write, or high-external-exposure, default to stronger monitoring, event logging, and residual-risk review.

## Gap-analysis workflow

Use this when the user wants a scored assessment, remediation plan, or audit-style current-state view.

1. Copy `assets/templates/owasp-iso-gap-questionnaire.csv` and fill `score`, `owner`, `evidence`, and `notes`.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review and use:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `residual_risk_profile.csv`
4. Tailor the summary for the audience:
   - ciso -> logging, monitoring, supplier exposure, containment, and drift detection
   - chief risk officer -> impact, risk treatment, residual-risk gates, and approval conditions
   - legal counsel -> documentation, governance evidence, communication, and accountability
   - audit -> design adequacy, evidence sufficiency, review cadence, and corrective action traceability

## Evidence and decision workflow

Use this when the user asks for audit, executive, or risk-acceptance outputs.

1. Start from:
   - `assets/templates/evidence-request-pack.md`
   - `assets/templates/executive-decision-memo.md`
   - `assets/templates/residual-risk-acceptance-memo.md`
   - `assets/templates/review-and-decision-log.csv`
2. Tie every mapped item to:
   - the ASI item
   - the ISO clause or Annex A control theme
   - the accountable owner
   - the evidence artifact
   - the next review date
3. Use `references/implementation-action-library.csv` when the user wants concrete next actions.
4. End with a decision and a named next review point.

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter ASI-to-ISO mapping profile for one use case
- `scripts/gap_analysis.py`
  - summarize a scored questionnaire into priorities and a residual-risk profile
- `scripts/crosswalk_lookup.py`
  - search the ASI, ISO, evidence, action, and overlay reference tables

## Resource map

### references/
- `how-the-skill-uses-the-sources.md` -> explains source grounding and derivative-mapping boundaries
- `implementation-workflows.md` -> concise workflow and decision rules for repeat use
- `publication-and-copyright-boundaries.md` -> public-distribution safety note
- `owasp-agentic-items.csv` -> derivative summary of ASI01-ASI10 and the main mitigation themes
- `iso42001-clause-guide.csv` -> clause and Annex A control themes used by the skill
- `asi-to-iso42001-crosswalk.csv` -> recommended primary mappings from ASI items to ISO 42001 governance controls
- `asi-llm-overlay.csv` -> optional LLM Top 10 overlay drawn from the OWASP matrix appendix
- `evidence-catalog.csv` -> evidence types and what they demonstrate
- `implementation-action-library.csv` -> standard implementation actions aligned to common ASI findings
- `residual-risk-decision-rules.csv` -> simple decision logic for approval posture

### assets/templates/
- `agentic-use-case-profile.csv`
- `owasp-iso-gap-questionnaire.csv`
- `mapped-control-tracker.csv`
- `implementation-action-plan.csv`
- `evidence-request-pack.md`
- `executive-decision-memo.md`
- `residual-risk-acceptance-memo.md`
- `review-and-decision-log.csv`
- `statement-of-applicability-helper.csv`

## Final checks before answering

Before finalizing an output, check that it answers these questions:
- which ASI items are in scope and why?
- which ISO 42001 clauses and Annex A controls are the primary recommended mappings?
- what evidence exists and what is missing?
- who owns implementation, monitoring, review, and residual-risk acceptance?
- what is the decision and what must happen before the next review?
