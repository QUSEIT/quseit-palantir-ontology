# GUI Principles

Use this file when the task is to make the output feel closer to a real Palantir-style operational application.

## Public product principles to preserve

These are drawn from Palantir's public Foundry documentation:

- Workshop uses the object layer as the primary building block for applications.
- Workshop emphasizes consistent design and interactivity beyond typical dashboards.
- Operational applications are meant to drive a specific decision and capture that decision through writeback.
- Actions are first-class, governed writeback mechanisms.
- Slate enables custom-styled operational applications and dashboards with CSS and dynamic layouts.

## Implications for this skill

Do not produce a chart deck when the user asks for GUI.

Prefer:
- object-centric layouts
- filterable queues and tables
- selected-object detail panes
- evidence and timeline panels
- visible writeback or review actions
- compact KPI rails
- explicit review modes such as `recommended`, `review required`, `blocked`

Avoid:
- long prose-heavy pages
- single-column report layouts
- static "dashboard only" views with no next action
- disconnected charts with no selected object and no action surface

## Canonical operational app shape

For most cases, the strongest default is:

1. top KPI rail
2. left queue or object list with filters
3. center detail view for selected object
4. right action and review pane
5. timeline or evidence section tied to the selected object

This shape matches the public Palantir emphasis on object data, actionability, and dynamic interactions.

## Public sources

- Workshop overview: https://www.palantir.com/docs/foundry/workshop/overview
- Workshop widgets: https://www.palantir.com/docs/foundry/workshop/concepts-widgets
- Workshop layouts: https://www.palantir.com/docs/foundry/workshop/concepts-layouts
- Operational applications: https://www.palantir.com/docs/foundry/app-building/operational-apps
- Actions overview: https://www.palantir.com/docs/foundry/workshop/actions-overview/
- Slate overview: https://www.palantir.com/docs/foundry/slate/overview/
- Slate style overview: https://www.palantir.com/docs/foundry/slate/style-overview
