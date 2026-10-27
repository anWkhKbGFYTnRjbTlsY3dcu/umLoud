# Class diagrams

Describe the **types** in a system and the **static relationships** between them, plus their
properties, operations and constraints. The most used UML diagram — and the easiest to overload.

## Use when / avoid when
- Use: domain vocabulary (conceptual), code structure (software), "table of contents" of a package.
- Avoid: showing control flow or time order (use sequence/activity); showing one concrete example (use object diagram).
- Always pair with a behavioural diagram when explaining software — structure alone misleads.

## Core notation (start here — ~90% of real diagrams)

| Element | Notation | Notes |
|---|---|---|
| Class | box: name / attributes / operations | Name bold, singular. Hide empty compartments. |
| Attribute | `visibility name : Type [multiplicity] = default {props}` | Only the name is mandatory. e.g. `- name : String [1] = "Untitled" {readOnly}` |
| Operation | `visibility name(direction param : Type = default) : ReturnType {props}` | direction `in` (default) / `out` / `inout`. Mark side-effect-free ones `{query}`. |
| Association | solid line; role name + multiplicity at the **target** end | Same concept as an attribute (both are *properties*). |
| Navigability | open arrowhead at the navigable end; arrows both ends = bidirectional | No arrows = bidirectional **or** unspecified. Omit arrows on conceptual diagrams. |
| Multiplicity | `1`, `0..1`, `*` (= `0..*`), `1..*`, `2..4` | No discontinuous ranges (`2,4`) — removed in UML 2. |
| Generalization | solid line, hollow triangle at supertype | Must satisfy substitutability (LSP). |
| Dependency | dashed line, open arrow from client to supplier | Optional keyword: `«use»`, `«call»`, `«create»`, `«instantiate»`, `«realize»`, `«refine»`, `«trace»`, `«permit»`, `«derive»`, `«substitute»`. |
| Note | dog-eared box, dashed line to element | Any diagram. |
| Constraint | `{text}` near the element(s) | Natural language, code, or OCL. |

### Attribute vs. association (same thing, different emphasis)
- Use **attribute** text for small value types (dates, booleans, money, strings).
- Use an **association** line for significant classes that deserve their own box on this diagram.
- Never show the same property both ways on one diagram.

### Multiplicity and collections
- Multivalued ends are **sets** by default (unordered, unique). Add `{ordered}` when order matters, `{nonunique}` to allow duplicates (`{bag}` = unordered + nonunique).
- Name multivalued properties in the plural (`lineItems`, `cars`).
- Don't draw collection classes (`List`, `ArrayList`) as associations — a `*` already means "a collection". Only low-level implementation diagrams show them.
- Optional = lower bound 0; mandatory = lower bound ≥ 1; single-valued = upper bound 1; multivalued = upper bound > 1.

### Operations
- Don't list operations that merely get/set properties — they are implied.
- Conceptual perspective: operations are **responsibilities** (a few words), not an interface spec.
- Prefer command–query separation: modifiers return nothing; value-returning operations are `{query}`.
- A property models something an object can **always** provide. A transient relationship (a parameter used during one call) is a **dependency**, not an association.

### Dependencies
- Show only dependencies relevant to the diagram's point; drawing all of them is futile (tools can generate them).
- Make them point one way across layers (presentation → domain → data). Flag cycles, especially across layers/packages.
- Dependency is **not** transitive: A→B→C does not mean A depends on C.

## Advanced notation (introduce only when needed)

