# Sequence diagrams

Show how a group of participants collaborate in **one scenario**, with time running **down** the page.
They make "who calls whom and who does the work" obvious; they are poor at algorithms (loops, branches).

## Use when / avoid when
- Use: behaviour of several objects in a single use case/scenario; comparing design alternatives (centralized vs distributed control); explaining a complex method when reverse-engineering.
- Avoid: one object's behaviour across many scenarios (→ state machine); control-heavy logic or many threads/scenarios (→ activity diagram or pseudocode); rapid exploration of many alternatives (CRC cards are faster).

## Core notation

| Element | Notation | Notes |
|---|---|---|
| Participant | box at top + dashed lifeline | Name `name : Class` (either part optional, keep the colon if only the class: `: Order`). Style `anOrder` is fine. **Not underlined** in UML 2. |
| Activation bar | thin rectangle on the lifeline | Shows a method on the stack. Optional but recommended for clarity; may be dropped for trivial "fire and forget" calls. |
| Synchronous message | solid line, **filled** arrowhead | Caller waits. |
| Asynchronous message | solid line, **open (stick)** arrowhead | Caller continues. The difference is subtle — if asynchrony is the point, say so in a note too. |
| Return | dashed line, open arrowhead | Show only when it adds information (e.g. naming a returned participant: `aProduct`), otherwise omit. |
| Found message | message from no participant (from the frame edge / a filled dot) | The first message of the scenario from an undetermined source. |
| Self-call | message looping back to the same lifeline, nested activation | |
| Creation | message arrow pointing at the participant's **box** (box drawn lower down); label `new` | Start an activation right after if the new object immediately does work. |
| Deletion | big **X** at the end of the lifeline | Arrow into X = deleted by another; X alone = self-deletion. Also fine for "no longer usable" (closed, ready for GC). |
| Interaction frame | rectangle with operator in the top-left pentagon; fragments separated by dashed lines, each with a `[guard]` | See operators below. |

### Frame operators

| Operator | Meaning |
|---|---|
| `alt` | Alternatives; only the fragment whose guard is true runs. Use `[else]` for the default. |
| `opt` | Optional; runs only if the guard is true (an `alt` with one fragment). |
| `loop` | Repeats; the guard states the basis of iteration (`[for each line item]`). |
| `par` | Fragments run in parallel. |
| `critical` | Only one thread may execute the fragment at a time. (Called `region` in UML 2.0 drafts and in *UML Distilled*.) |
| `neg` | Shows an **invalid** interaction. |
| `ref` | Reference to an interaction defined in another diagram; covers the lifelines involved. |
| `sd` | Frame around a whole sequence diagram (with its name). |

## Rules
1. **One scenario per diagram.** Name it in the title (`sd Calculate order price`).
2. Order participants left→right in the order they are first involved; put the initiator (actor/found message) at the far left.
3. Keep it to roughly ≤ 8 participants and ≤ ~25 messages. Split with `ref` frames.
4. Messages are labelled as operation calls: `calculatePrice()`, `getPrice(quantity)`, optionally `result := op(args)`.
5. Use the same name for the same participant everywhere (a returned `aProduct` *is* the `aProduct` lifeline).
6. Prefer distributed control (each object does its own part) when designing; the diagram makes centralized "god object" control visible — point it out.
7. Use frames sparingly; if the diagram becomes mostly frames, switch to an activity diagram or pseudocode.
8. Use filled vs open arrowheads deliberately and consistently; don't let a renderer default pick for you.

## Common mistakes
- Underlined participant names (UML 1 style).
- Iteration markers (`*[for each]`) and guards on single messages — dropped from UML 2 sequence diagrams (still legal on communication diagrams). Use `loop`/`alt`/`opt` frames.
- Return arrows for every call (clutter), or using a return arrow as if it were a new call.
- Mixing several scenarios in one diagram with nested `alt` frames.
- Arrows going **up** the page (time only flows down).
- Using sync arrowheads for queue/event messages (or vice versa).
- Participants that never send or receive anything.

## UML 1 → UML 2 notes
- Interaction frames (`alt`, `loop`, `opt`, `par`, `ref`…) are new in UML 2; UML 1 used iteration markers and guards on messages.
- Lifeline heads are *participants* (not instances) — no underline.
- Since UML 1.4, stick arrowhead = asynchronous (before that it was a half-stick). Returns are dashed.
- Common unofficial convention: a *pseudo-message* (a self-call-like bar with the guard/loop condition) instead of heavy frames. Acceptable in sketches if explained.

## Review checklist
- [ ] Exactly one scenario; title names it
- [ ] Participants named `name : Class` consistently, not underlined
- [ ] Time flows down only; first message is a found message or from an actor
- [ ] Sync/async arrowheads chosen deliberately; returns only where informative
- [ ] Loops/conditions use UML 2 frames with guards, and there aren't so many that code would be clearer
- [ ] ≤ ~8 participants; long parts factored into `ref`
