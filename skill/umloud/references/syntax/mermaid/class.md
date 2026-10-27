# Mermaid — Class diagrams

Rules live in `references/class.md`; this file is syntax only. Read `references/syntax/mermaid/_common.md` first.

```mermaid
classDiagram
  %% Order processing — software perspective (sketch)
  class Customer {
    <<abstract>>
    +name : String [1]
    +address : Address [0..1]
    +creditRating()* Rating
  }
  class CorporateCustomer {
    +contactName : String
    +creditLimit : Money
    +billForMonth(month : Integer)
  }
  class PersonalCustomer {
    +creditCardNumber : String [0..1]
  }
  class Order {
    +dateReceived : Date [0..1]
    +isPrepaid : Boolean [1]
    +/price : Money
    +dispatch()
    +close()
  }
  class OrderLine {
    +quantity : Integer [1]
    +price : Money
  }
  class Rating {
    <<enumeration>>
    POOR
    GOOD
    EXCELLENT
  }
  Customer <|-- CorporateCustomer
  Customer <|-- PersonalCustomer
  Order "*" --> "1" Customer : customer
  Order "1" *-- "*" OrderLine : lineItems ordered
  OrderLine "*" --> "1" Product : product
  Customer ..> Rating
  %% Constraint: if customer.creditRating is POOR then isPrepaid must be true (write it in the Confluence page text)
```

Mermaid syntax: `<|--` generalization, `<|..` realization, `*--` composition, `o--` aggregation (avoid),
`-->` association, `..>` dependency; `<<interface>>`/`<<abstract>>`/`<<enumeration>>` as first line in the class;
method suffix `*` = abstract, `$` = static; generics `class Set~T~`.

**Mermaid limitations (say so when it matters):** no qualified associations; no true association class
(approximate with a dashed link `..` to the class plus a note); role name and multiplicity can't be
placed independently at each end (put the role name in the link label); no italics for abstract — use
`<<abstract>>`; no generalization sets; no `{constraint}` placement except via notes; braces in labels
can break parsing — write `ordered` instead of `{ordered}` in link labels.
