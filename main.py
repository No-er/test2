import asyncio
from time import time

async def first():
    num = 0
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)

async def second():
    while True:
        print(time())
        await asyncio.sleep(1)

async def loop():
    task1 = asyncio.create_task(first())
    task2 = asyncio.create_task(second())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(loop())

