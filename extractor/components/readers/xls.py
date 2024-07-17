# components/excelreader.py
import pandas as pd
from ..documentreader import DocumentReader
from ..documentdata import DocumentData

class XlsReader(DocumentReader):

    @classmethod
    def accepted_extensions(cls):
        return ['.xls', '.xlsx']
    
    def read(self, file_path: str) -> DocumentData:
        # Read the Excel file
        xls = pd.ExcelFile(file_path)
        text = []
        for sheet_name in xls.sheet_names:
            sheet_df = pd.read_excel(xls, sheet_name=sheet_name)
            text.append(sheet_df.to_string(index=False))
        
        return self._create_document_data(
            text="\n".join(text),
            file_path=file_path,
            file_extension=file_path.split('.')[-1],
        )
