---
name: ai-incident-management-incident-disclosure
description: workflow-first ai incident management and incident disclosure support. use when chatgpt needs to design or review ai incident response programs, classify ai incidents, triage severity, assign escalation paths, build disclosure decision records, prepare stakeholder notice drafts, run after-action reviews, track near-misses and harmful impacts, or convert nist ai rmf, nist ai 600-1, and adjacent governance expectations into concrete incident artifacts for ciso, cro, legal, audit, compliance, product, or engineering stakeholders.
---

# AI Incident Management / Incident Disclosure

## Overview

Use this skill to turn incident response expectations into concrete operator artifacts. Focus on detection, classification, containment, escalation, disclosure, recovery, evidence preservation, and lessons learned.

## Workflow decision tree

1. Determine the request type:
   - **Need a full incident management operating package?** -> Run the **Incident program workflow**.
   - **Need help triaging a live or hypothetical incident?** -> Run the **Incident triage and disclosure workflow**.
   - **Need post-incident review and improvement actions?** -> Run the **After-action workflow**.
   - **Need a gap assessment?** -> Run the **Gap analysis workflow**.
   - **Need a quick lookup of incident controls, severity rules, or disclosure factors?** -> Run the **Control lookup workflow**.

2. Default output expectation:
   - Build outputs for executive and control stakeholders, not for general education.
   - Prefer structured artifacts over narrative explanation.
   - Always show: incident scope, severity rationale, affected parties, containment status, escalation path, disclosure logic, unresolved issues, and required next actions.

## Incident program workflow

Use when the user needs to stand up or improve an organizational AI incident management capability.

1. Build the operating profile.
   - Use `assets/templates/incident-program-profile.md`.
   - Capture system scope, deployment footprint, user populations, likely harm types, regulatory context, and critical dependencies.
2. Define the incident taxonomy.
   - Use `references/incident-taxonomy.csv` and `references/severity-decision-rules.csv`.
   - Cover security, privacy, harmful content, discrimination, safety, integrity, availability, autonomy failure, oversight failure, and supplier incidents.
3. Define roles and decision rights.
   - Use `references/stakeholder-notification-map.csv` and `assets/templates/escalation-and-notification-matrix.csv`.
   - Specify the incident commander, technical lead, legal/compliance lead, communications lead, business owner, and approver for external notices.
4. Define detection, intake, and evidence preservation.
   - Use `assets/templates/incident-intake-form.md`, `assets/templates/evidence-preservation-checklist.md`, and `assets/templates/near-miss-and-error-log.csv`.
5. Define escalation, containment, and service actions.
   - Require criteria for deactivation, rollback, user access suspension, model withdrawal, feature restriction, or compensating controls.
6. Define disclosure logic.
   - Use `references/disclosure-decision-factors.csv` and `assets/templates/disclosure-decision-memo.md`.
   - Distinguish internal reporting, customer notification, impacted-person communication, regulator notice, and voluntary public transparency reporting.
7. Define learning and continuous improvement.
   - Use `assets/templates/after-action-review.md`, `assets/templates/remediation-tracker.csv`, and `assets/templates/incident-trend-dashboard.csv`.
8. Produce the final package.
   - Output a program structure plus artifact list and decision governance.

## Incident triage and disclosure workflow

Use when the user needs to assess a live or hypothetical incident.

1. Capture incident facts.
   - Use `assets/templates/incident-intake-form.md`.
   - Record system, version, date/time, detection source, affected populations, evidence available, and immediate business or user impact.
2. Classify the incident.
   - Use `references/incident-taxonomy.csv`.
   - Select all relevant categories rather than forcing a single label.
3. Assess severity.
   - Use `references/severity-decision-rules.csv` and `assets/templates/incident-severity-matrix.csv`.
   - Consider impact magnitude, reversibility, scope, legal exposure, recurrence likelihood, and urgency.
4. Determine immediate actions.
   - Use `assets/templates/escalation-and-notification-matrix.csv`.
   - Specify containment, rollback, access restrictions, overrides, user support, and executive notification.
5. Evaluate disclosure obligations and choices.
   - Use `references/disclosure-decision-factors.csv` and `assets/templates/disclosure-decision-memo.md`.
   - State what is known, what is not yet known, who might need to be informed, and who has approval authority.
6. Draft communications.
   - Use `assets/templates/stakeholder-notice-draft.md` and `assets/templates/incident-board-briefing.md` if the audience includes customers, regulators, affected parties, or executives.
7. Document next actions.
   - Create immediate containment actions, required evidence collection, remediation steps, and follow-up dates.

## After-action workflow

Use when the user needs a post-incident review and improvement package.

1. Build the timeline and facts base.
   - Use incident records, evidence log, change history, version history, and communications records.
2. Run the after-action review.
   - Use `assets/templates/after-action-review.md`.
   - Cover root cause, detection effectiveness, response timing, communication quality, user harm, disclosure adequacy, and controls that failed or were absent.
