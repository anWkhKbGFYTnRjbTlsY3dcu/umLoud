# Mermaid — Use cases (text first, diagram second)

Rules live in `references/use-case.md`; this file is syntax only. Read `syntax/mermaid/_common.md` first.

Mermaid has **no use-case diagram type**. Use this flowchart convention and say it is an approximation:
actors as plain boxes marked «actor», use cases as stadium shapes inside a subgraph (system boundary).

```mermaid
flowchart LR
  Customer["«actor»<br/>Customer"]
  SM["«actor»<br/>Sales Manager"]
  PG["«actor»<br/>Payment Gateway"]
  subgraph store [Online Store]
    Buy([Buy a Product])
    Browse([Browse Catalog and Select Items])
    Track([Track Order])
    Report([Review Sales Report])
  end
  Customer --- Buy
  Customer --- Track
  SM --- Report
  Buy --- PG
  Buy -. "«include»" .-> Browse
```
