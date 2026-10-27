# PlantUML — common rules

- Wrap every diagram in `@startuml` / `@enduml`; put the purpose in `title`.
- Quote names with spaces and alias them: `class "Order Line" as OL`.
- Standard look for class-like diagrams: `hide empty members`, `hide circle` (removes PlantUML's non-UML C/A/I/E icons),
  `skinparam classAttributeIconSize 0` (shows `+ - # ~` as text).
- Declare composite states/packages before referencing their contents at top level.
- Supports every UML diagram type in this skill; approximations only for communication and interaction overview
  diagrams and the profile extension arrowhead (see the type's syntax file).
- Rendering needs `plantuml` on PATH or `PLANTUML_JAR` (+ java); Graphviz `dot` for class/component/use-case/deployment layouts.
