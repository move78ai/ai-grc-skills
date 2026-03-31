---
name: ai-system-inventory-shadow-ai-discovery
description: "Workflow-first inventory support for sanctioned and unsanctioned AI systems, ownership mapping, dependency capture, and risk tiering."
---

# AI System Inventory Shadow AI Discovery

Use this skill to turn AI inventory and shadow-AI questions into working governance artifacts, not summaries.






Default audience: Enterprise architects, compliance leads, security teams, IT operations, procurement owners, and risk operators responsible for AI inventory accuracy.

Default style: Evidence-led, operational, and explicit about discovery methods, ownership, dependencies, and remediation priorities.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the task type.
   - **Build or refresh an enterprise AI inventory** → follow **Inventory build workflow**.
   - **Find, scope, or govern unsanctioned AI usage** → follow **Shadow AI discovery workflow**.
   - **Classify AI systems by purpose, impact, and control requirements** → follow **Classification and risk-tiering workflow**.
   - **Map business, technical, and control ownership** → follow **Ownership and accountability workflow**.
   - **Document data, vendors, models, and integrations** → follow **Dependency and data workflow**.
   - **Prepare remediation, exception handling, or attestations** → follow **Remediation and attestation workflow**.
   - **Run a structured gap analysis** → use `scripts/gap_analysis.py` with `assets/templates/ai-inventory-gap-questionnaire.csv`.
   - **Generate a starter profile for one or more systems** → use `scripts/profile_builder.py` with `assets/templates/ai-system-intake-register.csv`.
   - **Search the bundled control and taxonomy tables** → use `scripts/control_lookup.py`.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and proceed.
   If discovery data is incomplete, record assumptions, identify evidence gaps, and continue. Do not block on perfect source data.

## Core operating rules

- Treat the NIST AI RMF inventory and governance model as the primary operating anchor for inventory design, evidence expectations, and lifecycle control.
- Treat ISO 42001 lifecycle scope, accountability, risk-source, and documentation concepts as complementary structure for inventory fields and control expectations.
- Treat shadow AI as a governance and operational exposure, not just a policy violation. Capture the business driver, not only the control gap.
- Maintain separation between **sanctioned**, **tolerated but unapproved**, **under review**, **prohibited**, and **decommissioned** states.
- Distinguish **AI systems**, **AI-enabled features**, **AI models/services**, **embedded AI in third-party products**, and **personal productivity tooling**. Do not collapse all of these into one bucket.
- Prefer full-scope inventories. If the available inventory is partial, state that clearly and identify the missing discovery channels.
- Require named ownership for every in-scope system: business owner, technical owner, risk/compliance contact, procurement/vendor contact if third-party, and review authority where relevant.
- Require evidence language. For every recommendation, specify the artifact, log, register, approval record, or control evidence that would prove implementation.
- When the user asks for a deployment or retention decision, conclude with one of: **retain and monitor**, **approve with conditions**, **move to review**, **restrict**, or **decommission**.
- When regulatory implications are raised, describe inventory and documentation implications, but do not present legal advice as definitive.
- Do not reproduce copyrighted source documents or long verbatim extracts. Use derivative summaries, tables, scripts, and templates only.

## Default output structure

Unless the user requests a different structure, use this format:

# [title]

## 1. executive summary
- inventory scope
- current posture
- most material blind spots
- immediate decisions required

## 2. inventory scope and assumptions
- business units covered
- geographies covered
- discovery channels used
- systems excluded and why

## 3. key findings
- sanctioned systems
- shadow ai findings
- high-risk or high-dependency systems
- ownership gaps
- data and vendor exposure

## 4. required controls and artifacts
| area | required control or artifact | owner | evidence |
|---|---|---|---|

## 5. prioritized action plan
| priority | action | owner | target timing | dependency |
|---|---|---|---|---|

## 6. residual risk and recommended decision
- remaining blind spots
- temporary compensating controls
- attestation or review requirement
- recommended decision

Adapt this structure when a template in `assets/templates/` is a better fit.

## Inventory build workflow

