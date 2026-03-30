---
name: mit-ai-risk-repository
description: comprehensive workflow skill for using the mit ai risk repository as a practical risk identification, classification, prioritization, and mitigation-planning tool for ai systems, models, agents, data pipelines, and supplier-provided ai capabilities. use when chatgpt needs to classify ai risk exposure against mit's domain and causal taxonomies, build a risk register, prioritize risks for one use case or portfolio, prepare mitigation and evidence plans, run a scored gap assessment, route work into governance, security, supplier, transparency, or incident workflows, or produce executive-ready ai risk summaries for ciso, cro, legal, assurance, product, and audit stakeholders.
---

# MIT AI Risk Repository

Use this skill to turn MIT's AI Risk Repository into working risk-management artifacts, not summaries.

Default audience: ciso, chief risk officer, legal counsel, product risk, security, assurance, audit, procurement, data governance, model governance, and executive oversight teams.

Default style: detailed, comprehensive, and actionable. Prefer decision-ready risk registers, mitigation plans, evidence requests, ownership assignments, and executive summaries over narrative explanation.

## Workflow decision tree

1. Determine the task type.
   - **Classify one AI system, model, agent, or use case against MIT risk domains and causal factors** -> use `scripts/profile_builder.py` with the system risk profile template.
   - **Build or refine a MIT-aligned risk register** -> follow **Risk register workflow**.
   - **Prioritize risks and turn them into mitigation actions** -> follow **Mitigation planning workflow**.
   - **Run a scored current-state or readiness assessment** -> use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Look up a risk domain, causal factor, mitigation category, evidence type, or routing suggestion** -> use `scripts/risk_lookup.py`.
   - **Prepare executive, legal, or residual-risk outputs** -> follow **Decision workflow**.

