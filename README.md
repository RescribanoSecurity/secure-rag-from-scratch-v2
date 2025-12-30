# 🔐 Secure RAG v2  
### Security-First Retrieval-Augmented Generation

Secure RAG v2 is a **security-first, end-to-end Retrieval-Augmented Generation (RAG) system** built as a **hands-on learning lab** and **reference architecture** for designing **defensible LLM applications**.

This project intentionally avoids “happy-path” demos.  
Its primary goal is to explore **how security controls should be designed, enforced, tested, and surfaced** in modern RAG systems.

---

## 📌 What this project is (and is not)

**This project is:**
- A security-focused RAG implementation
- Built from scratch with explicit architectural decisions
- Designed to be testable, auditable, and explainable
- Aligned with OWASP LLM Top 10 risks
- A learning lab that documents failures and lessons learned

**This project is NOT:**
- A production-ready product
- A framework or SDK
- A generic RAG tutorial
- A benchmark-optimized demo

---

## 🎯 Project Objectives

- Build a RAG pipeline from scratch with **production-inspired design**
- Apply **defense-in-depth** principles to LLM systems
- Clearly separate **Input Security** from **Output Security**
- Make security decisions **visible, auditable, and explainable**
- Validate security behavior through **tests and manual evidence**
- Align controls with the **OWASP LLM Top 10**

---

## 🧱 Architecture Overview (v2)

```
User
  ↓
[ Streamlit UI ]
  ↓
[ FastAPI API ]
  ↓
[ Input Security Analyzer ]
  ↓
[ Vector Retrieval (Qdrant) ]
  ↓
[ Answer Generation ]
  ↓
[ Output Security v2 ]
  ↓
User
```

---


**Key architectural principles:**
- Security controls are **independent modules**
- No security logic lives only in the UI
- All decisions are returned in structured form
- Request-level traceability is preserved

---

## 🔐 Security Model

### 🛡️ Input Security (v2)

The Input Security Analyzer inspects **user queries** before any retrieval or generation occurs.

**Capabilities:**
- Prompt injection detection
- Instruction override attempts
- Security bypass patterns
- Data exfiltration intent

**Actions:**
- `allow`
- `warn`
- `block`

Blocked requests never reach retrieval or generation.

---

### 🔒 Output Security (v2)

Output Security v2 analyzes **generated responses** before returning them to the user.

**Threats addressed:**
- PII disclosure (emails, phone numbers, identifiers)
- Accidental secret leakage (API keys, tokens)
- Unsafe model output

**Actions:**
- `allow` → return output as-is
- `warn` → return output with security flags
- `redact` → sensitive content replaced with placeholders
- `block` → output fully suppressed

All decisions include:
- risk score
- findings
- applied action

---

## 🧪 End-to-End Security Scenarios

| Scenario | Result |
|--------|--------|
| Clean input → clean output | ✅ ALLOW |
| Prompt injection detected | ⛔ BLOCK (Input Security) |
| PII generated in output | ✂️ REDACT (Output Security) |
| Secret generated in output | ⛔ BLOCK (Output Security) |

---

## 🧾 Auditability & Traceability

- Every request carries a `request_id`
- Security decisions are returned as structured metadata
- Designed for future SIEM / log pipeline integration
- Security logic is deterministic and testable

---

## 🧪 Testing & Validation

- Unit tests for security rules
- Integration tests for RAG pipeline
- Manual validation via Streamlit UI
- Visual evidence stored under: docs/screenshots/v2/


Screenshots demonstrate:
- Clean flows
- Redaction behavior
- Output blocking
- Security flags surfaced in UI

---

## 📊 OWASP LLM Top 10 – Status

| OWASP Risk | Status |
|----------|--------|
| LLM01 Prompt Injection | ✅ Input Security |
| LLM02 Data Leakage | ✅ Output Security |
| LLM06 Excessive Agency | ⚠️ Partial |
| LLM09 Overreliance | ⚠️ Partial |
| Others | 🚧 Planned |

This mapping reflects **actual enforcement**, not aspirational coverage.

---

## 🚧 What is NOT implemented (yet)

To remain honest and useful as a learning lab, the following are **explicitly out of scope for now**:

- Authentication / identity management
- Persistent audit logs
- Multi-LLM backends
- Cloud IAM integration
- Automated policy engines
- Production-grade rate limiting

These are planned future extensions.

---

## 🌐 Project Pages & Presentations

- 🇬🇧 Technical Presentation (EN):  
  https://github.com/RescribanoSecurity/secure-rag-from-scratch-v2/blob/main/docs/presentations/V2/Secure-RAG-v2-EN.pdf

- 🇪🇸 Presentación Técnica (ES):  
 https://github.com/RescribanoSecurity/secure-rag-from-scratch-v2/blob/main/docs/presentations/V2/Secure-RAG-v2-ES.pdf

- 📸 Security Evidence (Screenshots):  
  https://github.com/RescribanoSecurity/secure-rag-from-scratch-v2/tree/main/docs/screenshots

---

## 📜 License

MIT
