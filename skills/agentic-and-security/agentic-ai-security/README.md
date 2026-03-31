# Agentic AI Security

## What this skill does
Operator-grade security guidance for agentic threat models, least agency, memory risks, dependencies, and monitoring.

## Who it is for
- Teams threat-modeling or hardening agentic applications and agents.
- Operators reviewing tool permissions, memory patterns, inter-agent communication, and supply-chain exposure.
- Reviewers deciding whether current security conditions are sufficient for release.

## Use this skill when
- You need an agentic threat model or control plan.
- You need to review least-agency boundaries, memory risks, or dependency exposure.
- You need monitoring, containment, and incident expectations for an agentic system.

## Typical inputs
- Architecture, agent roles, tools, external connectors, and execution boundaries.
- Memory or context design, identity model, and privilege assumptions.
- Current detections, supplier dependencies, and incident-response posture.

## Typical outputs
- Threat model, least-agency matrix, or deployment-hardening plan.
- Monitoring and detection plan or containment playbook.
- Security decision memo with required remediation actions.

## How it works
- Map attack surfaces created by tools, permissions, connectors, and statefulness.
- Reduce privileges and trust boundaries before reaching for compensating controls.
- Define what must be logged, monitored, and blocked before release.

## Related skills
- [Agentic AI Governance](../agentic-ai-governance/)
- [MITRE ATLAS AI Security](../mitre-atlas-ai-security/)
- [OWASP Agentic AI Mapping to ISO/IEC 42001](../owasp-agentic-ai-mapping-to-iso-42001/)

## Notes / source boundaries
- Treat memory, delegation, and connector access as first-class security issues, not implementation details.
- This public repo centers on the instruction layer. If a referenced script, CSV, or template is not bundled in this folder, follow the workflow here and create the artifact directly.
