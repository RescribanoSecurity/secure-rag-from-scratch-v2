# Secure RAG from Scratch – Version 2 (Private)

This repository contains the **v2 evolution** of the Secure RAG project.

Version 2 focuses on transforming the original local baseline into a
**modular, security-driven, product-like architecture**, while remaining
local-first and cloud-ready.

This repository is currently **private** and under active development.

---

## Goals of Version 2

The main objectives of v2 are:

- Replace toy components with **real infrastructure**
- Introduce **clear architectural boundaries**
- Strengthen security controls across the entire RAG pipeline
- Add **automated testing**, including security tests
- Prepare the system for future cloud and enterprise environments

---

## Key Differences from Version 1

| Area | v1 | v2 |
|----|----|----|
| Vector Store | In-memory | Qdrant (Docker) |
| Architecture | Monolithic | Modular |
| Security | Input / Output | Input, Retrieval, Output, Policy |
| Testing | Manual | Automated + Security tests |
| Readiness | Learning baseline | Product-like foundation |

---

## Architecture Overview (v2)

Secure RAG v2 is composed of the following layers:

- **API Layer** (FastAPI)
- **RAG Core** (ingestion, retrieval, prompt building)
- **Vector Store Abstraction**
- **Security Layer**
- **Audit & Observability**
- **Testing Framework**

Security controls are implemented **outside the LLM** and enforced at
multiple stages of the pipeline.

---

## Vector Database: Qdrant

Version 2 introduces **Qdrant** as the primary vector database.

- Runs locally via Docker
- Real vector search engine
- Metadata filtering support
- Cloud-compatible

A vector store interface allows switching between implementations
without impacting the RAG core.

---

## Security Model

Security is applied as a **first-class concern**:

- Input security (prompt injection detection)
- Retrieval security (source and metadata controls)
- Output security (PII and sensitive data detection)
- Structured audit logging with correlation IDs

---

## Testing Strategy

Version 2 includes automated tests:

- Unit tests for core components
- Integration tests for API and vector store
- Security test suite simulating real attack scenarios

The goal is to validate **security correctness**, not model quality.

---

## Development Status

Version 2 is under active development.

Planned next steps include:

- Qdrant integration tests
- Policy engine expansion
- Rate limiting
- Threat modeling (OWASP LLM Top 10)
- Cloud-ready deployment patterns
