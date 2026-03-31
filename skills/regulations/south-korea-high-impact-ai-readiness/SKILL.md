---
name: south-korea-high-impact-ai-readiness
description: "Workflow-first South Korea AI Basic Act readiness support for high-impact screening, labeling, operator controls, and evidence packs."
---

# South Korea High-Impact AI Readiness

## Overview

Use this skill to convert South Korea's AI Basic Act and related MSIT implementation materials into operator-grade readiness artifacts. Treat the Act as a workflow driver, not a tutorial subject. Every response should end in concrete evidence artifacts that a CISO, Chief Risk Officer, legal counsel, or product governance lead can review, approve, and operate.

This is a public-distribution skill. Use concise derivative tables, original templates, and workflow logic. Do not provide Korean legal advice, certainty on classification, or guarantees of compliance. Where presidential decree details or agency guidance may evolve, identify the open variable and draft the artifact so it can be updated cleanly.




Default audience: Legal, policy, compliance, product, and risk teams operating AI systems that may affect South Korea users or markets.

Default style: Implementation-led, explicit about decree-sensitive variables, and focused on retained evidence and operating controls.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow Decision Tree

1. **Does the user need to know whether a system may qualify as high-impact ai?**
   - Start with `references/high-impact-areas.csv`, `assets/templates/high-impact-screening-questionnaire.csv`, and `assets/templates/use-case-profile.md`.
   - If structured answers are available and Python execution is available, run `scripts/classify_use_case.py`.
   - Otherwise, classify manually using the statutory area list and produce a confidence-rated screening memo.

2. **Does the user need a South Korea readiness gap analysis or implementation roadmap?**
   - Start with `assets/templates/readiness-gap-questionnaire.csv`, `references/readiness-control-library.csv`, `references/obligation-map.csv`, and `references/equivalence-crosswalk.csv`.
   - If questionnaire responses are available and Python execution is available, run `scripts/gap_analysis.py`.
   - Otherwise, score manually and produce a prioritized action plan tied to evidence artifacts.

3. **Does the user need transparency, labeling, or user-notice work?**
   - Use `references/transparency-and-labeling.csv`, `assets/templates/transparency-and-labeling-pack.md`, and `assets/templates/user-protection-measures.md`.
   - Distinguish clearly between:
     - notice that a product or service is AI-based,
     - notice that content is GenAI-generated,
     - clear indication when synthetic audio, image, or video may be hard to distinguish from authentic content.

4. **Does the user need high-impact operator obligations mapped into operating controls?**
   - Use `references/obligation-map.csv`, `assets/templates/risk-management-plan.md`, `assets/templates/explanation-feasibility-assessment.md`, `assets/templates/human-supervision-plan.md`, and `assets/templates/document-retention-pack.md`.
   - Always separate risk management, explanation planning, user protection, human supervision, and retained documentation.

5. **Does the user need an impact assessment or public-sector procurement readiness pack?**
   - Use `assets/templates/high-impact-impact-assessment.md`, `assets/templates/public-sector-priority-checklist.md`, and `assets/templates/go-no-go-memo.md`.
   - Treat the impact assessment as an advance human-rights-oriented review, not as a generic product questionnaire.

6. **Does the user need foreign-operator / domestic-representative readiness?**
   - Use `assets/templates/domestic-representative-checklist.md`, `references/foreign-operator-triggers.csv`, and `assets/templates/evidence-pack-checklist.md`.
   - Distinguish threshold uncertainty from known duties. Draft assignment and reporting workflows even when the exact decree thresholds are not yet included in the skill.

## Core Operating Rules

- Treat the work as **implementation readiness**, not as an article-by-article legal summary.
- Always establish these facts before drafting outputs:
  1. operator role,
  2. product or service,
  3. deployment market and whether Korea users are affected,
  4. likely high-impact sector or activity,
  5. whether the system uses GenAI,
  6. whether synthetic media is produced,
  7. whether public-sector procurement or use is in scope,
  8. data and learning-data profile,
  9. human oversight model,
  10. current evidence available.
- Separate five layers of analysis:
  1. **scope and role**,
  2. **high-impact screening**,
  3. **operator obligations**,
  4. **supporting evidence artifacts**,
  5. **open variables still awaiting decree/guideline specificity**.
- For high-impact analysis, always identify the statutory area first. Do not leap straight to controls without recording why the use case appears inside or outside a listed area.
- For explanation work, do not promise explainability in the abstract. Use the Act's framing: provide explanations **to the extent technically and reasonably possible** or **technically feasible**, and record constraints explicitly.
- For transparency work, distinguish product/service-level AI notice from content-level labeling.
- For safety work, treat lifecycle risk identification, assessment, mitigation, and incident-response capability as separate control themes.
- For high-impact operator obligations, always create evidence hooks for:
  - risk management plan,
  - explanation plan,
  - user protection measures,
  - human management and supervision,
  - stored documents proving safety and reliability actions.
- For public-sector contexts, call out that public institutions should prioritize high-impact AI that has undergone verification/certification and impact assessment.
- For foreign operators, identify whether a domestic representative may be required, but state clearly when user/revenue thresholds are still decree-dependent.
- When a user asks for a roadmap, prioritize the shortest set of artifacts needed to become decision-ready.
- Do not reproduce long verbatim extracts from the Act. Use derivative tables, short paraphrases, and templates.

## Required Output Patterns

### 1. South Korea High-Impact AI Screening Memo

