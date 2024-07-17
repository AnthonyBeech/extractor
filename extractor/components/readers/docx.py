# document_reader/docxreader.py
from docx import Document
import numpy as np
from PIL import Image
import io
from ..documentreader import DocumentReader
from ..documentdata import DocumentData

class DocxReader(DocumentReader):
    
    @classmethod
    def accepted_extensions(cls):
        return ['.docx']
    
    def read(self, file_path: str) -> DocumentData:
        document = Document(file_path)
        text = "\n".join([para.text for para in document.paragraphs])
        images = []
        for rel in document.part.rels.values():
            if "image" in rel.target_ref:
                img = rel.target_part.blob
                image = Image.open(io.BytesIO(img))
                images.append(np.array(image))
                
        return self._create_document_data(
            text=text,
            file_path=file_path,
            file_extension=".docx",
            images=images,
        )