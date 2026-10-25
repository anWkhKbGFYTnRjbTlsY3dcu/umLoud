# Mermaid — Sequence diagrams

Rules live in `references/sequence.md`; this file is syntax only. Read `syntax/mermaid/_common.md` first.

```mermaid
sequenceDiagram
  %% sd Calculate order price (distributed control)
  participant Caller as caller
  participant O as anOrder : Order
  participant L as anOrderLine : OrderLine
  participant P as aProduct : Product
  participant C as aCustomer : Customer

  Caller->>+O: calculatePrice()
  loop for each line item
    O->>+L: calculatePrice()
    L->>+P: getPrice(quantity)
    P-->>-L: price
    L-->>-O: price
  end
  O->>+C: getDiscountedValue(anOrder)
  C->>+O: getBaseValue()
  O-->>-C: baseValue
  C-->>-O: discountedValue
  O-)C: notifyPriceChanged()
  Note over O,C: ref: Notify customer (separate diagram)
  O-->>-Caller: price
```

Mermaid syntax: `->>` synchronous (filled head), `-)` asynchronous (open head), `-->>` return;
`+`/`-` after the arrow activate/deactivate; frames `loop`, `alt … else … end`, `opt`, `par … and … end`,
`critical … option … end`, `break`; `Note over A,B: text`.

**Mermaid limitations:** no found message (add a `caller` participant and say so); no `ref` frame (use a
note `ref: <name>`); no `neg` frame; `create participant` / `destroy` exist only in newer Mermaid
(v10.3+) — many Confluence Mermaid apps bundle older versions, so avoid them for Confluence or
check the app's version; nested activations on self-calls render, but less clearly than PlantUML.
