# Mermaid — Activity diagrams

Rules live in `references/activity.md`; this file is syntax only. Read `syntax/mermaid/_common.md` first.

Mermaid has **no UML activity diagram**; use this flowchart convention (and say so):
initial = small filled circle, final = double circle, actions = rounded boxes, decision/merge = diamonds,
fork/join = black bar node, partitions = subgraphs.

```mermaid
flowchart TB
  start((" ")):::initial
  submit(Submit Claim)
  fork1[" "]:::bar
  validate(Validate Receipts)
  budget(Check Budget)
  join1[" "]:::bar
  review(Review Claim)
  ok{"approved?"}
  pay(Pay Employee)
  notice(Receive Rejection Notice)
  merge1{ }
  archive(Archive Claim)
  done((("●"))):::final

  subgraph Employee
    submit
    notice
  end
  subgraph Finance
    fork1
    validate
    budget
    join1
    pay
    merge1
    archive
  end
  subgraph Manager
    review
    ok
  end

  start --> submit --> fork1
  fork1 --> validate --> join1
  fork1 --> budget --> join1
  join1 --> review --> ok
  ok -- "[yes]" --> pay --> merge1
  ok -- "[else]" --> notice --> merge1
  merge1 --> archive --> done

  classDef initial fill:#000,stroke:#000,color:#000
  classDef final fill:#fff,stroke:#000,stroke-width:2px,color:#000
  classDef bar fill:#000,stroke:#000,color:#000,font-size:2px
```

**Mermaid limitations:** fork/join bars, initial/final nodes and partitions are approximations of UML shapes;
subgraph "lanes" don't line up as true swim lanes; no signal, time-event, pin, expansion-region or flow-final
shapes (use a labelled node such as `⊗ flow final` or a note). For a strict UML activity diagram prefer PlantUML.
