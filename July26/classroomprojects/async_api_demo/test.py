import asyncio
import aiohttp
import time

PARALLEL_COUNT = 50
URL = "http://localhost:8000"

async def fetch(session, i):
    start = time.perf_counter()
    async with session.get(URL) as response:
        elapsed = time.perf_counter() - start
        print(f"[{time.strftime('%H:%M:%S')}] Request {i:>3} | Status: {response.status} | Time: {elapsed:.3f}s")
        return response.status

async def main():
    print(f"Sending {PARALLEL_COUNT} parallel requests to {URL}\n")
    overall_start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch(session, i) for i in range(PARALLEL_COUNT)], return_exceptions=True)
    total = time.perf_counter() - overall_start
    success = sum(1 for r in results if r == 200)
    failed = PARALLEL_COUNT - success
    print(f"\nDone in {total:.3f}s | Success: {success} | Failed: {failed}")

asyncio.run(main())
