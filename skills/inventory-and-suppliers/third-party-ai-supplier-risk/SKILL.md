---
name: third-party-ai-supplier-risk
description: comprehensive workflow skill for assessing, approving, contracting, monitoring, and offboarding third-party ai providers, foundation models, datasets, APIs, embedded ai components, and ai-enabled service suppliers. use when chatgpt needs to run supplier due diligence, build an approved-provider register, request missing evidence, score vendor risk, draft ai-specific contract and sla controls, design fallback and exit plans, monitor third-party ai trustworthiness over time, or perform a structured supplier-risk gap analysis for ciso, chief risk officer, legal counsel, procurement, compliance, security, and platform teams.
---

# Third-Party AI / Supplier Risk

Use this skill to turn vendor, model, API, and supplier-risk questions into working artifacts, not summaries.

Default audience: ciso, chief risk officer, legal counsel, procurement, compliance, security, platform engineering, data governance, and operational owners.

Default style: detailed, comprehensive, and actionable. Prefer decision-ready outputs, named owners, evidence requests, contract terms, monitoring requirements, and contingency plans.

## Workflow decision tree

1. Determine the task type.
   - **Assess a new vendor, model, API, dataset, or AI-enabled service** → follow **Supplier intake and approval workflow**.
   - **Request missing evidence or evaluate documentation quality** → follow **Evidence request workflow**.
   - **Draft contract, addendum, or SLA controls** → follow **Contract and SLA workflow**.
   - **Set up monitoring, re-review, or release-change review** → follow **Ongoing monitoring workflow**.
   - **Design fallback, redundancy, incident handling, or exit steps** → follow **Contingency and exit workflow**.
   - **Run a readiness or maturity assessment** → use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Score one supplier and generate a starter risk profile** → use `scripts/profile_builder.py` with the vendor intake profile template.
   - **Search the supplier-control library** → use `scripts/control_lookup.py`.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly wants prose only.

3. State assumptions and proceed.
   If details are missing, make reasonable assumptions, label them, and continue.

## Core operating rules

- Treat third-party ai as a lifecycle risk, not merely a procurement question.
- Separate the object being assessed: provider, model, api, dataset, toolchain component, embedded service, or sub-processor.
- Always identify what decisions, workflows, or user impacts the third-party ai influences.
- Require evidence proportionate to risk. High-impact or hard-to-replace suppliers need stronger documentation, monitoring, contractual protections, and fallback plans.
- Assess the full dependency stack where relevant: provider, model, dataset origin, hosting environment, sub-processors, and downstream integrations.
- Ask for both current-state evidence and ongoing-change commitments, such as incident notification, release notice, model changes, retraining changes, and support obligations.
- Distinguish between direct trustworthiness risk and supplier-operational risk. A vendor can have a capable model but weak notification, transparency, or support practices.
- Where the supplier refuses material transparency or hampers risk mapping, treat that as a risk signal rather than a neutral omission.
- When the user asks whether to proceed, conclude with one of: **approve**, **approve with conditions**, **restricted approval**, **hold**, or **do not approve**.
- Do not reproduce copyrighted source documents or long verbatim excerpts. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user requests a different structure, use this format:

# [title]

## 1. executive summary
- supplier and service scope
- risk posture
- approval recommendation
- key blockers, conditions, or gaps

## 2. dependency and use-case profile
- supplier type
- service or model type
- decisions or workflows influenced
- data classes and access level
- sub-processors or fourth-party exposure

## 3. key supplier-risk findings
- transparency and documentation findings
- security and resilience findings
- legal, privacy, and ip findings
- operational dependency findings

## 4. required controls and artifacts
| area | required control or evidence | owner | due date |
|---|---|---|---|

## 5. prioritized action plan
| priority | action | owner | timing | dependency |
|---|---|---|---|---|

## 6. decision and contingency position
- approval status
- fallback or exit requirements
- monitoring cadence
- residual-risk notes

Adapt this structure only when a template in `assets/templates/` is a better fit.

## Supplier intake and approval workflow

Use this when the user asks whether a vendor, model, or provider should be approved.

1. Collect or infer:
   - supplier name and service description
   - supplier type: model provider, API provider, SaaS with embedded AI, data broker, dataset provider, managed service, or tooling component
   - deployment context and user groups
   - whether the supplier affects consequential decisions, customer-facing outputs, security operations, or core internal workflows
   - data classes processed, stored, trained on, or derived
   - access rights: read, write, act, admin, or autonomous execution
   - concentration risk and replaceability
   - availability of documentation, audit reports, test reports, model cards, system cards, data provenance, sub-processor list, and incident policy
2. Start from `assets/templates/vendor-intake-profile.csv` and `assets/templates/supplier-due-diligence-questionnaire.csv`.
3. Run `scripts/profile_builder.py` to generate a starter supplier-risk profile.
4. Use `references/supplier-risk-domains.csv` and `references/supplier-risk-scoring-factors.csv` to refine the assessment.
5. Conclude with one of:
   - approve
   - approve with conditions
   - restricted approval
   - hold
   - do not approve

## Evidence request workflow

Use this when the supplier is missing documentation or the user asks what evidence to request.

