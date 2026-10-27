# Model Driven Architecture (MDA) and Executable UML

Load only when the user mentions MDA, Executable UML, fUML/Alf, PIM/PSM, or generating code from models.

**The idea.** Push "blueprint" to its limit: if a model is precise enough, a machine — not a programmer —
can produce the code. UML then works as a programming language, and the hand-written source disappears.

**MDA (an OMG standard, like UML itself).** Work is split in two:
1. Modellers build a **Platform Independent Model (PIM)** — a UML model of the application that mentions no
   specific technology.
2. Tools transform the PIM into one or more **Platform Specific Models (PSMs)** — one per target platform
   (e.g. Java EE, .NET) — and further tools generate code from each PSM. A PSM may or may not itself be UML.

Example: one PIM of a warehouse system → a Java PSM and a .NET PSM → two generated implementations.
If every step from PIM to code is automatic, UML really is the programming language; if any step needs a
human, you are back to blueprints. Vendors that follow MDA can, in principle, exchange models.

**Executable UML (Steve Mellor's approach).** Same starting point — a platform-independent model — but no
intermediate PSM: a **model compiler** turns the model into a deployable system in one automatic step. The
compiler is driven by reusable **archetypes**, one per target platform (buy the compiler plus a Java archetype
and a .NET archetype, and the same model yields both systems). It deliberately uses only a **subset** of UML,
dropping constructs it considers unnecessary, so it is simpler than full UML.

**How to describe behaviour in such a model.** UML 2 offers three candidates — interaction (sequence)
diagrams, state machines, and activity diagrams — each with supporters. Later OMG standards (fUML, a precise
executable subset of UML, and Alf, a textual action language for it) built on the activity-based route.

**A realistic view.** The approach pays off only if modelling is **clearly more productive** than writing
code in a modern language, the tools are mature enough, and enough people adopt it to sustain an ecosystem.
Graphical programming environments have historically struggled on all three, so most teams use UML as
sketch or blueprint and keep code as the source of truth.

**What this means for umLoud.**
- PlantUML and Mermaid output is **documentation**, not an executable model. Say so if the user is aiming at MDA/Executable UML.
- For such users: use strictly **normative UML 2.5.1** (no conventions, no suppressed multiplicities or types),
  keep PIM diagrams free of technology (no frameworks, SQL types, annotations), put platform detail only in
  PSM-level diagrams, and model behaviour with **state machines or activities** precise enough to execute.
- Point them to an MDA/fUML-capable modelling tool for the executable model itself.
