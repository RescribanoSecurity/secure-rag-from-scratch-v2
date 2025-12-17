# Secure RAG from Scratch – Technical Documentation

## Introduction

This project is a **personal learning journey** focused on understanding how to design, secure, and validate
LLM-based systems, starting from first principles.

Instead of relying on abstract diagrams or managed services, the goal is to:
- Build a Retrieval-Augmented Generation (RAG) system from scratch
- Apply concrete security controls
- Validate behavior through real tests
- Document both successes and failures

This repository reflects **what I actually tested and learned**, not just what worked on the first try.

## Project Goals

The main goals of this project are:

- Understand how RAG pipelines work end to end
- Identify real security risks in LLM-based systems
- Apply input, output, and audit controls
- Learn by breaking, fixing, and validating the system
- Create a solid baseline before moving to cloud or MLOps environments

## Architecture – Version 1 (Local Secure RAG)

This repository currently implements **Architecture v1**, designed as a local, security-first baseline.

Key characteristics:
- Local execution
- No external dependencies required to test security
- Explicit control points for input validation, output filtering, and auditing
- Configuration-based security modes (`local_basic`, `local_secure`)

This version serves as a **reference baseline** that will evolve in future iterations.


Client → FastAPI → Input Security → RAG Pipeline → Output Security → Audit → Response

```mermaid
flowchart LR
    User["User / Client"]
    API["FastAPI API"]
    InputSec["Input Security (Prompt Injection Detection)"]
    RAG["RAG Pipeline"]
    VS["Vector Store (In-Memory)"]
    LLM["LLM Client (Mock or Provider)"]
    OutputSec["Output Security (PII Detection and Redaction)"]
    Audit["Audit Logging"]
    Response["HTTP Response"]

    User --> API
    API --> InputSec
    InputSec --> RAG
    RAG --> VS
    RAG --> LLM
    LLM --> OutputSec
    OutputSec --> Audit
    Audit --> Response
    Response --> User
```

---

## Execution Modes (APP_MODE)

The system supports progressive security hardening using execution modes.

```mermaid
flowchart TB
    subgraph LocalBasic["APP_MODE = local_basic"]
        LB1["Input Security"]
        LB2["RAG Pipeline"]
        LB3["LLM Response"]
    end

    subgraph LocalSecure["APP_MODE = local_secure"]
        LS1["Input Security"]
        LS2["RAG Pipeline"]
        LS3["Output Security (PII Redaction)"]
        LS4["Audit Logging"]
    end

    LB1 --> LB2 --> LB3
    LS1 --> LS2 --> LS3 --> LS4
```
## Security Approach

Security controls are intentionally implemented **outside of the LLM**.

This project focuses on three main control layers:

- **Input Security**
  - Prompt injection detection
  - Fail-fast blocking before the RAG pipeline

- **Output Security**
  - Detection of personally identifiable information (PII)
  - Redaction of sensitive data before returning responses

- **Audit Logging**
  - Structured JSON logs
  - Explicit security events (`blocked_input`, `pii_detected`)
  - Designed for traceability and future compliance

---

## Security Flow (Detailed)

```mermaid
sequenceDiagram
    participant User
    participant API as FastAPI
    participant InputSec as Input Security
    participant RAG
    participant LLM
    participant OutputSec as Output Security
    participant Audit

    User->>API: POST /query
    API->>InputSec: Validate query

    alt Malicious input detected
        InputSec-->>API: Block request
        API->>Audit: Log blocked_input
        API-->>User: HTTP 400
    else Valid input
        InputSec->>RAG: Forward query
        RAG->>LLM: Generate response
        LLM-->>RAG: Raw answer
        RAG->>OutputSec: Check PII (local_secure)
        alt PII detected
            OutputSec->>Audit: Log pii_detected
            OutputSec-->>API: Redacted answer
        else No PII detected
            OutputSec-->>API: Clean answer
        end
        API-->>User: HTTP 200
    end
```

---
## Validation & Testing

All validation in this phase was performed manually to ensure full control and understanding
of system behavior.

The goal was **not model quality**, but **security correctness**.

### Evidence (Screenshots)

The following screenshots document the validation performed during this phase:

- API startup
- Swagger availability
- Baseline RAG response
- Prompt injection blocking
- Secure mode startup
- PII redaction
- Audit logs

Screenshots are available under:

docs/screenshots/


## Lessons Learned

Some key lessons from this first version:

- Security controls must be validated, not assumed
- Mocking the LLM is essential to test security independently of providers
- Running in different modes surfaced configuration-related issues early


These lessons directly influence the design of future versions.

## Out of Scope (For Now)

The following topics are intentionally not covered in this version:

- Model accuracy evaluation
- Performance and load testing
- Cloud-native authentication and IAM
- Multi-tenant isolation
- Production-grade persistence

These areas will be addressed in future iterations.

## Next Steps

Planned next steps include:

- Threat modeling based on this architecture
- Mapping controls to OWASP LLM Top 10
- Evolving the architecture to a cloud-ready version
- Introducing automated security tests
