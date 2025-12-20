from fastapi import FastAPI
from pydantic import BaseModel

from app.vectorstore.qdrant import QdrantVectorStore
from app.rag.pipeline import RAGPipeline

app = FastAPI(title="Secure RAG v2")

vectorstore = QdrantVectorStore()
rag_pipeline = RAGPipeline(vectorstore)


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query_rag(request: QueryRequest):
    response = rag_pipeline.run(request.query)
    return response
