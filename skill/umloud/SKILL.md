---
name: umloud
description: Create, review and fix UML 2.5.1 diagrams in PlantUML or Mermaid: class, sequence, use case, activity, state machine, component, deployment, package and more. Use whenever the user asks for a UML diagram, wants to model a system, visualise code structure or a flow, or have a UML diagram reviewed.
version: 1.0.0
allowed-tools: Read, Write, Bash(python scripts/validate.py:*)
metadata:
  author: umLoud contributors
  tags: [uml, diagrams, plantuml, mermaid]
---

# umLoud — UML diagrams done right

## Purpose
Produce, review and fix UML 2.5.1 diagrams as PlantUML and/or Mermaid source. Covers class, sequence, use case,
activity, state machine, component, deployment, package, object, communication, timing, interaction overview and profile.
UML 2.5.1, distilled from *UML Distilled* (3rd ed.). Load files **only when the step needs them**.

**Every output of this skill is PlantUML and/or Mermaid source — delivered as copy-pasteable code in the chat.**
Never answer a UML request with a hand-drawn picture, a generic SVG/image, or prose instead of that source.
If what you are about to produce isn't PlantUML or Mermaid text, stop — you have left the skill.

## Instructions

### 1. Ask for the format — once, first, before anything else
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

### 2. Pick the diagram
- User named a type that fits → skip to 3. Otherwise read `references/00-choosing-a-diagram.md`.
- One diagram = one purpose; split big requests. Default mode: sketch, software perspective.

### 3. Load only these
| Need | File |
|---|---|
| Rules for the type (always) | `references/<type>.md` — `class`, `object`, `package`, `sequence`, `communication`, `use-case`, `state-machine`, `activity`, `component`, `deployment`, `other-diagrams` (interaction overview, timing, collaboration, profile) |
| Syntax for the chosen format | `references/syntax/<plantuml|mermaid>/_common.md` + `references/syntax/<plantuml|mermaid>/<type>.md`; modern Mermaid also `references/syntax/mermaid/_modern.md` |
| Naming, notes, size limits | `references/01-general-principles.md` (first diagram of a conversation only) |
| Starting skeleton (optional) | `assets/templates/<plantuml|mermaid>/<type>.*` |
| MDA / Executable UML / code generation | `references/mda-executable-uml.md` |
| Old (UML 1) diagram or version questions | `references/uml-versions.md` |
| Final QA | `references/review-checklist.md` |

