# document_reader/readerregistry.py
from .readers.txt import TxtReader
from .readers.pdf import PdfReader
from .readers.docx import DocxReader
from .readers.csv import CsvReader
from .readers.html import HtmlReader
from .readers.image import ImageReader
from .readers.tiff import TiffReader

class ReaderRegistry:
    _readers = []

    @classmethod
    def register_reader(cls, reader):
        cls._readers.append(reader)
    
    @classmethod
    def get_reader(cls, file_extension):
        for reader in cls._readers:
            if file_extension in reader.accepted_extensions():
                return reader()
        raise ValueError(f"No reader found for file extension: {file_extension}")

# Register readers
ReaderRegistry.register_reader(TxtReader)
ReaderRegistry.register_reader(PdfReader)
ReaderRegistry.register_reader(DocxReader)
ReaderRegistry.register_reader(CsvReader)
ReaderRegistry.register_reader(HtmlReader)
ReaderRegistry.register_reader(ImageReader)
ReaderRegistry.register_reader(TiffReader)
