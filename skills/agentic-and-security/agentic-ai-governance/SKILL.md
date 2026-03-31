---
name: agentic-ai-governance
description: "Workflow-first guidance for agent suitability, bounded autonomy, accountability, oversight, and phased rollout decisions."
---

# Agentic AI Governance

Use this skill to turn agentic-ai governance questions into working artifacts, not summaries.






Default audience: CISOs, Chief Risk Officers, legal counsel, product owners, governance leads, and deployment teams responsible for agentic systems.

Default style: Decision-ready, evidence-aware, and explicit about autonomy limits, human checkpoints, and residual-risk ownership.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the task type.
   - **Assess whether a use case is suitable for agent deployment** → follow **Use-case suitability workflow**.
   - **Define agent boundaries, autonomy limits, identities, or permissions** → follow **Bounded autonomy workflow**.
   - **Clarify accountability across internal teams and external parties** → follow **Accountability workflow**.
   - **Design human checkpoints, overrides, and ongoing supervision** → follow **Oversight workflow**.
   - **Prepare testing, rollout, or monitoring plans** → follow **Operationalisation workflow**.
   - **Prepare user notices, training, and escalation paths** → follow **End-user responsibility workflow**.
   - **Run a structured governance gap analysis** → use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Score a proposed use case and generate a starter governance profile** → use `scripts/profile_builder.py` with the use-case profile template.
   - **Search the governance control library or factor tables** → use `scripts/control_lookup.py`.

2. Produce artifacts, not theory.
   Always generate one or more of the templates in `assets/templates/` unless the user explicitly wants prose only.

3. State assumptions.
   If critical details are missing, state reasonable assumptions and proceed. Do not block on perfect inputs.

## Core operating rules

- Treat the singapore imda framework as the primary operating model for deployers of agentic ai.
- Treat governance as lifecycle-wide: planning, design, testing, deployment, monitoring, user enablement, and residual-risk acceptance.
- Distinguish governance from security. Include security governance interfaces, but do not turn this into a pure threat-modeling or red-team skill.
- Prefer bounded autonomy over broad agent freedom. Document the rationale whenever an agent gets write access, external-system access, or high autonomy.
- Require explicit human accountability. Name owners, approvers, and escalation contacts.
- Require evidence language. For every recommendation, specify the artifact, log, decision record, or control evidence that would prove implementation.
- When the user asks whether deployment should proceed, conclude with one of: **go**, **go with conditions**, **hold**, or **do not deploy**.
- When legal exposure is implied, describe governance implications and documentation needs, but do not present legal advice as definitive.
- Do not reproduce copyrighted source documents or long verbatim excerpts. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user requests a different structure, use this format:

# [title]

## 1. executive summary
- deployment context
- key governance conclusion
- top blockers or conditions
- residual-risk position

## 2. use-case and agent profile
- objective
- actor or stakeholder groups
- agent pattern and topology
- autonomy, action-space, tools, data, external systems

## 3. key governance findings
- strengths
- material gaps
- decisions required now

## 4. required controls and artifacts
| area | required control | owner | evidence |
|---|---|---|---|

## 5. prioritized action plan
| priority | action | owner | target timing | dependency |
|---|---|---|---|---|

## 6. residual risk and approval
- remaining risks
- acceptance conditions
- escalation path
- recommended decision

Adapt this structure only when a template in `assets/templates/` is a better fit.

## Use-case suitability workflow

Use this when the user asks whether an agentic use case is appropriate, high risk, or ready to proceed.

1. Collect or infer the following from the user request:
   - domain and use case
   - sensitive data access
   - external-system exposure
   - action scope, especially read vs write
   - reversibility of actions
   - autonomy level
   - task complexity
   - whether the system is multi-agent
2. If structured input is useful, start from `assets/templates/agent-use-case-profile.csv`.
3. Run `scripts/profile_builder.py` to generate a starter risk profile and recommended governance posture.
4. Translate the script outputs into:
   - a recommended deployment tier
   - required boundaries
   - required oversight mode
   - pre-deployment conditions
5. If the use case is high-impact or hard to reverse, recommend **go with conditions**, **hold**, or **do not deploy** unless strong controls are already present.

## Bounded autonomy workflow

Use this when the user asks for autonomy limits, permission models, tool restrictions, or control boundaries.

1. Use the following design lenses from the IMDA framework:
   - action-space
   - autonomy
   - tool and system access
   - read vs write authority
   - reversibility of actions
   - identity and authorisation model
2. Start from `assets/templates/bounded-autonomy-and-permissions-matrix.csv`.
3. Specify:
   - which tools are allowed
   - which data stores are reachable
   - which actions require human approval
   - when the agent must be sandboxed or isolated
   - when the agent must be disabled or taken offline
