# Mermaid — less common diagrams

Rules live in `references/other-diagrams.md`. Read `references/syntax/mermaid/_common.md` first.

## Interaction overview diagrams (approximation)

```mermaid
flowchart TB
  s((" ")):::initial --> d{"customer external?"}
  d -- "[yes]" --> x["ref: Get order data from XML"]
  d -- "[else]" --> db["ref: Get order data from database"]
  x --> m{ }
  db --> m
  m --> f["ref: Format order summary report"]
  f --> e((("●"))):::final
  classDef initial fill:#000,stroke:#000,color:#000
  classDef final fill:#fff,stroke:#000,stroke-width:2px,color:#000
```

## Timing diagrams

Mermaid has **no timing diagram**. Use PlantUML, or a table of events with timing constraints as a fallback, and state that limitation.

## Collaborations

No collaboration notation — annotate classes with a `<<pattern: role>>` line or a note instead.

## Profile diagrams (added in UML 2.2) (approximation)

```mermaid
classDiagram
  class Class {
    <<metaclass>>
  }
  class Property {
    <<metaclass>>
  }
  class Entity {
    <<stereotype>>
    tableName : String [0..1]
  }
  class Id {
    <<stereotype>>
    generated : Boolean = true
  }
  Class <|-- Entity : extension
  Property <|-- Id : extension
  note "«profile» Persistence — hollow heads stand in for UML's filled extension arrow"
```
