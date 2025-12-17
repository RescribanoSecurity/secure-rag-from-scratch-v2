from app.vectorstore.qdrant import QdrantVectorStore


def test_qdrant_vectorstore_search():
    store = QdrantVectorStore(collection_name="test_collection")

    documents = [
        {"text": "A RAG system combines retrieval and generation"},
        {"text": "AI security is critical in enterprise environments"},
    ]

    store.add_documents(documents)

    results = store.search("What is a RAG system?", top_k=1)

    assert len(results) == 1
    assert "RAG" in results[0]["text"]
