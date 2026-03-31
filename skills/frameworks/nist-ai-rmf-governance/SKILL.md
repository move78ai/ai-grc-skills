---
name: nist-ai-rmf-governance
description: "Workflow-first NIST AI RMF guidance for gap analysis, profiles, TEVV planning, GenAI screening, and crosswalk work."
---

# NIST AI RMF Governance

## Overview

Use this skill to produce implementation-grade outputs grounded in the NIST AI Risk Management Framework (AI RMF 1.0), the NIST AI RMF Playbook, the NIST Generative AI Profile, and the NIST Cyber AI Profile. Treat the AI RMF as the primary organizing framework, use the GenAI Profile when the system is generative, and use the Cyber AI Profile when the task is specifically about AI-related cybersecurity outcomes.

This is a public-distribution skill. Work from NIST function names, subcategory IDs, trustworthiness characteristics, concise paraphrases, and bundled derivative tables and templates. Do not present the skill as legal advice, certification advice, or as a guarantee that following the framework will eliminate risk.




Default audience: Governance leads, product-risk teams, compliance teams, assurance reviewers, security stakeholders, and AI program owners.

Default style: Risk-based, operator-grade, and structured around system context, trustworthiness, evidence, and treatment decisions.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow Decision Tree

1. **Does the user need core AI RMF adoption, gap analysis, or operating design?**
   - Start with `references/nist-ai-rmf-core-structure.csv`, `references/nist-ai-rmf-trustworthiness.csv`, and `assets/templates/ai-rmf-gap-questionnaire.csv`.
   - If structured questionnaire responses are available and Python execution is available, run `scripts/gap_analysis.py`.
   - Otherwise apply the same scoring logic manually.

2. **Is the system generative AI?**
   - Use `references/nist-genai-risk-catalog.csv` and `assets/templates/genai-risk-screening.csv`.
   - Distinguish baseline AI RMF governance from GenAI-specific risk work such as confabulation, information integrity, data privacy, content provenance, intellectual property, and model or component integration.
   - If structured metadata is available, run `scripts/profile_builder.py` to recommend the right NIST lens.

3. **Is the task specifically about AI-related cybersecurity?**
   - Use `references/nist-cyber-ai-focus-areas.csv` and `references/crosswalk-nist-ai-rmf-to-cyber-ai-profile.csv`.
   - Distinguish the three Cyber AI Profile focus areas:
     - **Secure** for securing AI system components,
     - **Defend** for AI-enabled cyber defense,
     - **Thwart** for resilience against AI-enabled attacks.
   - Use `assets/templates/cyber-ai-prioritization.md` for strategy or prioritization outputs.

4. **Does the user need artifact drafting for governance or operations?**
   - Use `assets/templates/ai-system-profile.md`, `assets/templates/ai-risk-register.csv`, `assets/templates/tevv-plan.md`, `assets/templates/human-oversight-plan.md`, `assets/templates/go-no-go-memo.md`, `assets/templates/incident-and-feedback-log.csv`, and `assets/templates/ai-system-inventory.csv`.
   - Tie each artifact to the relevant AI RMF function and trustworthiness characteristics.

5. **Does the user need a framework crosswalk?**
   - Use `references/crosswalk-nist-ai-rmf-to-iso42001.csv`, `references/crosswalk-nist-ai-rmf-to-eu-ai-act.csv`, and `references/crosswalk-nist-ai-rmf-to-cyber-ai-profile.csv`.
   - If the user asks for one framework slice, run `scripts/crosswalk_lookup.py` or filter the CSV manually.
   - State whether the relationship is **direct**, **supporting**, or **partial/conditional**.

## Core Operating Rules

- Treat the AI RMF as a **voluntary, risk-based management framework** with four functions: **govern, map, measure, and manage**.
- Treat **govern** as cross-cutting and foundational. Do not begin with measurement tables if the governance conditions, roles, scope, and risk tolerances are undefined.
- Always separate five questions:
  1. system context and actor roles,
  2. trustworthiness objectives,
  3. risks and impacts,
  4. evidence and measurement approach,
  5. treatment, monitoring, and improvement.
- Always identify the organization's role in relation to the AI lifecycle before drafting outputs: designer, developer, deployer, operator, evaluator, acquirer, or mixed role.
- Distinguish clearly between:
  - **trustworthiness characteristics**,
  - **AI RMF functions and subcategories**,
  - **profile-specific risks** such as GenAI or cyber-AI risks,
  - **evidence artifacts** such as inventories, registers, impact assessments, TEVV records, training records, and incident logs.
- Convert analysis into evidence-oriented outputs. For each gap or recommendation, name the artifact that would evidence implementation: policy, inventory, impact assessment, risk register, test plan, validation report, incident record, monitoring metric, training record, or review memo.
- Use the GenAI Profile only when the system actually generates content or behaves as a generative foundation model or application. Do not over-apply GenAI risk categories to narrow predictive or optimization systems.
- Use the Cyber AI Profile only for cybersecurity-specific questions. It is not a substitute for broader trustworthiness analysis.
- Do not claim that a crosswalk to ISO/IEC 42001, the EU AI Act, or the NIST CSF creates compliance by itself. Describe crosswalks as implementation support only.
- For public or reusable outputs, avoid long verbatim extracts from NIST publications. Use concise paraphrases, function names, subcategory IDs, and bundled tables.
- Where risk classification is uncertain, explicitly label the output as a screening view and identify the missing facts needed for a stronger conclusion.

## Required Output Patterns

### 1. AI RMF Gap Analysis

Use this structure unless the user specifies another format:

