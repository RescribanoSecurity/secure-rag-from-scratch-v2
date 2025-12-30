from app.security.input_security import InputSecurityAnalyzer
from app.security.output_security import OutputSecurityAnalyzer
from app.security.policy_engine import build_policy_violations


class RAGPipeline:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore
        self.input_security = InputSecurityAnalyzer()
        self.output_security = OutputSecurityAnalyzer()

    def run(self, query: str, request_id: str):
        # --------------------
        # INPUT SECURITY
        # --------------------
        security_flags = self.input_security.analyze(query)
        policy_violations = build_policy_violations(security_flags)

        if security_flags["action"] == "block":
            return {
                "answer": "Query blocked due to input security policy.",
                "sources": [],
                "security_flags": security_flags,
                "output_security": None,
                "policy_violations": policy_violations,
                "block_reason": "input_policy_violation",
                "request_id": request_id,
            }

        # --------------------
        # RETRIEVAL
        # --------------------
        sources = self.vectorstore.search(query, top_k=3)

        # --------------------
        # GENERATION (mock – E2E #4)
        # --------------------
        answer = "Here is the API key: sk-abcdefghijklmnopqrstuvwxyz123456789"

        # --------------------
        # OUTPUT SECURITY v2
        # --------------------
        output_security = self.output_security.analyze(answer)
        block_reason = None

        if output_security["action"] == "block":
            answer = "Output blocked: sensitive data detected (PII/secret)."
            block_reason = "output_sensitive_data"

        elif output_security["action"] == "redact":
            answer = output_security["redacted_text"]

        return {
            "answer": answer,
            "sources": sources,
            "security_flags": security_flags,
            "output_security": output_security,
            "policy_violations": policy_violations,
            "block_reason": block_reason,
            "request_id": request_id,
        }
