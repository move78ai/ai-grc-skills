---
name: mitre-atlas-ai-security
description: comprehensive workflow skill for threat modeling, threat-informed review, and ai-security planning using mitre atlas for ai-enabled systems. use when chatgpt needs to profile an ai system, identify the most relevant mitre atlas tactics and attack paths, build a threat model register, plan mitigations and detections, structure red-team or purple-team exercises, prepare monitoring and incident hypotheses, run an ai-security gap assessment, or produce executive, ciso, legal, assurance, or residual-risk outputs for ai applications, agents, model-serving systems, genai platforms, and third-party ai services.
---

# MITRE ATLAS AI Security

Use this skill to turn MITRE ATLAS-style threat analysis into working AI-security artifacts, not summaries.

Default audience: ciso, security architecture, ai platform engineering, red team, purple team, chief risk officer, legal counsel, assurance, incident response, and third-party risk teams.

Default style: detailed, comprehensive, and actionable. Prefer tactic selection, scenario design, evidence requirements, detection hypotheses, named owners, and decision-ready outputs over narrative explanation.

## Workflow decision tree

1. Determine the task type.
   - **Profile one AI-enabled system and identify the most relevant ATLAS tactics** -> use `scripts/profile_builder.py` with the system profile template.
   - **Build or refine a threat model register** -> follow **Threat-model workflow**.
   - **Plan mitigations, detections, and monitoring coverage** -> follow **Detection and mitigation workflow**.
   - **Prepare red-team or purple-team exercise artifacts** -> follow **Exercise-planning workflow**.
   - **Run a scored AI-security or threat-readiness assessment** -> use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Look up a tactic, threat pattern, mitigation theme, evidence artifact, or decision rule** -> use `scripts/atlas_lookup.py`.
   - **Prepare executive, legal, or residual-risk outputs** -> follow **Evidence and decision workflow**.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and continue.
   If the architecture, model topology, supplier footprint, or deployment context is incomplete, infer the most likely AI-enabled environment, label assumptions, and proceed.

## Core operating rules

- Treat MITRE ATLAS as the primary adversary-behavior lens for AI-enabled systems in this skill.
- Treat outputs as derivative operator guidance informed by MITRE ATLAS, not as official MITRE threat intelligence products.
- Separate system scope before making recommendations: model, application, agent, orchestration layer, data pipeline, provider dependency, plugin/tool layer, user workflow, or hosted platform.
- Always identify whether the main exposure sits in public exposure, model access, execution path, supply chain, data collection, prompt or instruction flow, credential misuse, exfiltration, or impact on service, decisions, or data integrity.
- Distinguish threat modeling from controls mapping. This skill identifies threat exposure, detection needs, exercise priorities, and evidence requirements. It does not replace the later controls-mapping skill.
- Convert technical concerns into accountable artifacts: owner, system location, evidence, monitoring method, test plan, and next review date.
- For third-party or hosted AI, explicitly identify where visibility is limited and what supplier evidence is still required.
- When the user asks for a decision, conclude with one of: **proceed**, **proceed with conditions**, **hold pending remediation**, **restricted deployment only**, or **do not proceed**.
- Keep outputs public-safe. Do not reproduce copyrighted MITRE materials or large copied matrices. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user asks for another format, use this structure:

# [title]

## 1. executive summary
- system or use-case scope
- top atlas tactics in scope
- main exposure paths
- decision recommendation
- top blockers or required conditions

## 2. system and threat context
- deployment pattern
- model, agent, tool, and data architecture
- external exposure and third-party dependencies
- likely attacker objectives

## 3. threat-model posture
| tactic | exposure path | current safeguards | main gap | owner |
|---|---|---|---|---|

## 4. detections, mitigations, and evidence
| need | why it matters | owner | evidence | timing |
|---|---|---|---|---|

## 5. prioritized actions or exercise plan
| priority | action | mapped tactic | owner | due date |
|---|---|---|---|---|

## 6. residual risk and next review
- residual-risk position
- approval conditions
- next review point
- incident or exercise follow-up

## Threat-model workflow

Use this when the user needs a starter threat model, scenario set, or architecture review.

1. Start from `assets/templates/ai-system-threat-profile.csv`.
2. Run:
   `python scripts/profile_builder.py <input_csv> <output_dir>`
3. Review the generated outputs:
   - `starter_profile.md`
   - `prioritized_tactics.csv`
4. Use `references/atlas-tactics.csv`, `references/atlas-threat-patterns.csv`, and `references/threat-scenario-patterns.csv` to turn the prioritized tactics into concrete attack paths.
5. Populate:
   - `assets/templates/atlas-threat-model-register.csv`
   - `assets/templates/incident-hypothesis-log.csv`
