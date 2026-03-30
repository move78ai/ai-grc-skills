---
name: ai-board-reporting-executive-oversight
description: comprehensive workflow skill for turning ai governance, risk, compliance, incident, supplier, and assurance information into board-ready reporting and executive oversight artifacts. use when chatgpt needs to build a quarterly ai governance pack, executive dashboard, top-risk register, residual-risk acceptance memo, exception or waiver memo, management action tracker, incident board briefing, regulatory exposure summary, or portfolio heatmap for cisos, chief risk officers, legal counsel, compliance leaders, executive committees, and boards.
---

# AI Board Reporting / Executive Oversight

Use this skill to produce decision-ready executive and board artifacts, not educational summaries.

Default audience: board directors, audit and risk committees, executive committees, ciso, chief risk officer, legal counsel, compliance lead, and senior management.

Default style: detailed, comprehensive, and actionable. Prefer crisp executive framing, portfolio-level views, explicit decisions, risk tolerance language, named owners, deadlines, and evidence requirements.

## Workflow decision tree

1. Determine the task type.
   - **Build a quarterly or monthly board pack** -> follow **Board-pack workflow**.
   - **Prepare an executive dashboard or heatmap** -> follow **Dashboard workflow**.
   - **Summarize top portfolio risks and decisions required** -> follow **Top-risk workflow**.
   - **Prepare a residual-risk acceptance or exception memo** -> follow **Decision-memo workflow**.
   - **Brief the board on an incident, near miss, or major failure** -> follow **Incident-briefing workflow**.
   - **Summarize regulatory exposure or supplier concentration** -> follow **Exposure workflow**.
   - **Create or update the management action tracker** -> follow **Action-tracker workflow**.
   - **Run a readiness or maturity assessment of executive oversight** -> use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Score an organization and generate a starter executive oversight profile** -> use `scripts/profile_builder.py` with the board reporting profile template.
   - **Search the control, KPI, or board-pack library** -> use `scripts/control_lookup.py`.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and proceed.
   If a portfolio is only partially described, infer a sensible reporting baseline, label assumptions, and continue.

## Core operating rules

- Write for directors and executive sponsors who need to decide, approve, challenge, fund, escalate, or stop something.
- Prefer portfolio-level reporting over system-level detail unless the user asks for a deep dive.
- Distinguish clearly among **information**, **decision required**, **approval sought**, and **risk acceptance sought**.
- Translate technical signals into executive implications: regulatory exposure, customer impact, safety, operational dependency, concentration risk, incident severity, and remediation velocity.
- Include both current posture and trend. A static snapshot is insufficient for board oversight.
- When the user asks for a board paper, include: material facts, top risks, proposed decision, alternatives considered, residual risks, and management recommendation.
- When the user asks for a dashboard, include thresholds or red-amber-green logic, not just raw values.
- Require named owners and dates for all actions, exceptions, and accepted residual risks.
- Use conservative, plain, non-promotional language. Do not present legal advice.
- Do not reproduce copyrighted source documents or long verbatim excerpts. Use derivative tables, templates, and original instructions only.

## Default output structure

Unless the user requests a different structure, use this format:

# [title]

## 1. executive summary
- reporting period and scope
- portfolio posture
- decisions required
- material changes since last review

## 2. portfolio risk view
- top risks
- risk trend
- affected business areas
- dependencies and concentrations

## 3. governance and control status
- what is operating well
- what is not operating adequately
- exceptions, waivers, or gaps

## 4. regulatory and stakeholder exposure
- key obligations or deadlines
- customer, workforce, or public impact
- external scrutiny and disclosure implications

## 5. actions and decisions
| priority | action or decision | owner | due date | board or exec involvement |
|---|---|---|---|---|

## 6. residual risk and recommendation
- accepted residual risks
- hold points or conditions
- management recommendation

Adapt this structure only when a template in `assets/templates/` is a better fit.

## Board-pack workflow

Use this when the user needs a recurring board or executive oversight pack.

1. Start from `assets/templates/board-reporting-profile.csv` if the user has structured portfolio inputs.
2. If the task is to create a full pack, use:
   - `assets/templates/quarterly-ai-governance-summary.md`
   - `assets/templates/board-deck-outline.md`
   - `assets/templates/board-top-risks-register.csv`
   - `assets/templates/management-action-tracker.csv`
3. Build the pack around these sections:
   - portfolio scope and material changes
   - risk posture and trend
   - incidents, exceptions, and residual-risk acceptances
   - regulatory exposure and delivery milestones
   - decisions required from the board or committee
4. Use `references/board-pack-sections.csv`, `references/board-kpis.csv`, and `references/decision-memo-controls.csv` to select appropriate content.
5. Keep board sections short, decision-centric, and ranked by materiality.

## Dashboard workflow

Use this when the user needs a one-page executive dashboard or heatmap.

1. Start from:
   - `assets/templates/board-kpi-dashboard.csv`
   - `assets/templates/ai-portfolio-heatmap.csv`
2. Use `references/board-kpis.csv` to select metrics such as:
   - number of active systems and high-risk systems
   - number of open material gaps
   - incident counts and severity trend
   - number of exceptions or waivers
   - supplier concentration and unsupported dependencies
   - percentage of systems with current impact assessments, monitoring, and inventory status
3. Always include threshold logic for red, amber, and green states.
4. Call out which metrics require board attention versus management attention only.

## Top-risk workflow

Use this when the user asks for the most material risks or a board risk register.