4. If the user asks for policy language, draft policy clauses plus the control matrix.
5. For high-risk cases, require named approval gates and an explicit residual-risk decision.

## Accountability workflow

Use this when the user needs a RACI, role split, value-chain allocation, or board/accountability memo.

1. Use `references/accountability-roles.csv` and `assets/templates/human-accountability-raci.csv`.
2. Allocate responsibilities across:
   - key decision makers
   - product teams
   - cybersecurity teams
   - legal/compliance/risk teams where relevant
   - users or business operators
   - external parties such as model developers, tooling providers, or SaaS providers
3. Make adaptive governance explicit: identify who revisits policies when the agent changes, expands scope, or fails in production.
4. Always specify escalation contacts and ownership for incident decisions, overrides, and shutdown authority.

## Oversight workflow

Use this when the user asks for human-in-the-loop design, approvals, overrides, or meaningful human control.

1. Determine the intended oversight mode using `references/oversight-modes.csv`.
2. Start from `assets/templates/human-oversight-plan.md`.
3. Define:
   - significant checkpoints requiring human approval
   - conditions for intervention or pause
   - audit method for verifying that approvals remain effective over time
   - automated monitoring that complements human oversight
4. Explicitly address automation bias when the agent has performed reliably in the past.
5. If the task is high-stakes or irreversible, default to stronger approval checkpoints.

## Operationalisation workflow

Use this when the user needs test plans, rollout plans, monitoring plans, or shutdown criteria.

1. Use `assets/templates/pre-deployment-readiness-checklist.md` for readiness and test planning.
2. Use `assets/templates/phased-rollout-and-monitoring-plan.md` for rollout and monitoring.
3. Include the following test dimensions where relevant:
   - overall task execution
   - policy compliance
   - tool calling accuracy
   - robustness to errors and edge cases
   - workflow-level testing across multiple steps
   - multi-agent interaction testing if agents collaborate
   - realistic-environment testing calibrated against real-world risk
4. Include deployment safeguards:
   - phased rollout
   - real-time monitoring
   - kill switch or containment trigger
   - deactivation or disengagement criteria
5. If the user asks for an incident or shutdown approach, also use `assets/templates/incident-escalation-log.csv` and `assets/templates/residual-risk-acceptance-memo.md`.

## End-user responsibility workflow

Use this when the user needs user notices, training material, or operational guidance for staff using agents.

1. Start from `assets/templates/end-user-transparency-and-training-plan.md`.
2. Inform users about:
   - the agent’s range of actions
   - its access to data and systems
   - the user’s own responsibilities
   - human contact points for dissatisfaction, malfunction, or escalation
3. For users integrating agents into work processes, also include training on:
   - agent use cases and restrictions
   - prompting or instruction practices
   - common failure modes
   - effective oversight
   - preserving foundational tradecraft and domain skills
4. If the user base is external, tighten transparency, escalation, and communication requirements.

## Gap-analysis workflow

Use this when the user wants a readiness assessment, maturity rating, or remediation plan.

1. Copy `assets/templates/agentic-governance-gap-questionnaire.csv` and fill the `score`, `evidence`, and `notes` columns.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review the generated outputs and convert them into a board-ready summary:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `governance_profile.csv`
4. If needed, tailor the priorities for the specific audience:
   - ciso → operational controls, monitoring, evidence, residual risk
   - chief risk officer → risk appetite, controls, acceptance, escalation
   - legal counsel → documentation, accountability, approvals, notice and recourse

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter governance profile from an agent use-case CSV
- `scripts/gap_analysis.py`
  - convert a scored questionnaire into priorities and a governance profile
- `scripts/control_lookup.py`
  - search the control library, factor tables, and role tables

## Resource map

- `references/implementation-workflows.md`
  - detailed workflow and decision rules
- `references/imda-agentic-governance-dimensions.csv`
  - four-dimension control library
- `references/agentic-risk-factors.csv`
  - impact and likelihood factors for use-case suitability
- `references/agentic-risk-outcomes.csv`
  - common harmful outcomes to evaluate
- `references/oversight-modes.csv`
  - human involvement modes and recommended use
- `references/accountability-roles.csv`
  - internal and external responsibility patterns
- `references/how-the-skill-uses-the-sources.md`
  - source hierarchy and intended use
- `references/publication-and-copyright-boundaries.md`
  - public-package restrictions

## Final quality check

Before finalising an output:
- verify that every recommendation has an owner and evidence artifact
- verify that autonomy, tools, data access, and external-system access are stated explicitly
- verify that human checkpoints and shutdown authority are named
- verify that residual risk is addressed, not ignored
- verify that the result is usable by a ciso, chief risk officer, or legal counsel without further restructuring