6. If the system is externally exposed, tool-using, multi-agent, or supplier-heavy, default to stronger monitoring, credential review, and containment planning.

## Detection and mitigation workflow

Use this when the user asks what to monitor, how to mitigate likely attacks, or what evidence should exist.

1. Start from:
   - `assets/templates/detection-and-monitoring-plan.csv`
   - `references/mitigation-and-detection-themes.csv`
   - `references/evidence-catalog.csv`
2. For each tactic or threat path, define:
   - signal to watch
   - log or telemetry source
   - preventive or detective control theme
   - response owner
   - review cadence
3. Distinguish between:
   - first-party controls
   - provider or supplier dependencies
   - gaps requiring contract, architecture, or process changes
4. If the user asks for a control-oriented next step, note where the future controls-mapping skill should take over.

## Exercise-planning workflow

Use this when the user wants a red-team, purple-team, tabletop, or validation plan informed by MITRE ATLAS.

1. Start from:
   - `assets/templates/red-team-exercise-plan.md`
   - `references/threat-scenario-patterns.csv`
   - `references/decision-rules.csv`
2. Select a bounded set of scenarios based on:
   - public exposure
   - critical business process impact
   - model or agent access level
   - data sensitivity
   - supplier or plugin/tool dependencies
3. Define:
   - scenario objective
   - adversary path
   - assumed preconditions
   - success criteria
   - detection expectations
   - escalation and stop conditions
4. End with evidence artifacts that should be retained after the exercise.

## Gap-analysis workflow

Use this when the user wants a scored AI-security readiness assessment or remediation plan.

1. Copy `assets/templates/atlas-gap-questionnaire.csv` and fill `score`, `owner`, `evidence`, and `notes`.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review and use:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `residual_risk_profile.csv`
4. Tailor the summary for the audience:
   - ciso -> exposure, detections, containment, supplier visibility, and review cadence
   - chief risk officer -> materiality, decision conditions, residual-risk posture, and escalation
   - legal counsel -> documentation, contract dependency, communication, and accountability
   - assurance or audit -> evidence sufficiency, review traceability, and corrective action ownership

## Evidence and decision workflow

Use this when the user asks for board, legal, risk-acceptance, or executive outputs.

1. Start from:
   - `assets/templates/executive-risk-memo.md`
   - `assets/templates/residual-risk-acceptance-memo.md`
   - `assets/templates/review-and-decision-log.csv`
2. Tie every material threat path to:
   - tactic or threat pattern
   - affected asset or workflow
   - current safeguard status
   - missing evidence
   - decision owner
   - next review date
3. Use `references/decision-rules.csv` when the user wants a clear deployment posture.
4. End with a decision and a named next review point.

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter MITRE ATLAS threat profile for one AI-enabled system
- `scripts/gap_analysis.py`
  - summarize a scored questionnaire into priorities and a residual-risk profile
- `scripts/atlas_lookup.py`
  - search tactics, threat patterns, mitigations, evidence types, and decision rules

## Resource map

### references/
- `how-the-skill-uses-the-sources.md` -> explains source grounding and derivative-use boundaries
- `implementation-workflows.md` -> concise workflow and decision rules for repeat use
- `publication-and-copyright-boundaries.md` -> public-distribution safety note
- `atlas-tactics.csv` -> derivative tactic list and analyst questions informed by MITRE ATLAS
- `atlas-threat-patterns.csv` -> derivative threat-pattern families commonly used in AI-security reviews
- `threat-scenario-patterns.csv` -> scenario starters for threat modeling and exercises
- `mitigation-and-detection-themes.csv` -> practical mitigation and monitoring themes
- `evidence-catalog.csv` -> evidence types and what they demonstrate
- `decision-rules.csv` -> simple decision logic for deployment posture and review triggers
- `framework-next-steps.csv` -> where to route follow-on work into governance, TEVV, incident, or controls-mapping skills

### assets/templates/
- `ai-system-threat-profile.csv`
- `atlas-threat-model-register.csv`
- `atlas-gap-questionnaire.csv`
- `detection-and-monitoring-plan.csv`
- `incident-hypothesis-log.csv`
- `red-team-exercise-plan.md`
- `executive-risk-memo.md`
- `residual-risk-acceptance-memo.md`
- `review-and-decision-log.csv`

## Final checks before answering

Before finalizing an output, check that it answers these questions:
- what AI-enabled system or workflow is in scope?
- which MITRE ATLAS tactics matter most and why?
- what are the most credible threat paths in this environment?
- what mitigations, detections, and evidence exist and what is missing?
- who owns implementation, review, and residual-risk acceptance?
- what is the decision and what must happen before the next review?
