---
name: colorado-ai-act-impact-assessment
description: "Operator-grade Colorado AI Act workflows for high-risk screening, deployer impact assessments, notices, and retained evidence."
---

# Colorado AI Act Impact Assessment

Use this skill to produce operational compliance artifacts for the Colorado AI Act, not legal summaries.






Default audience: Legal counsel, compliance teams, product owners, privacy leads, and risk operators working on consequential-decision systems.

Default style: Workflow-first, role-aware, and explicit about in-scope use cases, evidence, notices, and review cadence.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the task type.
   - **Screen whether a system is likely in scope / high-risk** → follow **High-risk screening workflow**.
   - **Prepare or update a deployer impact assessment** → follow **Impact-assessment workflow**.
   - **Design or review the deployer risk management policy and program** → follow **Risk-management-policy workflow**.
   - **Prepare consumer-facing disclosures or adverse-decision notices** → follow **Consumer-disclosure workflow**.
   - **Assess developer documentation and evidence sufficiency** → follow **Developer-documentation workflow**.
   - **Prepare annual review, modification review, or incident-notice materials** → follow **Monitoring-and-incident workflow**.
   - **Run a structured readiness or gap analysis** → use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Run a high-risk screening or exemption screen** → use `scripts/classify_use_case.py` with the screening questionnaire template.
   - **Search the duty map, screening rules, or crosswalk tables** → use `scripts/control_lookup.py`.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and proceed.
   If facts are missing, state the assumptions needed to complete the workflow and proceed with a conservative but usable draft.

## Core operating rules

- Treat the Colorado AI Act as an operator workflow centered on **algorithmic discrimination**, **high-risk system screening**, **reasonable care**, **impact assessment**, **consumer notice**, **public summaries**, and **incident disclosure**.
- Distinguish **developer** duties from **deployer** duties. If the user occupies both roles, document both.
- Treat the current operative timing as amended by Colorado's 2025 extraordinary-session bill: the official Colorado General Assembly summary states SB25B-004 extends the effective date of SB24-205's requirements to **June 30, 2026**. Preserve that date in generated artifacts unless the user explicitly asks for historical text. Official Colorado General Assembly pages remain the source of truth for timing and amendment status.
- Do not present a definitive legal opinion. Translate statutory obligations into operating artifacts and evidence requirements.
- If it is unclear whether a system is high-risk, produce a reasoned screening memo with a confidence level and the additional facts needed to resolve uncertainty.
- Prefer plain-language, regulator-ready drafting for consumer-facing notices.
- For every recommendation, specify the owner and the artifact or evidence that would prove implementation.
- When the user asks whether deployment should proceed, conclude with one of: **go**, **go with conditions**, **hold**, or **likely out of scope**.
- Treat alignment to NIST AI RMF and ISO/IEC 42001 as implementation support, not as a guaranteed immunity. The law provides rebuttable-presumption and affirmative-defense mechanics under specified conditions; always document the additional Colorado-specific artifacts that must still exist.
- Do not reproduce copyrighted standards text or long verbatim legal extracts. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user requests another format, use this structure:

# [title]

## 1. executive summary
- system and business context
- likely role: developer, deployer, or both
- likely colorado status: high-risk, exempt, or needs more facts
- key obligations triggered
- recommended decision

## 2. screening result
- consequential-decision domain
- substantial-factor analysis
- exclusions / exemptions considered
- confidence level and missing facts

## 3. key compliance findings
- material gaps
- immediate blockers
- evidence already available
- evidence missing

## 4. required artifacts and owners
| artifact | why required | owner | due timing | evidence source |
|---|---|---|---|---|

## 5. prioritized action plan
| priority | action | owner | target timing | dependency |
|---|---|---|---|---|

## 6. residual risk and escalation
- remaining risks of algorithmic discrimination
- consumer-rights or notice implications
- escalation path
- recommended go / hold position

Adapt the structure when a template in `assets/templates/` is a better fit.

## High-risk screening workflow

