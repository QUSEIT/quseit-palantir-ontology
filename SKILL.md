---
name: palantir-ontology
description: Design Palantir-inspired local decision systems from messy business workflows, codebases, datasets, tickets, policies, and operating documents. Use when Codex needs to turn a real-world problem into an ontology-driven AI operating model with objects, actions, permissions, human review points, evaluation criteria, and an MVP implementation path.
---

# Palantir Ontology

## Overview

Turn a vague business problem or local context into a concrete `Decision System Spec` that resembles the useful parts of Palantir's public methodology without claiming proprietary access. Model the world as objects, signals, actions, permissions, and review boundaries; then produce an implementation-ready operating design that can run inside Codex, Claude Code, or a local toolchain.

This skill can also absorb two adjacent jobs when the user wants a simpler workflow:
- `Ingest mode`: extract ontology-ready objects, signals, metrics, risks, initiatives, and events from messy source documents before or while modeling the ontology
- `GUI mode`: turn the resulting decision spec or object model into a Palantir-style operational interface with overview pages, queues, detail views, timelines, and governed actions

## Core Principle

Design around the decision, not the prompt.

Treat prompts as implementation details inside a larger system that defines:
- what exists in the operating world
- what data matters
- what actions are allowed
- where human approval is required
- how success and failure will be evaluated

Replace this weak pattern:

`Files + Retrieval + Chat UI`

with this stronger pattern:

`Decision + Ontology + Actions + Guardrails + Evaluation`

## When to Use

- Turn a business problem like triage, allocation, escalation, review, routing, scheduling, compliance, or operations planning into a local AI decision workflow
- Inspect a codebase, ticket queue, data schema, CSV export, policy set, runbook, PRD, or operating document and decide what ontology and action model would make it agent-ready
- Design a Palantir-like operating model locally without pretending to recreate Palantir's internal systems or private prompts
- Produce a reusable `Decision System Spec` for later implementation, evaluation, or GitHub publication
- Decide what data is missing, what human approvals are needed, and what the MVP should automate first

## Inputs

Accept one or both of these:
- `goal`: the business judgment or operating problem to solve
- `context`: local files, code, schemas, tickets, docs, or datasets that describe the world

If the user only gives a goal, infer the missing world model and explicitly list unknowns. If the user only gives data, infer the likely decision surfaces and suggest the most promising first use cases.

## Working Modes

Choose the lightest mode that fits the task.

### Mode A: Ontology only

Use when the user mainly wants a decision model, object model, workflow, permissions, and review boundaries.

### Mode B: Ontology + ingest

Use when the input is a packet of filings, IR decks, operating documents, CSVs, or mixed materials and the user needs structured extraction before the ontology is clear.

In this mode:
- build a small source inventory
- extract canonical objects and aliases
- normalize periods, units, and naming
- separate `reported_value` from `normalized_value` when needed
- preserve provenance for non-trivial facts

Default extracted families:
- `Company`
- `BusinessSegment`
- `KPI`
- `StrategicInitiative`
- `Risk`
- `DisclosureEvent`
- `ManagementStatement`

### Mode C: Ontology + GUI

Use when the user already has a good ontology or decision spec and wants it turned into an operational interface.

Default deliverable order:
1. `HTML mock` if the user does not specify an implementation format
2. `React prototype` when the user asks for a richer local app
3. `Interface spec` only when the user explicitly wants planning or architecture without code

Default application patterns:
- `Queue + Detail + Action`
- `Common Operational Picture`
- `Plan vs Actual Tracker`
- `Object Explorer`

Default page set for action-oriented apps:
- `Overview`
- `Queue or Alert Feed`
- `Object Detail`
- `Timeline or Event Log`
- `Review / Action Panel`

Favor object-linked tables, filters, detail panes, and visible action states over chart-only dashboards.
Prefer visible output over prose. If GUI mode is requested and no contrary instruction is given, generate files for a mock or prototype instead of stopping at Markdown.
Treat HTML as a lightweight product surface, not a dressed-up document. The default should look and behave like an operational application rather than a report.

### Mode D: End-to-end

Use when the user wants one pass from messy inputs to usable interface.

Flow:
1. extract and normalize source material
2. define ontology and decision surface
3. derive interface pages, components, and actions
4. if requested, scaffold prototype code or HTML

## Recommended First Scope

Do not begin with a giant platform. Begin with one decision that has:
- clear business value
- available data
- bounded risk
- human reviewers available
- visible outcomes

Common first targets:
- incident escalation
- claims triage
- release readiness
- support prioritization
- inventory allocation

## Workflow

### Step 1: Define the decision surface

Reduce the request to a single operational decision.

Examples:
- "Which customer issues should escalate now?"
- "Which incidents require human review before deploy?"
- "Which claims can be auto-approved versus held?"
- "Which inventory movements should happen today?"

Use `references/methodology.md` for the canonical framing and selection rules.

### Step 2: Load only the minimum useful context

Inspect only the files, schemas, docs, or code needed to model the decision.

Prefer operating artifacts over summaries:
- queue exports
- runbooks
- policy docs
- schema definitions
- service code
- incident logs
- workflow screenshots or tables

Do not load everything by default. Emulate Palantir's controlled-context style by reading only the context that sharpens the decision.

If the request is document-heavy, do a compact ingest pass first:
- identify document type and period
- extract candidate objects, metrics, risks, and events
- note unresolved naming conflicts
- continue ontology design only after the schema stabilizes

### Step 3: Build the local ontology

Define the smallest useful operating model:
- `objects`: the core entities that matter
- `properties`: the fields that influence decisions
- `relations`: how the objects affect one another
- `states`: what can change over time
- `signals`: what evidence the system can observe

