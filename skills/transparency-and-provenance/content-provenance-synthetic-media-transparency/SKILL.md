---
name: content-provenance-synthetic-media-transparency
description: "Workflow-first provenance and transparency guidance for media workflows, synthetic content labels, supplier checks, and rollout planning."
---

# Content Provenance / Synthetic Media Transparency

Use this skill to turn provenance and transparency questions into working governance artifacts, not summaries.






Default audience: Trust and safety leads, product teams, communications, marketing operations, legal counsel, security, and governance operators managing media workflows.

Default style: Decision-led, rollout-aware, and explicit about disclosure triggers, credential choices, owners, and monitoring conditions.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the task type.
   - **Classify a media, publishing, or AI-generation workflow** -> follow **Workflow classification workflow**.
   - **Decide when provenance, disclosure, or content credentials are needed** -> follow **Disclosure and credentialing workflow**.
   - **Design or assess a provenance rollout program** -> follow **Rollout and operating-model workflow**.
   - **Assess a third-party platform, model, or supplier** -> follow **Supplier capability workflow**.
   - **Prepare evidence, review, or executive outputs** -> follow **Evidence and review workflow**.
   - **Run a structured gap analysis** -> use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Build a starter provenance profile** -> use `scripts/profile_builder.py` with the system profile template.
   - **Search control, evidence, or scenario libraries** -> use `scripts/provenance_lookup.py`.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and proceed.
   If important facts are missing, infer the most likely operating context, label the assumptions, and continue.

## Core operating rules

- Treat provenance and transparency as operational controls, not only public-relations signals.
- Separate the object in scope: asset, campaign, model output, editing workflow, media pipeline, publishing platform, or supplier capability.
- Distinguish between provenance capture, provenance preservation, provenance verification, user-facing disclosure, and downstream monitoring.
- Require explicit decisions on when content credentials, metadata preservation, visible disclosures, or manual review are needed.
- Record unknown fields explicitly as `unknown` rather than inferring them.
- For consequential, public-facing, or high-reach synthetic media, require evidence that the process could withstand legal, trust-and-safety, audit, or executive review.
- Distinguish policy language from actual technical and workflow implementation.
- When the user asks for a decision, conclude with one of: **proceed**, **proceed with conditions**, **hold pending remediation**, **restricted use only**, or **do not proceed**.
- Do not reproduce copyrighted source documents or gated material. Use derivative tables, templates, and implementation guidance only.

## Default output structure

Unless the user requests another format, use this structure:

# [title]

## 1. executive summary
- scope reviewed
- provenance and transparency posture
- decision recommendation
- key blockers or conditions

## 2. media and workflow context
- content type and use case
- creation and editing flow
- publication or distribution environment
- supplier and tooling dependencies

## 3. control and transparency findings
| area | current state | target state | owner | priority |
|---|---|---|---|---|

## 4. evidence and operating requirements
| artifact | why it is needed | owner | timing |
|---|---|---|---|

## 5. prioritized action plan
| priority | action | owner | due date | dependency |
|---|---|---|---|---|

## 6. decision and next review point
- approval status
- conditions or restrictions
- monitoring and review cadence
- residual-risk note

## Workflow classification workflow

Use this when the user needs to classify a media workflow or understand provenance and transparency obligations.

1. Start from `assets/templates/media-workflow-profile.md`.
2. Identify:
   - content type
   - whether content is fully synthetic, partially synthetic, edited, or non-synthetic
   - distribution channel and audience
   - public impact, reputational reach, or regulatory sensitivity
   - whether the workflow preserves, strips, or transforms metadata
3. Use `references/media-workflow-scenarios.csv` and `references/provenance-control-domains.csv`.
4. Output a classified workflow plus the minimum control and disclosure posture.

## Disclosure and credentialing workflow

Use this when the user needs to decide whether content credentials, visible labels, internal disclosures, or verification steps are needed.

1. Start from `assets/templates/disclosure-decision-log.csv`.
2. Use `references/disclosure-and-labeling-scenarios.csv` and `references/credential-verification-statuses.csv`.
3. Decide:
   - when content credentials should be attached
   - when visible disclosure is needed
   - when manual review is needed before release
   - when downstream verification or exception handling is needed
