import aiohttp
import asyncio


async def normal():
    return 'hui'


async def coro_long():
    try:
        print('start')
        await asyncio.sleep(2)
        print('stop')
        return 'coro_long'
    except asyncio.CancelledError as e:
        print(f'All Done for cancelling')
        raise asyncio.CancelledError


async def cor_TypeError():
    raise TypeError


async def cor_ValueError():
    raise ValueError


async def main():

    tasks = [normal(), cor_TypeError(), coro_long()]
    tasks = [asyncio.create_task(task, name=f"{task.__name__}") for task in tasks]

    try:
        result = await asyncio.gather(*tasks) #return_exceptions=True)
    except TypeError as e:
        print(f'{e=}')
    except ValueError as e:
        print(f'{e=}')
    else:
        print(result)

    for task in tasks:
        if not task.done():
            task.cancel()
            print(f'Pending: {task.get_name()}')

    print()

    await asyncio.sleep(3)
    for task in tasks:
        print(f'{task._state}')


if __name__ == "__main__":
    asyncio.run(main())




