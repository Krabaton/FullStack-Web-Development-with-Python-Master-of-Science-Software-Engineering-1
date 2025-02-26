import asyncio

from faker import Faker

from timing import async_timed

fake = Faker("uk-UA")  # en-GB

# Awaitable
# ├── Coroutine
# └── Future
#     └── Task

"""
Coroutine (корутина) — це об'єкт, який створюється при виклику асинхронної функції. 
Сам по собі він ще не виконується, а лише представляє майбутнє обчислення. 
Його можна запустити через await або передати в asyncio.create_task() чи asyncio.run().

Future — це низькорівневий об'єкт, який представляє обіцянку (promise) отримати результат у майбутньому. 
Future ще не виконується самостійно, але ним можна керувати, викликаючи set_result() або set_exception().

Task — це спеціальний підклас Future, який обгортає корутину й автоматично починає її виконання. 
При створенні asyncio.create_task(coroutine), передана корутина запускається у фоновому режимі й 
буде виконуватись незалежно від того, чекаємо ми її чи ні.
"""


async def async_get_user_from_db(uuid: int, future: asyncio.Future):
    await asyncio.sleep(0.5)
    future.set_result({"id": uuid, "username": fake.user_name(), "email": fake.email()})


def make_request(uuid: int) -> asyncio.Future:
    future = asyncio.Future()
    asyncio.create_task(async_get_user_from_db(uuid, future))
    return future


@async_timed("Перевірка future")
async def main():
    users = []
    for i in range(1, 6):
        users.append(make_request(i))

    print([user.done() for user in users])
    result = await asyncio.gather(*users)
    print([user.done() for user in users])
    return result


if __name__ == "__main__":
    users = asyncio.run(main())
    print(users)
