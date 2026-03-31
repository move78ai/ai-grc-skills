---
name: mitre-atlas-to-controls-mapping
description: "Operator-grade control-mapping support that turns MITRE ATLAS findings into control themes, evidence needs, and owner actions."
---

# MITRE ATLAS to Controls Mapping

Use this skill to turn MITRE ATLAS threat findings into working control artifacts, not generic commentary.






Default audience: Security architects, governance leads, assurance teams, auditors, and engineering owners turning threats into implementation work.

Default style: Controls-focused, evidence-aware, and explicit about owners, mapping strength, and residual decisions.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the task type.
   - **Map one AI-enabled system or use case from ATLAS tactics into control obligations** -> use `scripts/profile_builder.py` with the system mapping profile template.
   - **Build or refine a tactic-to-control crosswalk tracker** -> follow **Crosswalk workflow**.
   - **Identify evidence, owners, and implementation actions for mapped controls** -> follow **Evidence and implementation workflow**.
   - **Run a scored controls-readiness assessment** -> use `scripts/gap_analysis.py` with the controls gap questionnaire template.
   - **Look up a tactic, ISO 42001 clause, Annex A control, evidence type, or action theme** -> use `scripts/crosswalk_lookup.py`.
   - **Prepare executive, legal, or residual-risk outputs** -> follow **Decision workflow**.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and continue.
   If the architecture, supplier footprint, model topology, or ATLAS input is incomplete, infer the most likely AI-enabled environment, label assumptions, and proceed.

## Core operating rules

- Treat MITRE ATLAS as the primary adversary-behavior lens and ISO/IEC 42001 as the primary management-system control lens in this skill.
- Treat the mapping as derivative operator guidance, not as an official MITRE or ISO publication.
- Distinguish this skill from the standalone MITRE ATLAS AI Security skill. That skill identifies threat exposure and exercise priorities. This skill converts those findings into control themes, evidence, implementation actions, and management-system routing.
- Always separate the object being mapped: model, agent, application, plugin or tool layer, data pipeline, hosted provider dependency, orchestration layer, or business workflow.
- Map tactics to control themes, not to magical one-to-one compliance claims. Multiple tactics can route to the same control theme, and one tactic can require several controls.
- Identify whether the output should stay inside this skill or route into another portfolio skill such as governance, supplier risk, TEVV, incident management, board reporting, or agentic security.
- Require evidence language. For every mapped control, specify the artifact, log, review record, or control evidence that would prove implementation.
- When the user asks for a decision, conclude with one of: **proceed**, **proceed with conditions**, **hold pending remediation**, **restricted deployment only**, or **do not proceed**.
- Keep outputs public-safe. Do not reproduce copyrighted MITRE or ISO source material. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user asks for another structure, use this format:

# [title]

## 1. executive summary
- system or use-case scope
- top atlas tactics in scope
- main control themes triggered
- decision recommendation
- top blockers or required conditions

## 2. system and threat context
- deployment pattern
- model, agent, tool, and data architecture
- third-party dependencies
- likely attacker goals

## 3. atlas to control mapping posture
| tactic | attack path or concern | iso 42001 clause or annex a reference | control theme | owner |
|---|---|---|---|---|

## 4. evidence and implementation requirements
| control theme | evidence needed | implementation action | owner | timing |
|---|---|---|---|---|

## 5. prioritized action plan
| priority | action | mapped tactic | route | owner | due date |
|---|---|---|---|---|---|

## 6. residual risk and next review
- residual-risk position
- approval conditions
- next review point
- portfolio skill handoff if needed

## Crosswalk workflow

Use this when the user needs a starter mapping from MITRE ATLAS tactics or threat scenarios into ISO 42001-aligned control themes.

1. Start from `assets/templates/ai-system-mapping-profile.csv`.
2. Run:
   `python scripts/profile_builder.py <input_csv> <output_dir>`
3. Review the generated outputs:
   - `starter_mapping.md`
   - `prioritized_controls.csv`
4. Use:
   - `references/atlas-to-control-mapping.csv`
   - `references/iso-42001-control-themes.csv`
   - `references/implementation-action-library.csv`
