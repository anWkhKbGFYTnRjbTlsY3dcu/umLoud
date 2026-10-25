# Mermaid — Component and composite structure diagrams

Rules live in `references/component.md`; this file is syntax only. Read `syntax/mermaid/_common.md` first.

Mermaid has no UML component diagram. Approximate with a flowchart: components as boxes with «component»,
interfaces as small circles, provided = solid line, required = dashed line labelled "requires".

```mermaid
flowchart LR
  Till["«component»<br/>Till"]
  Q["«component»<br/>Message Queue"]
  subgraph Server["«component» Sales Server"]
    TP["«component»<br/>Transaction Processor"]
    AD["«component»<br/>Accounting Driver"]
  end
  Acc["«component»<br/>Accounting System"]
  SM1(("Sales<br/>Message"))
  SM2(("Sales<br/>Message"))
  AccI(("Accounting"))

  Till -. requires .-> SM1
  Q --- SM1
  Q -. requires .-> SM2
  TP --- SM2
  TP -.-> AD
  AD -. requires .-> AccI
  Acc --- AccI
```

**Mermaid limitations:** no ball/socket or port shapes — add a legend ("○ = interface; solid = provides; dashed = requires");
for anything beyond a simple overview prefer PlantUML. (Mermaid's C4 and architecture diagrams are not UML.)
