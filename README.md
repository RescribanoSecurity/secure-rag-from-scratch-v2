# 🔐 Secure RAG v2 – Security-First Retrieval-Augmented Generation

Secure RAG v2 is a **security-first, end-to-end Retrieval-Augmented Generation (RAG) system** built as a learning lab and reference architecture for designing **defensible LLM applications**.

This project intentionally avoids “happy-path” demos.  
Its primary goal is to explore **how security controls should be designed, enforced, and surfaced** in modern RAG systems.

---

## 🎯 Project Objectives

- Build a RAG pipeline from scratch with **production-inspired design**
- Apply **defense-in-depth** principles to LLM systems
- Clearly separate **input security** from **output security**
- Make security decisions **visible, auditable, and explainable**
- Align controls with **OWASP LLM Top 10**

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

## 🔐 Security Model

### Input Security
Detects explicit malicious intent such as prompt injection, instruction override, and data exfiltration.

### Output Security v2
Analyzes generated content to prevent disclosure of PII or secrets via redact/block.

---

## 🧪 End-to-End Scenarios

- Clean input/output → ALLOW  
- Prompt injection → BLOCK (input)  
- PII generated → REDACT (output)  
- Secret generated → BLOCK (output)

---

## 📜 License

MIT
