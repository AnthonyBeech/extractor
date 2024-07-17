import os
import requests

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

# Directory to save the downloaded files
save_directory = 'test/data'

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# URLs of the sample files
file_urls = {
    "sample_txt": "https://www.gutenberg.org/files/11/11-0.txt",
    "sample_pdf": "https://arxiv.org/pdf/2101.12345.pdf",
    "sample_docx": "https://filesamples.com/samples/document/docx/sample2.docx",
    "sample_csv": "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv",
    "sample_html": "https://www.nature.com/articles/s41586-020-2649-2",
    "sample_jpg": "https://sample-videos.com/img/Sample-jpg-image-50kb.jpg",
    "sample_tiff": "https://file-examples.com/wp-content/storage/2017/10/file_example_TIFF_1MB.tiff",
    "sample_pptx": "https://file-examples.com/wp-content/storage/2017/08/file_example_PPT_1MB.ppt"
}

# Downloading the files
for filename, url in file_urls.items():
    # Correct the file extension for HTML files
    if 'html' in filename:
        local_filename = f"{filename}.html"
    else:
        local_filename = f"{filename}.{url.split('.')[-1]}"
    
    # Define the full path to save the file
    local_filepath = os.path.join(save_directory, local_filename)
    
    # Download the file
    download_file(url, local_filepath)
    print(f"Downloaded {url} to {local_filepath}")
