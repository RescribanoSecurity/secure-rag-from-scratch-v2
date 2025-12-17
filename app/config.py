import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Chroma / RAG
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "docs")

# RAG parameters
TOP_K = int(os.getenv("TOP_K", "4"))

APP_MODE = os.getenv("APP_MODE", "local_basic")