4. If third-party tools or platforms are involved, continue into the supplier capability workflow.

## Rollout and operating-model workflow

Use this when the user needs a provenance operating model, rollout sequence, or governance plan.

1. Start from:
   - `assets/templates/content-credential-rollout-plan.md`
   - `assets/templates/provenance-evidence-checklist.csv`
   - `assets/templates/media-claim-review-register.csv`
2. Use `references/implementation-workflows.md` and `references/evidence-catalog.csv`.
3. Define:
   - owners for creation, editing, publishing, verification, and escalation
   - technical and workflow controls for credential attachment and preservation
   - review gates for high-risk or public-interest content
   - exceptions, fallback handling, and monitoring
4. End with a phased rollout decision.

## Supplier capability workflow

Use this when the user is evaluating a third-party model, platform, editing tool, media host, or agency.

1. Start from `assets/templates/third-party-provenance-evidence-request.md`.
2. Assess:
   - support for provenance capture and preservation
   - support for content credentials or equivalent records
   - metadata retention behavior across editing and publishing steps
   - verification and exception-handling capability
   - contract, SLA, and audit evidence implications
3. Record the result in `assets/templates/media-claim-review-register.csv` if supplier claims need validation.
4. End with **proceed**, **proceed with conditions**, **hold pending remediation**, or **do not proceed**.

## Evidence and review workflow

Use this when the user asks for audit support, executive review, legal review, or incident-ready documentation.

1. Start from:
   - `assets/templates/executive-transparency-memo.md`
   - `assets/templates/residual-risk-acceptance-memo.md`
   - `assets/templates/incident-escalation-log.csv`
2. Use `references/evidence-catalog.csv` and `references/framework-crosswalk.csv`.
3. Tie every recommendation to:
   - owner
   - process or system location
   - evidence artifact
   - review cadence
4. For gaps, assign remediation dates and accountable owners.
5. End with a named next review point.

## Gap-analysis workflow

Use this when the user wants a maturity score, remediation plan, or current-state assessment.

1. Copy `assets/templates/provenance-gap-questionnaire.csv` and fill the `score`, `evidence`, and `notes` columns.
2. Run:
   `python scripts/gap_analysis.py <input_csv>`
3. Convert the output into a decision-ready summary for the user's audience:
   - ciso -> control coverage, verification, supplier and monitoring gaps
   - chief risk officer -> material exposure, residual risk, conditions to proceed
   - legal counsel -> disclosure, recordkeeping, review, and escalation implications
   - trust and safety / communications -> release conditions, labeling, claims governance, exception handling

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter provenance and transparency profile
- `scripts/gap_analysis.py`
  - summarize a scored gap questionnaire into priorities and action items
- `scripts/provenance_lookup.py`
  - search the control, evidence, and scenario libraries

## Resource map

### references/
- `implementation-workflows.md` -> compact summary of repeatable workflows in this skill
- `how-the-skill-uses-the-sources.md` -> explains source grounding and public-package boundaries
- `publication-and-copyright-boundaries.md` -> public-distribution safety note
- `provenance-control-domains.csv` -> derivative control domains for provenance and transparency
- `media-workflow-scenarios.csv` -> common media and synthetic-content scenarios
- `disclosure-and-labeling-scenarios.csv` -> disclosure and label decision patterns
- `credential-verification-statuses.csv` -> verification and exception statuses
- `evidence-catalog.csv` -> evidence types and what they demonstrate
- `framework-crosswalk.csv` -> mapping to genai risk, governance, supplier risk, incident, and oversight themes

### assets/templates/
- `media-workflow-profile.md`
- `provenance-gap-questionnaire.csv`
- `disclosure-decision-log.csv`
- `content-credential-rollout-plan.md`
- `provenance-evidence-checklist.csv`
- `third-party-provenance-evidence-request.md`
- `media-claim-review-register.csv`
- `incident-escalation-log.csv`
- `executive-transparency-memo.md`
- `residual-risk-acceptance-memo.md`

## Final checks before answering

Before finalizing a recommendation, check that the output answers these questions:
- what content, workflow, or media pipeline is in scope?
- what provenance and disclosure posture is required now?
- what evidence exists and what is missing?
- who owns creation, review, verification, and escalation?
- what is the decision and what must happen before the next review?
