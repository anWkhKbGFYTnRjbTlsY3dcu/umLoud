# General principles (apply to every diagram)

## Standard vs. conventional UML
- UML in practice has **descriptive** rules: the OMG standard is the main authority, but teams and the industry
  also use widely understood conventions. Prefer **standard (normative)** notation; when you use a
  convention that is not in the standard, keep it widely recognised and say so in a note or legend.
- A good design in slightly non-standard UML beats a "legal" diagram of a poor design — but never invent
  symbols. If you need a concept UML lacks, reuse the closest UML symbol and add a **keyword** (`«temporal»`, `«value»`).
- Target **UML 2.5.1** (OMG, December 2017 — still the current version; see `uml-versions.md` for changes since the book). When a user's existing diagram uses UML 1 notation, keep it consistent but point out the UML 2 equivalent.

## Suppression: absence means nothing
- Any information may be hidden on a given diagram. Readers must not infer anything from a missing element
  (a missing multiplicity is *unknown*, not `1`).
- Therefore: **show explicitly what matters** (e.g. write `[1]` when mandatory-ness is important) and suppress the rest.

## Selectivity
- One diagram, one purpose. Put the purpose in the title.
- Comprehensiveness is the enemy of comprehensibility: prefer several focused diagrams over one wall chart.
- Rough sizes that stay readable: ≤ ~15 classes per class diagram, ≤ ~8 lifelines per sequence diagram,
  ≤ ~20 actions per activity diagram, ≤ ~12 states per state machine level. Split or nest beyond that.
- Do not repeat information the code makes obvious (trivial getters/setters, every dependency).

## Names
- Classes/types: singular nouns in UpperCamelCase (`OrderLine`). Multivalued properties: plural (`lineItems`).
- Operations: verbs (`calculatePrice`). Use cases: verb phrase with the actor's goal (`Buy a Product`).
- States: adjectives or "-ing" forms (`Waiting`, `Open`). Actions: imperative verb phrases (`Fill Order`).
- Use the domain's own vocabulary; avoid vague association names like "has" or "is related to" — leave an
  association unnamed rather than name it meaninglessly.

## Keywords, stereotypes, property strings
- Keywords go in guillemets: `«interface»`, `«enumeration»`, `«component»`. In plain text `<<interface>>` is acceptable.
- Properties/constraints go in braces: `{abstract}`, `{ordered}`, `{readOnly}`, `{query}`.
- Do not call every guillemet word a "stereotype" — in UML 2 stereotypes belong to profiles; generic term is *keyword*.
- Abbreviations like `«I»`, `{A}` are non-standard: only use with a legend.

## Notes and constraints
- Notes (dog-eared box, dashed line to the element) can appear on any diagram. Use them for rationale,
  assumptions, and anything a reader would otherwise misread.
- Constraints go in `{ }` and may be natural language, code or OCL. Prefer natural language unless the readers know OCL.
  A constraint can be named: `{noSelfReference: a manager cannot manage themself}`.
- Document **design alternatives rejected and why** in notes or surrounding text — often the most useful documentation.

## Pair structure with behaviour
- A structural diagram alone hides how things work. When explaining software, pair a class/component
  diagram with at least one behavioural diagram (sequence, state, or activity).

## Layout hygiene (both tools)
- Main flow top→bottom or left→right; keep it consistent within a diagram.
- Avoid crossing lines; group related elements; put supertypes above subtypes, suppliers below or right of clients.
- Give every diagram a title. Add a legend when you use colours, abbreviations or conventions.
- Do not use colour as the only carrier of meaning.
