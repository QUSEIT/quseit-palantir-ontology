# GUI Patterns

Use this file to choose the right UI pattern before building.

## 1. Queue + Detail + Action

Use when the system supports:
- triage
- approvals
- escalations
- task review
- exception handling

Must include:
- filters
- object table or queue
- selected object detail
- evidence or timeline
- visible action buttons
- review status

## 2. Common Operational Picture

Use when the user wants:
- shared awareness
- cross-team monitoring
- big-screen operational visibility
- map or topology views

Must include:
- KPI rail
- global filters
- central situational canvas
- issue feed
- drill-down into linked objects

## 3. Plan vs Actual Tracker

Use when the user wants:
- strategy tracking
- KPI delivery monitoring
- mid-term plan progress
- initiative oversight

Must include:
- target versus actual summary
- variance visual
- initiative table
- issue queue
- event timeline

## 4. Object Explorer

Use when the user wants:
- linked-object analysis
- investigation across related entities
- relationship-heavy exploration

Must include:
- searchable object list
- relationship context
- tabs or panes for evidence, actions, and history

## Pattern selection rule

If the user says:
- "review", "triage", "approve", "queue" -> choose Queue + Detail + Action
- "monitor", "overview", "shared view", "control room" -> choose Common Operational Picture
- "progress", "plan", "targets", "variance" -> choose Plan vs Actual Tracker
- "explore", "relations", "linked objects" -> choose Object Explorer
