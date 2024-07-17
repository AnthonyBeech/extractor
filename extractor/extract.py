# extract_text.py
import os
import pandas as pd
import matplotlib.pyplot as plt
from extractor.components.readregistry import ReaderRegistry

def extract_text(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    reader = ReaderRegistry.get_reader(file_extension)
    return reader.read(file_path)

# Function to display images
def display_images(images):
    for i, img in enumerate(images):
        plt.figure()
        plt.imshow(img)
        plt.title(f'Image {i+1}')
        plt.axis('off')  # Hide axes
    plt.show()

# Example usage
if __name__ == "__main__":
    output_dir = "test/data/output"
    image_output_dir = os.path.join(output_dir, "images")
    os.makedirs(image_output_dir, exist_ok=True)
    
    all_data = []
    for file in os.listdir("test/data"):
        file_path = os.path.join("test/data", file)
        document_data = extract_text(file_path)
        
        # Save to DataFrame and write images
        df = document_data.write(image_output_dir)
        all_data.append(df)
        print()

    # Concatenate all DataFrames
    result_df = pd.concat(all_data, ignore_index=True)
    # Save DataFrame to CSV
    result_df.to_csv(os.path.join(output_dir, "extracted_data.csv"), index=False)
