---
name: agentic-ai-security
description: comprehensive workflow skill for securing agentic ai applications using owasp top 10 for agentic applications 2026 as the primary threat taxonomy, with nist cyber ai profile and nist genai security concepts as complementary operating anchors. use when chatgpt needs to build agent threat models, assess least-agency boundaries, design tool and privilege controls, review memory and context risks, evaluate insecure inter-agent communication, harden supply chains and dependencies, plan observability and incident response, run agentic security gap analysis, or produce evidence-oriented security artifacts for cisos, chief risk officers, legal counsel, security architects, red teams, and engineering leads.
---

# Agentic AI Security

## Overview

Use this skill to turn agentic-ai security questions into implementation-grade artifacts, not tutorials. Treat the OWASP Top 10 for Agentic Applications 2026 as the primary threat taxonomy, then use the NIST Cyber AI Profile and NIST GenAI security concepts to structure control priorities, monitoring expectations, and incident handling.

Default audience: ciso, chief risk officer, legal counsel, security architect, red team lead, platform owner, and engineering lead.

Default style: detailed, comprehensive, and actionable. Prefer decision-ready outputs, explicit threat assumptions, evidence artifacts, control owners, logging requirements, and deployment conditions.

## Workflow decision tree

1. Determine the task type.
   - **Threat-model an agentic system or use case** → follow **Threat-model workflow**.
   - **Review autonomy, tools, permissions, or identities** → follow **Least-agency and access-control workflow**.
   - **Assess memory, context, prompts, or inter-agent trust boundaries** → follow **State and communication workflow**.
   - **Assess suppliers, dependencies, MCP or external components** → follow **Supply-chain workflow**.
   - **Prepare monitoring, detection, containment, or incident plans** → follow **Detection and response workflow**.
   - **Run a structured security gap analysis** → use `scripts/gap_analysis.py` with the gap questionnaire template.
   - **Create a starter ASI profile from structured system data** → use `scripts/threat_mapper.py` with the system security profile template.
   - **Search the control library or ASI mapping tables** → use `scripts/control_lookup.py`.

2. Produce artifacts, not theory.
   Always generate one or more of the templates in `assets/templates/` unless the user explicitly asks for prose only.

3. State assumptions and proceed.
   If the user does not supply complete architecture detail, state reasonable assumptions and continue. Do not block on perfect inputs.

## Core operating rules

- Treat the OWASP Top 10 for Agentic Applications 2026 as the primary risk taxonomy: ASI01 through ASI10.
- Treat **least-agency**, **least privilege**, **strong observability**, **environment isolation**, and **fast containment** as the default design stance.
- Distinguish security from governance. Include governance interfaces where needed, but keep this skill focused on threat modeling, hardening, monitoring, containment, and evidence of security control operation.
- Always separate five layers of analysis:
  1. architecture and trust boundaries,
  2. ASI threat exposure,
  3. control and mitigation design,
  4. monitoring and incident readiness,
  5. residual-risk and deployment decision.
- Always identify these facts before drafting outputs:
  1. agent pattern and topology,
  2. tool access and action-space,
  3. identity model and credential handling,
  4. memory and context model,
  5. inter-agent communication paths,
  6. external systems and data stores,
  7. supplier and package dependencies,
  8. deployment environments,
  9. monitoring and logging coverage,
  10. human override or kill-switch design.
- When the user asks whether deployment should proceed, conclude with one of: **deploy**, **deploy with conditions**, **hold**, or **block pending remediation**.
- For every material recommendation, name the evidence artifact that would prove implementation: threat model, allowlist, identity matrix, log design, test report, architecture review, supplier review, incident playbook, or deployment decision memo.
- Prefer bounded tool use over broad tool access. If a tool can change state, spend money, delete data, communicate externally, write code, or modify infrastructure, default to stronger authorization and stronger logging.
- Treat non-human identities, credentials, model context, and agent memory as primary attack surfaces.
- Treat multi-agent systems as materially higher risk whenever they share memory, credentials, tool channels, or decision authority.
- Do not reproduce copyrighted source documents or long verbatim excerpts. Use derivative summaries, IDs, tables, and templates only.

## Default output structure

Unless the user requests a different format, use this structure:

# [title]

## 1. executive summary
- system in scope
- primary threat drivers
- most exposed ASI categories
- highest-priority controls
- deployment recommendation

## 2. architecture and trust assumptions
- topology and agents
- tools, memory, and external systems
- identities and privileges
- communication paths
- human oversight or approval points

## 3. threat findings
| ASI category | why it applies | severity | attack path | current controls | gaps |
|---|---|---|---|---|---|

## 4. required controls and evidence
| area | required control | owner | evidence |
|---|---|---|---|

## 5. monitoring and incident readiness
- logging requirements
- anomaly and abuse indicators
- containment triggers
- kill-switch or deactivation conditions

## 6. prioritized action plan
| priority | action | owner | target timing | dependency |
|---|---|---|---|---|

## 7. residual risk and deployment decision
- unresolved exposure
- acceptance conditions
- escalation path
- recommended decision

Adapt this structure only when a bundled template is a better fit.

## Threat-model workflow

Use this when the user asks for a threat model, security review, or top risks for an agentic system.

1. Capture or infer the following from the request:
   - system objective and business process
   - single-agent or multi-agent topology
   - tool use and state-changing actions
   - identity and privilege model
   - memory, context, and retrieval mechanisms
   - external data sources and communication paths
   - deployment environment and trust boundaries
