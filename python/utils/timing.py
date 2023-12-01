
from functools import wraps
from time import perf_counter

from utils.parsing import day_str



def timer(day: int):
    "Print the runtime of the decorated function."
    def timer_decorator(func):
        @wraps(func)
        def wrapper_timer(*args, **kwargs):
            start = perf_counter()
            value = func(*args, **kwargs)
            end = perf_counter()
            run_time = end - start
            if value is not None:
                print(f'Finished Day {day_str(day)} {func.__name__!r} in {run_time:.4f} seconds. Answer: {value}')
            return value
        return wrapper_timer
    return timer_decorator