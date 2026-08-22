import time
import asyncio
from pathlib import Path

import aiohttp


def measure_time(func):
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = await func(*args, **kwargs)

        elapsed_time = time.perf_counter() - start_time

        print(
            f"\n[TOTAL] {func.__name__} "
            f"took {elapsed_time:.4f} seconds"
        )

        return result

    return wrapper


async def download_file(
    session: aiohttp.ClientSession,
    url: str,
    dest_folder: str = "downloads",
) -> str:

    Path(dest_folder).mkdir(exist_ok=True)

    filename = url.split("/")[-1] or "downloaded_file"
    dest_path = Path(dest_folder) / filename

    print(f"[START] {filename}")

    start_time = time.perf_counter()

    async with session.get(url) as response:
        response.raise_for_status()

        with open(dest_path, "wb") as f:

            while True:
                chunk = await response.content.read(8192)

                if not chunk:
                    break

                f.write(chunk)

                # Give other async tasks an opportunity to run
                await asyncio.sleep(0)

    elapsed_time = time.perf_counter() - start_time

    print(
        f"[DONE ] {filename} "
        f"({elapsed_time:.2f}s)"
    )

    return str(dest_path)


@measure_time
async def download_all(urls: list[str]):

    print("[MAIN ] Creating HTTP session")

    async with aiohttp.ClientSession() as session:

        tasks = []

        for i, url in enumerate(urls, 1):

            filename = url.split("/")[-1]

            print(
                f"[MAIN ] Creating task {i}: {filename}"
            )

            task = asyncio.create_task(
                download_file(session, url)
            )

            tasks.append(task)

        print("\n[MAIN ] All tasks created")
        print("[MAIN ] Starting concurrent downloads...\n")

        results = await asyncio.gather(*tasks)

        print("\n[MAIN ] All downloads completed")

        return results


if __name__ == "__main__":

    urls = [
        "https://testfile.to/dl/100mb",
        "https://testfile.to/dl/10mb",
        "https://testfile.to/dl/1mb",
    ]

    asyncio.run(download_all(urls))