2. If structured input is useful, start from `assets/templates/agentic-system-security-profile.csv`.
3. Run `scripts/threat_mapper.py` if Python execution is available.
4. Translate the output into a threat model using `assets/templates/agent-threat-model.md`.
5. Always cover all ten ASI categories, even if some are rated low.

## Least-agency and access-control workflow

Use this when the user asks about permissions, identities, tools, approval gates, or autonomy hardening.

1. Use `assets/templates/tool-and-action-allowlist.csv` and `assets/templates/identity-and-privilege-matrix.csv`.
2. Evaluate:
   - which tools are enabled,
   - which actions are read-only versus state-changing,
   - which identities are used,
   - where secrets are stored,
   - whether identities are shared across agents or environments,
   - where human approval is mandatory.
3. Consult `references/least-agency-principles.csv` and `references/agentic-security-control-library.csv`.
4. If the user asks for policy language, draft control statements plus the matrix.
5. For high-risk uses, require short-lived credentials, scoped identities, explicit approvals, and separate audit logs.

## State and communication workflow

Use this when the user asks about prompt injection, memory poisoning, context abuse, inter-agent protocols, or cascading failures.

1. Start from:
   - `assets/templates/memory-and-context-risk-register.csv`
   - `assets/templates/inter-agent-communication-review.md`
2. Evaluate:
   - persistent memory design,
   - context ingestion,
   - separation of instructions from untrusted content,
   - shared versus isolated memory,
   - protocol trust assumptions,
   - message signing, validation, and source attribution,
   - blast-radius controls for cross-agent failures.
3. Prioritize ASI01, ASI06, ASI07, ASI08, and ASI10 when the system is collaborative or tool-using.
4. Require explicit deactivation and containment paths if poisoned state can propagate.

## Supply-chain workflow

Use this when the user needs package, supplier, dependency, AIBOM, MCP, or third-party security review.

1. Start from `assets/templates/supplier-and-aibom-review.csv` and `references/owasp-agentic-aibom-relationship.csv`.
2. Assess:
   - model provider dependencies,
   - orchestration libraries,
   - tool plugins and MCP servers,
   - package provenance,
   - update channels,
   - signing and integrity verification,
   - fallback and revocation paths.
3. If the system depends on multiple third parties, also evaluate concentrated failure and cascading-failure risk.
4. Require a known-supplier list, update monitoring, and revocation criteria before recommending deployment.

## Detection and response workflow

Use this when the user asks for logging, abuse detection, response, or kill-switch design.

1. Start from:
   - `assets/templates/monitoring-and-detection-plan.md`
   - `assets/templates/incident-containment-playbook.md`
   - `assets/templates/secure-deployment-checklist.md`
2. Use `references/nist-cyber-ai-security-anchors.csv` to add NIST-style monitoring and containment expectations.
3. Ensure the plan covers:
   - separate AI traffic and event logging,
   - tool invocation logging,
   - identity and approval traces,
   - anomaly indicators,
   - rapid disable or privilege reduction for compromised agents,
   - eradication actions for poisoned data, libraries, or tools,
   - recovery criteria.
4. When the user asks for a deployment decision, finish with `assets/templates/deployment-decision-memo.md`.

## Gap-analysis workflow

Use this when the user wants a maturity rating, remediation roadmap, or control baseline assessment.

1. Copy `assets/templates/agentic-security-gap-questionnaire.csv` and complete the `score`, `evidence`, and `notes` columns.
2. Run:
   `python scripts/gap_analysis.py <input_csv> <output_dir>`
3. Convert outputs into a board-ready summary and action plan:
   - `gap_summary.md`
   - `prioritized_actions.csv`
   - `risk_register.csv`
4. Tailor the emphasis to the audience:
   - ciso → architecture, logging, detection, containment, residual risk
   - chief risk officer → prioritization, scenario severity, supplier concentration, acceptance conditions
   - legal counsel → evidence retention, supplier terms, incident triggers, human approval and accountability records

## Script quick reference

- `scripts/threat_mapper.py`
  - build a starter ASI exposure profile from structured system data
- `scripts/gap_analysis.py`
  - convert a scored questionnaire into priorities and a risk register
- `scripts/control_lookup.py`
  - search the control library, ASI catalog, and NIST anchor tables

## Resource map

- `references/asi-top-10-catalog.csv`
  - concise catalog of ASI01-ASI10
- `references/agentic-threat-and-mitigation-matrix.csv`
  - threat-to-control mappings and evidence suggestions
- `references/agentic-security-control-library.csv`
  - reusable security controls and hardening actions
- `references/least-agency-principles.csv`
  - autonomy and permission design rules
- `references/nist-cyber-ai-security-anchors.csv`
  - NIST cyber AI profile anchors for secure, detect, respond, and supply-chain practices
- `references/owasp-agentic-aibom-relationship.csv`
  - supply-chain and AIBOM implications from the OWASP appendix
- `references/implementation-workflows.md`
  - expanded decision rules for recurring tasks
- `references/how-the-skill-uses-the-sources.md`
  - source hierarchy and intended use
- `references/publication-and-copyright-boundaries.md`
  - public-package restrictions

## Final quality check

Before finalizing any output, verify that it:
- names the agent pattern, trust boundaries, and most exposed ASI categories,
- specifies at least one evidence artifact for each major recommendation,
- includes logging and containment, not only prevention,
- states residual risk and a deployment recommendation,
- avoids vague advice such as "improve security" without concrete control language.
