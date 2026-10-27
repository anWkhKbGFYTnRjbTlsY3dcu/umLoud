# PlantUML — Component and composite structure diagrams

Rules live in `references/component.md`; this file is syntax only.

```plantuml
@startuml
title Point of sale — components
skinparam componentStyle uml2

component "Till" as Till
component "Message Queue" as Q
component "Sales Server" as Server {
  component "Transaction Processor" as TP
  component "Accounting Driver" as AD
  portin " " as p1
}
component "Accounting System" as Acc

() "Sales Message" as SM1
() "Sales Message" as SM2
() "Accounting" as AccI

Till --( SM1
Q - SM1
Q --( SM2
p1 - SM2
p1 --> TP
TP ..> AD
AD --( AccI
Acc - AccI
@enduml
```

PlantUML tips: `skinparam componentStyle uml2` gives the UML 2 rectangle + icon; `() "Name" as I` declares an interface;
`A - I` = A provides I (lollipop), `B --( I` = B requires I (socket); `port`, `portin`, `portout` for ports;
nest components in `component X { ... }` for composite structure.
