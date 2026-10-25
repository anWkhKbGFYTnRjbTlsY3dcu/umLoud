# PlantUML — Sequence diagrams

Rules live in `references/sequence.md`; this file is syntax only.

```plantuml
@startuml
title sd Calculate order price (distributed control)
hide footbox
autoactivate on

participant "anOrder : Order" as O
participant "anOrderLine : OrderLine" as L
participant "aProduct : Product" as P
participant "aCustomer : Customer" as C

[-> O : calculatePrice()
loop for each line item
  O -> L : calculatePrice()
  L -> P : getPrice(quantity : number)
  return price
  return price
end
O -> C : getDiscountedValue(anOrder)
C -> O : getBaseValue()
return baseValue
return discountedValue
[<-- O
@enduml
```

Creation, deletion, alt/opt, async and ref:

```plantuml
@startuml
title sd Dispatch order
hide footbox

participant "anOrder : Order" as O
participant "careful : Distributor" as CD
participant "regular : Distributor" as RD
participant "aMessenger : Messenger" as M

[-> O : dispatch()
activate O
loop for each line item
  alt product.value > $10K
    O -> CD : dispatch(lineItem)
  else else
    O -> RD : dispatch(lineItem)
  end
end
opt needsConfirmation
  O ->> M : confirm()
end
create participant "aQuery : DbQuery" as Q
O -> Q : new
O -> Q : execute()
activate Q
Q --> O : results
deactivate Q
O -> Q : close()
destroy Q
ref over O, M : Notify customer
deactivate O
@enduml
```

PlantUML tips: `->` synchronous (filled), `->>` asynchronous (open), `-->` return; `[->` found message,
`[<--` return to caller; `autoactivate on` + `return` keeps activations tidy; `hide footbox` removes the
repeated participant boxes at the bottom; `create participant`/`destroy`; `ref over A, B : name`.
