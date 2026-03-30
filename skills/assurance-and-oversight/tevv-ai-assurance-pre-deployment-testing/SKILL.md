---
name: tevv-ai-assurance-pre-deployment-testing
description: workflow-first ai assurance support for testing, evaluation, verification, validation, and pre-deployment approval. use when chatgpt needs to design or review tevv programs, draft pre-deployment test plans, define metrics and pass-fail thresholds, build go-no-go packages, assess model or system readiness, set retest triggers, or convert nist ai rmf and nist ai 600-1 expectations into concrete assurance artifacts for ciso, cro, legal, audit, compliance, product, or engineering stakeholders.
---

# TEVV / AI Assurance / Pre-Deployment Testing

## Overview

Use this skill to turn AI assurance expectations into concrete operator artifacts. Focus on evidence, decision gates, test coverage, residual risk, and repeatable release or deployment approval.

## Workflow decision tree

1. Determine the request type:
   - **Need a full TEVV operating package?** → Run the **Assurance program workflow**.
   - **Need a system-specific approval package?** → Run the **Pre-deployment workflow**.
   - **Need a gap assessment?** → Run the **Gap analysis workflow**.
   - **Need a quick lookup of TEVV controls or evidence expectations?** → Run the **Control lookup workflow**.

2. Default output expectation:
   - Build outputs for executive and control stakeholders, not for general education.
   - Prefer structured artifacts over narrative explanation.
   - Always show: scope, assumptions, test coverage, pass/fail logic, unresolved risks, required actions, and release recommendation.

## Assurance program workflow

Use when the user needs to stand up or improve an organizational TEVV capability.

1. Build the system context and intended-use profile.
   - Use `assets/templates/system-assurance-profile.md`.
   - Capture lifecycle stage, use case, operator role, user population, impact severity, human oversight model, and dependencies.
2. Define the assurance scope.
   - Use `references/tevv-domain-catalog.csv` and `references/assurance-stage-map.csv`.
   - Select which domains apply: performance, safety, robustness, security, privacy, fairness, explainability, human factors, monitoring readiness, and supplier assertions.
3. Define evidence requirements.
   - Use `assets/templates/evidence-pack-checklist.csv` and `references/nist-tevv-anchors.csv`.
   - Require artifacts for data, model, testing methodology, results, limitations, and approval records.
4. Define test governance.
   - Specify independent review roles, approval rights, conflict controls, and escalation.
   - Use `assets/templates/independent-review-log.csv` if review independence matters.
5. Define decision thresholds.
   - Use `assets/templates/evaluation-metric-register.csv`.
   - Require metric name, rationale, threshold, owner, evidence source, and disposition when threshold is missed.
6. Define re-test triggers and lifecycle carry-forward.
   - Use `assets/templates/post-deployment-retest-trigger-log.csv`.
   - Cover data drift, model changes, prompt changes, new integrations, new users, new regions, incidents, and regulatory change.
7. Produce the final package.
   - Output a program structure plus artifact list and decision governance.

## Pre-deployment workflow

Use when the user needs a release or deployment approval package for a specific AI system.

1. Create the assurance profile.
   - Use `assets/templates/system-assurance-profile.md`.
2. Draft the pre-deployment test plan.
   - Use `assets/templates/pre-deployment-test-plan.md`.
   - Include objectives, scope, exclusions, test environments, datasets, scenarios, red-team or adversarial elements, evaluator roles, and required evidence.
3. Build the metric and threshold register.
   - Use `assets/templates/evaluation-metric-register.csv`.
4. Review data readiness.
   - Use `assets/templates/dataset-readiness-review.md`.
5. Review model validation and limitations.
   - Use `assets/templates/model-validation-report.md`.
6. Review human factors and deployment context.
   - Use `assets/templates/human-factors-review.md`.
7. Summarize residual risk and approval outcome.
   - Use `assets/templates/go-no-go-memo.md` and `assets/templates/residual-risk-acceptance-memo.md`.
8. If the user needs a board or executive output, summarize the approval basis in 1 page and attach the evidence checklist.

## Gap analysis workflow

