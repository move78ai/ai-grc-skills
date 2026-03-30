---
name: iso-42001-governance
description: "use this skill when chatgpt needs to help with iso/iec 42001 ai management systems, including aims scoping, self-assessment, gap analysis, statement of applicability drafting, ai policy drafting, ai system impact assessments, governance design, internal audit readiness, and crosswalks to nist ai rmf or the eu ai act. use it for both organizations building an ai management system and teams trying to align existing ai governance artifacts to iso 42001, iso 22989, and iso 38507."
---

# ISO/IEC 42001 Governance

## Overview

Use this skill to produce management-grade outputs for AI governance work grounded in ISO/IEC 42001 as the primary management-system framework, ISO/IEC 22989 for terminology, stakeholder roles, trustworthiness concepts, and AI life-cycle structure, and ISO/IEC 38507 for governing-body oversight, accountability, decision-making, data use, compliance, culture, and risk.

This is a public-distribution skill. Work from clause numbers, control identifiers, paraphrases, and bundled derivative tables. Do not reproduce long verbatim extracts from ISO standards.

## Workflow Decision Tree

1. **Self-assessment or gap analysis request?**
   - Use `references/iso-42001-clause-map.csv`, `references/iso-42001-annex-a-controls.csv`, and `assets/templates/self-assessment-questionnaire.csv`.
   - If structured questionnaire responses are available and Python execution is available, run `scripts/gap_analysis.py`.
   - Otherwise apply the same scoring logic manually.

2. **Policy drafting request?**
   - Start from `assets/templates/ai-policy-template.md`.
   - Tailor policy clauses using `references/how-the-skill-uses-the-standards.md` and `references/implementation-workflows.md`.
   - Make the policy role-aware: provider, developer, deployer, customer, partner, or mixed role.

3. **Crosswalk or framework mapping request?**
   - Use `references/crosswalk-iso42001-to-nist-ai-rmf.csv` and `references/crosswalk-iso42001-to-eu-ai-act.csv`.
   - If the user asks for one framework slice, run `scripts/crosswalk_lookup.py` or filter the CSV manually.
   - State whether the relationship is **direct**, **supporting**, or **partial/conditional**.

4. **Governance model, board pack, or executive oversight request?**
   - Use `references/iso-38507-governance-themes.csv` and `assets/templates/board-governance-prompts.md`.
   - Frame outputs around direction, oversight, evaluation, accountability, decision rights, data use, compliance, and risk appetite.

5. **Terminology, roles, or life-cycle clarification request?**
   - Use `references/iso-22989-roles-lifecycle-trustworthiness.csv`.
   - Normalize terms before drafting controls, policies, or crosswalks.

## Core Operating Rules

- Treat **ISO/IEC 42001 clauses 4-10** as management-system requirements and **Annex A / Annex B** as the reference control catalog plus implementation guidance.
- Distinguish clearly between:
  - **management-system requirements**,
  - **control selection / statement of applicability decisions**,
  - **implementation examples**, and
  - **regulatory obligations** coming from external frameworks such as the EU AI Act.
- Always identify the organization's role in the AI ecosystem before drafting outputs. Mixed-role organizations often need split guidance for provider, developer, deployer, and user responsibilities.
- Always convert analysis into evidence-oriented outputs. For each gap, ask for or name the expected artifact: policy, register, workflow, test record, training record, incident log, impact assessment, supplier control, or review minutes.
- When producing a gap analysis, prioritize gaps that affect:
  1. governance scope and role determination,
  2. risk assessment and treatment,
  3. impact assessment,
  4. data governance,
  5. human oversight and monitoring,
  6. technical documentation and records,
  7. incident reporting and third-party accountability.
- Do not claim that ISO/IEC 42001 certification guarantees legal compliance. Describe crosswalks as alignment support, not legal equivalence.
- For public or reusable outputs, avoid copying standards text. Use clause/control IDs plus concise paraphrases.

## Required Output Patterns

