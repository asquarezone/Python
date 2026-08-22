import asyncio

def test_something():
    print("testing")

async def print_something():
    print("hello")

async def do_something():
    print("doing something")

async def main():
    test_something()
    #await print_something()
    #await do_something()
    await asyncio.gather(do_something(), print_something())
    print("finished")

if __name__ == "__main__":
    # creates the event loop
    asyncio.run(main())