from app.vectorstore.qdrant import QdrantVectorStore
from app.rag.pipeline import RAGPipeline


def test_rag_pipeline_returns_structured_response():
    store = QdrantVectorStore(collection_name="rag_test")

    # Seed minimal data
    store.add_documents([
        {"text": "RAG combines retrieval and generation"},
        {"text": "Secure RAG applies security controls outside the LLM"},
    ])

    pipeline = RAGPipeline(store)

    response = pipeline.run("What is RAG?", top_k=1)

    # Assertions
    assert response.answer
    assert len(response.sources) > 0
    assert isinstance(response.sources, list)
    assert "text" in response.sources[0]

    assert isinstance(response.security_flags, dict)
    assert "prompt_injection_detected" in response.security_flags
    assert "pii_detected" in response.security_flags

    assert response.request_id
