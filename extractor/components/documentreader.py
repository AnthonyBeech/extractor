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

    def _create_document_data(self, text, file_path, file_extension, images=[]):
        data = DocumentData(
            text=text,
            file_path=file_path,
            file_extension=file_extension,
            images=images,
        )
        data.tokenize_text()
        return data