2. Produce artifacts, not theory.
   Always generate one or more templates from `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and continue.
   If the deployment context, supplier footprint, customer impact, or lifecycle stage is incomplete, infer the most likely AI environment, label assumptions, and proceed.

## Core operating rules

- Treat the MIT AI Risk Repository as the primary risk-identification and classification lens in this skill.
- Treat the MIT AI Risk Mitigation Map as the primary mitigation-routing lens in this skill.
- Treat this skill as derivative operator guidance, not as an official MIT publication.
- Always separate the object being assessed: model, agent, application, data pipeline, AI-enabled workflow, third-party service, provider, or portfolio.
- Use both MIT taxonomies when possible: domain taxonomy for what can go wrong and causal taxonomy for how, when, and by whom the risk manifests.
- Do not stop at naming risks. Convert them into owners, mitigations, evidence, review cadence, and decision outputs.
- Distinguish between present risks, plausible emerging risks, and unknowns that need investigation.
- Require evidence language. For every material risk, specify the artifact, log, review record, or evidence that would prove the mitigation exists.
- When the user asks for a decision, conclude with one of: **proceed**, **proceed with conditions**, **hold pending remediation**, **restricted deployment only**, or **do not proceed**.
- Keep outputs public-safe. Do not reproduce copyrighted or gated MIT source documents. Use derivative summaries, tables, and templates only.

## Default output structure

Unless the user asks for another structure, use this format:

# [title]

## 1. executive summary
- system or use-case scope
- top MIT risk domains in scope
- top causal factors or triggers
- decision recommendation
- top blockers or required conditions

## 2. system and risk context
- deployment pattern
- user and stakeholder impact
- third-party dependencies
- lifecycle stage and change exposure

## 3. risk posture
| risk domain | causal factor | main concern | priority | owner |
|---|---|---|---|---|

## 4. mitigation and evidence requirements
| risk | mitigation category | key action | evidence needed | owner |
|---|---|---|---|---|

## 5. prioritized action plan
| priority | action | risk route | owner | due date |
|---|---|---|---|---|

## 6. residual risk and next review
- residual-risk position
- approval conditions
- next review point
- downstream skill handoff if needed

## Risk register workflow

Use this when the user needs a starter MIT-aligned risk register for one AI system, use case, supplier, or portfolio slice.

1. Start from `assets/templates/ai-system-risk-profile.csv`.
2. Run:
   `python scripts/profile_builder.py <input_csv> <output_dir>`
3. Review the generated outputs:
   - `starter_profile.md`
   - `prioritized_risks.csv`
4. Use:
   - `references/domain-taxonomy.csv`
   - `references/causal-taxonomy.csv`
   - `references/mitigation-categories.csv`
   - `references/framework-next-steps.csv`
5. Populate:
   - `assets/templates/mit-risk-register.csv`
   - `assets/templates/mitigation-plan.csv`
6. If the input shows supplier dependence, synthetic-media issues, governance immaturity, or incident exposure, route follow-on work into the relevant downstream skill using `references/framework-next-steps.csv`.

## Mitigation planning workflow

Use this when the user asks what to do about the identified risks or how to prioritize action.

1. Start from:
   - `assets/templates/mitigation-plan.csv`
   - `assets/templates/evidence-request-checklist.csv`
   - `references/mitigation-categories.csv`
   - `references/evidence-catalog.csv`
2. For each material risk, define:
   - risk owner
   - mitigation category
   - concrete implementation action
   - evidence artifact
   - review cadence
   - whether the action is first-party, provider-dependent, or supplier-dependent
3. Distinguish between:
   - governance and oversight actions
   - technical and security actions
   - operational process actions
   - transparency and accountability actions
4. Note where a deeper downstream skill should take over.

## Gap-analysis workflow

Use this when the user wants a scored current-state assessment or remediation plan.

1. Copy `assets/templates/mit-risk-gap-questionnaire.csv` and fill `score`, `owner`, `evidence`, and `notes`.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Review and use:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `residual_risk_profile.csv`
4. Tailor the summary for the audience:
   - ciso -> operational exposure, monitoring, attack surface, and third-party visibility
   - chief risk officer -> materiality, concentration, conditions to proceed, residual-risk posture
   - legal counsel -> documentation, user impact, disclosure, supplier dependency, and accountability
   - audit or assurance -> evidence sufficiency, ownership traceability, corrective actions, review cadence

## Decision workflow

Use this when the user needs an executive, legal, or risk-acceptance output.

1. Start from:
   - `assets/templates/executive-risk-summary.md`
   - `assets/templates/residual-risk-acceptance-memo.md`
   - `assets/templates/review-and-decision-log.csv`
2. Tie each material risk to:
   - MIT risk domain
   - MIT causal factors
   - mitigation category
   - current evidence status
   - missing action
   - owner and next review point
3. Use `references/decision-rules.csv` when the user wants a clear deployment posture.
4. End with a decision and a named next review point.

## Script quick reference

- `scripts/profile_builder.py`
  - build a starter MIT-aligned risk profile for one AI-enabled system or use case
- `scripts/gap_analysis.py`
  - summarize a scored questionnaire into priorities and a residual-risk profile
- `scripts/risk_lookup.py`
  - search domains, causal factors, mitigation categories, evidence types, and next-step routes

## Resource map

### references/
- `how-the-skill-uses-the-sources.md` -> explains source grounding and derivative-use boundaries
- `implementation-workflows.md` -> concise workflow and decision rules for repeat use
- `publication-and-copyright-boundaries.md` -> public-distribution safety note
- `domain-taxonomy.csv` -> derivative MIT risk domains and practical usage notes
- `causal-taxonomy.csv` -> derivative causal factors and operator interpretation notes
- `mitigation-categories.csv` -> derivative mitigation routing categories informed by MIT's mitigation map
- `risk-prioritization-factors.csv` -> practical scoring factors for using this skill
- `evidence-catalog.csv` -> evidence types and what they demonstrate
- `decision-rules.csv` -> simple decision logic for deployment posture and review triggers
- `framework-next-steps.csv` -> where to route follow-on work into governance, supplier risk, incident, transparency, provenance, or atlas workflows

### assets/templates/
- `ai-system-risk-profile.csv`
- `mit-risk-register.csv`
- `mit-risk-gap-questionnaire.csv`
- `mitigation-plan.csv`
- `evidence-request-checklist.csv`
- `executive-risk-summary.md`
- `residual-risk-acceptance-memo.md`
- `review-and-decision-log.csv`

## Final checks before answering

Before finalizing an output, check that it answers these questions:
- what AI-enabled system, workflow, or supplier capability is in scope?
- which MIT risk domains matter most and why?
- which causal factors matter most and why?
- what mitigation categories and concrete actions are most relevant now?
- what evidence exists and what is missing?
- who owns implementation, review, and residual-risk acceptance?
- what is the decision and what must happen before the next review?
