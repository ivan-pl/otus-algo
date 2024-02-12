from numpy import random, arange
import time
from typing import Callable, Sequence


def timeit_sort(size: int, sort_func: Callable[[Sequence[int]], Sequence[int]], max_random_value: int = 100_000,
                seed: int = 49) -> None:
    random.seed(seed)

    array = random.randint(max_random_value, size=size)
    start_time = time.time()
    sort_func(array)
    print(f'{sort_func.__name__} RANDOM size={size!r} time: {time.time() - start_time:.3f} seconds')

    array = arange(size)
    start_time = time.time()
    sort_func(array)
    print(f'{sort_func.__name__} SORTED size={size!r} time: {time.time() - start_time:.3f} seconds')

    array = arange(size - 1, -1, -1)
    start_time = time.time()
    sort_func(array)
    print(f'{sort_func.__name__} REVERSED size={size!r} time: {time.time() - start_time:.3f} seconds')
