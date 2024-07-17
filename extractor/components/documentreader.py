from abc import ABC, abstractmethod
from .documentdata import DocumentData

class DocumentReader(ABC):

    @abstractmethod
    def read(self, file_path: str) -> DocumentData:
        pass

    @classmethod
    @abstractmethod
    def accepted_extensions(cls):
        pass
