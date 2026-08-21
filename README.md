# Palantir Ontology — Hermes Skill

Design Palantir-inspired **local decision systems** from messy business workflows, codebases, datasets, tickets, policies, and operating documents. Turn a real-world problem into an ontology-driven AI operating model with objects, actions, permissions, human review points, evaluation criteria, and an MVP implementation path.

> Inspired by Palantir's public methodology. No proprietary internals. Models the world as objects + signals + actions + guardrails, with humans explicitly in the loop for risky decisions.

---

## What This Skill Does

Replaces the weak pattern:

```
Files + Retrieval + Chat UI
```

with a stronger pattern:

```
Decision + Ontology + Actions + Guardrails + Evaluation
```

Instead of building yet another chatbot, you produce a **Decision System Spec** — a working artifact your engineering team can build from.

## When to Use

Say **"ontology"**, **"palantir"**, or load this skill directly when you want to:

- Turn a vague workflow problem into a clear AI decision system (not just a chatbot)
- Design what an AI agent should and should NOT do automatically in a process
- Build a system where humans stay in the loop for risky decisions
- Create a shared vocabulary between humans and AI about how work gets done
- Go from messy tickets/docs/data to a structured decision model you can implement

**Typical scenarios:** triage, allocation, escalation, review, routing, scheduling, compliance, operations planning.

## Four Working Modes

Pick the lightest mode that fits:

| Mode | Use when |
|------|----------|
| **A — Ontology only** | You mainly want a decision model, object model, workflow, permissions, and review boundaries |
| **B — + Ingest** | Input is messy filings, IR decks, CSVs, or operating documents — needs extraction first |
| **C — + GUI** | You have a good ontology and want it turned into a Palantir-style operational interface (HTML mock by default; React prototype on request) |
| **D — End-to-end** | One pass from messy inputs to usable interface |

## Quick Start

**Input:** A business problem like *"帮我设计一个工单优先级决策系统"*

**Output:** A `Decision System Spec` covering the decision, objects, signals, actions, permissions, failure cases, evaluation plan, missing data, and an MVP build plan.

To run the helper script manually:

```powershell
python "scripts\bootstrap_decision_spec.py" `
  --goal "Triage incidents for release readiness" `
  --context-file "docs\runbook.md" `
  --output "decision-system-spec.md"
```

## Repository Layout

```
palantir-ontology/
├── SKILL.md                          # Skill definition (YAML frontmatter + body)
├── LICENSE                           # Apache 2.0
├── README.md                         # This file
├── agents/                           # Optional agent prompts and contracts
├── assets/
│   ├── decision-system-spec-template.md   # Canonical output template
│   ├── palantir-html-mock-starter.html
│   ├── palantir-queue-detail-action.html
│   └── palantir-plan-tracker.html
├── references/                       # In-depth methodology and patterns
│   ├── methodology.md
│   ├── ontology-patterns.md
│   ├── action-guardrails.md
│   ├── framework.md
│   ├── gui-principles.md
│   ├── gui-patterns.md
│   ├── industry-packs.md
│   └── use-cases.md
└── scripts/
    ├── bootstrap_decision_spec.py    # Helper to scaffold a Decision System Spec
    └── tests/                        # Pytest suite (28 tests)
```

## Installation

### For Codex / Claude Code

Copy this directory into your skills folder, or symlink it:

```bash
# Codex (Windows)
xcopy /E /I palantir-ontology %USERPROFILE%\.codex\skills\palantir-ontology

# Hermes
xcopy /E /I palantir-ontology %LOCALAPPDATA%\hermes\skills\palantir-ontology
```

### As a Standalone

Just clone the repo and use the helper script directly:

```bash
git clone https://github.com/QUSEIT/quseit-palantir-ontology.git
cd quseit-palantir-ontology
python scripts/bootstrap_decision_spec.py --goal "Your decision here" --output spec.md
```

## Resources

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill routing and workflow (this is what agents read) |
| `references/methodology.md` | Core design method and operating principles |
| `references/ontology-patterns.md` | Object families, relations, signals, MVP recipe |
| `references/action-guardrails.md` | Action taxonomy (auto / recommend / review / forbidden) |
| `references/framework.md` | Short mental model aligned with the public Palantir thesis |
| `references/gui-patterns.md` | Pattern selection for queue/detail/action apps |
| `references/gui-principles.md` | Public Palantir UI patterns (Workshop, Slate, Actions) |
| `references/industry-packs.md` | Industry-specific examples |
| `references/use-cases.md` | Example starting points (incident triage, claims, support, inventory) |
| `assets/decision-system-spec-template.md` | Output template |
| `scripts/bootstrap_decision_spec.py` | Helper to scaffold a Decision System Spec |
| `scripts/tests/` | Pytest test suite (28 tests) |

## Key Principles

1. Model the real decision before modeling the prompt.
2. Keep the ontology minimal but operational.
3. Make actions explicit and permissions visible.
4. Default to human review where risk is unclear.
5. Design for implementation, not just analysis.
6. If source materials are messy, perform the minimum ingest needed before deciding.
7. If the user wants a dashboard, design around objects and actions, not only charts.
8. If the user wants GUI, prefer generating something visible and runnable before writing long Markdown.

## Testing

```bash
cd scripts
python -m pytest tests -v
```

The test suite covers the bootstrap script, reference files, asset files, and HTML template structure (25 tests in `test_skill.py` + 3 tests in `test_bootstrap_decision_spec.py`).

## License

Apache License 2.0. See `LICENSE` for the full text.

## Acknowledgements

Derived from the open methodology discussed in Palantir's public documentation. The skill package is an independent reproduction of publicly inferable design logic — no proprietary internals are claimed or reproduced.