```markdown
# South Korea High-Impact AI Screening Memo

## Executive Summary
- likely scope position
- likely operator role
- top readiness actions
- key open variables

## Use Case and Role Assumptions
- product or service
- deployment context
- affected users or persons
- genai / synthetic media profile
- public-sector involvement

## High-Impact Area Analysis
| Candidate Area | Why It May Apply | Why It May Not Apply | Confidence | Evidence Needed |

## Immediate Compliance-Relevant Actions
| Action | Owner | Artifact | Timing |

## Open Questions for Counsel or Policy Review
- decree-dependent issue
- classification uncertainty
- evidence gap
```

### 2. South Korea Readiness Gap Analysis

```markdown
# South Korea AI Basic Act Readiness Gap Analysis

## Executive Summary
- current maturity
- strongest areas
- highest-priority gaps
- near-term operating actions

## Scope and Assumptions
- operator role
- high-impact status
- genai status
- public-sector or private-sector context

## Findings by Obligation Theme
| Theme | Current State | Gap | Priority | Required Artifact | Notes |

## 30-60-90 Day Action Plan
- first 30 days
- next 30 days
- following 30 days
```

### 3. High-Impact Operator Controls Pack

```markdown
# High-Impact AI Operator Controls Pack

## Risk Management Plan Summary
## Explanation Feasibility Position
## User Protection Measures
## Human Supervision Design
## Document Retention and Evidence Plan
## Monitoring and Incident Escalation
## Residual Risk Position
```

### 4. Transparency and Labeling Pack

```markdown
# South Korea AI Transparency and Labeling Pack

## In-Scope User Touchpoints
## AI-Based Service Notice
## GenAI Output Notice
## Synthetic Media Labeling Method
## Exceptions / Creative Work Considerations
## Deployment and Monitoring Notes
```

### 5. Impact Assessment Starter

```markdown
# High-Impact AI Impact Assessment Starter

## System and Context Description
## Potential Impact on Basic Human Rights
## Affected Persons and Groups
## Foreseeable Failure and Harm Scenarios
## Mitigations and Safeguards
## Human Supervision and Escalation
## Remaining Questions and Residual Concerns
## Approval Recommendation
```

## Scripts

### `scripts/classify_use_case.py`

Use when structured use-case metadata is available. The script checks candidate fit against the listed high-impact areas and produces a screening memo plus a structured results CSV.

Expected input columns:
- `field`
- `value`

Recommended fields:
- `sector`
- `use_case`
- `decision_type`
- `public_sector`
- `genai`
- `synthetic_media`
- `biometric`
- `employment_or_lending`
- `transport`
- `healthcare`
- `education`
- `critical_infrastructure`
- `notes`

Run:

```bash
python scripts/classify_use_case.py input.csv output_dir
```

### `scripts/gap_analysis.py`

Use when readiness questionnaire responses are available in CSV form. The script scores responses, highlights the lowest-scoring control themes, and produces a markdown report plus an action register.

Expected input columns:
- `question_id`
- `theme`
- `question`
- `score` (0-3)
- `evidence`
- `notes`
- `reference`

Run:

```bash
python scripts/gap_analysis.py input.csv output_dir
```

### `scripts/control_lookup.py`

Use when the user needs fast filtering of the derivative control library by theme, role, or artifact.

Examples:

```bash
python scripts/control_lookup.py --theme transparency
python scripts/control_lookup.py --role foreign_operator
python scripts/control_lookup.py --artifact impact_assessment
```

## Resource Map

### References
- `references/high-impact-areas.csv` — derivative map of listed high-impact areas and screening cues
- `references/obligation-map.csv` — operator obligations translated into workflow themes and evidence artifacts
- `references/transparency-and-labeling.csv` — notice and labeling requirements split by scenario
- `references/readiness-control-library.csv` — detailed readiness controls for screening, planning, transparency, supervision, evidence, and foreign-operator readiness
- `references/equivalence-crosswalk.csv` — crosswalk to NIST AI RMF, ISO/IEC 42001, and practical evidence equivalence logic
- `references/foreign-operator-triggers.csv` — domestic representative workflow notes and decree-dependent threshold reminder
- `references/publication-and-copyright-boundaries.md` — public-distribution boundaries and source handling rules
- `references/source-register.md` — official and supporting public sources used to construct this skill

### Templates
- `assets/templates/use-case-profile.md`
- `assets/templates/high-impact-screening-questionnaire.csv`
- `assets/templates/readiness-gap-questionnaire.csv`
- `assets/templates/risk-management-plan.md`
- `assets/templates/explanation-feasibility-assessment.md`
- `assets/templates/user-protection-measures.md`
- `assets/templates/human-supervision-plan.md`
- `assets/templates/high-impact-impact-assessment.md`
- `assets/templates/transparency-and-labeling-pack.md`
- `assets/templates/document-retention-pack.md`
- `assets/templates/domestic-representative-checklist.md`
- `assets/templates/public-sector-priority-checklist.md`
- `assets/templates/evidence-pack-checklist.md`
- `assets/templates/annual-review-log.csv`
- `assets/templates/safety-measures-submission-log.csv`
- `assets/templates/incident-response-log.csv`
- `assets/templates/go-no-go-memo.md`

## Quality Bar

- Make outputs detailed, comprehensive, and actionable.
- Default to crisp professional language suitable for CISO, CRO, legal counsel, and governance leaders.
- Always identify the minimum evidence pack needed to defend a decision.
- Where legal specificity depends on later decree or guideline detail, say so plainly and draft the artifact with update hooks rather than omitting the control entirely.
