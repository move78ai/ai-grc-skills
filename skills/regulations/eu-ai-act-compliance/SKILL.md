---
name: eu-ai-act-compliance
description: "Workflow-first EU AI Act support for scope screening, high-risk analysis, FRIA work, GPAI readiness, and evidence planning."
---

# EU AI Act Compliance

## Overview

Use this skill to produce implementation-grade outputs for the EU AI Act grounded in Regulation (EU) 2024/1689. The skill is designed for public distribution and thought leadership. Work from article numbers, annex references, concise paraphrases, and bundled derivative tables and templates. Do not present the skill as legal advice and do not imply that any template or crosswalk guarantees legal compliance.




Default audience: Legal counsel, compliance teams, product owners, risk leads, public-sector reviewers, and operators dealing with EU-facing AI systems.

Default style: Article-aware, role-specific, and explicit about scope, operator obligations, artifacts, and open legal questions.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow Decision Tree

1. **Does the user need to decide whether a use case is prohibited, high-risk, transparency-only, GPAI-related, or likely out of scope?**
   - Start with `assets/templates/prohibited-practices-screening.csv` and `assets/templates/high-risk-classification-questionnaire.csv`.
   - Use `references/eu-ai-act-article-map.csv` and `references/eu-ai-act-annex-iii-catalog.csv`.
   - If structured use-case data is available and Python execution is available, run `scripts/classify_use_case.py`.

2. **Does the user need provider or deployer gap analysis for a high-risk AI system?**
   - Start with `assets/templates/high-risk-gap-questionnaire.csv` and `assets/templates/ai-system-inventory.csv`.
   - Use `references/eu-ai-act-operator-obligations.csv`, `references/eu-ai-act-article-map.csv`, and `references/eu-ai-act-gpai-obligations.csv` as needed.
   - If questionnaire responses are available in CSV form and Python execution is available, run `scripts/gap_analysis.py`.

3. **Does the user need a fundamental-rights impact assessment?**
   - Start from `assets/templates/fria-template.md`.
   - Use Article 27 focused materials in `references/how-the-skill-uses-the-regulation.md` and `references/implementation-workflows.md`.
   - Make the assessment context-specific: public authority, private entity providing public services, or Annex III point 5(b)/(c) deployer.

4. **Does the user need provider documentation or operational planning?**
   - Use `assets/templates/provider-compliance-plan.md`, `assets/templates/technical-documentation-starter.md`, `assets/templates/post-market-monitoring-plan.md`, `assets/templates/incident-log.csv`, and `assets/templates/eu-declaration-of-conformity-starter.md`.
   - Tie each artifact to the relevant article and annex references.

5. **Does the user need transparency or content-labeling help?**
   - Use `assets/templates/transparency-notice-examples.md`.
   - Apply Article 50 separately from high-risk obligations. A system can be transparency-scoped without being high-risk.

6. **Does the user need GPAI or GPAI systemic-risk readiness?**
   - Use `references/eu-ai-act-gpai-obligations.csv` and `assets/templates/gpai-readiness-checklist.md`.
   - Distinguish Article 53 baseline GPAI duties from Article 55 systemic-risk duties.

7. **Does the user need a framework crosswalk?**
   - Use `references/crosswalk-eu-ai-act-to-iso42001.csv` and `references/crosswalk-eu-ai-act-to-nist-ai-rmf.csv`.
   - If the user asks for one framework slice, run `scripts/crosswalk_lookup.py` or filter the CSV manually.
   - State whether the relationship is **direct**, **supporting**, or **partial/conditional**.

## Core Operating Rules

- Always determine the operator role first: provider, deployer, authorised representative, importer, distributor, product manufacturer, GPAI provider, or mixed role.
- Always separate five questions:
  1. scope and territorial applicability,
  2. prohibited practice screening,
  3. high-risk classification,
  4. operator obligations,
  5. evidence and implementation artifacts.
- Treat Article 5, Article 6 and Annex III, Article 16 and Article 26, Article 27, Article 50, Articles 53 to 56, Article 72, Article 99, and Article 113 as the core action set unless the user asks for a narrower issue.
- Use article numbers and annex references directly in all tables.
- Convert legal requirements into evidence-oriented outputs. For each obligation, name the artifact that would evidence implementation: policy, register, procedure, contract clause, FRIA, training record, technical document, log extract, monitoring report, label, or incident record.
- Do not collapse provider obligations into deployer obligations. Keep them separate even when the same organization plays both roles.
- Where the classification is uncertain, explicitly label the output as a screening view and identify the missing facts needed for a final legal determination.
- Do not claim that a crosswalk to ISO 42001 or NIST AI RMF creates compliance by itself. Describe crosswalks as implementation support only.
- For public or reusable outputs, avoid reproducing long verbatim legal extracts. Use concise paraphrases plus citations to article numbers when relevant.
- The Act can apply to providers and deployers established outside the EU where the output is intended to be used in the Union. Ask about market, users, and output destination before concluding that the Act does not apply.

## Required Output Patterns

### 1. Risk Classification Memo

Use this structure unless the user specifies another format:

