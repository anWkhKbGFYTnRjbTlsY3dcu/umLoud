# Less common diagrams: interaction overview, timing, collaborations, profiles

Use these rarely. Before drawing one, check whether an activity, sequence or state diagram answers the question more simply — and say so if it does.

## Interaction overview diagrams
An activity diagram whose nodes are interactions: inline small sequence diagrams (`sd` frames) or
references to other interactions (`ref` frames), connected by activity control flow (decisions, forks…).

- Use: a high-level map of how several scenarios connect, when each step is itself an interaction.
- Prefer instead: a plain activity diagram (when the steps are actions) or one sequence diagram with `ref`/`alt` frames. Mixing both styles is often harder to read.

## Timing diagrams
Show **state changes over time** of one or more participants, with **timing constraints** between them.
Familiar to hardware/embedded engineers.

- Notation: one lane per participant; time runs left→right; state shown as a line on a level (few states, "robust")
  or as labelled regions with crossings (many states, "concise"); constraints as `{> 10s}`, `{< 15 min}` between events.
- Use: when **duration** constraints between state changes matter. Otherwise use a state machine (states only) or sequence diagram (order only).

## Collaborations (not an official UML 2 diagram type)
A dashed ellipse naming a collaboration (e.g. a pattern, *Auction*) containing **roles** (lower-case names: `seller`, `buyer`, `lot`)
and their relationships; interactions use `participant / role : Class`. A *collaboration use* (called *collaboration occurrence* in UML 2.0 drafts) on a class diagram
links real classes to the roles they play.

- Use: documenting a pattern/protocol where different classes play the roles in different places. Rarely compelling in practice —
  a note `«pattern: role»` on classes (Gamma-style annotation) is often clearer.

## Profile diagrams (added in UML 2.2)
Define a **profile**: a coherent set of **stereotypes** (with tagged values / properties and constraints) that extend
UML **metaclasses** for a domain or platform (e.g. persistence, REST, EJB, safety). Applying the profile lets other
diagrams use `«Entity»`, `«Resource»`, etc. with defined meaning.

| Element | Notation |
|---|---|
| Profile | package with `«profile»` |
| Metaclass | class box with `«metaclass»` (the UML element being extended: `Class`, `Property`, `Operation`, `Component`…) |
| Stereotype | class box with `«stereotype»`; attributes = its tagged values |
| Extension | solid line with a **filled** triangle from the stereotype to the metaclass (`{required}` if every instance must carry it) |
| Profile application | dashed arrow `«apply»` from a model/package to the profile |

- Use: only when a team defines its own stereotypes and wants their meaning documented. Most teams *use* profiles (from tools) and never draw one.
- Rules: stereotype names UpperCamelCase; every stereotype extends at least one metaclass; tagged values typed; keep one profile per concern.