1. Start from `assets/templates/evidence-request-pack.csv`.
2. Use `references/supplier-evidence-requests.csv` to tailor requests by supplier type and risk level.
3. Request evidence across the relevant domains:
   - service scope and architecture
   - data provenance and handling
   - model documentation and evaluation
   - privacy, security, and resilience controls
   - sub-processors and supply-chain visibility
   - change management and release notification
   - incident response and support commitments
4. If evidence is refused, incomplete, or materially delayed, flag this as a risk factor in the approval decision.

## Contract and SLA workflow

Use this when the user needs AI-specific terms for a vendor agreement.

1. Start from `assets/templates/contract-and-sla-annex.md`.
2. Use `references/contract-and-sla-controls.csv` to choose clauses for:
   - scope and permitted use
   - data restrictions and retention
   - model change and retraining notice
   - sub-processor disclosure and approval
   - security controls and audit rights
   - support, uptime, and incident notification
   - output ownership, ip, and indemnity allocation
   - decommissioning, transition support, and evidence preservation
3. Match clause strength to the risk posture and criticality of the supplier.
4. For high-risk providers, include explicit notification windows, evidence-delivery duties, and exit assistance expectations.

## Ongoing monitoring workflow

Use this when the user asks how to monitor an approved provider or how to handle updates.

1. Start from `assets/templates/monitoring-and-rereview-log.csv` and `assets/templates/approved-provider-register.csv`.
2. Use `references/ongoing-monitoring-controls.csv` to define:
   - review cadence
   - release and model-change review
   - incident and outage monitoring
   - trustworthiness regression checks
   - policy and sub-processor change review
   - periodic attestation and re-approval triggers
3. If the supplier provides pre-trained models or connected APIs, require recurring review of performance, trustworthiness, and operational dependency.
4. For critical suppliers, specify who monitors advisories, support notices, release notes, and incident disclosures.

## Contingency and exit workflow

Use this when the user needs fallback, redundancy, or supplier-failure planning.

1. Start from `assets/templates/contingency-and-fallback-plan.md` and `assets/templates/decommission-and-exit-checklist.md`.
2. Use `references/contingency-and-exit-controls.csv` to define:
   - service-failure response
   - fallback provider or non-AI alternative
   - evidence preservation steps
   - incident escalation path
   - migration and cutover tasks
   - contract termination triggers
   - post-exit access revocation and data return or deletion
3. For vital or hard-to-replace suppliers, require tested redundancy or manual fallback procedures.
4. If the supplier exceeds risk tolerance and cannot remediate, recommend restriction, replacement, or exit.

## Gap-analysis workflow

Use this when the user wants a maturity score, remediation plan, or supplier-governance current-state assessment.

1. Copy `assets/templates/third-party-ai-gap-questionnaire.csv` and fill the `score`, `evidence`, and `notes` columns.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review the generated outputs and convert them into a decision-ready summary:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `supplier_risk_profile.csv`
4. Tailor the remediation framing by audience:
   - ciso → security, operational dependency, monitoring, incident response
   - chief risk officer → concentration risk, criticality, residual risk, approvals, exit triggers
   - legal counsel → contract clauses, data restrictions, audit rights, ip, evidence preservation
   - procurement → due diligence process, provider register, approval gates, renewal conditions

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter supplier-risk profile from one vendor intake CSV
- `scripts/gap_analysis.py`
  - convert a scored questionnaire into priorities and a supplier-risk posture
- `scripts/control_lookup.py`
  - search the supplier-risk control, evidence, contract, monitoring, and crosswalk libraries

## Resource map

### references/
- `implementation-workflows.md` → compact summary of repeatable supplier-risk workflows in this skill
- `how-the-skill-uses-the-sources.md` → explains source grounding and how to treat cross-framework references
- `publication-and-copyright-boundaries.md` → public-distribution safety note
- `supplier-risk-domains.csv` → standard supplier-risk domains and what to assess in each
- `supplier-risk-scoring-factors.csv` → scoring factors for criticality, replaceability, access, and transparency risk
- `supplier-evidence-requests.csv` → evidence items to request by supplier type and risk scenario
- `contract-and-sla-controls.csv` → clause ideas for contracts, addenda, and SLAs
- `ongoing-monitoring-controls.csv` → monitoring and re-review controls after approval
- `contingency-and-exit-controls.csv` → fallback, redundancy, migration, and exit controls
- `crosswalk-third-party-frameworks.csv` → mapping to NIST AI RMF, NIST Playbook, NIST AI 600-1, cyber ai profile, ISO 42001, and Colorado concepts

### assets/templates/
- `vendor-intake-profile.csv`
- `third-party-ai-gap-questionnaire.csv`
- `supplier-due-diligence-questionnaire.csv`
- `approved-provider-register.csv`
- `evidence-request-pack.csv`
- `contract-and-sla-annex.md`
- `monitoring-and-rereview-log.csv`
- `contingency-and-fallback-plan.md`
- `decommission-and-exit-checklist.md`
- `third-party-ai-risk-register.csv`
- `supplier-decision-memo.md`

## Final checks before answering

Before finalizing a recommendation, check that the output answers these questions:
- what exactly is the third-party ai dependency?
- what decisions, actions, or user impacts does it influence?
- what evidence has been seen and what is still missing?
- what contract or monitoring controls are required?
- what fallback exists if the supplier fails, changes, or becomes unacceptable?
- what is the approval decision and who owns it?
