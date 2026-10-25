# UML versions: what changed after *UML Distilled* (3rd ed.)

Load when reviewing older diagrams or when the user asks about UML versions.
The book follows the late UML 2.0 drafts (2003). Versions 2.1–2.4.1 were corrections and 2.5 (2015) rewrote the
specification text (single document, compliance levels removed) with very few notation changes. What matters for drawing:
- **14 official diagram types**, not 13: the **profile diagram** was added in UML 2.2 (see `other-diagrams.md`).
- Final names differ from the book's draft terms: sequence frame **`critical`** (book: `region`); **collaboration use** (book: collaboration occurrence).
- **Association-end ownership dot** (small filled dot at an association end = that end is a property owned by the class at the opposite end) — optional; use only in blueprints/tool models.
- `{frozen}` was **not** reinstated; the standard term is `{readOnly}`. Treat `{frozen}` as a labelled convention.
- SysML v2 is now a separate language with its own syntax (no longer a UML profile); don't mix its notation into UML diagrams.

