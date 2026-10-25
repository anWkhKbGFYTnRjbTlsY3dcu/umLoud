# Mermaid — State machine diagrams

Rules live in `references/state-machine.md`; this file is syntax only. Read `syntax/mermaid/_common.md` first.

```mermaid
stateDiagram-v2
  [*] --> Active
  state Active {
    [*] --> Pending
    Pending --> Authorizing : submit
    state "Authorizing" as Authorizing
    Authorizing : entry / start timer
    Authorizing : do / request authorization from gateway
    Authorizing : exit / stop timer
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
```

Concurrent regions in Mermaid use `--` inside a composite state:

```mermaid
stateDiagram-v2
  [*] --> Off
  Off --> On : switchOn
  On --> Off : switchOff
  state On {
    [*] --> Stopped
    Stopped --> Playing : play
    Playing --> Paused : pause
    Paused --> Playing : play
    Playing --> Stopped : stop
    --
    [*] --> Normal
    Normal --> Muted : mute
    Muted --> Normal : unmute
  }
```

Mermaid syntax: `[*]` initial/final; `state Name { ... }` composite; `--` concurrent regions; `Name : text`
adds description lines (use for `entry /`, `exit /`, `do /`) — **declare `state "Name" as Name` first**, otherwise
the first description line replaces the state name; `state c <<choice>>`, `<<fork>>`, `<<join>>`;
`note right of State ... end note`.

**Mermaid limitations:** no history pseudostate (add a note "resumes last substate (H)"); transitions
out of a composite to an inner state of another composite can render poorly; description lines are
not visually separated into a compartment; guards with `{ }` may break parsing — use `[ ]` only.
