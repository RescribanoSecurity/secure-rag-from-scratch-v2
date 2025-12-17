from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.rag import rag_pipeline
from app.security import detect_prompt_injection

from app.config import APP_MODE
from app.security_output import detect_pii, redact_pii
from app.audit import audit_event

app = FastAPI(title="Secure RAG from Scratch - Phase 1")


class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=2000)


@app.post("/query")
def query_rag(req: QueryRequest):
    is_malicious, reason = detect_prompt_injection(req.query)

    if is_malicious:
        audit_event(
            "blocked_input",
            req.query,
            {"reason": reason}
        )
        raise HTTPException(
            status_code=400,
            detail="Query blocked by security policy",
        )

    answer = rag_pipeline(req.query)

    # --- FASE 2: output security ---
    if APP_MODE == "local_secure":
        findings = detect_pii(answer)
        if findings:
            audit_event(
                "pii_detected",
                req.query,
                {"types": findings}
            )
            answer = redact_pii(answer)

    return {"answer": answer}
  
