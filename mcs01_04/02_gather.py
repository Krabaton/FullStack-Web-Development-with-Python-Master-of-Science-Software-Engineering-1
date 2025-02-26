import asyncio
from time import sleep, time, perf_counter

from faker import Faker

fake = Faker("uk-UA")  # en-GB


def get_user_from_db(uuid: int):
    sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def async_get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def main():
    users = []
    for i in range(1, 6):
        users.append(async_get_user_from_db(i))
    result = await asyncio.gather(*users)  # Promise.all
    return result


if __name__ == "__main__":
    start = perf_counter()
    for i in range(1, 6):
        user = get_user_from_db(i)
        print(user)
    print(perf_counter() - start)

    start = perf_counter()
    users = asyncio.run(main())
    print(users)
    print(perf_counter() - start)
