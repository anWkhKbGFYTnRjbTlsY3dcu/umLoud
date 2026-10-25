# Package diagrams

Show **compile-time grouping** (namespaces, modules, layers, subject areas) and the **dependencies**
between groups. One of the most valuable diagrams for keeping a large system's structure under control.

## Use when / avoid when
- Use: logical road map of a system; checking/communicating layering; dependency control; deciding module boundaries.
- Avoid: runtime structure (→ composite structure/component); physical deployment (→ deployment).

## Notation

| Element | Notation | Notes |
|---|---|---|
| Package | tabbed folder; name on the tab (contents shown) or in the body (contents hidden) | Contents may be listed by name or drawn as class boxes. |
| Fully qualified name | `Outer::Inner::ClassName` | Packages are namespaces; names unique within a package. |
| Visibility of contents | `+` public (part of the package's interface), `-` private | Follow your language's rules. |
| Dependency | dashed arrow from client package to supplier package | Exists if any class in the client depends on any class in the supplier. |
| Realization between packages | dashed line + hollow triangle | One package implements interfaces defined in another. |
| Import / merge | dependency with `«import»`, `«access»`, `«merge»` | Language-specific; prefer plain dependencies. |
| Widely used package | keyword `«global»` on the package | Avoids drawing a dependency from everything to it (convention). |

## Design rules to check (and comment on)
- **Clear flow**: dependencies mostly run one way (e.g. presentation → domain → data mapper → database).
- **No cycles across layers**; keep any cycles local (Acyclic Dependencies Principle).
- **Stable Dependencies**: depend in the direction of stability; heavily depended-on packages need stable interfaces.
- **Stable Abstractions**: stable packages should contain a higher proportion of interfaces/abstract classes.
- **Common Closure**: classes that change together belong together. **Common Reuse**: classes reused together belong together.
- **Separated Interface**: to break an unwanted dependency, define the interface in the client package and implement it elsewhere.
- **Facade**: shrink a package's public surface by exposing a few public facade classes.
- Dependencies are **not transitive** — a change rippling A→B stops unless B's interface changes.
- Ideally generate the package diagram from the code to see what's really there; draw the intended one to compare.

## Common mistakes
- Arrows pointing from supplier to client (they go from the dependent package to the one it depends on).
- Showing every class inside every package — use names or hide contents.
- Mixing two structures (layers × subject areas) in one tangled diagram; split into two aspect views (non-standard but clear — label it).
- Cycles between layers not flagged.
- Using packages to show runtime containment.

## Review checklist
- [ ] Arrows from dependent → depended-on package
- [ ] Clear direction of flow; cycles absent or flagged and local
- [ ] Contents hidden unless they make the point
- [ ] Separated interfaces / facades shown where they explain a broken dependency
