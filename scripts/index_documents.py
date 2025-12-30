"""
Index initial documents into Qdrant for Secure RAG v2
"""

from app.vectorstore.qdrant import QdrantVectorStore


def main():
    print("[*] Initializing Qdrant Vector Store...")

    store = QdrantVectorStore(collection_name="rag_documents")

    documents = [
        {
            "text": "A RAG system combines retrieval and generation to ground LLM responses in external knowledge."
        },
        {
            "text": "Vector databases store embeddings and enable semantic similarity search."
        },
        {
            "text": "Secure RAG systems apply security controls outside the LLM, including input validation and output filtering."
        },
        {
            "text": "Audit logging is critical for traceability and security monitoring in AI systems."
        },
        {
            "text": "Prompt injection is a major security risk for LLM-based applications."
        },
    ]

    print(f"[*] Indexing {len(documents)} documents...")
    store.add_documents(documents)

    print("[✓] Documents indexed successfully.")


if __name__ == "__main__":
    main()
