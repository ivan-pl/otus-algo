from numpy import random
import time


def timeit_sort(size, sort_func, low=10000, high=None, seed=49):
    random.seed(seed)
    array = random.randint(low, high, size)
    start_time = time.time()
    sort_func(array)
    print(f'{sort_func.__name__} size={size!r} time: {time.time() - start_time:.3f} seconds')
