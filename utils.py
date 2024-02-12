from numpy import random, arange
import time
from typing import Callable, Sequence, Any
import os


def timeit_sort(size: int, sort_func: Callable[[Sequence[int]], Sequence[Any]], max_random_value: int = 100_000,
                seed: int = 49) -> None:
    r = random.RandomState(seed)

    array = r.randint(max_random_value, size=size)
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


def generate_file(row_count: int, max_number: int, seed: int = 49) -> str:
    r = random.RandomState(seed)
    path = os.path.join('generated_files', f'{row_count}_rows_{max_number}_max.txt')
    with open(path, 'w') as f:
        for i in range(row_count):
            f.write(f'{r.randint(1, max_number)}\n')

    return path
