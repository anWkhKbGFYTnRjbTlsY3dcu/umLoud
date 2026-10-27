# PlantUML — less common diagrams

Rules live in `references/other-diagrams.md`.

## Interaction overview diagrams (approximation with an activity diagram)

```plantuml
@startuml
title Interaction overview: produce order summary
start
if (customer is external?) then ([yes])
  :ref: Get order data from XML]
else ([else])
  :ref: Get order data from database]
endif
:ref: Format order summary report]
stop
@enduml
```

## Timing diagrams

```plantuml
@startuml
title Coffee maker timing constraints
robust "Pump" as Pump
robust "Hotplate" as Plate
Pump is Off
Plate is Off

@0
Pump is On
@10
Plate is On
@60
Pump is Off
@100
Plate is Off

Pump@0 <-> @10 : {>= 10 s}
Plate@60 <-> @100 : {<= 15 min}
caption Time axis not to scale
@enduml
```

## Collaborations (not an official UML 2 diagram type) (approximation)

```plantuml
@startuml
title Observer collaboration use
allowmixing
hide empty members
usecase "Observer" as Obs
class Sensor
class Display
Obs .. Sensor : subject
Obs .. Display : observer
note "Dashed ellipse = collaboration;\nlink labels = roles played" as N
@enduml
```


## Profile diagrams (added in UML 2.2)

```plantuml
@startuml
title «profile» Persistence
hide circle
hide empty members
package "Persistence" <<profile>> {
  class Class <<metaclass>>
  class Property <<metaclass>>
  class Entity <<stereotype>> {
    tableName : String [0..1]
  }
  class Id <<stereotype>> {
    generated : Boolean = true
  }
}
Class <|-- Entity : <<extension>>
Property <|-- Id : <<extension>>
package "Order Model" as OM {
}
OM ..> Persistence : <<apply>>
@enduml
```

PlantUML can't draw the **filled** extension triangle: it uses the hollow generalization head labelled `«extension»`
— state that in a note when precision matters.