Use this when the user wants to create or refresh the enterprise AI inventory.

1. Define the inventory scope:
   - enterprise-wide or business-unit specific
   - production systems, pilots, proofs of concept, and employee productivity tooling
   - internal builds, third-party SaaS, embedded vendor features, APIs, model endpoints, and agentic tools
2. Start from `assets/templates/ai-system-inventory-master-register.csv` and `assets/templates/ai-system-intake-register.csv`.
3. Capture minimum fields:
   - system name, owner, purpose, deployment stage, sanctioned status
   - model or provider type
   - data sensitivity and access type
   - integration scope and external systems touched
   - user groups and geographic reach
   - risk tier, review cadence, and evidence status
4. Use `scripts/profile_builder.py` to generate a starter classification and control posture from the intake register.
5. Translate results into:
   - inventory completeness statement
   - high-priority review list
   - missing-owner list
   - systems requiring restriction, approval, or remediation

## Shadow AI discovery workflow

Use this when the user wants to identify or govern unsanctioned AI use.

1. Define discovery channels using `references/discovery-methods-and-evidence.csv`.
2. Start from `assets/templates/shadow-ai-discovery-questionnaire.csv` and `assets/templates/discovery-sources-log.csv`.
3. Evaluate evidence from channels such as:
   - procurement and expense signals
   - identity and SSO application discovery
   - endpoint or browser telemetry where lawful and available
   - network or CASB logs where lawful and available
   - software safelist exceptions and browser extension reviews
   - department interviews and self-reporting campaigns
   - legal, privacy, and information-security incident reviews
4. Classify each finding as:
   - sanctioned
   - tolerated but unapproved
   - under review
   - prohibited
   - decommissioned
5. For each shadow AI finding, document:
   - why users adopted it
   - whether sensitive data is being entered
   - whether outputs influence decisions or customer-facing work
   - whether the tool has third-party retention, training, or sharing risk
6. Produce:
   - shadow-ai finding log
   - immediate containment list
   - review queue for business/legal/security
   - remediation backlog

## Classification and risk-tiering workflow

Use this when the user asks how to classify AI systems or prioritize reviews.

1. Use `references/system-classification-taxonomy.csv`, `references/data-and-access-sensitivity-taxonomy.csv`, and `references/risk-tiering-model.csv`.
2. Classify each system across:
   - system archetype
   - sanctioned state
   - lifecycle stage
   - impact on individuals or customers
   - autonomy or decision influence
   - data sensitivity
   - vendor dependency and lock-in
   - write access or external-system action capability
3. Use `assets/templates/ai-risk-tiering-worksheet.csv`.
4. Apply the following posture logic:
   - **tier 1** → basic inventory and annual review
   - **tier 2** → inventory plus owner validation and quarterly review
   - **tier 3** → risk review, legal/privacy/security sign-off, evidence pack, quarterly review
   - **tier 4** → executive approval, enhanced monitoring, exception governance, possible no-go or containment
5. Where shadow AI uses sensitive data, significant external access, or customer-impacting outputs, default to **move to review** or **restrict** pending formal approval.

## Ownership and accountability workflow

Use this when ownership is unclear or fragmented across teams.

1. Start from `assets/templates/ai-owner-and-raci-matrix.csv`.
2. Assign at minimum:
   - business owner
   - technical owner
   - security contact
   - legal or compliance contact where relevant
   - privacy contact where personal data is involved
   - vendor or procurement contact for third-party systems
   - executive review owner for higher tiers
3. If there is no accountable owner, treat the system as not governance-ready.
4. For shadow AI, require a named decision owner for one of these actions:
   - approve and onboard
   - approve with restrictions
   - replace with sanctioned alternative
   - prohibit and contain
   - decommission

## Dependency and data workflow

Use this when documenting data, models, vendors, or integrations.

1. Start from `assets/templates/data-dependency-and-access-register.csv`.
2. Record:
   - provider, model family, API or service type
   - training or retention statements if known
   - contractual status and review status
   - inbound data types and outbound destinations
   - identities, permissions, and integrations
   - whether the tool can write, transact, or trigger downstream changes
