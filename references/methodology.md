# Palantir-Inspired Methodology

## Purpose

Use this reference to turn a messy operating problem into a local, ontology-driven AI decision system. The goal is not to copy Palantir's proprietary internals; the goal is to reproduce the publicly inferable design logic:

- model the world as operating objects
- define what can change
- define who can act
- restrict agent behavior to permitted actions
- route risky changes through human review
- evaluate the system against real failure modes

## Core Claim

Most enterprise AI projects fail because they start with prompts or chatbots instead of decisions.

The unit of design is not:
- the prompt
- the dashboard
- the model

The unit of design is:
- the decision
- the object model behind the decision
- the action model behind the decision
- the governance around the action

## Canonical Flow

### 1. Define the decision

Phrase the problem as a single operational judgment:

- Which orders should ship first?
- Which alerts should escalate?
- Which claims can be auto-approved?
- Which changes require sign-off?

Bad framing:
- "Build an AI for support"
- "Use LLMs on our data"
- "Make a smart chatbot"

Good framing:
- "Classify incoming cases into resolve / escalate / hold"
- "Decide which incidents block release"
- "Recommend which accounts deserve executive outreach"

### 2. Identify actors and stakes

List:
- who currently makes the decision
- who is affected
- what costs a bad decision creates
- what regulatory or trust boundary exists

This turns "interesting AI" into "safe and useful AI."

### 3. Model the world

Extract the smallest useful ontology:

- objects
- fields
- states
- relations
- key evidence signals

The ontology is good enough when the decision can be explained in terms of those elements.

### 4. Define actions

For each decision outcome, define the operational action:

- recommend
- update
- assign
- block
- approve
- escalate
- schedule
- notify

If the design has no actions, it is probably just analysis.

### 5. Define control boundaries

Assign each action to one of these classes:

- auto
- recommend
- review
- forbidden

This is the minimum governance layer for real-world use.

### 6. Define the agent contract

Only now define the agent behavior:

- mission
- visible context
- allowed tools
- response format
- escalation rules
- stop conditions

### 7. Evaluate with failure cases

Test not only expected cases but also:

- incomplete data
- conflicting signals
- adversarial inputs
- stale states
- high-cost edge cases

## Design Heuristics

### Keep the ontology minimal

Avoid over-modeling. Start with 3-7 important objects unless the domain clearly requires more.

### Prefer operational nouns

Use real-world entities:
- `Order`
- `Ticket`
- `Case`
- `Deployment`
- `Invoice`
- `Patient`

Avoid vague abstractions:
- `BusinessEntity`
- `GenericTask`
- `DecisionItem`

### Prefer verbs that can be governed

Strong:
- assign
- escalate
- approve
- defer
- reroute

Weak:
- think about
- analyze more
- suggest improvements

### Human review is not a failure

Human approval is a feature, not a defect, when:
- cost of error is high
- evidence is incomplete
- policy is ambiguous
- trust is not yet earned

### Build the MVP around one decision

Do not automate an entire department first. Automate one decision cleanly.

## Anti-Patterns

- Starting with a long system prompt and no operating model
- Treating retrieval as equivalent to decision intelligence
- Defining objects with no actions
- Letting the agent see everything by default
- Hiding approval policy in prose instead of explicit rules
- Measuring "good vibes" instead of operational outcomes

## What Success Looks Like

A strong output from this skill should make a builder say:

"I know what the system is deciding, what objects matter, what actions it can take, where humans stay in the loop, and what we can implement first."