1. Start from `assets/templates/board-top-risks-register.csv`.
2. Rank risks by severity, breadth of impact, and immediacy.
3. For each risk, state:
   - what could go wrong
   - what evidence supports the assessment
   - existing controls
   - residual exposure
   - decision or funding needed
4. Use `references/board-reporting-domains.csv` and `references/escalation-and-exception-controls.csv` to choose framing.
5. Where relevant, separate portfolio risks into:
   - governance and accountability
   - regulatory exposure
   - operational resilience and incidents
   - third-party dependency
   - security and misuse
   - customer or public harm

## Decision-memo workflow

Use this when the user asks for approval, exception, or risk-acceptance materials.

1. Start from one of:
   - `assets/templates/residual-risk-acceptance-memo.md`
   - `assets/templates/exception-waiver-memo.md`
2. State clearly:
   - the request
   - why management cannot fully remediate before the requested date
   - alternatives considered
   - conditions attached to approval
   - expiry or review date
   - named approving authority
3. Use `references/decision-memo-controls.csv` and `references/escalation-and-exception-controls.csv` to ensure decision records are complete.

## Incident-briefing workflow

Use this when briefing the board or executives on incidents, near misses, or material failures.

1. Start from `assets/templates/incident-board-briefing.md`.
2. Cover:
   - what happened and when
   - who or what was affected
   - severity, duration, and business consequences
   - containment and remediation status
   - disclosure or regulatory implications
   - what management recommends the board should know, approve, or challenge
3. If there is no confirmed root cause, say so directly and state what is under investigation.

## Exposure workflow

Use this when the user asks for regulatory, stakeholder, or supplier exposure summaries.

1. Start from:
   - `assets/templates/regulatory-exposure-summary.csv`
   - `assets/templates/supplier-dependency-summary.csv`
2. Focus on exposure that is material to executive oversight:
   - upcoming deadlines or enforcement triggers
   - incomplete assessments or evidence packs
   - high-dependency suppliers or unsupported systems
   - concentration risk and weak fallback plans
3. When appropriate, map to portfolio decision needs: fund, remediate, hold, decommission, or accept risk.

## Action-tracker workflow

Use this when the user needs a board-facing or committee-facing action plan.

1. Start from `assets/templates/management-action-tracker.csv`.
2. For every action specify:
   - owner
   - due date
   - status
   - dependency
   - whether board or committee review is needed
3. Prioritize by materiality and near-term deadlines, not by team convenience.
4. Keep actions limited to what leadership can realistically monitor.

## Gap-analysis workflow

Use this when the user wants a maturity score, remediation plan, or oversight-readiness review.

1. Copy `assets/templates/board-reporting-gap-questionnaire.csv` and fill the `score`, `evidence`, and `notes` columns.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review the generated outputs and convert them into a decision-ready summary:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `executive_oversight_profile.csv`
4. Tailor the remediation framing by audience:
   - board or committee -> material risks, approvals, challenge, and cadence
   - ciso or cro -> metrics, owners, trend, tolerance, and controls
   - legal counsel -> regulatory exposure, disclosure, evidence, and approval record quality

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter executive oversight profile from one portfolio profile CSV
- `scripts/gap_analysis.py`
  - convert a scored questionnaire into priorities and a board-reporting posture
- `scripts/control_lookup.py`
  - search the board-pack section, KPI, governance-role, decision-control, and exception-control libraries

## Resource map

### references/
- `implementation-workflows.md` -> compact summary of repeatable executive oversight workflows in this skill
- `how-the-skill-uses-the-sources.md` -> explains source grounding and how to treat cross-framework references
- `publication-and-copyright-boundaries.md` -> public-distribution safety note
- `board-reporting-domains.csv` -> domains to cover in executive and board reporting
- `executive-governance-roles.csv` -> executive, committee, and board role definitions
- `board-kpis.csv` -> common AI governance KPIs with thresholds and interpretation guidance
- `board-pack-sections.csv` -> standard board-pack sections and decision triggers
- `decision-memo-controls.csv` -> required elements for approvals, exceptions, and residual-risk acceptances
- `escalation-and-exception-controls.csv` -> escalation, waiver, exception, and challenge controls
- `crosswalk-board-reporting-frameworks.csv` -> mapping to NIST AI RMF, ISO 42001, EU AI Act, Colorado, South Korea, and supplier-risk / oversight outputs

### assets/templates/
- `board-reporting-profile.csv`
- `board-reporting-gap-questionnaire.csv`
- `quarterly-ai-governance-summary.md`
- `board-deck-outline.md`
- `ai-portfolio-heatmap.csv`
- `board-top-risks-register.csv`
- `residual-risk-acceptance-memo.md`
- `exception-waiver-memo.md`
- `regulatory-exposure-summary.csv`
- `supplier-dependency-summary.csv`
- `management-action-tracker.csv`
- `incident-board-briefing.md`
- `board-kpi-dashboard.csv`

## Execution notes

- When the user provides structured data, prefer using the scripts first, then translate outputs into a concise executive memo or board pack.
- When the user asks for a board deck, use the template as the starting structure and keep each section decision-led.
- When the user asks what should go to the board versus management, default to board treatment for material incidents, residual-risk acceptance, unresolved high risks, material regulatory exposure, or concentration risk that cannot be mitigated quickly.
- When the user asks how to evidence oversight, prioritize logs, inventories, risk registers, approval records, incident records, exceptions, and trend metrics.
