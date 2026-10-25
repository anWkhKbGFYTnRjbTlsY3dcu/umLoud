# Object diagrams

A **snapshot** of objects (instance specifications) and their links at one point in time — "an example
configuration". Often a communication diagram without messages.

## Use when / avoid when
- Use: when a class diagram is precise but hard to understand (recursive structures, many optional links) — 1–2 examples make it click; test data; explaining a bug's object graph.
- Avoid: as a substitute for the class diagram; showing behaviour.

## Notation

| Element | Notation |
|---|---|
| Object (instance specification) | box with **underlined** name `instanceName : ClassName` (both parts optional; `:Person` keeps the colon; `john` alone is legal) |
| Attribute values (slots) | `name = value` in the second compartment |
| Link | solid line (instance of an association), optionally with role names |

Instance specifications may be partial: mandatory values may be omitted, and an abstract class may be named.

## Rules
- Every link must correspond to an association in the class model; respect its multiplicities.
- Show only slots that make the example meaningful.
- Pair the object diagram with (or place it next to) the class diagram it illustrates.
- Use realistic example values, not `foo`/`bar`.

## Common mistakes
- Names not underlined, or class names without the colon (`Person` reads as a class, `:Person` is an object).
- Links that violate the class model's multiplicities or don't exist as associations.
- Generalization arrows between objects (objects don't generalize).

## Review checklist
- [ ] Names `name : Class`, underlined (PlantUML) or explicitly noted as instances (Mermaid)
- [ ] Every link matches an association and its multiplicity
- [ ] Values are meaningful examples; only relevant slots shown
