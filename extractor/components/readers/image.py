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
        image_np = np.array(image)  # Convert to numpy array
        text = reader.readtext(image_np, detail=0)
        return self._create_document_data(
            text="\n".join(text),
            file_path=file_path,
            file_extension=os.path.splitext(file_path)[1],
            images=[image_np]
        )