from fastapi import FastAPI
from pydantic import BaseModel
import uuid 

from app.vectorstore.qdrant import QdrantVectorStore
from app.rag.pipeline import RAGPipeline

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Secure RAG v2")

vectorstore = QdrantVectorStore()
rag_pipeline = RAGPipeline(vectorstore)


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query_rag(req: QueryRequest):
    request_id = str(uuid.uuid4())
    query = req.query

    logger.info(f"[{request_id}] Incoming query: {query}")

    result = rag_pipeline.run(query, request_id=request_id)
    logger.info(
        f"[{request_id}] Answer preview: {result['answer'][:200]}"
    )
    logger.info(
        f"[{request_id}] Security flags: {result['security_flags']}"
    )
    logger.info(
        f"[{request_id}] Sources returned: {len(result['sources'])}"
    )
    logger.info(
    f"[{request_id}] Output security: {result.get('output_security')}"
    )
    logger.info(
        f"[{request_id}] Block reason: {result.get('block_reason')}"
    )

    return result
