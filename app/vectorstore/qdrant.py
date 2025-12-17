from typing import List, Dict
from uuid import uuid4

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

from app.vectorstore.base import VectorStore


class QdrantVectorStore(VectorStore):
    def __init__(self, collection_name: str = "documents"):
        self.client = QdrantClient(host="localhost", port=6333)
        self.collection_name = collection_name
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")

        self._ensure_collection()

    def _ensure_collection(self):
        collections = self.client.get_collections().collections
        if self.collection_name not in [c.name for c in collections]:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config={
                    "size": 384,
                    "distance": "Cosine",
                },
            )

    def add_documents(self, documents: List[Dict]) -> None:
        texts = [doc["text"] for doc in documents]
        embeddings = self.encoder.encode(texts).tolist()

        points = []
        for doc, vector in zip(documents, embeddings):
            points.append({
                "id": str(uuid4()),
                "vector": vector,
                "payload": doc,
            })

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def search(self, query: str, top_k: int) -> List[Dict]:
        query_vector = self.encoder.encode(query).tolist()

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k,
            with_payload=True,
        )

        return [r.payload for r in results]
