from app.vectorstore.qdrant import QdrantVectorStore
from app.rag.pipeline import RAGPipeline


def test_rag_pipeline_basic():
    vectorstore = QdrantVectorStore(collection_name="test_collection")
    pipeline = RAGPipeline(vectorstore)

    query = "What is a RAG system?"
    request_id = "test-request-id"

    result = pipeline.run(query, request_id=request_id)

    # Basic structure checks
    assert "answer" in result
    assert "sources" in result
    assert "security_flags" in result
    assert "request_id" in result

    # Type checks
    assert isinstance(result["answer"], str)
    assert isinstance(result["sources"], list)
    assert isinstance(result["security_flags"], dict)

    # Traceability
    assert result["request_id"] == request_id

    # RAG sanity
    assert len(result["sources"]) > 0
