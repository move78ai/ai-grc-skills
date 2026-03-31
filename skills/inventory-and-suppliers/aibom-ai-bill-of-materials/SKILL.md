---
name: aibom-ai-bill-of-materials
description: "Operator-grade AIBOM workflows for component inventories, provenance, dependency mapping, version tracking, and supplier evidence requests."
---

# AIBOM / AI Bill of Materials

Use this skill to create a structured AI Bill of Materials for a single AI system, an AI portfolio, or a supplier-provided AI capability.




Default audience: Governance, security, procurement, audit, platform, and supplier-risk teams documenting AI system components and dependencies.

Default style: Inventory-first, dependency-aware, and explicit about provenance, update history, and evidence gaps.

Public repo note: This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.

## Workflow decision tree

1. **Need to create a new AIBOM?**
   - Build the system profile first.
   - Populate the core AIBOM register.
   - Add dependency, provenance, and version records.

2. **Need to assess an existing AIBOM or incomplete inventory?**
   - Run the gap analysis workflow.
   - Identify missing components, ownership, supplier, provenance, and update-history fields.
   - Produce remediation actions.

3. **Need to review supplier-provided AI?**
   - Build a supplier evidence request pack.
   - Document model, dataset, API, runtime, and hosted-service dependencies.
   - Record contract, SLA, and monitoring implications.

4. **Need executive or audit output?**
   - Produce the executive AIBOM summary memo.
   - Highlight unknown dependencies, unsupported components, restricted providers, and high-impact change exposure.

## Core operating rules

- Treat the AIBOM as an operational control artifact, not a static inventory.
- Separate first-party, third-party, open-source, hosted-service, and user-supplied components.
- Record unknown fields explicitly as `unknown` rather than inferring them.
- Distinguish between model, dataset, tool, provider, runtime, orchestration, and deployment dependencies.
- Capture both current-state and change-history information.
- Flag components that materially affect security, privacy, safety, compliance, or business continuity.
- Prefer concise, decision-useful output over narrative explanation.

## Required output structure

Use this structure unless the user asks for a different format.

# [AIBOM analysis title]

## Executive summary
- Scope reviewed
- Key dependency findings
- Main risk flags
- Immediate actions

## AIBOM profile
- System / service name
- Owner
- Use case
- Deployment context
- Criticality

## Key findings
- Component coverage
- Provenance and versioning gaps
- Supplier and hosted-service gaps
- Monitoring / update exposure

## Recommended actions
1. [Action]
2. [Action]
3. [Action]

## Artifact outputs
- Templates completed
- Registers updated
- Evidence still required

## Build or assess an AIBOM

### A. New AIBOM build
1. Use `assets/templates/aibom-register.csv` as the base register.
2. Use `assets/templates/ai-component-intake.csv` for each significant component or service.
3. Use `assets/templates/dependency-map.csv` to record upstream and downstream dependencies.
4. Use `assets/templates/provenance-record.csv` and `assets/templates/update-change-log.csv` to capture lineage and changes.
5. If supplier dependencies exist, use `assets/templates/third-party-evidence-request.md`.
6. Summarize decision-relevant findings using `assets/templates/executive-aibom-summary-memo.md`.

### B. Existing AIBOM gap assessment
1. Ask for the current register or a description of the system stack.
2. Run `scripts/gap_analysis.py` against the available AIBOM CSV.
3. Map missing fields to the field catalog in `references/field-catalog.csv`.
4. Produce remediation priorities using the gap report.
5. Output a concise memo plus updated template list.

### C. Supplier review workflow
1. Use `assets/templates/third-party-evidence-request.md` to request missing BOM information.
2. Use `assets/templates/component-approval-memo.md` to document approval conditions.
3. Use `assets/templates/vulnerability-impact-review.csv` for exposure and patch-impact review.
4. Use `assets/templates/decommission-replacement-record.csv` if a component must be restricted or replaced.

## Scripts

### `scripts/gap_analysis.py`
Use to assess AIBOM completeness against the required field catalog.

Example:
```bash
python scripts/gap_analysis.py path/to/aibom-register.csv
```

### `scripts/profile_builder.py`
Use to generate a starter AIBOM profile JSON from prompt answers.

Example:
```bash
python scripts/profile_builder.py --name "Customer Service Copilot" --owner "AI Platform Team" --criticality high
```

### `scripts/control_lookup.py`
Use to look up AIBOM field requirements and control themes.

Example:
```bash
python scripts/control_lookup.py provenance
```

## References

- `references/component-taxonomy.csv` — component types and definitions.
- `references/field-catalog.csv` — required and optional AIBOM fields.
- `references/provenance-versioning-controls.csv` — lineage and versioning control themes.
- `references/dependency-update-tracking.csv` — change and dependency tracking themes.
- `references/supplier-open-source-evidence.csv` — evidence expectations for external components.
- `references/exposure-impact-analysis.csv` — impact review dimensions.
- `references/framework-crosswalk.csv` — crosswalk to inventory, supplier-risk, security, and governance controls.

## Assets

Use the templates in `assets/templates/` directly when the user asks for working artifacts.
