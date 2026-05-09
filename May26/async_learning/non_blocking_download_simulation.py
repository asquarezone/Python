import asyncio


async def download_file(url: str, dest: str) -> None:
    print(f"Downloading {url} to {dest}")
    await asyncio.sleep(2)
    print(f"Download complete {url}")

# 10 files to download
urls = [f"http://example.com/file{i}.txt" for i in range(10)]

# created 10 coroutines
tasks = []
for url in urls:
    tasks.append(download_file(url, f"/tmp/{url.split('/')[-1]}"))

async def main():
    # await is used to wait for a coroutine to finish
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main()) # creates event loop