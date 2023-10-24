import aiohttp
import asyncio


async def normal():
    return 'hui'


async def cor_TypeError():
    raise TypeError


async def cor_ValueError():
    raise ValueError


async def main():

    try:
        async with asyncio.TaskGroup() as tg:
            res1 = tg.create_task(normal())
            res2 = tg.create_task(cor_TypeError())
            res3 = tg.create_task(cor_ValueError())

        results = [res1.result(), res2.result(), res3.result()]

    except* TypeError as e:
        print(f'{e=}')
    except* ValueError as e:
        print(f'{e=}')

    else:
        print(results)


    # try:
    #     result = await asyncio.gather(
    #         normal(),
    #         cor_TypeError(),
    #         cor_ValueError(),
    #         #return_exceptions=True
    #     )
    # except TypeError as e:
    #     print(f'{e=}')
    # except ValueError as e:
    #     print(f'{e=}')
    # else:
    #     print(result)


if __name__ == "__main__":
    asyncio.run(main())




