# extract_text.py
import os
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
from components.readerregistry import ReaderRegistry

class Extractor:
    def __init__(self, input_dir, output_dir, tokenize=False, save_images=False):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.save_images = save_images
        os.makedirs(output_dir, exist_ok=True)
        self.tokenize = tokenize
    
    def extract_text(self, file_path):
        file_extension = os.path.splitext(file_path)[1].lower()
        reader = ReaderRegistry.get_reader(file_extension)
        document_data = reader.read(file_path)
        if self.tokenize:
            document_data.tokenize_text()
        return document_data

    def run(self):
        all_data = []
        for file in tqdm(os.listdir(self.input_dir)):
            file_path = os.path.join(self.input_dir, file)
            document_data = self.extract_text(file_path)
            
            # Save to DataFrame and write images
            df = document_data.write(self.output_dir, save_images=self.save_images)
            all_data.append(df)

        # Concatenate all DataFrames
        result_df = pd.concat(all_data, ignore_index=True)
        # Save DataFrame to CSV
        result_df.to_csv(os.path.join(self.output_dir, "extracted_data.csv"), index=False)

# Example usage
if __name__ == "__main__":
    input_dir = "data/test/data"
    output_dir = "data/test/output"
    extractor = Extractor(input_dir, output_dir, tokenize=True, save_images=False)
    extractor.run()