Use when the user wants to assess whether an existing TEVV setup is sufficient.

1. Use `assets/templates/tevv-gap-questionnaire.csv` as the input structure.
2. Run:
   - `python scripts/gap_analysis.py assets/templates/tevv-gap-questionnaire.csv`
   - or point it to a completed CSV supplied by the user.
3. Convert the output into four sections:
   - Executive summary
   - High-priority gaps
   - Recommended remediation actions
   - Required evidence before next approval decision
4. Rate findings using a simple RAG logic unless the user gives another scoring model.
5. Distinguish between:
   - policy/process gaps
   - evidence gaps
   - independence/governance gaps
   - test coverage gaps
   - monitoring and retest gaps

## Control lookup workflow

Use when the user needs quick support mapping a TEVV question to an assurance expectation.

1. Run `python scripts/control_lookup.py <keyword>`.
2. Use `references/nist-tevv-anchors.csv`, `references/tevv-domain-catalog.csv`, and `references/pre-deployment-test-catalog.csv`.
3. Return short, decision-useful guidance plus the matching artifact to produce.

## Operating rules

- Treat TEVV as socio-technical, not only technical. Include operational context, human oversight, and deployment conditions.
- Prefer explicit pass/fail or go/no-go criteria over vague statements like "appears acceptable".
- Always identify who performed testing, who reviewed it, and who has release authority.
- Separate developer-generated evidence from independent review evidence whenever feasible.
- Always state limitations, exclusions, open issues, and residual risks.
- When the user asks for a testing pack, include both pre-deployment testing and post-deployment retest triggers.
- When the user asks for GenAI assurance, explicitly include prompt-based misuse testing, safety guardrail testing, provenance of evaluation data, and incident escalation.
- When the user asks for high-impact or high-risk systems, increase the expected depth of evidence, independence, and human review.
- Do not reproduce copyrighted source text. Use original wording, derivative tables, and artifact templates only.

## Default report structure

Use this exact structure unless the user asks for another format:

# [System or Program Name] TEVV Assessment

## Executive summary
- system and scope
- approval question
- current assurance status
- release recommendation

## Assurance scope
- lifecycle stage
- domains tested
- exclusions
- dependencies and third parties

## Test design and evidence basis
- methodologies used
- datasets / scenarios / environments
- evaluators and reviewers
- evidence reviewed

## Key findings
- finding
- impact
- evidence gap or control gap
- remediation owner

## Decision gates
- pass criteria met / not met
- no-go triggers
- required conditional controls

## Residual risk
- unresolved issues
- accepted / not accepted
- accountable approver

## Required next actions
1. immediate actions
2. pre-release actions
3. post-release monitoring or retest actions

## Resources in this skill

### Scripts
- `scripts/gap_analysis.py` - converts a completed TEVV questionnaire CSV into a prioritized markdown gap report.
- `scripts/profile_builder.py` - creates a system assurance profile markdown file from CLI inputs.
- `scripts/control_lookup.py` - searches TEVV control and evidence references by keyword.

### References
- `references/tevv-domain-catalog.csv` - core TEVV domains and what to test.
- `references/assurance-stage-map.csv` - lifecycle stages and corresponding assurance focus.
- `references/pre-deployment-test-catalog.csv` - test types, expected artifacts, and common failure signals.
- `references/nist-tevv-anchors.csv` - derivative NIST-aligned expectations and action anchors.
- `references/publication-and-copyright-boundaries.md` - public distribution boundaries.

### Templates
- `assets/templates/system-assurance-profile.md`
- `assets/templates/tevv-gap-questionnaire.csv`
- `assets/templates/pre-deployment-test-plan.md`
- `assets/templates/evaluation-metric-register.csv`
- `assets/templates/dataset-readiness-review.md`
- `assets/templates/model-validation-report.md`
- `assets/templates/human-factors-review.md`
- `assets/templates/evidence-pack-checklist.csv`
- `assets/templates/independent-review-log.csv`
- `assets/templates/post-deployment-retest-trigger-log.csv`
- `assets/templates/go-no-go-memo.md`
- `assets/templates/residual-risk-acceptance-memo.md`
