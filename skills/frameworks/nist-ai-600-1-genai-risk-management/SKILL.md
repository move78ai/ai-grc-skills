---
name: nist-ai-600-1-genai-risk-management
description: "Operator-grade NIST AI 600-1 workflows for GenAI risk review, provenance planning, supplier checks, and incident readiness."
---

# NIST AI 600-1 GenAI Risk Management

## Overview

Use this skill to produce implementation-grade outputs grounded in NIST AI 600-1, the NIST AI RMF 1.0, and the AI RMF Playbook. Treat NIST AI 600-1 as the GenAI-specific profile, use the AI RMF core as the control structure behind the work, and convert every analysis into evidence-oriented artifacts that a CISO, Chief Risk Officer, legal counsel, or governance lead can review and act on.

This is a public-distribution skill. Work from NIST function names, subcategory IDs, concise derivative tables, and bundled templates. Do not present the skill as legal advice, certification advice, or a guarantee that following the profile eliminates risk.




Default audience: Governance leads, legal counsel, assurance teams, product owners, and risk teams responsible for generative AI use cases.

Default style: Workflow-first, risk-specific, and explicit about GenAI failure modes, evidence, and release decisions.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow Decision Tree

1. **Does the user need GenAI risk identification or prioritization?**
   - Start with `references/nist-ai-600-1-risk-catalog.csv`, `references/nist-ai-600-1-primary-considerations.csv`, and `assets/templates/genai-system-profile.md`.
   - If structured system metadata is available and Python execution is available, run `scripts/profile_builder.py`.
   - Otherwise, profile the use case manually using the same fields and then map the result to the 12 GenAI risks.

2. **Does the user need a GenAI gap analysis or implementation roadmap?**
   - Start with `assets/templates/genai-gap-questionnaire.csv`, `references/nist-ai-600-1-action-library.csv`, `references/nist-ai-rmf-core-slim.csv`, and `references/nist-ai-rmf-trustworthiness.csv`.
   - If questionnaire responses are available and Python execution is available, run `scripts/gap_analysis.py`.
   - Otherwise, score manually using the same logic and produce a prioritized action plan.

3. **Does the user need content provenance, transparency, or disclosure work?**
   - Use `assets/templates/content-provenance-plan.md`, `assets/templates/transparency-and-user-notice.md`, `assets/templates/incident-disclosure-log.csv`, and the action library rows tagged to content provenance or incident disclosure.
   - Distinguish clearly between disclosure to users, traceability of content lineage, provenance data tracking, and external incident reporting or coordination.

4. **Does the user need pre-deployment testing, red-teaming, TEVV, or go/no-go support?**
   - Use `assets/templates/pre-deployment-testing-plan.md`, `assets/templates/go-no-go-memo.md`, `assets/templates/genai-risk-register.csv`, and the action library rows tagged to pre-deployment testing.
   - Always identify whether the task is benchmark testing, scenario testing, structured public feedback, adversarial testing, or operational-readiness gating.

5. **Does the user need third-party, supplier, or value-chain controls?**
   - Use `assets/templates/supplier-risk-review.csv`, `assets/templates/genai-risk-register.csv`, and `references/nist-ai-600-1-action-library.csv`.
   - If the user needs fast filtering of applicable actions, run `scripts/action_lookup.py --risk "value chain"` or filter manually.
   - Tie outputs to contracts, vendor due diligence, approved-provider lists, fallback paths, and ongoing monitoring.

6. **Does the user need stakeholder feedback, recourse, or operating monitoring?**
   - Use `assets/templates/stakeholder-feedback-and-recourse.md`, `assets/templates/incident-disclosure-log.csv`, and `assets/templates/genai-risk-register.csv`.
   - Distinguish direct user feedback, affected-community feedback, red-teaming, structured public feedback, and internal issue escalation.

## Core Operating Rules

- Treat the work as **profile-driven risk management**, not as a narrative summary of the framework.
- Always identify these facts before drafting outputs:
  1. system or use case,
  2. modality or modalities,
  3. lifecycle stage,
  4. actor role,
  5. deployment context,
  6. data sensitivity,
  7. model and component sourcing,
  8. public exposure and distribution,
  9. human oversight model,
  10. testing and monitoring maturity.
- Always separate four layers of analysis:
  1. **NIST AI 600-1 GenAI risks**,
  2. **primary considerations** (governance, content provenance, pre-deployment testing, incident disclosure),
  3. **AI RMF function and subcategory anchors**,
  4. **evidence artifacts** needed to show implementation.
- Always map the use case against the 12 GenAI risk categories. Do not stop after naming only one or two “headline” risks.
- Always name the artifact that would evidence implementation for each recommendation: policy, system profile, supplier review, contract clause, provenance plan, test plan, risk register, notice, incident log, review memo, or training record.
- Treat content provenance and disclosure as related but distinct:
  - **content provenance** is about origin, lineage, metadata, watermarking, traceability, and authenticity support,
  - **disclosure** is about what must be communicated to users, stakeholders, downstream actors, or incident recipients.
- Treat structured public feedback, red-teaming, and TEVV as separate mechanisms with different purposes. Do not collapse them into one generic “testing” bucket.
- For supplier and value-chain work, distinguish:
  - training data origin,
  - upstream model origin,
  - embedded tools and APIs,
  - contracts and SLAs,
  - approved provider governance,
  - monitoring and fallback paths.
- Use the AI RMF core and Playbook to structure outputs, but keep the skill centered on GenAI-specific risks and actions.
- Do not claim that following this profile ensures legal compliance. Describe it as a risk management aid.
- Do not reproduce long verbatim passages from NIST publications. Use concise derivative tables, paraphrases, IDs, and templates.

## Required Output Patterns

