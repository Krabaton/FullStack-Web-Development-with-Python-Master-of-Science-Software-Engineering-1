from functools import wraps
from time import perf_counter


def async_timed(name: str = None):
    if name:
        print(name)

    def wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            start = perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                print(perf_counter() - start)

        return wrapped

    return wrapper


def sync_timed(name: str = None):
    if name:
        print(name)

    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            start = perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                print(perf_counter() - start)

        return wrapped

    return wrapper
