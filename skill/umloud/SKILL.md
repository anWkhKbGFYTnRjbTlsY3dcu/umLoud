---
name: umloud
description: Create clear, correct, standards-compliant UML 2.5.1 diagrams (class, sequence, use case, activity, state machine, component, deployment, package, object, communication, timing, profile) as PlantUML and/or Mermaid. Use whenever the user asks for a UML diagram, to model or document a system, to visualise code structure or a flow, or to review/fix an existing UML diagram.
---

# umLoud — UML diagrams done right

UML 2.5.1, distilled from *UML Distilled* (3rd ed.). Load files **only when the step needs them**.

**Every output of this skill is PlantUML and/or Mermaid source — a code block and/or a `.puml`/`.mmd` file.**
Never answer a UML request with a hand-drawn picture, a generic SVG/image, or prose instead of that source.
If what you are about to produce isn't PlantUML or Mermaid text, stop — you have left the skill.

## 1. Ask for the format — once, first, before anything else
This is a single step: ask the question below, then wait. Don't also react to the need for a format anywhere
else — there is exactly one question call for format (+ Confluence), made here, not repeated or pre-empted.

Runs **first**, before reading any other file, before picking a diagram type, before drawing or writing
anything — no exceptions for a request that sounds "small", "quick", "simple", or "just one diagram".

**"The user didn't specify a format" is not a green light to pick one yourself — it's the reason to ask.**
Not-specified means ask, it never means default; there is no default format for a live conversation. Writing
"since you didn't specify a format, I'll use PlantUML" is the exact mistake this step exists to stop.

Ask (use a multiple-choice question tool if one is available; otherwise ask in plain text and wait for the
reply — do not answer your own question):

> **Which format?**
> - **PlantUML** — full, standard UML notation for all 14 diagram types; needs a PlantUML renderer or IDE/Confluence plugin.
> - **Mermaid** — renders natively in GitHub, GitLab, Notion, Obsidian (Confluence via an app); simpler, but only class, sequence and state diagrams are true UML — others are approximations.
> - **Both**

If the answer includes Mermaid and the user hasn't said where it goes, also ask (same question call):
> **Is the Mermaid for Confluence?**
> - **Yes** — older, conservative syntax that Confluence Mermaid apps accept; raw code to paste into the macro.
> - **No** — modern Mermaid (titles, notes, namespaces, object boxes) for GitHub, GitLab, Notion, Obsidian, docs sites.

Skip this only in these two cases, and no others:
- **Already known** — the user named the format (or Confluence/not) earlier in this same conversation.
- **Unattended** — this is a scheduled/background run with no person to reply to a question at all (not simply
  "the person hasn't answered yet in this message"). Here, default to PlantUML and say so explicitly in the
  delivered output.

Remember the answer(s) for the rest of the conversation.

## 2. Pick the diagram
- User named a type that fits → skip to 3. Otherwise read `references/00-choosing-a-diagram.md`.
- One diagram = one purpose; split big requests. Default mode: sketch, software perspective.

## 3. Load only these
| Need | File |
|---|---|
| Rules for the type (always) | `references/<type>.md` — `class`, `object`, `package`, `sequence`, `communication`, `use-case`, `state-machine`, `activity`, `component`, `deployment`, `other-diagrams` (interaction overview, timing, collaboration, profile) |
| Syntax for the chosen format | `syntax/<plantuml|mermaid>/_common.md` + `syntax/<plantuml|mermaid>/<type>.md`; modern Mermaid also `syntax/mermaid/_modern.md` |
| Naming, notes, size limits | `references/01-general-principles.md` (first diagram of a conversation only) |
| Starting skeleton (optional) | `templates/<plantuml|mermaid>/<type>.*` |
| MDA / Executable UML / code generation | `references/mda.md` |
| Old (UML 1) diagram or version questions | `references/uml-versions.md` |
| Final QA | `references/review-checklist.md` |

## 4. Draw and review
1. Use only facts from the user; list assumptions instead of inventing elements.
2. Write the source to `<name>.puml` / `<name>.mmd`, applying the loaded syntax rules carefully — this is a
   draft, not yet render-checked (that's step 6, and it's opt-in).
3. Run `review-checklist.md` by reading the source back against it; fix what fails. Its technical item allows
   for not having rendered yet: "Sources render … or stated that rendering wasn't possible."

## 5. Deliver
Give the plain, copyable source — some clients turn a ` ```mermaid ` block into a live diagram preview and hide
the underlying code from selection/copy, so never rely on the code block alone as "the preview". Always also
save the source to `<name>.puml` / `<name>.mmd` as a real file, and say so ("source saved as `<name>.mmd`").

**Mermaid for Confluence →** one copy-paste block per diagram with only raw Mermaid (no fences inside), preceded by its
name and *"Paste into your Confluence Mermaid macro."*; save as `<name>.mmd`.
**Mermaid modern →** fenced ```` ```mermaid ```` blocks (render in Markdown hosts); save as `<name>.mmd`.
**PlantUML →** code block(s) and `<name>.puml` files.
Then 2–4 bullets: assumptions,
key modelling decisions, approximations/gaps. For use cases, also the use-case text. No step-by-step recap.

End the delivery with a follow-up question (same message, not a separate turn):
> **Want me to validate this?** I'll render-check it and send a preview image.

## 6. If they say yes to validation
Run `python scripts/validate.py <files> --out <dir> --format png` (PNG renders inline more reliably than SVG
in most clients); add `--confluence` for Confluence Mermaid and fix any `WARN`. If it fails to render, fix the
source and re-deliver the corrected version. On success, send/attach the rendered `<name>.png` as the preview
image alongside the already-delivered source.

**No Python/shell/code execution available at all** (some agent environments don't have one): say so plainly
instead of running it — don't fabricate a render result. Point the person to https://www.plantuml.com/plantuml/uml/
or https://mermaid.live to check it themselves.

## Non-negotiables
UML 2.5.1 notation, no invented symbols · correct directions (generalization → supertype, dependency → supplier,
composition diamond at the whole, `«include»` → included, `«extend»` → base) · no aggregation diamond ·
sequence: one scenario, UML 2 frames · activity: explicit merge/join · state machine: one object, `event [guard] / activity` ·
small, selective diagrams.

## Reviewing an existing diagram
Load its type reference + checklist; list problems (most serious first, with the rule broken); give the corrected
diagram in the user's format.
