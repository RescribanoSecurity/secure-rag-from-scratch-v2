from abc import ABC, abstractmethod
from typing import List, Dict


class VectorStore(ABC):
    @abstractmethod
    def add_documents(self, documents: List[Dict]) -> None:
        pass

    @abstractmethod
    def search(self, query: str, top_k: int) -> List[Dict]:
        pass