3. Update issue tracking.
   - Use `assets/templates/remediation-tracker.csv` and `assets/templates/lessons-learned-register.csv`.
4. Update program artifacts.
   - Revise severity rules, escalation paths, detection sources, playbooks, training requirements, and disclosure templates where needed.
5. Produce an executive summary.
   - Use `assets/templates/incident-board-briefing.md` if executive or board escalation is needed.

## Gap analysis workflow

Use when the user wants to assess whether an existing incident management setup is sufficient.

1. Use `assets/templates/incident-gap-questionnaire.csv` as the input structure.
2. Run:
   - `python scripts/gap_analysis.py assets/templates/incident-gap-questionnaire.csv`
   - or point it to a completed CSV supplied by the user.
3. Convert the output into four sections:
   - Executive summary
   - Highest-priority gaps
   - Required remediation actions
   - Required evidence before relying on the current incident process
4. Rate findings using a simple RAG logic unless the user gives another scoring model.
5. Distinguish between:
   - governance and roles gaps
   - intake and evidence gaps
   - containment and recovery gaps
   - disclosure and communication gaps
   - after-action and continual improvement gaps

## Control lookup workflow

Use when the user needs quick support mapping an incident question to a control or artifact.

1. Run `python scripts/control_lookup.py <keyword>`.
2. Use `references/incident-taxonomy.csv`, `references/severity-decision-rules.csv`, `references/nist-incident-anchors.csv`, `references/disclosure-decision-factors.csv`, and `references/stakeholder-notification-map.csv`.
3. Return short, decision-useful guidance plus the matching artifact to produce.

## Operating rules

- Treat AI incidents as socio-technical events, not only technical failures. Include user impact, stakeholder communication, and governance response.
- Always separate confirmed facts from assumptions, hypotheses, and pending verification.
- Prefer explicit triage criteria and decision thresholds over vague severity labels.
- Always identify who can authorize containment, external notices, deactivation, and service restoration.
- Include near-misses and harmful-but-not-yet-reportable events in the operating record.
- When the request involves GenAI, explicitly cover harmful content, data leakage, provenance or authenticity issues, jailbreak or prompt-manipulation scenarios, plugin or connector risks, and downstream distribution effects.
- When third parties are involved, include vendor coordination, evidence requests, contract notice requirements, and shared-response dependencies.
- Always state limitations, open issues, residual risks, and follow-up deadlines.
- Do not reproduce copyrighted source text. Use original wording, derivative tables, and artifact templates only.

## Default report structure

Use this exact structure unless the user asks for another format:

# [Incident or Program Name] AI Incident Assessment

## Executive summary
- incident or program scope
- severity position
- current containment status
- disclosure recommendation

## Facts and scope
- systems and versions involved
- affected users or stakeholders
- timeline and detection source
- known dependencies and third parties

## Severity and impact assessment
- incident categories
- harm types and magnitude
- reversibility and spread
- legal or contractual sensitivity

## Response status
- containment actions taken
- escalation status
- communications sent or pending
- evidence preserved

## Disclosure and decision gates
- who may need notice
- what is confirmed versus pending
- approval authority
- no-go or deactivation triggers

## Root cause or working hypothesis
- confirmed cause or current hypothesis
- control failures
- unresolved questions

## Required next actions
1. immediate actions
2. disclosure or communication actions
3. remediation and monitoring actions
4. after-action review actions

## Resources in this skill

### Scripts
- `scripts/gap_analysis.py` - converts a completed incident questionnaire CSV into a prioritized markdown gap report.
- `scripts/profile_builder.py` - creates an incident program profile markdown file from CLI inputs.
- `scripts/control_lookup.py` - searches incident control and disclosure references by keyword.

### References
- `references/incident-taxonomy.csv` - incident categories, likely harm types, and default response lenses.
- `references/severity-decision-rules.csv` - severity criteria, escalation triggers, and default actions.
- `references/disclosure-decision-factors.csv` - decision factors for internal, customer, impacted-party, regulator, and public notifications.
- `references/stakeholder-notification-map.csv` - common stakeholder groups and what each needs to know.
- `references/nist-incident-anchors.csv` - derivative NIST-aligned expectations and action anchors.
- `references/publication-and-copyright-boundaries.md` - public distribution boundaries.

### Templates
- `assets/templates/incident-program-profile.md`
- `assets/templates/incident-gap-questionnaire.csv`
- `assets/templates/incident-intake-form.md`
- `assets/templates/incident-severity-matrix.csv`
- `assets/templates/escalation-and-notification-matrix.csv`
- `assets/templates/disclosure-decision-memo.md`
- `assets/templates/stakeholder-notice-draft.md`
- `assets/templates/evidence-preservation-checklist.md`
- `assets/templates/near-miss-and-error-log.csv`
- `assets/templates/after-action-review.md`
- `assets/templates/remediation-tracker.csv`
- `assets/templates/lessons-learned-register.csv`
- `assets/templates/incident-board-briefing.md`
- `assets/templates/incident-trend-dashboard.csv`
