# document_reader/txtreader.py
from ..documentreader import DocumentReader
from ..documentdata import DocumentData


class TxtReader(DocumentReader):

    @classmethod
    def accepted_extensions(cls):
        return [".txt"]

    def read(self, file_path: str) -> DocumentData:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            
        return self._create_document_data(
            text=text,
            file_path=file_path,
            file_extension=".txt",
        )
