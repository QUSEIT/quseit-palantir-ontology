# Framework

## The idea in one sentence

Turn messy real-world operations into a governed, ontology-driven AI decision system.

## Design thesis

Do not begin with:
- a model
- a prompt
- a chatbot
- retrieval

Begin with:
- the decision
- the world model behind the decision
- the actions tied to that decision
- the review and permission boundaries around those actions

## Canonical method

1. Define the decision.
2. Define the world with objects, states, relations, and signals.
3. Define the actions.
4. Define governance with `auto`, `recommend`, `review`, and `forbidden`.
5. Define the agent contract.
6. Define evaluation for missing data, edge cases, unsafe actions, and operator burden.

## Practical rule

If the design cannot answer these questions, it is not ready:
1. What exactly is the decision?
2. What object is the decision acting on?
3. What evidence is the decision based on?
4. What action follows the decision?
5. Who approves the risky cases?
