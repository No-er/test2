import asyncio
import aiohttp
from time import time
import random


def write_files(file):
    file_name = random.randint(0, 100000)
    with open(f'{file_name}', 'wb') as f:
        f.write(file)


async def get_files(url, session):
    async with session.get(url, allow_redirects=True) as resp:
        file = await resp.read()
        write_files(file)


async def main():
    url = 'http://placekitten.com/200/300'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            task = asyncio.create_task(get_files(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time()
    asyncio.run(main())
    print(time()-start_time)