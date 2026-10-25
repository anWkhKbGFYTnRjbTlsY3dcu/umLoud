# PlantUML — Communication diagrams

Rules live in `references/communication.md`; this file is syntax only.

PlantUML has no native communication diagram; use an object-style layout with numbered link labels.

```plantuml
@startuml
title Communication: calculate price (nested numbering)
object ":Order" as O
object ":OrderLine" as L
object ":Product" as P
object ":Customer" as C
O -right- L : "1: calculatePrice() →\n1.1*[for each line]: calculatePrice() →"
L -down- P : "1.1.1: getPrice(quantity) →"
O -down- C : "1.2: getDiscountedValue(this) →"
@enduml
```
