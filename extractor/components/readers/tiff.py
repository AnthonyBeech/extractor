# document_reader/tiffreader.py
import easyocr
from PIL import Image
import numpy as np
import os
from ..documentreader import DocumentReader
from ..documentdata import DocumentData

class TiffReader(DocumentReader):
    
    @classmethod
    def accepted_extensions(cls):
        return ['.tiff', '.tif']
    
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