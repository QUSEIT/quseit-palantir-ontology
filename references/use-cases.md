# Example Use Cases

## 1. Incident Triage for Release Readiness

Input:
- on-call runbook
- incident export CSV
- service ownership map
- deployment policy

Expected output:
- `Incident`, `Service`, `Deployment`, `Reviewer` objects
- signals such as severity, blast radius, unresolved dependencies, rollback readiness
- actions like `block_release`, `escalate`, `assign`, `request_review`

## 2. Claims Review and Approval Routing

Input:
- claim records
- policy rules
- reviewer thresholds
- fraud heuristics

Expected output:
- `Claim`, `PolicyRule`, `Reviewer`, `Exception` objects
- actions like `approve`, `hold`, `request_documentation`, `escalate_to_analyst`

## 3. Customer Escalation Routing

Input:
- support tickets
- customer tier data
- SLA rules
- incident history

Expected output:
- `Ticket`, `Customer`, `SLA`, `EscalationOwner` objects
- signals like age, severity, contract tier, renewal risk, repeated reopen count
- actions like `assign`, `escalate`, `notify_account_team`, `hold_for_review`

## 4. Inventory Allocation

Input:
- order backlog
- warehouse inventory
- customer priority rules
- shipping constraints

Expected output:
- `Order`, `InventoryPosition`, `Warehouse`, `Carrier` objects
- actions like `allocate`, `reroute`, `hold`, `expedite`
