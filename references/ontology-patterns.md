# Ontology Patterns

## Purpose

Use this reference to build a minimal but operational world model from local data and workflow context.

## Ontology Template

For each object, define:

- `name`
- `business meaning`
- `key properties`
- `states`
- `relations`
- `decision relevance`

## Common Object Families

### Work Items

- Ticket
- Case
- Alert
- Incident
- Request
- Claim

Useful properties:
- severity
- age
- owner
- status
- source
- SLA deadline
- customer tier

### Operational Assets

- Service
- Deployment
- Warehouse
- Vehicle
- Machine
- Facility

Useful properties:
- capacity
- health
- region
- maintenance state
- throughput
- availability

### Business Parties

- Customer
- Vendor
- Employee
- Approver
- Team
- Partner

Useful properties:
- segment
- risk level
- contract tier
- region
- authority

### Financial Objects

- Invoice
- Payment
- Order
- Exposure
- Budget

Useful properties:
- amount
- due date
- delinquency
- margin
- approval threshold

## Relationship Patterns

Common relation types:

- belongs_to
- owned_by
- depends_on
- blocks
- triggered_by
- linked_to
- escalated_to
- fulfilled_by

Ask:
- Does this relation affect the decision?
- Does it explain why a state changes?
- Does it create or remove an allowed action?

If not, leave it out of the MVP.

## State Modeling

Objects need states when the decision depends on change over time.

Examples:
- Ticket: new -> triaged -> assigned -> resolved
- Claim: submitted -> under_review -> approved -> paid
- Deployment: draft -> staged -> approved -> live -> rolled_back

Use states when they affect:
- action eligibility
- escalation policy
- metrics
- review rules

## Signals

Signals are the observed evidence used to make the decision.

Examples:
- error rate spike
- SLA breach risk
- missing documentation
- repeated reopen count
- customer spend
- compliance flag
- device temperature

Good signals are:
- measurable
- available
- explainable
- timely

## Modeling Rule of Thumb

The ontology is good enough when:
- the decision can be described only using these objects and signals
- every action has a clear target object
- the review boundaries can be explained in object/state terms

The ontology is too big when:
- it mirrors the entire source system
- half the properties never affect any action
- the model explains everything but drives nothing

## MVP Recipe

For the first pass:
- 1 decision
- 3-7 objects
- 5-12 key properties per important object
- 3-6 relation types
- 2-5 actions
- explicit review policy

Anything more should be justified by real complexity, not completeness anxiety.
