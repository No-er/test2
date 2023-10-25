import asyncio
from faker import Faker


data = Faker('en_US')


async def generator(n=1):
    #await asyncio.sleep(0)
    for _ in range(n):
        name, surname = data.name_male().split()
        yield name, surname


async def main():

    # l = [i async for i in generator(3)]
    # print(l)

    d = {k: v async for k, v in generator(3)}
    print(d)

    # async for i in generator(3):
    #     print(i)


if __name__ == "__main__":
    asyncio.run(main())




