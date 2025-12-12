from abc import ABC, abstractmethod
from typing import List

class BaseChunker(ABC):
    @abstractmethod
    def split_text(self, text: str) -> List[str]:
        pass

    # Method that can be overwritten by implementations from visual-chunking
    # Allows the method to use the structured ParsingResult as input instead of the corpus string
    def get_chunks_from_corpus_path(self, corpus_id: str) -> List[str] | None:
        return None
