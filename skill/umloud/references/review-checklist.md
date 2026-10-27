# Final review checklist (run before delivering any diagram)

Go through every item. Fix what fails; mention anything deliberately left non-standard.

## 1. Purpose
- [ ] The diagram type answers the reader's question (see `00-choosing-a-diagram.md`).
- [ ] Title states what it shows; mode (sketch/blueprint) and perspective (conceptual/software) are clear.
- [ ] It's focused: one scenario / one object / one concern. Size within limits (classes ≤ ~15, lifelines ≤ ~8, actions ≤ ~20, states ≤ ~12 per level).

## 2. Correctness (standard UML 2)
- [ ] Every symbol means what UML says it means (arrowheads, line styles, diamonds, triangles).
- [ ] Relationship directions are right: generalization → supertype; dependency → supplier; include → included use case; extend → base use case; composition diamond on the whole.
- [ ] Multiplicities present where they matter, and consistent across diagrams.
- [ ] Guards on decisions/transitions are mutually exclusive (and complete where needed, `[else]`).
- [ ] No UML 1-only notation (underlined lifelines, iteration markers on sequence messages, discontinuous multiplicities, `«uses»`), unless matching an existing UML 1 model on purpose.
- [ ] No invented symbols; non-standard conventions are explained in a note/legend.

## 3. Consistency with the user's facts
- [ ] Every element comes from the user's description/code — nothing invented. Assumptions are listed for the user.
- [ ] Names match the user's domain vocabulary (and match across formats if both were produced).
- [ ] If both formats: they show the same model (Mermaid may only lose notation, never content).

## 4. Readability
- [ ] Main flow direction consistent; minimal line crossings.
- [ ] Nothing shown that doesn't serve the purpose (trivial getters, every dependency, every return arrow).
- [ ] Labels short; naming conventions followed (see `01-general-principles.md`).

## 5. Technical
- [ ] Sources render (ran `scripts/validate.py`, or stated that rendering wasn't possible).
- [ ] For complex layouts, looked at the rendered image (overlaps, labels on the right lines).
- [ ] Mermaid approximations are labelled as such, with known gaps stated.

## Cross-diagram mistakes seen most often
1. Too much detail — completeness over communication.
2. Aggregation diamonds with no defined meaning.
3. Mixing several scenarios/objects/concerns in one diagram.
4. Control logic stuffed into sequence diagrams (use activity diagrams or code).
5. Use-case diagrams without use-case text; functional decomposition of use cases.
6. Activity diagrams with implicit joins/merges (multiple arrows into an action).
7. State machines that are really flowcharts.
8. Structural diagrams without any behavioural companion.
9. Wrong arrow directions on dependencies/includes/extends.
10. Using a UML diagram where a table (decision table, state table) or short text is clearer — it's fine to recommend that.