Use `references/ontology-patterns.md` to choose modeling patterns and avoid over-modeling.

### Step 4: Define actions and review boundaries

Translate the decision into executable or recommendable actions.

For each action, classify it as:
- `auto`: safe to execute automatically
- `recommend`: safe to recommend but not execute
- `review`: requires explicit human approval
- `forbidden`: never execute automatically

Use `references/action-guardrails.md` to design action boundaries, logs, and escalation rules.

### Step 5: Design the agent contract

Specify the local agent behavior without centering the entire design on prompting.

Define:
- mission
- visible objects and signals
- allowed tools
- output contract
- escalation rules
- failure conditions

Treat prompt text as one implementation detail inside this larger contract.

If GUI work is requested, also define the interface contract:
- primary user
- primary decision loop
- main object set
- writeback actions
- review boundaries
- evidence panels
- status transitions

### Step 6: Produce the Decision System Spec

Use `assets/decision-system-spec-template.md` as the canonical output shape. The spec must include:
- Decision
- Objects
- Signals
- Actions
- Permissions
- Human review points
- Workflow
- Failure cases
- Evaluation plan
- Missing data
- MVP build plan

If running in ingest mode, prepend a short `Ingest Summary` with:
- sources used
- normalized objects
- key signals and metrics
- events and risks
- unresolved data issues

If running in GUI mode:
- default to creating an `HTML mock` file
- create a `React prototype` when the user asks for a working app, richer interactions, or local preview
- append a short `Interface Spec` only as support for the generated UI, not as the primary deliverable

When selecting a GUI pattern, use these rules:
- choose `Queue + Detail + Action` for triage, approval, escalation, and task handling
- choose `Common Operational Picture` for awareness, shared monitoring, or cross-team situational views
- choose `Plan vs Actual Tracker` for mid-term plans, KPI delivery, and strategy progress
- choose `Object Explorer` for relationship-heavy analysis across linked objects

In all GUI outputs:
- make filters visible
- keep the selected object persistent while users review evidence
- place actions near the evidence and current state they affect
- show status chips and review modes explicitly
- prefer dense tables and side panels over long prose blocks

The supporting `Interface Spec` should cover:
- user and decision
- primary objects
- pages
- components
- actions and review
- state model
- build plan

If useful, scaffold the file with the helper script:

```powershell
& 'C:\Users\sheng\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\sheng\.codex\skills\palantir-ontology\scripts\bootstrap_decision_spec.py' `
  --goal "Triage incidents for release readiness" `
  --context-file "docs\runbook.md" `
  --context-file "data\incident_export.csv" `
  --output "reports\decision-system-spec.md"
```

### Step 7: Stress-test the design

Before calling the design good, challenge it:
- What data is missing?
- What action is too risky to automate?
- What object definition is too broad?
- What review point will create bottlenecks?
- What failure mode would make the system unsafe or useless?

Use `references/industry-packs.md` to compare against industry-specific patterns when relevant.

Before calling the design ready, make sure it can answer:
1. What exactly is the decision?
2. What object is the decision acting on?
3. What evidence is the decision based on?
4. What action follows the decision?
5. Who approves the risky cases?

## Output Format

Return a `Decision System Spec` in Markdown for ontology work. When GUI work is requested, return code and files first, then a concise supporting spec.

### Required sections

```markdown
# Decision System Spec

## 1. Decision
## 2. Objects
## 3. Signals
## 4. Actions
## 5. Permissions and Review
## 6. Workflow
## 7. Failure Cases
## 8. Evaluation Plan
## 9. Missing Data
## 10. MVP Build Plan
```

When GUI work is requested, add supporting sections as needed:

```markdown
## 11. Interface Spec
### User and Decision
### Primary Objects
### Pages
### Components
### Actions and Review
### State Model
### Build Plan
```

## Prerequisites

- No external API keys required for the skill itself
- Access to local files, repos, tickets, docs, or datasets improves quality
- Use the bundled Python runtime when running the helper script on Windows

## Resources

- `references/methodology.md` -- The core Palantir-inspired design method and operating principles
- `references/ontology-patterns.md` -- Patterns for objects, states, links, signals, and world modeling
- `references/action-guardrails.md` -- Action classes, approval boundaries, logging, and safety design
- `references/framework.md` -- Short mental model and design thesis aligned with the public GitHub repo
- `references/gui-principles.md` -- Public Palantir UI patterns from Workshop, Slate, operational applications, and Actions
- `references/gui-patterns.md` -- Pattern selection guide for queue/detail/action apps, COPs, plan trackers, and object explorers
- `references/industry-packs.md` -- Industry-specific examples for manufacturing, healthcare, logistics, finance, and internal ops
- `references/use-cases.md` -- Example starting points such as incident triage, claims review, support routing, and inventory allocation
- `assets/decision-system-spec-template.md` -- Canonical template for final output
- `assets/palantir-html-mock-starter.html` -- Default starter for Palantir-style queue/detail/timeline mocks
- `assets/palantir-queue-detail-action.html` -- Higher-fidelity action-oriented operational UI starter
- `assets/palantir-plan-tracker.html` -- Higher-fidelity plan-vs-actual tracker starter
- `scripts/bootstrap_decision_spec.py` -- Helper script to scaffold a Decision System Spec file from a goal and local context list

## Key Principles

1. Model the real decision before modeling the prompt.
2. Keep the ontology minimal but operational.
3. Make actions explicit and permissions visible.
4. Default to human review where risk is unclear.
5. Design for implementation, not just analysis.
6. If source materials are messy, perform the minimum ingest needed before deciding.
7. If the user wants a dashboard, design around objects and actions, not only charts.
8. If the user wants GUI, prefer generating something visible and runnable before writing long Markdown.