### 1. NIST AI 600-1 GenAI Risk Review

Use this structure unless the user specifies another format:

```markdown
# NIST AI 600-1 GenAI Risk Review

## Executive Summary
- intended use
- primary risk drivers
- top control priorities
- residual concerns

## System and Context Assumptions
- use case and modality
- deployment environment
- actor role(s)
- data sensitivity
- third-party dependencies
- human oversight model

## Risk-by-Risk Findings
| GenAI Risk | Why It Applies | Severity | Existing Controls | Gaps | Evidence Needed |

## Primary Consideration Priorities
| Primary Consideration | Why It Matters Here | Immediate Artifact |

## 30-60-90 Day Actions
- governance and documentation
- testing and measurement
- monitoring, disclosure, and supplier controls
```

### 2. GenAI Gap Analysis

```markdown
# NIST AI 600-1 GenAI Gap Analysis

## Executive Summary
- overall maturity score
- strongest areas
- highest-priority gaps
- near-term operating actions

## Scope and Role Assumptions
- system or use case
- model sourcing
- deployment stage
- primary stakeholders

## Findings by AI RMF Function
| AI RMF Reference | Current State | Gap | Priority | Suggested Artifact | Relevant GenAI Risk |

## Immediate Artifacts to Create
- system profile
- risk register
- provenance plan
- pre-deployment test plan
- notice/disclosure pack
- incident disclosure path
```

### 3. Content Provenance Plan

```markdown
# GenAI Content Provenance Plan

## Objective and Scope
## Content Types and Distribution Paths
## Provenance Methods
## Required Metadata Fields
## Detection / Validation Approach
## Known Limitations and Failure Modes
## Human Review and Escalation
## Monitoring Metrics
## Incident and Disclosure Linkage
```

### 4. Pre-Deployment Test Plan

```markdown
# GenAI Pre-Deployment Test Plan

## Test Objectives
## Use Cases and Out-of-Scope Uses
## Risk Hypotheses to Test
## Test Methods
- benchmark and scenario tests
- red-teaming
- structured public feedback
- human review and domain expert review

## Go / No-Go Thresholds
## Evidence and Reporting
## Remediation Loop
```

### 5. Supplier / Third-Party Review

```markdown
# GenAI Supplier and Value-Chain Review

## Third-Party Components in Scope
## Rights, Privacy, and Security Questions
## Provenance and Transparency Requirements
## Monitoring and Fallback Requirements
## Contract / SLA Actions
## Residual Risk Position
```

## Scripts

### `scripts/gap_analysis.py`

Use when questionnaire responses are available in CSV form and Python execution is available.

Expected input columns:
- `question_id`
- `section`
- `nist_reference`
- `question`
- `score` (0-3)
- `evidence`
- `notes`
- `related_risk`
- `primary_consideration`

Outputs:
- markdown summary report
- prioritized action register CSV
- risk register starter CSV

Run:

```bash
python scripts/gap_analysis.py input.csv output_dir
```

### `scripts/action_lookup.py`

Use to filter the bundled action library by risk, function, primary consideration, or keyword.

Run:

```bash
python scripts/action_lookup.py --risk "information integrity"
python scripts/action_lookup.py --function govern --consideration provenance
python scripts/action_lookup.py --keyword vendor
```

### `scripts/profile_builder.py`

Use when the user has one or more GenAI systems and needs fast prioritization of risks, considerations, and starter artifacts.

Expected input columns:
- `use_case_id`
- `modality`
- `public_facing`
- `generates_public_content`
- `high_impact_domain`
- `sensitive_data`
- `third_party_model`
- `fine_tuned`
- `rag_or_grounding`
- `plugins_or_tools`
- `human_review`
- `notes`

Outputs:
- CSV recommendation file with priority risks, primary considerations, AI RMF function emphasis, and starter artifacts.

Run:

```bash
python scripts/profile_builder.py input.csv output.csv
```

## References

- `references/how-the-skill-uses-nist-ai-600-1.md` - explains how the skill applies NIST AI 600-1 together with the AI RMF and Playbook.
- `references/implementation-workflows.md` - reusable workflows for risk review, gap analysis, provenance planning, pre-deployment testing, supplier review, and incident disclosure.
- `references/nist-ai-600-1-risk-catalog.csv` - GenAI risk catalog with trustworthiness links, common triggers, and starter artifacts.
- `references/nist-ai-600-1-primary-considerations.csv` - the four primary considerations and how they show up in practice.
- `references/nist-ai-600-1-action-library.csv` - selected NIST AI 600-1 action IDs with concise derivative paraphrases for implementation work.
- `references/nist-ai-rmf-core-slim.csv` - AI RMF function and subcategory anchors for GenAI workflows.
- `references/nist-ai-rmf-trustworthiness.csv` - trustworthiness characteristics and typical evidence.
- `references/publication-and-copyright-boundaries.md` - public-use limits and safe publishing guidance.

## Assets

- `assets/templates/genai-system-profile.md`
- `assets/templates/genai-gap-questionnaire.csv`
- `assets/templates/genai-risk-register.csv`
- `assets/templates/content-provenance-plan.md`
- `assets/templates/pre-deployment-testing-plan.md`
- `assets/templates/transparency-and-user-notice.md`
- `assets/templates/stakeholder-feedback-and-recourse.md`
- `assets/templates/supplier-risk-review.csv`
- `assets/templates/go-no-go-memo.md`
- `assets/templates/incident-disclosure-log.csv`

## Style Guidance

- Write like a governance, risk, or security lead.
- Keep outputs neutral, evidence-oriented, and decision-useful.
- Prefer implementation actions and operating artifacts over explanation.
- Use NIST IDs where helpful, but explain what must actually be done.
- Make assumptions explicit when facts are missing.
