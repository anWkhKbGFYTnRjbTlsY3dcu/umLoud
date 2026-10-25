# State machine diagrams

Describe the **lifetime behaviour of one object** (or system/controller): the states it can be in and how
events move it between them. A "state" here is an abstract mode of reacting to events — not "the current
values of all fields".

## Use when / avoid when
- Use: a class with interesting lifecycle behaviour across several use cases — UI controllers, protocol
  handlers, orders/tickets/payments with a status, devices.
- Avoid: drawing one for every class (waste); behaviour that involves many collaborating objects (→ sequence/activity).

## Notation

| Element | Notation | Notes |
|---|---|---|
| Initial pseudostate | filled circle with an arrow to the first state | Not a state itself. |
| State | rounded rectangle with a name | Name as adjective/"-ing" (`Waiting`, `Authorizing`, `Open`). |
| Transition | arrow labelled `trigger [guard] / activity` | All three parts optional. Missing guard → always taken on the event; missing trigger → taken immediately (completion transition, typically after a do-activity). |
| Final state | bull's-eye | Machine completed (object usually deleted). |
| Internal activity | inside the state box: `event [guard] / activity` | Reacts **without** leaving the state: entry/exit are **not** run. |
| Self-transition | arrow from a state back to itself | Leaves and re-enters: exit **and** entry **are** run. |
| Entry / exit | `entry / activity`, `exit / activity` inside the state | Run on every entry / every exit. |
| Do-activity | `do / activity` | Ongoing, takes time, **interruptible** by events; regular (transition/entry/exit) activities are "instantaneous" and not interruptible. |
| Superstate (composite state) | state box containing substates | Put shared transitions (e.g. `cancel`) on the superstate once instead of on each substate. |
| Concurrent (orthogonal) regions | composite state divided by dashed lines | Each region is an independent sub-machine active at the same time. |
| History pseudostate | circle with `H` (shallow) / `H*` (deep) | Re-entering the composite resumes the last active substate; an arrow from H gives the default for the first time. |
| Choice | diamond | Dynamic branch with guards. |
| Fork / join | thick bar | Split into / merge from orthogonal regions. |

## Rules
1. One state machine per class/object; title names the class: `Order — lifecycle`.
2. Every state must be reachable from the initial state, and every non-final state must have a way out (unless it is deliberately a terminal state — then use a final state).
3. Guards on transitions leaving the same state on the **same event** must be **mutually exclusive**.
4. Events with no matching transition are **ignored** — if an event must be handled in a state, draw it.
5. Show only what the object itself can observe or cause.
6. Use superstates to remove duplicated transitions; use orthogonal regions instead of a combinatorial explosion of states.
7. ≤ ~12 states per level; nest deeper levels in separate diagrams if needed.
8. Use the trigger/guard/activity label order exactly: `event [guard] / activity`.

## Common mistakes
- Drawing a flowchart (actions as states, no events) — that's an activity diagram.
- States named as actions/verbs (`Validate`) instead of conditions (`Validating`, `Valid`).
- Overlapping guards on the same event, or missing `[else]`-style coverage when it matters.
- Confusing internal activities with self-transitions (entry/exit behaviour differs).
- Missing initial state; several initial states in one region.
- Using UML 1 terms "action" vs "activity" — UML 2 calls both *activities*; long-running ones are *do-activities*.

## Implementation hint (optional notes for blueprints)
State machines map to nested switch statements (avoid — unwieldy), the **State pattern** (one subclass per state),
or a **state table** (source, target, event, guard, activity) interpreted or code-generated. A state table is
also a great textual companion to a complex diagram.

## Review checklist
- [ ] Describes one object; title names it
- [ ] Single initial state per region; final state if the object's life ends
- [ ] Labels follow `event [guard] / activity`; guards on the same event are exclusive
- [ ] States are conditions/modes, not actions
- [ ] Superstates used for shared transitions; orthogonal regions instead of state explosion
- [ ] Internal activities vs self-transitions chosen deliberately
