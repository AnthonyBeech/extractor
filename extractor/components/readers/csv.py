# document_reader/csvreader.py
import pandas as pd
from ..documentreader import DocumentReader
from ..documentdata import DocumentData

class CsvReader(DocumentReader):
    
    @classmethod
    def accepted_extensions(cls):
        return ['.csv']
    
    def read(self, file_path: str) -> DocumentData:
        df = pd.read_csv(file_path)
        text = df.to_string()
        return DocumentData(text=text, file_path=file_path, file_extension='.csv', metadata={}, images=[])
