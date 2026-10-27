# Deployment diagrams

Show the **physical** layout: which software artifacts run on which hardware/runtime nodes, and how the nodes communicate.

## Use when / avoid when
- Use: any non-trivial deployment — environments, servers, containers, devices, protocols between them.
- Avoid: logical structure (→ component/package).

## Notation

| Element | Notation | Notes |
|---|---|---|
| Node | 3-D box | Something that can host software. |
| Device | node with `«device»` | Hardware (server, phone, sensor). |
| Execution environment | node with `«executionEnvironment»` (or a specific keyword like `«OS»`, `«container»`, `«JVM»`) | Software hosting other software. Nest inside a device. |
| Artifact | rectangle with `«artifact»` (or document icon), or just its name listed inside a node | Physical file: jar, exe, dll, script, config, container image. |
| Deployment | artifact drawn/listed inside a node | "This artifact is deployed on this node". |
| Manifestation | dashed arrow `«manifest»` from artifact to component | Artifact implements a component (or a tag on the artifact). |
| Communication path | solid line between nodes, labelled with protocol | `https`, `JDBC`, `AMQP`… |
| Tagged values | `{os = Linux, instances = 3}` | Number of replicas, vendor, OS, location — there's no standard "count" tag; say what you use. |

## Rules
- Nest execution environments inside devices; artifacts inside the environment that runs them.
- Label every communication path with protocol (and port/encryption when relevant).
- Show replicas with a tagged value (`{instances = 3}`) instead of copying nodes, unless differences matter.
- One environment (prod/staging) per diagram, named in the title.
- Use artifacts (physical files), not components, on deployment diagrams (UML 2 change).

## Common mistakes
- Logical components drawn as if they were deployable files.
- Unlabelled connections; arrows (communication paths are undirected unless you mean a dependency).
- Mixing environments, or mixing deployment with request flow (that's a sequence diagram).

## Review checklist
- [ ] Devices contain execution environments contain artifacts
- [ ] Every path labelled with protocol
- [ ] Artifacts (files) not components; replicas as tagged values
- [ ] One environment per diagram, named in the title