Use this when the user asks whether a system is likely in scope, high-risk, or exempt.

1. Start from `assets/templates/colorado-high-risk-screening-questionnaire.csv`.
2. Evaluate in this order:
   - is the organisation a **developer**, **deployer**, or both?
   - is the system used in a **consequential decision** domain?
   - is the system a **substantial factor** in making that decision?
   - does the system fit an exclusion such as a narrow procedural task or specified commodity/security technology?
   - is there a potentially relevant exemption or sector carve-out?
3. Run:
   `python scripts/classify_use_case.py <input_csv> <output_dir>`
4. Convert the outputs into a screening memo that states:
   - likely classification
   - rationale
   - missing facts
   - whether to proceed to full impact assessment
5. If the screening result is uncertain, recommend **go with conditions** or **hold** and name the fact pattern needed to resolve uncertainty.

## Impact-assessment workflow

Use this when the user needs a new, updated, annual, or modification-triggered impact assessment.

1. Start from `assets/templates/colorado-impact-assessment-template.md`.
2. Ensure the assessment covers the Colorado minimum content set:
   - purpose, intended use cases, deployment context, and benefits
   - analysis of known or reasonably foreseeable algorithmic-discrimination risk and mitigation steps
   - categories of input data and outputs
   - any deployer customization data categories
   - performance metrics and known limitations
   - transparency measures, including consumer disclosure measures
   - post-deployment monitoring and user safeguards
   - when applicable, whether use remained consistent with or diverged from the developer's intended uses after intentional and substantial modification
3. Use the duty and minimum-content tables in `references/` to make sure every required section appears.
4. If the user also has a prior NIST AI RMF or ISO/IEC 42001 pack, use the crosswalk tables to map existing evidence into the Colorado assessment.
5. End with an owner-by-owner remediation table for missing evidence.

## Risk-management-policy workflow

Use this when the user needs a deployer policy or wants to test whether an existing policy is likely sufficient.

1. Start from `assets/templates/colorado-deployer-risk-management-policy-outline.md`.
2. Structure the policy and program as an iterative lifecycle process that identifies, documents, and mitigates known or reasonably foreseeable risks of algorithmic discrimination.
3. Make the policy reasonable in light of:
   - organisational size and complexity
   - nature and scope of the high-risk system and intended uses
   - sensitivity and volume of data processed
   - use of recognised frameworks such as NIST AI RMF or ISO/IEC 42001
4. Always include:
   - named personnel and escalation authorities
   - annual review trigger
   - substantial-modification trigger
   - consumer-notice and appeal linkage
   - evidence retention expectations
5. If the organisation deploys multiple high-risk systems, define how the common policy covers all of them and where system-specific annexes are needed.

## Consumer-disclosure workflow

Use this when the user needs pre-decision notice text, adverse-decision explanation language, or public-facing summaries.

1. Use the following templates as needed:
   - `assets/templates/colorado-consumer-pre-decision-notice.md`
   - `assets/templates/colorado-adverse-decision-explanation-template.md`
   - `assets/templates/colorado-public-summary-template.md`
2. For consumer-facing text, ensure it is:
   - plain language
   - accessible
   - available in the languages used by the business for ordinary consumer communications
3. For adverse decisions, include:
   - principal reason or reasons
   - degree and manner in which the AI system contributed
   - data type(s) processed and source(s)
   - opportunity to correct incorrect personal data
   - opportunity to appeal, with human review if technically feasible unless contrary to the consumer's best interests
4. If information must be withheld because of trade secret or protected information limits, include a basis-for-withholding statement.

## Developer-documentation workflow

Use this when the user is a developer, or is a deployer requesting materials from a developer.

1. Use `assets/templates/colorado-developer-disclosure-request-list.csv`.
2. Verify the pack covers, at minimum:
   - reasonably foreseeable uses and known harmful or inappropriate uses
   - high-level summary of training-data types
   - known limitations and foreseeable discrimination risks
   - purpose, intended benefits, intended uses, and intended outputs
   - pre-release performance and discrimination-mitigation evaluation summary
   - data-governance measures and suitability / bias review measures
   - monitoring instructions and all other information reasonably necessary for deployer compliance
   - artifacts needed for a deployer impact assessment, such as model cards or dataset cards where feasible
   - the public summary the developer must maintain
