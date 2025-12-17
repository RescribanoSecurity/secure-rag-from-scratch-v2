from __future__ import annotations


def call_llm(prompt: str) -> str:
    """
    Local mock LLM for development and security testing.
    This avoids external dependencies and quota issues.
    """
    return (
        "A RAG combines retrieval and text generation."
    )
