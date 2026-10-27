# Mermaid — Communication diagrams

Rules live in `references/communication.md`; this file is syntax only. Read `references/syntax/mermaid/_common.md` first.

```mermaid
flowchart LR
  O[":Order"]
  L[":OrderLine"]
  P[":Product"]
  C[":Customer"]
  O -- "1.1 *[for each line]: calculatePrice() →" --- L
  L -- "1.1.1: getPrice(quantity) →" --- P
  O -- "1.2: getDiscountedValue(this) →" --- C
```

**Limitations (both tools):** message arrows are written as text (`→`) on the link label, not drawn alongside the link.
