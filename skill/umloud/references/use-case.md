# Use cases (text first, diagram second)

A **use case** is a set of scenarios tied together by one **user goal**. Almost all the value is in the
**text**; the UML only standardizes the diagram, which is a graphical table of contents of the use-case set.
When asked for a "use case diagram", also offer (or produce) the use-case text for the key use cases.

## Use when / avoid when
- Use: capturing functional requirements from the outside; scoping what the system does for whom; context/boundary overview.
- Avoid: designing internals (no correspondence between use cases and classes should be expected);
  functional decomposition into sub-sub-use-cases; UI design.

## Vocabulary
- **Actor** — a *role* (not a person) that interacts with the system; may be another system. One person can play several actors; one actor can be many people.
- **Primary actor** — has the goal the use case satisfies (usually the initiator). **Secondary actors** — the system talks to them during the use case.
- **Scenario** — one sequence of steps. **Main success scenario (MSS)** + **extensions**.
- **Levels** (Cockburn): *kite* (business-level summary), *sea level* (one actor, one sitting, delivers value — most use cases belong here), *fish* (exists only because sea-level ones include it).

## Use-case text template

```text
Use Case: <Verb phrase goal, e.g. Buy a Product>
Primary actor: <Customer>        Level: <sea level>
Trigger: <what starts it>
Precondition: <what the system ensures before start>
Guarantees: success — <...>; minimal — <...>

Main success scenario:
  1. Customer browses the catalog and selects items to buy (include: Browse Catalog).
  2. Customer goes to check out.
  3. Customer fills in shipping information.
  4. System presents full pricing information, including shipping.
  5. Customer fills in credit card information.
  6. System authorizes purchase.
  7. System confirms sale immediately.
  8. System sends confirming e-mail to customer.

Extensions:
  3a. Customer is a regular customer:
      .1 System displays current shipping, pricing and billing information.
      .2 Customer may accept or override these defaults; return to MSS at step 6.
  6a. System fails to authorize credit purchase:
      .1 Customer may re-enter credit card information or cancel.
```

Text rules:
1. Each step is one simple sentence that clearly names **who** acts.
2. Steps state **intent**, not UI mechanics ("Customer enters shipping info", not "clicks the blue button").
3. Extensions name the step number + condition, then numbered steps, then where they rejoin the MSS (or that the use case ends).
4. Brainstorm all extension conditions first ("what could go wrong at each step?"), then resolve them.
5. Mark included use cases like a hyperlink (underline or "include:").
6. Keep it short — a page or two. Detail only the risky use cases early; flesh others out just before implementation.
7. Pre-condition/guarantee/trigger only when they add value.

## Diagram notation

| Element | Notation |
|---|---|
| Actor | stick figure (or class box with `«actor»`), name below — a role noun |
| Use case | ellipse with a verb-phrase name |
| System boundary | rectangle with the system's name; use cases inside, actors outside |
| Association | solid line between actor and use case (no arrowheads needed; optionally arrow from primary actor) |
| Include | dashed arrow from the **including** (base) use case to the **included** one, labelled `«include»` |
| Extend | dashed arrow from the **extending** use case to the **base**, labelled `«extend»`; base declares extension points |
| Generalization | hollow triangle, between actors or between use cases |

## Rules
- Show only actors and **sea-level** use cases (plus includes that matter). ≤ ~15 use cases per diagram.
- Actors outside the boundary, use cases inside. Primary actors on the left, secondary (systems) on the right.
- Prefer `«include»` only. Avoid `«extend»` and use-case generalization unless the team already uses them precisely — they cause long, unproductive debates; handle variants as extensions in the text.
- Name use cases from the actor's point of view as goals: "Withdraw Cash", not "Cash Withdrawal Processing".

## Common mistakes
- Spending effort on the diagram while the text is missing.
- Functional decomposition: use cases for every step/screen ("Click Login", "Validate Field").
- Include/extend arrows pointing the wrong way (include: base → included; extend: extension → base).
- Data flows or sequencing drawn between use cases (a use case diagram has no order).
- Actors named after people or job titles that are not roles in this system; system internals (database) as actors.
- UML 1.1 `«uses»`/`«extends»` — replaced by `«include»`, `«extend»` and generalization.

## Review checklist
- [ ] Text exists (at least MSS + extensions) for the key use cases
- [ ] Use cases are goals (verb phrases), mostly sea level; no functional decomposition
- [ ] Actors are roles, outside the boundary; systems shown as actors when they're external
- [ ] Include/extend arrows point the right way; extend/generalization avoided unless justified
- [ ] No ordering/data flow between use cases
