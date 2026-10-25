# PlantUML — Class diagrams

Rules live in `references/class.md`; this file is syntax only.

```plantuml
@startuml
title Order processing — software perspective (sketch)
hide empty members
hide circle
skinparam classAttributeIconSize 0

abstract class Customer {
  name : String [1]
  address : Address [0..1]
  {abstract} + creditRating() : Rating {query}
}
class CorporateCustomer {
  contactName : String
  creditLimit : Money
  + billForMonth(month : Integer)
}
class PersonalCustomer {
  creditCardNumber : String [0..1]
}
class Order {
  dateReceived : Date [0..1]
  isPrepaid : Boolean [1]
  /price : Money
  + dispatch()
  + close()
}
class OrderLine {
  quantity : Integer [1]
  price : Money
}
class Product
enum Rating <<enumeration>> {
  POOR
  GOOD
  EXCELLENT
}

Customer <|-- CorporateCustomer
Customer <|-- PersonalCustomer
Order "*" --> "1\ncustomer" Customer
Order "1" *-- "*\nlineItems {ordered}" OrderLine
OrderLine "*" --> "1\nproduct" Product
Customer ..> Rating

note right of Order
  {if Order.customer.creditRating is POOR
   then Order.isPrepaid must be true}
end note
@enduml
```

Interfaces, ball-and-socket and dependency keywords:

```plantuml
@startuml
title Programming to an interface
hide empty members
interface Collection <<interface>>
interface List <<interface>> {
  + get(index : Integer) : Object
  + add(o : Object)
}
abstract class AbstractList {
  {abstract} + get(index : Integer) : Object
  + add(o : Object)
}
class ArrayList {
  + get(index : Integer) : Object
  + add(o : Object)
}
class Order

Collection <|-- List
List <|.. AbstractList
AbstractList <|-- ArrayList
Order ..> List : <<use>>
@enduml
```

Association class and qualified association:

```plantuml
@startuml
hide empty members
class Person
class Meeting
class Attendance {
  attentiveness : Level
}
Person "*" -- "*" Meeting
(Person, Meeting) .. Attendance

class Order
class OrderLine
class Product
Order [product : Product] --> "0..1\nlineItem" OrderLine
@enduml
```

PlantUML tips: `hide empty members` removes empty compartments; `hide circle` removes PlantUML's
(non-UML) C/A/I/E icons for a standard look; `skinparam classAttributeIconSize 0`
shows `+ - # ~` as text instead of icons; `{static}` / `{abstract}` modifiers; `<|--` generalization,
`<|..` realization, `*--` composition, `o--` aggregation (avoid), `..>` dependency, `-->` navigable association.
Put multiplicity and role name together in the end label: `"1\ncustomer"`.
