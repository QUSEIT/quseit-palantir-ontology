# Industry Packs

## Purpose

Use these patterns to accelerate design. They are starting points, not truth.

## Manufacturing

### Common decisions

- Which orders should run next?
- Which machine issues require stoppage?
- Which quality exceptions need supervisor review?

### Common objects

- WorkOrder
- Machine
- MaterialLot
- Shift
- QualityEvent

### Common actions

- schedule
- defer
- inspect
- stop_line
- escalate_to_supervisor

### Common signals

- downtime
- defect rate
- queue length
- material availability
- planned maintenance overlap

## Healthcare Operations

### Common decisions

- Which patients need escalation?
- Which discharges are at risk of delay?
- Which supply shortages require intervention?

### Common objects

- Patient
- Bed
- NurseShift
- SupplyItem
- CareTask

### Common actions

- escalate
- reroute
- request_supply
- flag_for_review
- assign_follow_up

### Common signals

- acuity
- discharge blockers
- staffing gap
- missing meds
- delayed imaging or labs

## Logistics and Supply Chain

### Common decisions

- Which shipments should reroute?
- Which orders risk SLA breach?
- Which inventory movements should happen now?

### Common objects

- Shipment
- Order
- Warehouse
- Carrier
- InventoryPosition

### Common actions

- reroute
- expedite
- hold
- allocate
- notify_account_team

### Common signals

- delay probability
- lane congestion
- stockout risk
- customer priority
- customs/document issues

## Finance and Risk

### Common decisions

- Which transactions need review?
- Which invoices can be auto-approved?
- Which accounts need intervention?

### Common objects

- Transaction
- Invoice
- Account
- Counterparty
- PolicyRule

### Common actions

- approve
- reject
- hold
- escalate_to_analyst
- request_documentation

### Common signals

- amount threshold
- policy mismatch
- velocity anomaly
- overdue status
- exposure concentration

## Internal Engineering and Ops

### Common decisions

- Which incidents block release?
- Which tickets should escalate?
- Which deploys require extra approval?

### Common objects

- Incident
- Service
- Deployment
- Ticket
- Runbook

### Common actions

- escalate
- assign
- block_release
- request_review
- run_playbook

### Common signals

- severity
- blast radius
- recent regressions
- unresolved dependencies
- missing rollback path

## How to Use These Packs

Start with one pack when the user context clearly matches it.

Then customize:
- add missing objects
- remove irrelevant ones
- tighten action permissions
- rewrite signals to fit available data

Do not force-fit a domain pack when the local operating reality points elsewhere.
