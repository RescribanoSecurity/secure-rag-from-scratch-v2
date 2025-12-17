from __future__ import annotations

from app.config import TOP_K
from app.vector_store import search_docs
from app.llm_client import call_llm


def build_prompt(query: str, contexts: list[str]) -> str:
    context_block = "\n\n---\n\n".join(contexts) if contexts else ""

    return f"""
You are an assistant that answers ONLY using the provided context.
If the answer is not in the context, respond exactly:
"I do not have enough data to answer."

[CONTEXT]
{context_block}

[QUESTION]
{query}
""".strip()


def rag_pipeline(query: str) -> str:
    contexts = search_docs(query, k=TOP_K)
    prompt = build_prompt(query, contexts)
    return call_llm(prompt)
