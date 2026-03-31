---
name: ai-grc-and-regulatory
description: "Workflow-first router for AI GRC tasks that classifies the request, routes it to the right skill family, and returns decision-ready outputs."
---

# AI GRC and Regulatory

Use this skill as the umbrella entry point for the broader AI GRC skill library. Its job is to classify the user's task, route the work into the right workflow family, and return outputs in one consistent operator style.






Default audience: CISOs, Chief Risk Officers, legal counsel, compliance teams, audit leads, procurement owners, and product-governance operators.

Default style: Operator-grade, workflow-first, and explicit about scope, ownership, evidence, and decision gates.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. Determine the primary task family.
   - **Build or assess a governance framework, operating model, or crosswalk** -> use the **framework governance route** in `references/framework-governance-route.md`.
   - **Screen regulatory scope, obligations, notices, impact assessments, or jurisdiction-specific readiness** -> use the **regulatory route** in `references/regulatory-route.md`.
   - **Inventory systems, classify systems, manage dependencies, or assess suppliers** -> use the **inventory, supplier, and dependency route** in `references/inventory-supplier-route.md`.
   - **Threat-model, secure, test, or convert threat findings into controls** -> use the **security and threat route** in `references/security-threat-route.md`.
   - **Run TEVV, human oversight, incident, board, or executive oversight work** -> use the **assurance and oversight route** in `references/assurance-oversight-route.md`.
   - **Handle provenance, synthetic media transparency, MIT risk mapping, MIT governance mapping, or OECD classification/governance work** -> use the **classification, provenance, and landscape route** in `references/classification-landscape-route.md`.
   - **The request spans several domains** -> start with `assets/templates/unified-intake-profile.md`, then route each workstream separately and merge the output using `references/common-output-contract.md`.

2. Produce artifacts, not theory.
   Always generate one or more structured outputs unless the user explicitly asks for prose only.

3. State assumptions and proceed.
   If facts are missing, label assumptions, identify unknowns, and continue.

## Core operating rules

- Treat this skill as an orchestration layer, not as a replacement for domain-specific depth.
- Classify the object in scope before recommending actions: framework, law, system, agent, model, supplier, portfolio, incident, board pack, or media workflow.
- Separate these five questions:
  1. what is in scope,
  2. what decision is being made,
  3. which workflow family applies,
  4. what evidence artifacts are needed,
  5. who owns implementation and next review.
- When a task spans multiple domains, keep the workstream split explicit. Do not collapse governance, legal, security, supplier, and incident logic into one blurred recommendation.
- Use the bundled catalog in `references/skill-domain-catalog.csv` to decide which branch or branches are relevant.
- Use the common templates in `assets/templates/` when no narrower domain template is available.
- Keep outputs public-safe. Use derivative summaries, tables, and templates only.
- When the user asks for a decision, conclude with one of: **proceed**, **proceed with conditions**, **hold pending remediation**, **restricted use only**, or **do not proceed** unless a child workflow requires a narrower label.

## Default output contract

Unless a route-specific template is better, use this structure:

# [title]

## 1. executive summary
- scope reviewed
- primary task family
- current posture
- decision recommendation
- top blockers or required conditions

## 2. scope and assumptions
- object in scope
- actor or operator role
- systems, suppliers, jurisdictions, or stakeholders affected
- knowns, assumptions, and unknowns

## 3. workflow findings
| area | main finding | why it matters | owner |
|---|---|---|---|

## 4. required artifacts and evidence
| artifact | why it is needed | owner | timing |
|---|---|---|---|

## 5. prioritized action plan
| priority | action | route | owner | due date |
|---|---|---|---|---|

## 6. decision and next review
- decision status
- conditions or hold points
- residual-risk position
- next review date or trigger

## Route selection guidance

### Framework governance route
Use for management systems, principles-to-action work, governance operating models, and crosswalks.
See `references/framework-governance-route.md`.

### Regulatory route
Use for EU AI Act, Colorado, South Korea, and related jurisdiction-specific readiness.
See `references/regulatory-route.md`.

### Inventory, supplier, and dependency route
Use for AI inventory, shadow AI, AIBOM, supplier risk, and dependency reviews.
See `references/inventory-supplier-route.md`.

### Security and threat route
Use for agentic security, OWASP mapping, MITRE ATLAS security, MITRE ATLAS controls mapping, and control-routing after threat analysis.
See `references/security-threat-route.md`.

### Assurance and oversight route
Use for TEVV, oversight, incident management, board reporting, and executive decision materials.
See `references/assurance-oversight-route.md`.

### Classification, provenance, and landscape route
Use for OECD classification, content provenance, MIT risk repository work, and MIT governance mapping.
See `references/classification-landscape-route.md`.

## Bundled resources

### references/
- `skill-domain-catalog.csv` -> portfolio-wide routing map covering all integrated child skills
- `common-output-contract.md` -> shared output logic and merger rules for multi-domain work
- `framework-governance-route.md` -> route for ISO, NIST, OECD, and framework operating work
- `regulatory-route.md` -> route for EU AI Act, Colorado, and South Korea readiness
- `inventory-supplier-route.md` -> route for inventory, AIBOM, and third-party risk
- `security-threat-route.md` -> route for agentic security, OWASP, and MITRE work
- `assurance-oversight-route.md` -> route for TEVV, oversight, incident, and board outputs
- `classification-landscape-route.md` -> route for OECD, provenance, MIT risk, and MIT governance mapping
- `publication-and-copyright-boundaries.md` -> umbrella public-distribution note

### assets/templates/
- `unified-intake-profile.md`
- `unified-action-register.csv`
- `executive-decision-memo.md`
- `residual-risk-note.md`
- `multi-domain-routing-log.csv`

## Final checks before answering

Before finalizing an output, check that it answers these questions:
- what object, system, law, framework, or portfolio is in scope?
- which route or routes are being used and why?
- what evidence exists and what is missing?
- who owns implementation, review, and residual-risk acceptance?
- what is the decision and what must happen before the next review?
