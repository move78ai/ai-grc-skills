# AIBOM / AI Bill of Materials

## What this skill does
Operator-grade AIBOM workflows for component inventories, provenance, dependency mapping, version tracking, and supplier evidence requests.

## Who it is for
- Teams creating an AI Bill of Materials for one system or a broader portfolio.
- Operators documenting provenance, versions, and third-party component exposure.
- Reviewers who need a defensible component record for governance, security, or procurement decisions.

## Use this skill when
- You need to build or refresh an AIBOM.
- You need to assess whether an existing BOM is incomplete or stale.
- You need supplier evidence or component approval support tied to a BOM view.

## Typical inputs
- System or service name, owner, use case, and deployment context.
- Models, datasets, providers, tools, runtimes, and hosted-service dependencies.
- Known provenance records, version history, and update or exposure concerns.

## Typical outputs
- AIBOM register, dependency map, or provenance record.
- Supplier evidence request or component approval memo.
- Executive summary of component risk and change exposure.

## How it works
- Separate first-party, third-party, open-source, hosted-service, and user-supplied components.
- Track both current-state composition and meaningful change history.
- Use the AIBOM as an operating control artifact instead of a static spreadsheet.

## Related skills
- [AI System Inventory and Shadow AI Discovery](../ai-system-inventory-shadow-ai-discovery/)
- [Third-Party AI / Supplier Risk](../third-party-ai-supplier-risk/)
- [Content Provenance / Synthetic Media Transparency](../../transparency-and-provenance/content-provenance-synthetic-media-transparency/)

## Notes / source boundaries
- Unknown component facts should stay marked as unknown until verified.
- This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.
