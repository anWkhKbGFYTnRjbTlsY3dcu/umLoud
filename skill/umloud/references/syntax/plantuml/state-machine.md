# PlantUML — State machine diagrams

Rules live in `references/state-machine.md`; this file is syntax only.

```plantuml
@startuml
title Payment — lifecycle
hide empty description

[*] --> Active
state Active {
  [*] --> Pending
  Pending --> Authorizing : submit
  state Authorizing : entry / start timer
  state Authorizing : do / request authorization from gateway
  state Authorizing : exit / stop timer
  Authorizing --> Authorized : approved
  Authorizing --> Declined : declined
  Authorizing --> Pending : timeout [retries < 3] / increment retries
  Authorizing --> Declined : timeout [retries >= 3]
  Declined --> Pending : updateCard
}
Active --> Cancelled : cancel / notify customer
Authorized --> Captured : capture [amount <= authorizedAmount]
Captured --> [*]
Cancelled --> [*]
@enduml
```

Orthogonal (concurrent) regions:

```plantuml
@startuml
title Media player — concurrent regions
[*] --> Off
Off --> On : switchOn
On --> Off : switchOff
state On {
  [*] --> Stopped
  Stopped --> Playing : play
  Playing --> Paused : pause
  Paused --> Playing : play
  Playing --> Stopped : stop
  Paused --> Stopped : stop
  --
  [*] --> Normal
  Normal --> Muted : mute
  Muted --> Normal : unmute
}
note right of On : Each region runs independently.
@enduml
```

History pseudostate (resume the last substate on re-entry):

```plantuml
@startuml
title Alarm clock — source selection with history
[*] --> Off
Off --> On[H] : switchOn
On --> Off : switchOff
state On {
  [*] --> Radio
  Radio --> CD : selectCD
  CD --> Radio : selectRadio
}
note bottom of On : First switchOn: Radio (default).\nLater: the source active at switchOff.
@enduml
```

PlantUML tips: `[*]` initial/final; `state X : entry / ...` adds internal activity lines; `--` (or `||`)
separates concurrent regions inside a composite; `X[H]` / `X[H*]` are shallow/deep history; `<<choice>>`,
`<<fork>>`, `<<join>>` stereotypes on states give pseudostates; `hide empty description`.
Declare composite states before (or instead of) referencing their substates at top level, otherwise
PlantUML creates the substate outside the composite. Avoid history inside a state that also has `--`
regions (PlantUML drops the region separator); point the history at a single-region composite.
