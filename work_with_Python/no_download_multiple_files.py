"""
The example of how to implement download of many file simultaneously
Files are downloaded via requests GET and saved into provided directory
"""
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import os

def download_file_threaded(args: tuple) -> str:
    url, output_dir, filename = args
    try:
        filepath = os.path.join(output_dir, filename)
        
        url = f"{url}{filename}"
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=16384):
                file.write(chunk)
        
        return filepath
    except Exception as e:
        print(f"Failed to download with error:{str(e)}")
        return ''

def download_multiple_files(url: str, files: str, output_dir: str ="data", max_workers: int =5) -> int:
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Prepare arguments for thread pool
    args = [(url, output_dir, file) for file in files]

    # Download files using thread pool
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(tqdm(
            executor.map(download_file_threaded, args),
            total=len(url),
            desc="Downloading files"
        ))
    
    # Process results
    successful = [r for r in results if r != '']
    failed = len(results) - len(successful)
    
    print(f"\nDownload complete:")
    print(f"{len(successful)} - successful downloads")
    print(f"{failed} - failed downloads")
    
    return successful

# Example usage
url = 'https://www.examples.com/'

files = [
    'file.txt',
    'file.zip',
    'big-file.zip',
]

downloaded_files = download_multiple_files(url, files, "data", max_workers=len(files))
print('done...')