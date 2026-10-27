# Component and composite structure diagrams

**Component diagrams** show replaceable, independently upgradable parts of a system and how they connect
through **provided** and **required interfaces**. **Composite structure** shows the **runtime internal
decomposition** of a class or component into parts, ports and connectors. They share notation, so they live together here.

## Use when / avoid when
- Use component: dividing a system into components (services, libraries, subsystems) and showing the interface contracts between them; showing a component's breakdown.
- Use composite structure: explaining how a complex class/component is wired internally at runtime.
- Avoid: physical files (→ artifacts on a deployment diagram); compile-time grouping (→ package); very fine-grained "components" (one per class) — too many is unmanageable.

What counts as a component is a judgement call: think "a piece a customer could buy or upgrade independently" — it's as much a business decision as a technical one.

## Notation

| Element | Notation | Notes |
|---|---|---|
| Component | rectangle with `«component»` and/or the small component icon at top-right | UML 1's big component symbol is gone. |
| Provided interface | ball ("lollipop") on a line from the component | Component realizes the interface. |
| Required interface | socket (half circle) on a line from the component | Component needs it. |
| Assembly | ball fitted into socket | Wiring between components. |
| Port | small square on the boundary | Groups related provided/required interfaces into one interaction point. |
| Part | box inside the component/class, `name : Type [multiplicity]`, **not underlined** | Parts are roles, not instances. |
| Connector | line between parts (or ball-and-socket) | |
| Delegation connector | arrow from an outer port/interface to the inner part that implements (or needs) it | |
| Dependency | dashed arrow | Between components when no interface is modelled. |

## Rules
- Connect components through **interfaces**, not directly, when the contract matters; name interfaces by role (`SalesMessage`, `PaymentAuthorization`).
- Each provided interface should be realized by something inside (delegate it to a part) in a composite view.
- Use ports when a component has several distinct conversations with the outside.
- Keep a component diagram at one level of granularity; decompose a component in its own diagram.
- ≤ ~10 components per diagram.

## Common mistakes
- Using the UML 1 component icon (two small bars) as the main shape.
- Components that are just classes (too fine-grained) or just deployment files (use artifacts).
- Ball and socket reversed (ball = provided, socket = required).
- Parts drawn underlined (that's instance notation).

## Review checklist
- [ ] Components at one level of granularity; ≤ ~10
- [ ] Interfaces named; provided (ball) vs required (socket) correct
- [ ] Provided interfaces delegate to internal parts in composite views
- [ ] Physical files appear as artifacts on deployment diagrams, not here
