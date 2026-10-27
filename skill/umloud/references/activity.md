# Activity diagrams

Describe procedural logic, business processes and workflows — like flowcharts, but with first-class
**parallelism** (fork/join). In UML 2 they are defined by **token flow** (Petri-net-like), not as state machines.

## Use when / avoid when
- Use: business process / workflow modelling; procedures with concurrent steps; who-does-what across departments (partitions); UML-compliant flowcharts.
- Avoid: replacing use-case text for domain experts who don't read diagrams; algorithms that code expresses better;
  object-interaction detail (→ sequence).

## Notation

| Element | Notation | Notes |
|---|---|---|
| Initial node | filled circle | Creates the starting token. |
| Action | rounded rectangle, imperative verb phrase | Nodes are *actions*; the whole diagram is an *activity*. |
| Control flow (edge) | arrow | Usually unlabeled. |
| Decision | diamond, 1 in, several guarded outs | Guards in `[ ]`, **mutually exclusive**; `[else]` for the default. |
| Merge | diamond, several in, 1 out | Ends the conditional behaviour started by a decision. |
| Fork | thick bar, 1 in, several outs | Outgoing flows are concurrent — any order/interleaving is valid. |
| Join | thick bar, several in, 1 out | Continues only when **all** incoming flows have arrived. Optional join specification `{joinSpec = ...}`. |
| Activity final | bull's-eye | Ends the **whole** activity (all tokens). |
| Flow final | circle with X | Ends **one** flow only; the rest continues. |
| Partition (swim lane) | vertical/horizontal lanes (or a 2-D grid) labelled with a class/org unit | Shows **who** does each action. |
| Call behaviour (subactivity) | action with a rake (trident) icon | Decompose into another activity diagram. `Class::method` for a method call. |
| Accept signal | concave pentagon | Waits for an external event. Inflow → start listening only when reached. |
| Time signal | hourglass | Event caused by passage of time (`end of month`, `2h before departure`). |
| Send signal | convex pentagon | Sends an event to an outside process. |
| Object node / pins | rectangle on the flow, or small squares (pins) on actions | Data passed between actions; a transformation can be noted on the flow. |
| Expansion region | dashed rounded box with input/output collection pins, keyword `«concurrent»` / `«iterative»` | Actions run once per element of a collection. |
| Connector | small circle with a label, used in pairs | Avoid — breaks visual flow. |

## Rules
1. **Every action has exactly one incoming and one outgoing flow.** Show all merges and joins explicitly.
   (UML 2 treats multiple incoming flows to an action as an *implicit join* — UML 1 treated them as a merge. Explicit nodes avoid the ambiguity.)
2. Exactly one initial node per activity (per partition context); at least one final.
3. Every decision's guards are mutually exclusive and cover all cases (use `[else]`).
4. Pair decisions with merges, forks with joins, where it helps readability (UML 2 no longer requires balancing, but readers expect it).
5. Use **flow final** for branches that stop while others continue; **activity final** only where everything should stop (racing flows: first to reach it wins).
6. Name actions with imperative verb phrases: `Fill Order`, not `Order Filling` or `Order`.
7. Partitions only when "who does what" is part of the question.
8. ≤ ~20 actions per diagram; extract subactivities (rake) beyond that.

## Common mistakes
- Multiple arrows into one action instead of an explicit merge/join (meaning silently changes between UML 1 and 2).
- Using a decision diamond to join parallel flows (or a fork bar to branch on a condition).
- Overlapping or incomplete guards.
- Activity final used where a flow final was meant (kills parallel work).
- States (`Approved`) instead of actions (`Approve Claim`) — that's a state machine.
- Swim lanes for every diagram even when responsibility is irrelevant.

## UML 1 → UML 2 notes
- No longer a special case of state machines; fork/join balancing rules dropped.
- Multiple incoming flows: implicit merge (UML 1) → implicit **join** (UML 2).
- New: partitions (multi-dimensional "swim lanes"), signals, pins, transformations, rakes, expansion regions, flow finals, join specifications.
- "Branch" (UML 1) = decision; "synchronization bar" = fork/join; UML 1 "dynamic concurrency" `*` ≈ expansion region shorthand.

## Review checklist
- [ ] One initial node; finals correct (flow final vs activity final)
- [ ] One in / one out per action; explicit merges and joins
- [ ] Decisions have exclusive, complete guards (`[else]`)
- [ ] Forks/joins used for concurrency, diamonds for choice — never swapped
- [ ] Actions are imperative verb phrases; partitions only if "who" matters
- [ ] ≤ ~20 actions; subactivities extracted
