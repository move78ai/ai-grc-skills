# Skills Catalog

This catalog is the fastest way to understand what sits where in the repository.

If you already know the problem you are solving, skip the umbrella skill and go straight to the relevant domain folder.

If you do **not** know where to start, begin with:

- [AI GRC and Regulatory umbrella skill](umbrella/ai-grc-and-regulatory/)

---

## Umbrella controller

| Skill | Purpose | Path |
|---|---|---|
| AI GRC and Regulatory | Intake and routing layer for the full library. Helps classify the user’s problem and point to the right domain skill. | `umbrella/ai-grc-and-regulatory/` |

---

## Frameworks

| Skill | What it is for | Path |
|---|---|---|
| ISO 42001 Governance | AI management system scoping, self-assessment, SoA drafting, policy drafting, governance design, and crosswalk work. | `skills/frameworks/iso-42001-governance/` |
| NIST AI RMF Governance | AI RMF adoption, trustworthy AI analysis, gap analysis, profiles, TEVV planning, GenAI review, cyber-AI prioritization, and crosswalks. | `skills/frameworks/nist-ai-rmf-governance/` |
| NIST AI 600-1 GenAI Risk Management | GenAI risk screening, content provenance planning, supplier review, incident disclosure planning, and evidence-pack drafting. | `skills/frameworks/nist-ai-600-1-genai-risk-management/` |
| OECD AI Governance and Classification | OECD-based AI system classification, lifecycle-stage governance, inventory records, and principle-to-action operationalization. | `skills/frameworks/oecd-ai-governance-and-classification/` |
| Financial Services AI Risk Management Framework | Sector-specific AI governance for financial institutions, with control mapping, evidence planning, and exam-readiness outputs. | `skills/frameworks/financial-services-ai-risk-management-framework/` |

---

## Regulations

| Skill | What it is for | Path |
|---|---|---|
| EU AI Act Compliance | Scope checks, prohibited-practice screening, high-risk classification, FRIA work, technical documentation, GPAI readiness, and post-market monitoring. | `skills/regulations/eu-ai-act-compliance/` |
| Colorado AI Act Impact Assessment | Colorado SB24-205 / SB25B-004 high-risk screening, deployer impact assessments, consumer notices, developer documentation requests, and readiness analysis. | `skills/regulations/colorado-ai-act-impact-assessment/` |
| South Korea High-Impact AI Readiness | South Korea AI Basic Act readiness, high-impact screening, transparency/labeling analysis, risk planning, explanation feasibility, and domestic representative readiness. | `skills/regulations/south-korea-high-impact-ai-readiness/` |

---

## Agentic and security

| Skill | What it is for | Path |
|---|---|---|
| Agentic AI Governance | Use-case suitability, bounded autonomy, accountability, human oversight, rollout planning, and residual-risk decisions for agentic systems. | `skills/agentic-and-security/agentic-ai-governance/` |
| Agentic AI Security | Threat modeling, least-agency design, memory/context risk review, supply-chain hardening, observability, and incident planning for agentic applications. | `skills/agentic-and-security/agentic-ai-security/` |
| MITRE ATLAS AI Security | Threat-informed AI security review using MITRE ATLAS for AI-enabled systems, including threat models, detections, exercises, and residual-risk outputs. | `skills/agentic-and-security/mitre-atlas-ai-security/` |
| MITRE ATLAS to Controls Mapping | Converts ATLAS-informed threat findings into derivative ISO 42001 control themes, evidence needs, implementation actions, and decision outputs. | `skills/agentic-and-security/mitre-atlas-to-controls-mapping/` |
| OWASP Agentic AI Mapping to ISO 42001 | Maps OWASP Agentic AI Top 10 findings into ISO 42001 clauses, Annex A controls, evidence requirements, and implementation actions. | `skills/agentic-and-security/owasp-agentic-ai-mapping-to-iso-42001/` |

---

## Inventory and suppliers

| Skill | What it is for | Path |
|---|---|---|
| AI System Inventory Shadow AI Discovery | Enterprise AI inventory design, shadow AI discovery, classification, ownership mapping, dependency documentation, and remediation planning. | `skills/inventory-and-suppliers/ai-system-inventory-shadow-ai-discovery/` |
| AIBOM AI Bill of Materials | AI bill of materials creation and maintenance for systems, models, agents, datasets, providers, tools, and dependencies. | `skills/inventory-and-suppliers/aibom-ai-bill-of-materials/` |
| Third-Party AI Supplier Risk | Supplier due diligence, evidence requests, contract/SLA controls, monitoring, contingency planning, and third-party approval decisions. | `skills/inventory-and-suppliers/third-party-ai-supplier-risk/` |

