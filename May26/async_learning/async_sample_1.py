import asyncio

async def do_something():
    await asyncio.sleep(2)
    return "Did something"

async def do_something_else():
    await asyncio.sleep(1)
    return  "did something else"

# waiting in sequence
async def main_sequence():
    # await is used to wait for a coroutine to finish
    result = await do_something()
    print(result)
    # await is used to wait for a coroutine to finish
    result = await do_something_else()
    print(result)


# non blocking way
async def main():
    # await is used to wait for a coroutine to finish
    results = await asyncio.gather(do_something(), do_something_else())
    for result in results:
        print(result)

asyncio.run(main()) # creates event loop