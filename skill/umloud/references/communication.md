# Communication diagrams

An interaction diagram that emphasises the **links** between participants; message order is given by
numbers instead of vertical position. (Called *collaboration diagrams* in UML 1.)

## Use when / avoid when
- Use: when the structure of links matters more than the exact order; quick whiteboard exploration (easy to rearrange).
- Avoid: when sequence matters or there are many messages — sequence diagrams are clearer and more widely understood. Default to a sequence diagram unless the user asks for this one.

## Notation

| Element | Notation |
|---|---|
| Participant | box `name : Class` (free placement) |
| Link | solid line between participants (an association instance or transient link) |
| Transient link | link labelled `«local»`, `«parameter»`, `«global»` (UML 1 keywords, still common convention) |
| Message | small arrow alongside a link, labelled `sequenceNumber: message(args)` |
| Sequence numbers | **nested decimal** (`1`, `1.1`, `1.2`, `1.2.1`) is legal UML — it shows which call happens inside which |
| Threads | letters: `A1`, `B2`; `1a1`, `1b1` = concurrent threads within message 1 |
| Iteration / guard | `*[for each line]` and `[condition]` on messages (legal here, unlike in UML 2 sequence diagrams) |
| Creation/deletion | keywords `«create»`, `«delete»` (convention) |

## Rules
- Use nested decimal numbering when there are nested calls; flat numbering (1, 2, 3) is common but ambiguous and non-standard — if used, say so.
- Keep it small (≤ ~6 participants, ≤ ~12 messages); otherwise draw a sequence diagram.

## Review checklist
- [ ] A sequence diagram wouldn't be clearer
- [ ] Links exist for every message path; transient links marked
- [ ] Numbering nested decimal (or flat, explicitly noted)
