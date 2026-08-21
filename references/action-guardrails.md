# Action and Guardrail Patterns

## Purpose

Use this reference to decide what the local AI system may do, what it may only recommend, and where humans must stay in the loop.

## Action Taxonomy

### Auto

Use when:
- error cost is low
- policy is explicit
- input data is reliable
- rollback is easy

Examples:
- assign a low-risk support ticket
- tag a document
- sort a queue
- generate a draft summary

### Recommend

Use when:
- the action is useful but trust is not yet earned
- the result should be accepted by a human in the short term

Examples:
- recommend reprioritization
- recommend a vendor follow-up
- recommend escalation to legal

### Review

Use when:
- consequences are material
- policy interpretation is required
- evidence is incomplete
- regulation or trust is sensitive

Examples:
- approve a claim
- block a release
- alter customer pricing
- change compliance status

### Forbidden

Use when:
- the action is unsafe without explicit external control
- the agent cannot observe enough state
- the organization is not willing to delegate

Examples:
- terminate a customer account
- issue payments automatically
- approve medical treatment changes
- disable security controls

## Review Boundaries

For each review action, define:
- reviewer role
- approval threshold
- required evidence
- fallback path if reviewer unavailable
- audit record expectations

## Escalation Triggers

Escalate when:
- confidence is low
- policy conflicts
- data is stale or missing
- cost of false positive is high
- cost of false negative is high
- cross-team coordination is required

## Logging Requirements

Every action decision should log:
- timestamp
- target object
- observed signals
- proposed action
- execution class
- reviewer if needed
- final disposition

## Failure Modes to Defend Against

- wrong object identity
- stale state
- missing prerequisite
- hidden dependency
- biased or noisy signal
- over-automation of edge cases

## Good Guardrail Design

Strong guardrails are:
- explicit
- testable
- understandable by operators
- tied to objects and states

Weak guardrails are:
- buried in vague prose
- based on "the model should know"
- not represented in evaluation