3. If the developer evidence is weak, convert the gaps into a due-diligence deficiency register and condition deployment on closure or compensating controls.

## Monitoring-and-incident workflow

Use this when the user needs annual review plans, incident notices, or modification reviews.

1. Use the following templates as needed:
   - `assets/templates/colorado-annual-review-log.csv`
   - `assets/templates/colorado-algorithmic-discrimination-incident-log.csv`
   - `assets/templates/colorado-modification-review-memo.md`
2. Ensure the workflow captures:
   - annual review cadence
   - review following intentional and substantial modification
   - retention of the most recent impact assessment, prior impact assessments, and related records
   - incident discovery date and the date of notice to the attorney general
3. If the system is high-risk and discrimination is discovered or reasonably likely, prepare the incident disclosure package and identify legal review checkpoints.
4. If the user asks for a regulator-ready pack, assemble: policy, impact assessment, records, public summary, notice templates, and review log.

## Gap-analysis workflow

Use this when the user wants a readiness assessment, remediation plan, or evidence-gap view.

1. Copy `assets/templates/colorado-ai-act-gap-questionnaire.csv` and fill the `score`, `evidence`, and `notes` columns.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review the generated outputs:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `colorado_compliance_profile.csv`
4. Tailor the action plan by audience:
   - ciso → controls, monitoring, evidence, incident response, system inventory
   - chief risk officer → risk appetite, review cadence, evidence retention, residual-risk treatment
   - legal counsel → notices, adverse-decision content, attorney-general disclosures, privilege-preserving record structure

## Script quick reference

- `scripts/classify_use_case.py`
  - classify likely high-risk status, exclusions, and obligation triggers from a screening questionnaire
- `scripts/gap_analysis.py`
  - convert a scored questionnaire into priorities and a Colorado compliance profile
- `scripts/control_lookup.py`
  - search duty maps, screening rules, minimum-content tables, and framework crosswalks

## Resource map

### Templates in `assets/templates/`
- `colorado-high-risk-screening-questionnaire.csv`
- `colorado-ai-act-gap-questionnaire.csv`
- `colorado-impact-assessment-template.md`
- `colorado-deployer-risk-management-policy-outline.md`
- `colorado-consumer-pre-decision-notice.md`
- `colorado-adverse-decision-explanation-template.md`
- `colorado-public-summary-template.md`
- `colorado-developer-disclosure-request-list.csv`
- `colorado-algorithmic-discrimination-incident-log.csv`
- `colorado-annual-review-log.csv`
- `colorado-modification-review-memo.md`

### Reference files in `references/`
- `colorado-duty-map.csv`
- `consequential-decision-domains.csv`
- `high-risk-screening-rules.csv`
- `impact-assessment-minimum-content.csv`
- `consumer-notice-requirements.csv`
- `developer-documentation-and-disclosure.csv`
- `deployer-duty-map.csv`
- `crosswalk-colorado-to-nist-ai-rmf.csv`
- `crosswalk-colorado-to-iso42001.csv`
- `implementation-workflows.md`
- `how-the-skill-uses-the-sources.md`
- `publication-and-copyright-boundaries.md`

## Output quality standard

Every final answer produced with this skill should be detailed, comprehensive, and actionable.

Minimum quality bar:
- identify whether the user is acting as a developer, deployer, or both
- identify likely consequential-decision domain(s)
- state whether the system appears high-risk, exempt, or fact-dependent
- state which Colorado artifacts are required now
- provide owner-specific next steps
- name the missing evidence, not just the missing conclusion

If the user asks for a policy, assessment, or notice, draft the artifact directly.
If the user asks for readiness, run the questionnaire-driven workflow and provide the remediation plan.
