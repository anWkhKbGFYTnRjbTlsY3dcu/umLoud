# Choosing a diagram

Pick the diagram from the **question the reader needs answered**, not from what you know how to draw.
If two diagrams fit, choose the one the audience will read most easily (sequence > communication,
text use case > use case diagram, activity > interaction overview).

| The reader's question | Diagram | Reference |
|---|---|---|
| What things exist and how are they related? (domain vocabulary or code structure) | Class | `class.md` |
| What does one concrete example configuration look like? | Object | `object.md` |
| How is the code split into modules, and which depends on which? | Package | `package.md` |
| How do several objects collaborate in **one** scenario, in time order? | Sequence | `sequence.md` |
| Same as above, but the **links** between participants matter more than the order | Communication | `communication.md` |
| What can users/external systems do with the system? | Use case (text first, diagram as a table of contents) | `use-case.md` |
| How does **one** object react to events over its whole lifetime? | State machine | `state-machine.md` |
| What is the procedure / workflow / business process, including parallel work? | Activity | `activity.md` |
| What replaceable parts make up the system and through which interfaces do they connect? | Component (+ composite structure for internals) | `component.md` |
| Which software runs on which hardware / runtime, and how do nodes talk? | Deployment | `deployment.md` |
| Control flow between several interactions; timing constraints between state changes; patterns/roles | Interaction overview, Timing, Collaboration | `other-diagrams.md` |
| Which custom stereotypes/tagged values does our modelling profile define, and what do they extend? | Profile | `other-diagrams.md` |

## Quick discriminators

- **One object, many scenarios** → state machine. **Many objects, one scenario** → sequence.
  **Many objects, many scenarios / parallel steps** → activity.
- **Compile-time grouping** (namespaces, modules) → package. **Run-time decomposition** of a thing into parts → composite structure / component.
- **Logical pieces** (components) vs. **physical files** (artifacts, shown on deployment diagrams).
- Complicated conditional logic with many combinations → a **decision table** (not UML) is often clearer than any diagram. Say so.
- If no UML diagram fits (e.g., screen flow), it is fine to use a clear non-UML diagram — state that it is non-UML.

## Usage mode and perspective (decide before drawing)

Ask (or infer) two things; they change how much detail is correct:

1. **Mode**
   - *Sketch* (default): selective, communicates the important parts only. Leave out anything that does not serve the point.
   - *Blueprint*: complete for the area it covers; every element a programmer needs is present and precise.
   - *Programming language*: the model **is** the source — tools turn it into running code (see the box below). Rare; only on request — then read `mda-executable-uml.md`.
2. **Perspective**
   - *Conceptual*: vocabulary of a business domain. No navigability arrows, no visibility, no implementation types, operations only as responsibilities.
   - *Software*: elements map to code; types, navigability, visibility and operations are meaningful.

State the chosen mode and perspective in the diagram title or a note when it is not obvious.


## Recommended "document a system" set

For documentation of an existing system, a small, curated set beats a complete one:
1. One **package** diagram as the logical road map (plus a **deployment** diagram for the physical picture).
2. Per important package, one **class** diagram showing only key features ("graphical table of contents").
3. A handful of **sequence** diagrams for the most important interactions.
4. A **state machine** only for classes with genuinely complex lifecycles.
5. An **activity** diagram only for an algorithm/process that the diagram explains better than code.
