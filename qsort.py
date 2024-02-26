from typing import Sequence, Any


def qsort(array: Sequence[Any]) -> Sequence[Any]:
    m = _split(array, 0, len(array) - 1)
    _qsort(array, 0, m - 1)
    _qsort(array, m, len(array) - 1)
    return array


def _split(array: Sequence[Any], left: int, right: int) -> int:
    pivot = array[right]
    m = left - 1
    for j in range(left, right + 1):
        if array[j] <= pivot:
            m += 1
            array[m], array[j] = array[j], array[m]
    return m


def _qsort(array: Sequence[Any], left: int, right: int) -> None:
    if left >= right:
        return
    m = _split(array, left, right)
    _qsort(array, left, m - 1)
    _qsort(array, m + 1, right)


if __name__ == "__main__":
    from numpy import random
    from utils import timeit_sort
    import sys

    sys.setrecursionlimit(1_000_000)
    print('SHOW RESULT'.center(10, '-'))
    array = random.randint(0, 10, 10)
    print(array)
    print(qsort(array))

    print("TEST".center(10, '-'))
    for size in [100, 1000, 10_000, 100_000]:
        timeit_sort(size, qsort, size)