3. Use `references/crosswalk-to-nist-ai-rmf.csv`, `references/crosswalk-to-iso42001.csv`, and `references/crosswalk-to-colorado-ai-act.csv` to identify additional evidence requirements.
4. Escalate any system with unknown vendor terms, unknown data retention, or unapproved external sharing.

## Remediation and attestation workflow

Use this when the organisation wants to close gaps, manage exceptions, or run periodic attestation.

1. Use `scripts/gap_analysis.py` to generate a prioritised action list.
2. Start from `assets/templates/shadow-ai-remediation-backlog.csv`, `assets/templates/quarterly-ai-attestation-log.csv`, and `assets/templates/exception-and-restriction-memo.md`.
3. Convert findings into actions with:
   - owner
   - control objective
   - evidence required
   - due date
   - escalation path
4. For periodic attestations, require each owner to confirm:
   - the inventory entry is still accurate
   - usage remains within approved scope
   - no new sensitive data or integrations were added without review
   - review dates, incidents, and approvals are current
5. For exceptions, state:
   - why the system remains in use
   - compensating controls
   - expiry date of the exception
   - approval authority

## Bundled resources

### Scripts
- `scripts/gap_analysis.py` — score the inventory program questionnaire and generate a prioritised remediation output.
- `scripts/profile_builder.py` — convert an intake register into starter classifications, review urgency, and control expectations.
- `scripts/control_lookup.py` — search the bundled control, taxonomy, and crosswalk tables.

### References
- `references/implementation-workflows.md` — compact procedural workflows for inventory, discovery, classification, ownership, and remediation.
- `references/how-the-skill-uses-the-sources.md` — source handling and design logic.
- `references/publication-and-copyright-boundaries.md` — what can and cannot be redistributed.
- `references/inventory-control-library.csv` — core inventory control objectives and evidence expectations.
- `references/shadow-ai-indicators.csv` — typical signals that point to unsanctioned or ungoverned AI use.
- `references/system-classification-taxonomy.csv` — system types and inventory buckets.
- `references/data-and-access-sensitivity-taxonomy.csv` — data and access classification anchors.
- `references/risk-tiering-model.csv` — tier logic and review expectations.
- `references/discovery-methods-and-evidence.csv` — discovery channels and what each can prove.
- `references/crosswalk-to-nist-ai-rmf.csv` — relevant NIST AI RMF and Playbook anchors.
- `references/crosswalk-to-iso42001.csv` — relevant ISO 42001 scoping, lifecycle, accountability, and risk anchors.
- `references/crosswalk-to-colorado-ai-act.csv` — inventory implications for high-risk system review and impact assessment readiness.
- `references/executive-metrics-catalog.csv` — reporting metrics for CISO/CRO/legal and board summaries.

### Assets and templates
- `assets/templates/ai-system-inventory-master-register.csv`
- `assets/templates/ai-system-intake-register.csv`
- `assets/templates/shadow-ai-discovery-questionnaire.csv`
- `assets/templates/discovery-sources-log.csv`
- `assets/templates/sanctioned-status-review-log.csv`
- `assets/templates/ai-owner-and-raci-matrix.csv`
- `assets/templates/data-dependency-and-access-register.csv`
- `assets/templates/ai-risk-tiering-worksheet.csv`
- `assets/templates/ai-inventory-gap-questionnaire.csv`
- `assets/templates/shadow-ai-remediation-backlog.csv`
- `assets/templates/quarterly-ai-attestation-log.csv`
- `assets/templates/executive-inventory-summary-memo.md`
- `assets/templates/exception-and-restriction-memo.md`
- `assets/templates/system-decommission-record.md`

## Output expectations

- Make outputs decision-ready for CISO, CRO, and legal review.
- Separate confirmed facts, inferred facts, and unknowns.
- Prefer tables, registers, and memos over narrative explanation.
- When discovery is incomplete, explicitly say the inventory is partial and list the discovery gaps.
- When a system influences consequential decisions or handles sensitive data, recommend enhanced review rather than light-touch treatment.
