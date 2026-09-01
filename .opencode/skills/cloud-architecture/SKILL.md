---
name: cloud-architecture
description: Use when designing cloud architectures with appropriate patterns for microservices, event-driven systems, or fault tolerance.
---

# Cloud Architecture

## When to Use This Skill
- Designing a new system on AWS, GCP, or Azure
- Choosing between sync and async communication patterns
- Implementing fault tolerance with circuit breakers and retries
- Applying CQRS or saga patterns for complex domains

## Workflow
1. Identify the workload type: compute, storage, event processing, or ML
2. Map domain requirements to cloud services (compute, storage, messaging, databases)
3. Choose communication pattern: synchronous for queries, asynchronous for commands
4. Design for failure: add retries, circuit breakers, and fallbacks
5. Select storage: relational for transactions, NoSQL for scale, object storage for files
6. Set up monitoring: metrics, logs, and traces from the start
7. Define scaling policies: auto-scaling triggers and cooldown periods
8. Document the architecture with diagrams and decision records

## Rules
- Prefer managed services over self-hosted when possible
- Design for horizontal scaling, not vertical
- Use regions and availability zones for high availability
- Encrypt data at rest and in transit
- Set cost alerts before deploying — don't discover a $10K bill later
- Review architecture against the well-architected framework pillars