### 4. Draw and review
1. Use only facts from the user; list assumptions instead of inventing elements.
2. Write the source in your reply (nothing is saved to the user's disk), applying the loaded syntax rules carefully —
   this is a draft, not yet render-checked (step 6 is optional and only runs with the user's permission).
3. Run `review-checklist.md` by reading the source back against it; fix what fails. Its technical item allows
   for not having rendered yet: "Sources render … or stated that rendering wasn't possible."

### 5. Deliver
Give the plain, copyable source in the chat — the user copies it from there. **Do not save any file to the user's
disk.** Some clients turn a ` ```mermaid ` block into a live diagram preview and hide the underlying code from
selection/copy; if so, put the source in a ` ```text ` block instead, so it is always copyable.

**Mermaid for Confluence →** one copy-paste block per diagram with only raw Mermaid (no fences inside), preceded by its
name and *"Paste into your Confluence Mermaid macro."*
**Mermaid modern →** fenced ```` ```mermaid ```` blocks (render in Markdown hosts).
**PlantUML →** ` ```plantuml ` code block(s).
Then 2–4 bullets: assumptions,
key modelling decisions, approximations/gaps. For use cases, also the use-case text. No step-by-step recap.

End the delivery with a permission question (same message, not a separate turn). Skip it if no code execution is
available (see step 6). Nothing is run unless the user answers yes:
> **Want me to render-check this?** It runs PlantUML/Mermaid on temporary files (nothing is saved to your folders) and I'll send a preview image here. Optional.

### 6. Only if the user says yes
Validation is **optional and permission-based**: never run `validate.py` unless the user clearly agrees. No answer,
a topic change or an unclear reply means no — don't run it and don't ask again.

Write the delivered source to a **temporary** `.puml` / `.mmd` file outside the user's folders (system temp or
scratch), then run `python scripts/validate.py <temp files> --format png` **without `--out`** — previews go to a temp
directory too. Add `--confluence` for Confluence Mermaid and fix any `WARN`. If it fails to render, fix the source and
re-deliver the corrected version in the chat. On success, show the rendered PNG **in the chat only** (attach/send it with
the client's file or image tool). Never write the sources or the preview into the user's project folder.

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

## Available Scripts
| Script | Purpose | Arguments |
|---|---|---|
| `scripts/validate.py` | Render-check `.puml` / `.mmd` sources and write PNG/SVG previews | `<files>` plus the options below |

Run only with the user's permission (step 6), on temporary files: `python scripts/validate.py <temp files> --format png`

| Option | Meaning |
|---|---|
| `<files>` | One or more `.puml` / `.mmd` files, Markdown files (fenced blocks are checked) or directories |
| `--format png\|svg` | Preview image type (default `svg`; use `png` for chat) |
| `--out <dir>` | Output folder (default: a new temp directory; the path is printed last) |
| `--confluence` | Also warn about Mermaid syntax that older Confluence apps reject |
| `--plantuml-jar <path>` | PlantUML jar to use with `java` when `plantuml` isn't on PATH |
| `--chrome <path>` | Chrome/Chromium binary for Mermaid CLI when it can't find a browser |

Exit codes: `0` everything rendered · `1` at least one diagram failed · `2` no renderer found.

## Prerequisites
- PlantUML: `plantuml` on PATH, or `java` plus `--plantuml-jar <path>` (Graphviz `dot` for most layouts).
- Mermaid: Mermaid CLI (`mmdc`); if it can't find a browser, pass `--chrome <path>`.
- Without these, validation is skipped (see Limitations).

## Examples
Each shows the request, then what the skill does.

1. *"Class diagram for this code, Mermaid"* → format known: read `references/class.md` + `references/syntax/mermaid/class.md`, deliver the source in the chat, offer validation.
2. *"Model our checkout flow"* → format unknown: ask format first, then pick the type via `references/00-choosing-a-diagram.md` (likely activity or sequence).
3. *"Sequence diagram of login between browser, API and database, PlantUML"* → one scenario with UML 2 frames; `references/sequence.md` + `references/syntax/plantuml/sequence.md`.
4. *"State machine for an order: draft, submitted, approved, shipped, cancelled, Mermaid for Confluence"* → one object, `event [guard] / activity` labels; Confluence-safe syntax, raw block, no fences, "Paste into your Confluence Mermaid macro."
5. *"Use case diagram for an online library, both formats"* → actors, system boundary and `«include»` / `«extend»` directions checked; deliver both sources plus the use-case text.
6. *"Deployment diagram: web app on Kubernetes with a Postgres database, PlantUML"* → nodes and artifacts (physical files), not components; `references/deployment.md`.
7. *"Timing diagram of a traffic light, Mermaid"* → Mermaid has no timing diagram: say so and offer PlantUML, or a table.
8. *"Review this sequence diagram"* (pasted) → load `references/sequence.md` + `references/review-checklist.md`, list problems most serious first with the rule broken, give the corrected diagram in the user's format.
9. *"Is this still valid UML 1 notation?"* → read `references/uml-versions.md` and answer; no diagram needed.
10. *"Draw me a logo"* or *"make a flowchart image in Photoshop"* → not this skill: UML only, and always as PlantUML or Mermaid source.

## Limitations
- Mermaid only supports class, sequence and state diagrams as true UML; other types are approximations.
- Rendering needs local tools; without them, validation is skipped and the user is pointed to plantuml.com or mermaid.live.
- Diagrams use only facts the user supplies; unstated elements are listed as assumptions, not invented.

## Troubleshooting
| Error | Cause | Solution |
|---|---|---|
| `validate.py` can't find a renderer | PlantUML or `mmdc` not installed | Install it, or use plantuml.com / mermaid.live |
| `WARN` with `--confluence` | Syntax too new for Confluence Mermaid apps | Use the conservative syntax from `references/syntax/mermaid/_common.md` |
| Render fails on a Mermaid block | Modern-only syntax in a Confluence diagram | Rewrite without titles, notes or namespaces |
| Exit code `2` / every diagram `SKIP` | No renderer installed | Say rendering wasn't possible and point to plantuml.com or mermaid.live |
| Diagram renders but looks wrong or crowded | Too many elements, or the wrong diagram type | Split into smaller diagrams; re-check the type via `references/00-choosing-a-diagram.md` |
| User doesn't answer or declines the validation offer | Validation is optional | Don't run it and don't ask again; the delivered source stands |
| Mermaid block shows a picture and the code can't be copied | The client renders the fence | Re-send the source in a ` ```text ` block |
