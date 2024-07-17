# document_reader/htmlreader.py
from bs4 import BeautifulSoup
from ..documentreader import DocumentReader
from ..documentdata import DocumentData
import os

class HtmlReader(DocumentReader):
    
    @classmethod
    def accepted_extensions(cls):
        return ['.html', '.htm']
    
    def read(self, file_path: str) -> DocumentData:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text()
        return self._create_document_data(
            text=text,
            file_path=file_path,
            file_extension=os.path.splitext(file_path)[1],
        )