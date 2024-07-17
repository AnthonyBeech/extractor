# document_reader/pdfreader.py
import pdfplumber
import numpy as np
from ..documentreader import DocumentReader
from ..documentdata import DocumentData

class PdfReader(DocumentReader):

    @classmethod
    def accepted_extensions(cls):
        return [".pdf"]

    def read(self, file_path: str) -> DocumentData:
        text = []
        images = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text.append(page.extract_text())
                for img in page.images:
                    x0, y0, x1, y1 = img["x0"], img["top"], img["x1"], img["bottom"]
                    img_cropped = page.within_bbox((x0, y0, x1, y1)).to_image()
                    images.append(np.array(img_cropped.original))
        return self._create_document_data(
            text="\n".join(text),
            file_path=file_path,
            file_extension=".pdf",
            images=images,
        )
