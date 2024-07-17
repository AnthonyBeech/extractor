from dataclasses import dataclass
import pandas as pd
import os
from PIL import Image
import nltk
from nltk.tokenize import word_tokenize

# Ensure you have downloaded the required NLTK data files
nltk.download('punkt')

@dataclass
class DocumentData:
    text: str
    file_path: str
    file_extension: str
    metadata: dict
    images: list  # This will store image arrays

    def write(self, output_dir: str) -> pd.DataFrame:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Save images and get paths
        image_paths = []
        for i, img in enumerate(self.images):
            image_filename = f"{os.path.splitext(os.path.basename(self.file_path))[0]}_image_{i + 1}.jpg"
            image_path = os.path.join(output_dir, image_filename)
            image = Image.fromarray(img)
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            image.save(image_path)
            image_paths.append(image_path)

        # Create a DataFrame
        data = {
            'file_path': [self.file_path],
            'file_extension': [self.file_extension],
            'metadata': [self.metadata],
            'text': [self.text],
            'images': [image_paths]
        }
        df = pd.DataFrame(data)
        return df
    
    def tokenize_text(self):
        return word_tokenize(self.text)