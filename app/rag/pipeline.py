import uuid
from typing import List

from app.vectorstore.base import VectorStore
from app.rag.types import RAGResponse


class RAGPipeline:
    def __init__(self, vectorstore: VectorStore):
        self.vectorstore = vectorstore

    def run(self, query: str, top_k: int = 3) -> RAGResponse:
        request_id = str(uuid.uuid4())

        # 1. Retrieve documents
        sources = self.vectorstore.search(query, top_k)

        # 2. Generate answer (temporal: simple concat / mock)
        context = " ".join([doc["text"] for doc in sources])
        answer = f"Answer based on retrieved context: {context}"

        # 3. Security flags (placeholder for v2)
        security_flags = {
            "prompt_injection_detected": False,
            "pii_detected": False,
        }

        return RAGResponse(
            answer=answer,
            sources=sources,
            security_flags=security_flags,
            request_id=request_id,
        )
