# PlantUML — Activity diagrams

Rules live in `references/activity.md`; this file is syntax only.

```plantuml
@startuml
title Process expense claim
|Employee|
start
:Submit Claim;
|Finance|
fork
  :Validate Receipts;
fork again
  :Check Budget;
end fork
|Manager|
:Review Claim;
if (approved?) then ([yes])
  |Finance|
  :Pay Employee;
else ([else])
  |Employee|
  :Receive Rejection Notice;
endif
|Finance|
:Archive Claim;
stop
@enduml
```

Signals, time events, flow final:

```plantuml
@startuml
title Leave for airport
start
fork
  :Flight departs in 2 hours<
  :Pack Bags;
fork again
  :Taxi Arrives<
end fork
:Leave for Airport;
split
  :Send "on my way" message>
  end
split again
  :Travel to Airport;
  stop
end split
@enduml
```

PlantUML tips: `start` / `stop` (activity final) / `end` (flow final ⊗); `:Action;`; `if (...) then ([guard]) ... else ([else]) ... endif`
draws decision + merge; `fork` / `fork again` / `end fork` (or `end merge`); `|Lane|` partitions;
`:Accept<` accept signal, `:Send>` send signal (no hourglass — put "after 2h" in the accept text or a note);
`split` for non-synchronised starts; expansion regions are not supported — use `partition "«concurrent» for each item" { }` + a note.
