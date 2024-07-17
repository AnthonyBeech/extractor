# document_reader/imagereader.py
import os
import easyocr
from PIL import Image
import numpy as np
from ..documentreader import DocumentReader
from ..documentdata import DocumentData

class ImageReader(DocumentReader):
    
    @classmethod
    def accepted_extensions(cls):
        return ['.jpg', '.jpeg', '.png', '.bmp']
    
    def read(self, file_path: str) -> DocumentData:
        reader = easyocr.Reader(['en'])
        image = Image.open(file_path)
        text = reader.readtext(image, detail=0)
        return DocumentData(text="\n".join(text), file_path=file_path, file_extension=os.path.splitext(file_path)[1], metadata={}, images=[np.array(image)])
