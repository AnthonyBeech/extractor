# components/documentdata.py
from dataclasses import dataclass
import pandas as pd
import numpy as np
import os
from PIL import Image
import nltk
from nltk.tokenize import word_tokenize
import re

# Ensure you have downloaded the required NLTK data files
def ensure_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

ensure_nltk_data()

@dataclass
class DocumentData:
    text: str
    file_path: str
    file_extension: str
    images: list  # This will store image arrays

    def write(self, output_dir: str, save_images: bool = False) -> pd.DataFrame:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        image_paths = []
        if save_images:
            # Create the image output directory if it doesn't exist
            image_output_dir = os.path.join(output_dir, "images")
            os.makedirs(image_output_dir, exist_ok=True)

            # Save images and get paths
            for i, img in enumerate(self.images):
                image_filename = f"{os.path.splitext(os.path.basename(self.file_path))[0]}_image_{i + 1}.jpg"
                image_path = os.path.join(image_output_dir, image_filename)
                image = Image.fromarray(img)
                if image.mode == 'RGBA':
                    image = image.convert('RGB')
                image.save(image_path)
                image_paths.append(image_path)

        # Create a DataFrame
        data = {
            'file_path': [self.file_path],
            'file_extension': [self.file_extension],
            'text': [self.text],
            'images': [image_paths]
        }
        df = pd.DataFrame(data)
        return df
    
    def tokenize_text(self):
        print(self.text)
        # Remove unwanted characters and keep only letters, numbers, and common symbols
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        cleaned_text = cleaned_text.replace('\n', ' ').replace('\r', ' ').strip()
        self.text = word_tokenize(cleaned_text)
