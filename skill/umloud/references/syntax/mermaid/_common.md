# Mermaid — common rules

## What Mermaid can draw
Native: **class**, **sequence**, **state** (good). Approximated with flowcharts/class boxes: object, package, use case,
activity, component, deployment, communication, interaction overview, profile. **No timing diagram** (use a table).
Under an approximation add: *"Mermaid approximation — not full UML notation."* It may lose notation, never content.

## Syntax safety
- First line is the diagram type. Ids simple (`OrderLine`); display text in labels (`A["name : Type"]`).
- Quote labels with punctuation; `<br/>` for line breaks; `%%` comments; avoid `{ }` inside labels.
- Flowcharts: never use `end` as a bare node id. Sequence: never name a participant `x`, `X` or `o`
  (`A-->>-X` parses as a cross arrow).
- State descriptions: declare `state "Name" as Name` before `Name : entry / ...`, or the name is replaced.

## Two profiles
- **Confluence** (user said yes to Confluence): the rules below. Run `validate.py --confluence`.
- **Modern** (not for Confluence): these rules still work, plus the newer features in `_modern.md` (load it).
  Deliver fenced ```` ```mermaid ```` blocks; front-matter titles allowed.

## Confluence profile
Output must paste straight into a Confluence Mermaid macro (Mermaid apps often bundle an **older Mermaid**):
- Deliver **raw Mermaid only** per diagram: no Markdown fences inside, no `---` front-matter, no `title`/`accTitle`, no `%%{init}%%`.
  Put the diagram's title as the first `%%` comment line; captions and constraints go in the page text, not the code.
- Use only long-established syntax: `classDiagram`, `sequenceDiagram`, `stateDiagram-v2`, `flowchart`; `classDef`, `<br/>`, subgraphs.
- Avoid newer features: `note for` (class notes), `class id["label"]`, `namespace`, `direction` inside class/state diagrams,
  `create participant`/`destroy`, `*-beta` types, Markdown strings in labels. The type syntax files already follow these rules.
- Plain ASCII ids; Unicode (`«»`, `●`, `📁`) only inside quoted labels.

Rendering check: `mmdc` on PATH (`npm i -g @mermaid-js/mermaid-cli`); set `PUPPETEER_EXECUTABLE_PATH` if it can't find Chrome.
