# Mermaid — Package diagrams

Rules live in `references/package.md`; this file is syntax only. Read `syntax/mermaid/_common.md` first.

Mermaid has no package diagram; use a flowchart with folder-labelled nodes and dashed dependency arrows.

```mermaid
flowchart TB
  LP["📁 Leasing Presentation"]
  AP["📁 Asset Presentation"]
  LD["📁 Leasing Domain"]
  AD["📁 Asset Domain"]
  LM["📁 Leasing Data Mapper"]
  AM["📁 Asset Data Mapper"]
  DB["📁 Database"]
  LP -.-> LD
  AP -.-> AD
  LD -.-> AD
  LM -.-> LD
  LM -.-> DB
  AM -.-> AD
  AM -.-> DB
  LM -.-> AM
```

For packages **with their classes**, use subgraphs as packages:

```mermaid
flowchart TB
  subgraph UIControls["📁 UI Controls"]
    Button["Button"]
    OnOff["«interface»<br/>OnOff"]
  end
  subgraph Heating["📁 Heating"]
    Heater["Heater"]
  end
  Button -.-> OnOff
  Heater -. "realizes" .-> OnOff
```

**Mermaid limitations:** no folder shape (use the 📁 label or a note); no `«import»`/`«merge»` semantics.
