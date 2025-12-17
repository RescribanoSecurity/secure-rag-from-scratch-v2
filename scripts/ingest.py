from __future__ import annotations

from pathlib import Path

from app.config import get_settings
from app.rag import RAGPipeline


def main() -> None:
    settings = get_settings()
    pipeline = RAGPipeline(settings)
    source_dir = settings.data_dir / "raw"

    if not source_dir.exists():
        raise SystemExit(f"Source directory not found: {source_dir}")

    added = pipeline.ingest_directory(source_dir)
    print(f"Ingested {added} documents from {source_dir}")


if __name__ == "__main__":
    main()
