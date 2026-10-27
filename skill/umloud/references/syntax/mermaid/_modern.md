# Mermaid — modern profile (not for Confluence)

Load only when the user wants Mermaid **not** for Confluence (GitHub, GitLab, Notion, Obsidian, docs sites, current Mermaid Live).
Start from the type's syntax file (Confluence-safe, works everywhere), then use these newer features where they help.
Deliver as a fenced ```` ```mermaid ```` block so Markdown hosts render it.

| Feature | Use for |
|---|---|
| Front-matter `---` / `title: …` / `---` before the diagram type | Real diagram title (instead of a `%%` comment) |
| `direction LR` / `TB` inside `classDiagram` and `stateDiagram-v2` | Better layout |
| `note for Class "…"` in class diagrams | Constraints and notes attached to a class |
| `class id["label"]` | Object diagrams (`name : Class` boxes with slots) |
| `namespace Name { … }` in class diagrams | Packages that show their classes |
| `create participant X` / `destroy X` in sequence diagrams | UML creation and deletion |

## Class diagram with title, direction and note

```mermaid
---
title: Order processing — software perspective (sketch)
---
classDiagram
  direction TB
  class Order {
    +isPrepaid : Boolean [1]
    +dispatch()
  }
  class Customer {
    <<abstract>>
    +creditRating()* Rating
  }
  Order "*" --> "1" Customer : customer
  note for Order "If customer.creditRating is POOR then isPrepaid must be true"
```

## Object diagram with labelled instance boxes

```mermaid
classDiagram
  class eng["engineering : Organization"] {
    location = "Boston"
  }
  class tools["tools : Organization"] {
    location = "Chicago"
  }
  class don["don : Person"] {
    location = "Champaign"
  }
  eng -- tools : children
  tools -- don
  note "Object diagram: boxes are instances (name : Class)"
```

## Packages with their classes

```mermaid
classDiagram
  namespace UIControls {
    class Button
    class OnOff {
      <<interface>>
      +turnOn()
      +turnOff()
    }
  }
  namespace Heating {
    class Heater
  }
  Button ..> OnOff
  OnOff <|.. Heater
```

## Sequence diagram with title, creation and deletion

```mermaid
---
title: sd Run a query
---
sequenceDiagram
  participant O as anOrder : Order
  O->>O: prepare()
  create participant Q as aQuery : DbQuery
  O->>Q: new
  O->>+Q: execute()
  Q-->>-O: results
  destroy Q
  O->>Q: close()
```
