import time

def download_file(url: str, dest: str) -> None:
    print(f"Downloading {url} to {dest}")
    time.sleep(2)
    print(f"Download complete {url}")


# 10 files to download
urls = [f"http://example.com/file{i}.txt" for i in range(10)]

for url in urls:
    download_file(url, f"/tmp/{url.split('/')[-1]}")

