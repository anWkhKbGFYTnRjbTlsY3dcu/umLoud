# Mermaid — Deployment diagrams

Rules live in `references/deployment.md`; this file is syntax only. Read `references/syntax/mermaid/_common.md` first.

Mermaid has no deployment diagram; use nested subgraphs (node ⟶ execution environment ⟶ artifact) and labelled undirected links.

```mermaid
flowchart TB
  subgraph client["«device» Browser"]
  end
  subgraph web["«device» Web Server"]
    subgraph nginx["«executionEnvironment» Nginx"]
      site["«artifact» static-site.zip"]
    end
  end
  subgraph app["«device» App Server {instances = 3}"]
    subgraph jvm["«executionEnvironment» JVM 21"]
      jar["«artifact» orders-service.jar"]
    end
  end
  subgraph dbs["«device» DB Server"]
    subgraph pg["«executionEnvironment» PostgreSQL 16"]
      schema["«artifact» orders schema"]
    end
  end
  client ---|HTTPS| web
  web ---|HTTP/REST| app
  app ---|JDBC/TLS| dbs
```

**Mermaid limitations:** no 3-D node shape (keywords carry the meaning); links between subgraphs can render on odd sides;
for large deployments prefer PlantUML.