5. Populate:
   - `assets/templates/atlas-control-mapping-tracker.csv`
   - `assets/templates/control-implementation-register.csv`
6. If the input shows supplier dependence, limited visibility, model testing needs, or likely incident exposure, route follow-on work into the relevant downstream skill using `references/framework-next-steps.csv`.

## Evidence and implementation workflow

Use this when the user asks what evidence should exist, what owners are needed, or what actions convert the mapping into an operational control plan.

1. Start from:
   - `assets/templates/atlas-evidence-checklist.csv`
   - `assets/templates/control-implementation-register.csv`
   - `references/evidence-catalog.csv`
   - `references/implementation-action-library.csv`
2. For each mapped tactic or control theme, define:
   - control owner
   - evidence artifact
   - implementation action
   - review cadence
   - whether the control is first-party, provider-dependent, or supplier-dependent
3. Distinguish between:
   - governance and policy controls
   - design and development controls
   - operational monitoring controls
   - incident and containment controls
   - supplier and contract controls
4. Note where a deeper downstream skill should take over.

## Gap-analysis workflow

Use this when the user wants a scored controls-readiness assessment or remediation plan.

1. Copy `assets/templates/atlas-control-gap-questionnaire.csv` and fill `score`, `owner`, `evidence`, and `notes`.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review and use:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `residual_risk_profile.csv`
4. Tailor the summary for the audience:
   - ciso -> control coverage, monitoring, containment, and supplier visibility
   - chief risk officer -> materiality, conditions to proceed, residual-risk posture
   - legal counsel -> obligations, documentation, third-party dependency, communication and accountability
   - audit or assurance -> evidence sufficiency, ownership traceability, corrective actions

## Decision workflow

Use this when the user needs an executive, legal, or risk-acceptance output.

1. Start from:
   - `assets/templates/executive-summary-memo.md`
   - `assets/templates/residual-risk-acceptance-memo.md`
   - `assets/templates/review-and-decision-log.csv`
2. Tie each material tactic or threat path to:
   - mapped control theme
   - relevant ISO 42001 clause or Annex A control family
   - current evidence status
   - missing action
   - owner and next review point
3. Use `references/decision-rules.csv` when the user wants a clear deployment posture.
4. End with a decision and a named next review point.

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter ATLAS-to-control mapping profile for one AI-enabled system
- `scripts/gap_analysis.py`
  - summarize a scored questionnaire into priorities and a residual-risk profile
- `scripts/crosswalk_lookup.py`
  - search tactics, ISO 42001 references, control themes, evidence types, and next-step routes

## Resource map

### references/
- `how-the-skill-uses-the-sources.md` -> explains source grounding and derivative-use boundaries
- `implementation-workflows.md` -> concise workflow and decision rules for repeat use
- `publication-and-copyright-boundaries.md` -> public-distribution safety note
- `atlas-to-control-mapping.csv` -> derivative tactic-to-control crosswalk informed by MITRE ATLAS and ISO 42001 control structure
- `iso-42001-control-themes.csv` -> derivative clause and Annex A control themes used in this skill
- `implementation-action-library.csv` -> practical implementation action ideas by control theme
- `evidence-catalog.csv` -> evidence types and what they demonstrate
- `decision-rules.csv` -> simple decision logic for deployment posture and review triggers
- `framework-next-steps.csv` -> where to route follow-on work into governance, supplier risk, TEVV, incident, board reporting, or agentic-security skills
- `optional-llm-overlay.csv` -> optional bridge from common LLM attack concerns into the same control themes

### assets/templates/
- `ai-system-mapping-profile.csv`
- `atlas-control-mapping-tracker.csv`
- `atlas-control-gap-questionnaire.csv`
- `atlas-evidence-checklist.csv`
- `control-implementation-register.csv`
- `executive-summary-memo.md`
- `residual-risk-acceptance-memo.md`
- `review-and-decision-log.csv`

## Final checks before answering

Before finalizing an output, check that it answers these questions:
- what AI-enabled system or workflow is in scope?
- which MITRE ATLAS tactics matter most and why?
- which ISO 42001 control themes are most relevant now?
- what evidence exists and what is missing?
- who owns implementation, review, and residual-risk acceptance?
- what is the decision and what must happen before the next review?