---

## Assurance and oversight

| Skill | What it is for | Path |
|---|---|---|
| TEVV AI Assurance Pre-Deployment Testing | TEVV program design, pre-deployment test plans, metric thresholds, go/no-go packages, and readiness assessments. | `skills/assurance-and-oversight/tevv-ai-assurance-pre-deployment-testing/` |
| Human Oversight Meaningful Human Control | Oversight mode selection, checkpoint and override design, escalation, appeal, competency, and oversight effectiveness reviews. | `skills/assurance-and-oversight/human-oversight-meaningful-human-control/` |
| AI Board Reporting Executive Oversight | Board-ready reporting, executive dashboards, top-risk registers, residual-risk memos, incident briefings, and management action tracking. | `skills/assurance-and-oversight/ai-board-reporting-executive-oversight/` |
| AI Incident Management Incident Disclosure | AI incident response design, incident classification, severity triage, escalation, disclosure decisions, after-action reviews, and operator artifacts. | `skills/assurance-and-oversight/ai-incident-management-incident-disclosure/` |

---

## Risk and landscape

| Skill | What it is for | Path |
|---|---|---|
| MIT AI Risk Repository | Practical risk identification, classification, prioritization, mitigation planning, and risk-register generation using MIT’s risk repository structure. | `skills/risk-and-landscape/mit-ai-risk-repository/` |
| MIT AI Governance Mapping | Governance landscape analysis across frameworks, laws, standards, and guidance using MIT’s governance mapping lens. | `skills/risk-and-landscape/mit-ai-governance-mapping/` |

---

## Transparency and provenance

| Skill | What it is for | Path |
|---|---|---|
| Content Provenance Synthetic Media Transparency | Provenance design, synthetic media transparency controls, disclosure and labeling logic, supplier capability review, and rollout planning. | `skills/transparency-and-provenance/content-provenance-synthetic-media-transparency/` |

---

## Suggested starting points by use case

### If the problem is “Which framework should I use?”
Start with:
- `skills/frameworks/iso-42001-governance/`
- `skills/frameworks/nist-ai-rmf-governance/`
- `skills/frameworks/oecd-ai-governance-and-classification/`

### If the problem is “What law applies?”
Start with:
- `skills/regulations/eu-ai-act-compliance/`
- `skills/regulations/colorado-ai-act-impact-assessment/`
- `skills/regulations/south-korea-high-impact-ai-readiness/`

### If the problem is “How do I govern or secure an agentic system?”
Start with:
- `skills/agentic-and-security/agentic-ai-governance/`
- `skills/agentic-and-security/agentic-ai-security/`
- `skills/agentic-and-security/mitre-atlas-ai-security/`

### If the problem is “How do I manage inventory, suppliers, or dependencies?”
Start with:
- `skills/inventory-and-suppliers/ai-system-inventory-shadow-ai-discovery/`
- `skills/inventory-and-suppliers/aibom-ai-bill-of-materials/`
- `skills/inventory-and-suppliers/third-party-ai-supplier-risk/`

### If the problem is “How do I test, oversee, or report on this?”
Start with:
- `skills/assurance-and-oversight/tevv-ai-assurance-pre-deployment-testing/`
- `skills/assurance-and-oversight/human-oversight-meaningful-human-control/`
- `skills/assurance-and-oversight/ai-board-reporting-executive-oversight/`
- `skills/assurance-and-oversight/ai-incident-management-incident-disclosure/`

### If the problem is “How do I classify risk or understand the governance landscape?”
Start with:
- `skills/risk-and-landscape/mit-ai-risk-repository/`
- `skills/risk-and-landscape/mit-ai-governance-mapping/`
- `skills/frameworks/oecd-ai-governance-and-classification/`

### If the problem is “How do I handle provenance, labels, or synthetic media?”
Start with:
- `skills/transparency-and-provenance/content-provenance-synthetic-media-transparency/`

---

## Operating note

This repository is intentionally modular.

The umbrella skill gives the library a unified front door, but the standalone domain skills remain the real working units. That keeps the repo easier to maintain, easier to update, and easier to use.