### 1. Gap Analysis

Use this structure unless the user specifies another format:

```markdown
# ISO/IEC 42001 Gap Analysis

## Executive Summary
- overall maturity score
- strongest areas
- highest-priority gaps
- likely near-term actions

## Scope and Role Assumptions
- organizational role(s)
- in-scope AI systems or use cases
- excluded items / assumptions

## Clause-by-Clause Findings
| ISO Reference | Current State | Gap | Evidence Needed | Priority | Related NIST / EU AI Act |

## Statement of Applicability Implications
- controls likely in scope
- controls likely excluded with rationale
- controls needing design work

## 30-60-90 Day Action Plan
- quick wins
- foundational build items
- operating-rhythm items
```

### 2. Policy Drafting

Use this structure unless the user provides their own template:

```markdown
# AI Policy

## Purpose
## Scope
## Roles and Accountability
## AI Objectives
## Risk and Impact Management
## Data Governance
## Human Oversight and Acceptable Use
## Documentation, Monitoring, and Logging
## Incident and Escalation Handling
## Third-Party / Supplier Controls
## Training and Awareness
## Review, Exceptions, and Version Control
```

### 3. Crosswalks

Use a compact table with explicit mapping strength:

```markdown
| ISO 42001 Reference | Target Framework Reference | Mapping Strength | Why It Maps | Output / Evidence Implication |
```

## Scripts

### `scripts/gap_analysis.py`

Use when questionnaire responses are in CSV form and Python execution is available.

Expected input columns:
- `question_id`
- `section`
- `iso_reference`
- `question`
- `score` (0-3)
- `evidence`
- `notes`
- `related_controls`
- `related_nist`
- `related_eu_ai_act`

Outputs:
- markdown summary report
- prioritized action register CSV
- statement-of-applicability starter CSV

Run:

```bash
python scripts/gap_analysis.py input.csv output_dir
```

### `scripts/crosswalk_lookup.py`

Use to filter bundled crosswalk tables by ISO clause/control, NIST term, or EU AI Act reference.

Run:

```bash
python scripts/crosswalk_lookup.py --framework nist --query risk
python scripts/crosswalk_lookup.py --framework eu --query article 9
```

If Python execution is unavailable, perform the same filtering manually against the bundled CSV files.

## References

- `references/how-the-skill-uses-the-standards.md` — concrete use of ISO 42001, ISO 22989, and ISO 38507 in this skill.
- `references/implementation-workflows.md` — reusable workflows for self-assessment, policy drafting, crosswalks, and audit readiness.
- `references/iso-42001-clause-map.csv` — clause-level paraphrased requirements and expected evidence.
- `references/iso-42001-annex-a-controls.csv` — Annex A control catalog with practical artifacts.
- `references/iso-22989-roles-lifecycle-trustworthiness.csv` — role, life-cycle, and terminology normalization aid.
- `references/iso-38507-governance-themes.csv` — governing-body prompts and oversight themes.
- `references/crosswalk-iso42001-to-nist-ai-rmf.csv` — alignment table.
- `references/crosswalk-iso42001-to-eu-ai-act.csv` — alignment table.
- `references/publication-and-copyright-boundaries.md` — public-use limits and safe publishing guidance.

## Assets

- `assets/templates/self-assessment-questionnaire.csv`
- `assets/templates/ai-policy-template.md`
- `assets/templates/ai-risk-register.csv`
- `assets/templates/statement-of-applicability.csv`
- `assets/templates/ai-system-impact-assessment.md`
- `assets/templates/internal-audit-program.md`
- `assets/templates/board-governance-prompts.md`

## Style Guidance

- Write like an auditor or governance advisor, not a marketer.
- Keep outputs neutral and reusable. Do not mention any company-specific methodology unless the user explicitly asks.
- Use clause IDs and control IDs directly in tables.
- Prefer evidence requests over abstract recommendations.
- Where a mapping is weak or conditional, say so explicitly.
