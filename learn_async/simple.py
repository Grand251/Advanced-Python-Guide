import time
import asyncio


async def do_something():
    asyncio.sleep(2)


if __name__ == '__main__':

    start = time.time()
    asyncio.run(do_something())
    asyncio.run(do_something())
    end = time.time()
    print('Synchronous Execution Elapsed time: ', end - start)

    start = time.time()
    task1 = asyncio.create_task(do_something())
    task2 = asyncio.create_task(do_something())
    await task1
    await task2
    end = time.time()
    print("Asynchronous Execution time: ", end - start)