```markdown
# EU AI Act Risk Classification Memo

## Executive Summary
- likely bucket: prohibited / high-risk / transparency / GPAI / minimal or out of scope
- main legal basis
- confidence level and missing facts

## Scope and Operator Assumptions
- operator role(s)
- market or output destination
- intended purpose
- affected persons

## Screening Results
| Question | Finding | Article / Annex | Why It Matters | Evidence Needed |

## Immediate Actions
- stop / redesign / classify / document / notify / monitor
```

### 2. High-Risk Gap Analysis

Use this structure unless the user specifies another format:

```markdown
# EU AI Act High-Risk Gap Analysis

## Executive Summary
- overall maturity score
- highest-priority provider gaps
- highest-priority deployer gaps
- near-term actions

## System and Role Assumptions
- AI system or use case
- Annex III area or Annex I basis
- provider / deployer split

## Article-by-Article Findings
| EU Reference | Current State | Gap | Evidence Needed | Priority | Related ISO 42001 | Related NIST |

## Required Artifacts
- technical documentation
- FRIA
- instructions for use
- logging / monitoring
- incident and complaint handling

## 30-60-90 Day Action Plan
- urgent controls
- evidence build
- operating rhythm
```

### 3. FRIA

Use this structure unless the user provides another template:

```markdown
# Fundamental Rights Impact Assessment

## Context and Intended Purpose
## Use Process Description
## Time, Frequency, and Operational Scope
## Affected Persons and Groups
## Specific Risks of Harm
## Human Oversight Measures
## Complaint, Escalation, and Redress Measures
## Residual Risks and Go / No-Go Decision
## Review Trigger and Owner
```

### 4. Crosswalks

Use a compact table with explicit mapping strength:

```markdown
| EU AI Act Reference | Target Framework Reference | Mapping Strength | Why It Maps | Output / Evidence Implication |
```

## Scripts

### `scripts/classify_use_case.py`

Use when a user has multiple use cases in CSV form and wants fast screening.

Expected input columns:
- `use_case_id`
- `description`
- `sector`
- `annex_i_product`
- `annex_iii_candidate`
- `profiling`
- `prohibited_practice_candidate`
- `interactive_ai`
- `synthetic_content`
- `emotion_or_biometric`
- `deepfake_output`
- `gpai_model_provider`
- `public_authority_use`

Outputs:
- CSV classification file with primary bucket, likely legal basis, and immediate actions.

Run:

```bash
python scripts/classify_use_case.py input.csv output.csv
```

### `scripts/gap_analysis.py`

Use when questionnaire responses are in CSV form and Python execution is available.

Expected input columns:
- `question_id`
- `section`
- `eu_reference`
- `question`
- `score` (0-3)
- `evidence`
- `notes`
- `related_iso42001`
- `related_nist`

Outputs:
- markdown summary report
- prioritized action register CSV
- article evidence register CSV

Run:

```bash
python scripts/gap_analysis.py input.csv output_dir
```

### `scripts/crosswalk_lookup.py`

Use to filter bundled crosswalk tables by EU AI Act article, ISO 42001 clause/control, or NIST AI RMF term.

Run:

```bash
python scripts/crosswalk_lookup.py --framework iso --query article 27
python scripts/crosswalk_lookup.py --framework nist --query transparency
```

If Python execution is unavailable, perform the same filtering manually against the bundled CSV files.

## References

- `references/how-the-skill-uses-the-regulation.md` - concrete use of the Act in this skill.
- `references/implementation-workflows.md` - reusable workflows for screening, gap analysis, FRIA, GPAI readiness, and audit preparation.
- `references/eu-ai-act-article-map.csv` - action-focused article and annex map with expected evidence.
- `references/eu-ai-act-annex-iii-catalog.csv` - Annex III catalog in working-table form.
- `references/eu-ai-act-operator-obligations.csv` - role-based obligations for providers, deployers, authorised representatives, importers and distributors.
- `references/eu-ai-act-gpai-obligations.csv` - Article 53 to 56 duties and decision points.
- `references/crosswalk-eu-ai-act-to-iso42001.csv` - alignment table.
- `references/crosswalk-eu-ai-act-to-nist-ai-rmf.csv` - alignment table.
- `references/publication-and-copyright-boundaries.md` - public-use limits and safe publishing guidance.

## Assets

- `assets/templates/ai-system-inventory.csv`
- `assets/templates/prohibited-practices-screening.csv`
- `assets/templates/high-risk-classification-questionnaire.csv`
- `assets/templates/high-risk-gap-questionnaire.csv`
- `assets/templates/fria-template.md`
- `assets/templates/provider-compliance-plan.md`
- `assets/templates/deployer-operating-procedure.md`
- `assets/templates/technical-documentation-starter.md`
- `assets/templates/post-market-monitoring-plan.md`
- `assets/templates/incident-log.csv`
- `assets/templates/transparency-notice-examples.md`
- `assets/templates/gpai-readiness-checklist.md`
- `assets/templates/eu-declaration-of-conformity-starter.md`

## Style Guidance

- Write like a regulatory implementation advisor, not a marketer.
- Keep outputs neutral and reusable.
- Use article IDs and annex references directly in tables.
- Prefer evidence requests over abstract recommendations.
- Where a mapping is weak or conditional, say so explicitly.
- Distinguish legal obligation, implementation recommendation, and optional good practice.