| Concept | Notation | Guidance |
|---|---|---|
| Interface | class box with `«interface»`, or a ball (lollipop) | A class **provides** an interface (realization: dashed line + hollow triangle, or a ball) and **requires** one (dependency, or a socket). Ball-and-socket is the clearest UML 2 notation. |
| Abstract class / operation | *italic* name, or `{abstract}` | Use `{abstract}` where italics are unreliable (whiteboards, some renderers). |
| Enumeration | box with `«enumeration»`, values listed | Values have no properties beyond their symbol. |
| Static feature | underlined | |
| Visibility | `+` public, `-` private, `#` protected, `~` package | Meaning varies by language; show only when it matters. |
| Derived property | prefix `/` (e.g. `/length`) | Best read as a constraint between values, not "computed vs stored". |
| Read-only / immutable | `{readOnly}` (clients can't change) / `{frozen}` (never changes; a convention — dropped in UML 2.0 and not reinstated through 2.5.1) | |
| Composition | filled diamond at the **owner (whole)** end | An instance has **at most one owner** at a time ("no sharing"); deleting the owner deletes parts. Owner-end multiplicity is `0..1` or `1`. |
| Aggregation | hollow diamond | Has no defined semantics — **avoid it**. If you meet it, ask what the author meant. Use plain association or composition instead. |
| Association class | class box attached to the association by a dashed line | Implies **only one** instance per pair of linked objects. If the pair may have several (e.g. a company with several roles on one contract) promote it to a full class. |
| Qualified association | small box (qualifier) at the source end | UML's map/dictionary. Multiplicity at the far end is **per qualifier value** (`0..1` = at most one line per product). |
| Template (generic) class | dashed box with type parameter at top-right; bound: `Set<T->Employee>` or `«bind»` | A bound element cannot add features — subclass it instead. |
| Active class | class box with double vertical side lines | Instances run their own thread of control. |
| Generalization set | label on the generalization arrows; `{disjoint}`/`{overlapping}`, `{complete}`/`{incomplete}` | For multiple classification. Default: single static classification — use that unless modelling concepts. |
| Association-end ownership | small filled dot on the line at an end (UML 2.1+) | The end is a property owned by the class at the **opposite** end. Optional — leave it out of sketches. |
| Responsibilities | an extra compartment with short sentences | Handy on conceptual diagrams and CRC-style design. |
| Value object | composition to it, or keyword `«value»`/`«struct»`; UML `«dataType»` when it has no identity | Value objects should be immutable. |
| Classification ("is instance of") | dependency `«instantiate»` | Don't confuse with generalization: generalization is transitive, classification is not. Test subtypes with "every instance of X is an instance of Y". |

## Common mistakes
1. Drawing **everything**: all classes, all operations, all getters/setters, all dependencies.
2. Aggregation diamonds used vaguely to mean "has".
3. Composition where parts are actually shared between owners.
4. Composition diamond on the wrong end (it goes on the **whole**).
5. Collection classes drawn as associations instead of using multiplicity `*`.
6. The same property shown as both an attribute and an association.
7. Associations named "has"/"contains"/"relates to".
8. Navigability arrows and visibility markers on a conceptual model.
9. Inheritance used for "is-a" that fails substitutability, or for an instance-of relationship.
10. Data-only classes (fields + accessors) — a design smell; behaviour should live with the data.
11. Association used for a transient relationship (a method parameter) — that's a dependency.
12. Association class used when the pair can legitimately repeat.
13. Missing multiplicity where it matters (readers can't assume a default).
14. Discontinuous multiplicities (`2,4`) or UML 1 keywords on associations (`«parameter»`, `«local»`).

## UML 1 → UML 2 notes
- Attributes and unidirectional associations are the same concept (*property*).
- Discontinuous multiplicities and `{frozen}` dropped (frozen still common as convention).
- Guillemet words are *keywords*; only some are stereotypes.
- Classes can **require** interfaces (socket notation is new in UML 2).
- Generalization sets replace the UML 1 "discriminator".
- Active class: double side bars (UML 1 used a thick border).

## Review checklist
- [ ] Title states purpose, perspective (conceptual/software) and mode (sketch/blueprint)
- [ ] Only classes/features relevant to the purpose; ≤ ~15 classes
- [ ] Every association end that matters has multiplicity; multivalued names plural
- [ ] No aggregation; composition only with exclusive ownership, diamond on the whole
- [ ] Generalizations pass "every instance of Sub is an instance of Super"
- [ ] Conceptual diagram: no navigability, visibility or implementation types
- [ ] Dependencies one-directional across layers; cycles flagged
- [ ] Constraints that the shapes can't express are written in `{ }` or notes
