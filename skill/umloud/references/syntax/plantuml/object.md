# PlantUML — Object diagrams

Rules live in `references/object.md`; this file is syntax only.

```plantuml
@startuml
title Example organization structure (object diagram)
object "<u>engineering : Organization</u>" as eng {
  location = "Boston"
}
object "<u>tools : Organization</u>" as tools {
  location = "Chicago"
}
object "<u>apps : Organization</u>" as apps {
  location = "Saba"
}
object "<u>don : Person</u>" as don {
  location = "Champaign"
}
object "<u>john : Person</u>" as john {
  location = "Champaign"
}
eng -- tools : parent / children
eng -- apps : parent / children
tools -- don
tools -- john
@enduml
```

PlantUML tip: wrap the name in `<u>…</u>` to underline it as UML requires; `object "label" as id { slot = value }`.
