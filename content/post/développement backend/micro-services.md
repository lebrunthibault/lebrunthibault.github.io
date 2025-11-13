---
title: "Micro Services"
draft: true
---

[https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part-2/](https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part-2/)

- well-known patterns for distributed transactions

- By Event / Choregraphy (services listen and communicate via events): easy to implement but not so scalable. Not easy to rollback
- Command / Orchestration : stronger but heavier
  - orchestrator communicates via messages 
  - orchestrator can become bloated 
