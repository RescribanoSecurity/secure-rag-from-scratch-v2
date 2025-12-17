from __future__ import annotations
from typing import List


# ===============================
# In-memory Vector Store (LOCAL)
# ===============================

_DOCUMENTS: List[str] = []


def add_doc(doc_id: str, text: str, metadata: dict | None = None) -> None:
    """
    Adds a document to the in-memory store.
    Metadata is ignored in this implementation but kept for compatibility.
    """
    _DOCUMENTS.append(text)


def search_docs(query: str, k: int = 4) -> List[str]:
    """
    Simple keyword-based retrieval.
    This is NOT semantic search.
    It is intentionally simple for local development and security testing.
    """
    if not _DOCUMENTS:
        return []

    query_terms = query.lower().split()

    scored = []
    for doc in _DOCUMENTS:
        score = sum(1 for term in query_terms if term in doc.lower())
        if score > 0:
            scored.append((score, doc))

    scored.sort(reverse=True, key=lambda x: x[0])

    results = [doc for _, doc in scored[:k]]
    return results if results else _DOCUMENTS[:k]

