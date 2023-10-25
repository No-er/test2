from redis import asyncio as aioredis
import asyncio


class Rediska:
    def __init__(self, redis, keys):
        self._redis = redis
        self._keys = keys


    def __aiter__(self):
        self.ikeys = iter(self._keys)
        return self


    async def __anext__(self):
        try:
            key = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration

        async with self._redis.client() as session:
            data = await session.get(key)

        return data


async def main():
    redis = await aioredis.from_url("redis://localhost")
    keys = ['hui', 'a', 'c']

    async for data in Rediska(redis, keys):
        print(data)


if __name__ == "__main__":
    asyncio.run(main())




