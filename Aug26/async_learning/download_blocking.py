import time
import requests
from pathlib import Path


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds")
        return result
    return wrapper


def download_file(url: str, dest_folder: str = "downloads") -> str:
    """
    Blocking download of a file from a URL.
    Saves the file to dest_folder and returns the saved file path.
    """
    Path(dest_folder).mkdir(exist_ok=True)

    filename = url.split("/")[-1] or "downloaded_file"
    dest_path = Path(dest_folder) / filename

    start = time.perf_counter()
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    elapsed = time.perf_counter() - start
    print(f"Downloaded: {filename} took {elapsed:.4f} seconds")
    return str(dest_path)


@measure_time
def download_all(urls: list[str]):
    for i, url in enumerate(urls, 1):
        print(f"Starting download {i}/{len(urls)}: {url}")
        download_file(url)


if __name__ == "__main__":
    urls = [
        "https://testfile.to/dl/100mb",
        "https://testfile.to/dl/10mb",
        "https://testfile.to/dl/1mb",
    ]
    download_all(urls)