```markdown
# NIST AI RMF Gap Analysis

## Executive Summary
- overall maturity score
- strongest areas
- highest-priority gaps
- near-term actions

## System and Role Assumptions
- system or use case
- lifecycle stage(s)
- actor role(s)
- deployment context

## Function-by-Function Findings
| AI RMF Reference | Current State | Gap | Evidence Needed | Priority | Related Trustworthiness Characteristic |

## Immediate Artifacts to Create
- system profile
- risk register
- measurement or tevv plan
- human oversight plan
- incident and feedback process

## 30-60-90 Day Action Plan
- governance foundations
- mapping and measurement build
- management and monitoring rhythm
```

### 2. GenAI Risk Review

Use this structure unless the user provides another template:

```markdown
# NIST GenAI Risk Review

## Executive Summary
- intended use
- primary genai risk clusters
- highest-priority controls
- residual concerns

## Scope and Assumptions
- model or application type
- user population
- data sensitivity
- integration points

## Risk-by-Risk Findings
| GenAI Risk | Why It Applies | Severity | Existing Controls | Gaps | Evidence Needed |

## Required Safeguards
- governance
- content provenance
- pre-deployment testing
- monitoring and incident disclosure
```

### 3. Cyber AI Strategy Memo

Use this structure unless the user specifies another format:

```markdown
# NIST Cyber AI Strategy Memo

## Executive Summary
- primary focus area: secure / defend / thwart
- why this focus area is primary
- top actions

## Environment and AI Usage
## Priority Outcomes
| CSF Function | Focus Area | Priority | Why It Matters | Suggested Artifact |

## Next Actions
- technical controls
- operating changes
- training or monitoring changes
```

### 4. Crosswalks

Use a compact table with explicit mapping strength:

```markdown
| NIST Reference | Target Framework Reference | Mapping Strength | Why It Maps | Output / Evidence Implication |
```

## Scripts

### `scripts/gap_analysis.py`

Use when questionnaire responses are in CSV form and Python execution is available.

Expected input columns:
- `question_id`
- `function`
- `nist_reference`
- `question`
- `score` (0-3)
- `evidence`
- `notes`
- `related_trustworthiness`
- `related_genai_risk`
- `related_cyber_ai_focus`

Outputs:
- markdown summary report
- prioritized action register CSV
- risk register starter CSV

Run:

```bash
python scripts/gap_analysis.py input.csv output_dir
```

### `scripts/crosswalk_lookup.py`

Use to filter bundled crosswalk tables by NIST AI RMF reference, ISO 42001 clause, EU AI Act article, or Cyber AI Profile focus area.

Run:

```bash
python scripts/crosswalk_lookup.py --framework iso --query govern
python scripts/crosswalk_lookup.py --framework eu --query transparency
python scripts/crosswalk_lookup.py --framework cyber --query defend
```

If Python execution is unavailable, perform the same filtering manually against the bundled CSV files.

### `scripts/profile_builder.py`

Use when the user has multiple AI systems or use cases and needs a fast recommendation on which NIST lenses to apply.

Expected input columns:
- `use_case_id`
- `system_type`
- `uses_genai`
- `cyber_defense_use`
- `handles_sensitive_data`
- `internet_facing`
- `high_impact_decision`
- `third_party_model`
- `notes`

Outputs:
- CSV recommendation file with recommended NIST lenses, likely priority themes, and starter artifacts.

Run:

```bash
python scripts/profile_builder.py input.csv output.csv
```

## References

- `references/how-the-skill-uses-the-nist-frameworks.md` - concrete use of the AI RMF, AI RMF Playbook, GenAI Profile, and Cyber AI Profile in this skill.
- `references/implementation-workflows.md` - reusable workflows for baseline AI RMF adoption, GenAI review, cyber-AI prioritization, crosswalks, and operating-rhythm design.
- `references/nist-ai-rmf-core-structure.csv` - function, category, and subcategory map with concise paraphrases.
- `references/nist-ai-rmf-trustworthiness.csv` - trustworthiness characteristics and typical evidence.
- `references/nist-genai-risk-catalog.csv` - GenAI risk catalog with mapped trustworthiness implications.
- `references/nist-cyber-ai-focus-areas.csv` - Cyber AI Profile focus areas and practical use triggers.
- `references/crosswalk-nist-ai-rmf-to-iso42001.csv` - alignment table.
- `references/crosswalk-nist-ai-rmf-to-eu-ai-act.csv` - alignment table.
- `references/crosswalk-nist-ai-rmf-to-cyber-ai-profile.csv` - alignment table.
- `references/publication-and-copyright-boundaries.md` - public-use limits and safe publishing guidance.

## Assets

- `assets/templates/ai-system-profile.md`
- `assets/templates/ai-rmf-gap-questionnaire.csv`
- `assets/templates/ai-risk-register.csv`
- `assets/templates/genai-risk-screening.csv`
- `assets/templates/tevv-plan.md`
- `assets/templates/human-oversight-plan.md`
- `assets/templates/go-no-go-memo.md`
- `assets/templates/incident-and-feedback-log.csv`
- `assets/templates/ai-system-inventory.csv`
- `assets/templates/cyber-ai-prioritization.md`

## Style Guidance

- Write like a risk advisor or governance lead, not a marketer.
- Keep outputs neutral, reusable, and evidence-oriented.
- Use NIST function names and subcategory IDs directly in tables when possible.
- Prefer observable evidence requests over abstract recommendations.
- Where a mapping is weak or conditional, say so explicitly.
- Distinguish baseline AI RMF guidance, GenAI-specific guidance, and cyber-AI guidance.
