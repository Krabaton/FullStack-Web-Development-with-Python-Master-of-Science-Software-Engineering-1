import asyncio
from random import randint


async def producer(q: asyncio.Queue):
    num = randint(1, 1000)
    await asyncio.sleep(0.1)
    await q.put(num)


async def consumer(q: asyncio.Queue):
    while True:
        num = await q.get()
        print(f"Consumer: {num ** 2}")
        q.task_done()


async def main():
    queue = asyncio.Queue()
    loop = asyncio.get_running_loop()
    consumer_task = loop.create_task(consumer(queue))
    producer_tasks = [loop.create_task(producer(queue)) for _ in range(100)]
    await asyncio.gather(*producer_tasks)
    await queue.join()  # Чекаємо доки всі task будуть виконані
    consumer_task.cancel()


if __name__ == '__main__':
    asyncio.run(main())


