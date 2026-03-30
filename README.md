# AI GRC Skills

A practical open library of workflow-first skills for AI governance, risk, compliance, assurance, and regulatory work.

This repository is built for people who need to **do the work**, not just talk about it. The skills here are designed to turn frameworks, laws, and threat models into usable artifacts: screening memos, gap assessments, inventories, evidence packs, control trackers, board summaries, supplier reviews, incident materials, and deployment decisions.

The point is simple: most AI governance material stays too abstract for operators. This repo does the opposite.

## What this repository is

This is a modular library of standalone skills covering:

- core AI governance frameworks
- major regulatory workflows
- agentic AI governance and security
- AI inventory, AIBOM, and supplier risk
- TEVV, incident, oversight, and executive reporting
- MIT and MITRE risk and mapping workflows
- provenance and synthetic media transparency

Each skill is meant to stand on its own.

There is also one umbrella controller skill in `umbrella/ai-grc-and-regulatory/`. That umbrella skill is a router. It helps classify the user’s problem and point to the right domain skill. It is **not** a giant merged super-skill, and that is deliberate.

## Who this is for

This library is aimed at:

- CISOs
- Chief Risk Officers
- legal counsel
- compliance teams
- audit and assurance teams
- AI governance leads
- procurement and supplier-risk teams
- product and platform teams dealing with regulated or high-impact AI
- consultants and practitioners who need structured starting points

If you are looking for blog-style explainers, this repo is probably not for you.

## How the library is organized

The repo is organized by operating need, not by theory.

- `umbrella/`  
  Contains the controller skill that routes users to the right domain skill.

- `skills/frameworks/`  
  Framework-led governance and classification skills.

- `skills/regulations/`  
  Jurisdiction-specific regulatory readiness and compliance skills.

- `skills/agentic-and-security/`  
  Agentic governance, agentic security, OWASP, and MITRE ATLAS skills.

- `skills/inventory-and-suppliers/`  
  Inventory, AIBOM, and third-party AI governance skills.

- `skills/assurance-and-oversight/`  
  TEVV, incident, oversight, and executive reporting skills.

- `skills/risk-and-landscape/`  
  MIT risk and governance-mapping skills.

- `skills/transparency-and-provenance/`  
  Provenance, synthetic media transparency, and content-credentialing workflows.

## Skill categories

### Frameworks
- [ISO 42001 Governance](skills/frameworks/iso-42001-governance/)
- [NIST AI RMF Governance](skills/frameworks/nist-ai-rmf-governance/)
- [NIST AI 600-1 GenAI Risk Management](skills/frameworks/nist-ai-600-1-genai-risk-management/)
- [OECD AI Governance and Classification](skills/frameworks/oecd-ai-governance-and-classification/)
- [Financial Services AI Risk Management Framework](skills/frameworks/financial-services-ai-risk-management-framework/)

### Regulations
- [EU AI Act Compliance](skills/regulations/eu-ai-act-compliance/)
- [Colorado AI Act Impact Assessment](skills/regulations/colorado-ai-act-impact-assessment/)
- [South Korea High-Impact AI Readiness](skills/regulations/south-korea-high-impact-ai-readiness/)

### Agentic and security
- [Agentic AI Governance](skills/agentic-and-security/agentic-ai-governance/)
- [Agentic AI Security](skills/agentic-and-security/agentic-ai-security/)
- [MITRE ATLAS AI Security](skills/agentic-and-security/mitre-atlas-ai-security/)
- [MITRE ATLAS to Controls Mapping](skills/agentic-and-security/mitre-atlas-to-controls-mapping/)
- [OWASP Agentic AI Mapping to ISO 42001](skills/agentic-and-security/owasp-agentic-ai-mapping-to-iso-42001/)

### Inventory and suppliers
- [AI System Inventory Shadow AI Discovery](skills/inventory-and-suppliers/ai-system-inventory-shadow-ai-discovery/)
- [AIBOM AI Bill of Materials](skills/inventory-and-suppliers/aibom-ai-bill-of-materials/)
- [Third-Party AI Supplier Risk](skills/inventory-and-suppliers/third-party-ai-supplier-risk/)

### Assurance and oversight
- [TEVV AI Assurance Pre-Deployment Testing](skills/assurance-and-oversight/tevv-ai-assurance-pre-deployment-testing/)
- [Human Oversight Meaningful Human Control](skills/assurance-and-oversight/human-oversight-meaningful-human-control/)
- [AI Board Reporting Executive Oversight](skills/assurance-and-oversight/ai-board-reporting-executive-oversight/)
- [AI Incident Management Incident Disclosure](skills/assurance-and-oversight/ai-incident-management-incident-disclosure/)

### Risk and landscape
- [MIT AI Risk Repository](skills/risk-and-landscape/mit-ai-risk-repository/)
- [MIT AI Governance Mapping](skills/risk-and-landscape/mit-ai-governance-mapping/)

### Transparency and provenance
- [Content Provenance Synthetic Media Transparency](skills/transparency-and-provenance/content-provenance-synthetic-media-transparency/)

## Start here

If you do not know where to begin, use the umbrella controller skill first:

- [AI GRC and Regulatory umbrella skill](umbrella/ai-grc-and-regulatory/)

If you already know the problem category, go straight to the domain skill.

A simple rule:
- governance framework problem -> start in `skills/frameworks/`
- law or jurisdiction problem -> start in `skills/regulations/`
- agentic threat or hardening problem -> start in `skills/agentic-and-security/`
- inventory, BOM, or vendor problem -> start in `skills/inventory-and-suppliers/`
- testing, oversight, incident, or board problem -> start in `skills/assurance-and-oversight/`

## How to install or use a skill

There are two ways to use this library.

### 1. Browse the source
Open the skill folder and review:
- `SKILL.md`
- `references/`
- `assets/`
- `scripts/`

This is useful if you want to understand how the skill is structured or adapt it.

### 2. Download the packaged skill
Packaged `skill.zip` files are published through GitHub Releases.

Use Releases when you want the ready-to-upload bundle rather than the raw source structure.

See:
- [Skill installation guide](docs/skill-installation.md)
- [Release policy](docs/release-policy.md)

## Release downloads

Published releases are the download layer for the library.

Expected release assets include:
- `ai-grc-and-regulatory-skill.zip`
- one `*-skill.zip` file for each standalone skill

The repo keeps the source. Releases carry the portable packaged bundles.

## Repository map

For the file and folder layout, see:
- [Repo map](docs/repo-map.md)
- [Skills catalog](SKILLS-CATALOG.md)
- [Naming conventions](docs/naming-conventions.md)

## Related projects

This repo is part of a wider public body of work around practical AI governance and regulatory implementation.

- [Move78 International](https://www.move78int.com)
- [EU AI Compass](https://www.euaicompass.com)

Those sites are where broader public resources, products, and operating context live. This repo stays focused on the open skill library.

## License

This repository is licensed under the terms in the [LICENSE](LICENSE) file.

## Notes

A few boundaries matter:

- These skills are implementation aids, not legal advice.
- Crosswalks are support tools, not claims of legal equivalence.
- Public packaging uses derivative tables, templates, and workflow logic rather than reproducing copyrighted standards or source texts.
- The repo is modular on purpose. That is a feature, not unfinished work.