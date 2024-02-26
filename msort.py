from typing import Sequence, Any

import numpy as np


def msort(array: Sequence[Any]) -> Sequence[Any]:
    _msort(array, 0, len(array) - 1)
    return array


def _msort(array: Sequence[Any], left: int, right: int) -> None:
    if left >= right:
        return
    m = (left + right) // 2
    _msort(array, left, m)
    _msort(array, m + 1, right)
    _merge(array, left, m, right)


def _merge(array: Sequence[Any], left: int, mid: int, right: int) -> None:
    tmp = np.empty(right - left + 1, dtype=object)
    a = left
    b = mid + 1
    m = 0

    while a <= mid and b <= right:
        if array[a] <= array[b]:
            tmp[m] = array[a]
            a += 1
        else:
            tmp[m] = array[b]
            b += 1
        m += 1

    while a <= mid:
        tmp[m] = array[a]
        a += 1
        m += 1

    while b <= right:
        tmp[m] = array[b]
        b += 1
        m += 1

    for i in range(left, right + 1):
        array[i] = tmp[i - left]


if __name__ == "__main__":
    from numpy import random
    from utils import timeit_sort
    import sys

    sys.setrecursionlimit(1_001_000)
    print('SHOW RESULT'.center(10, '-'))
    array = random.randint(0, 10, 10)
    print(array)
    print(msort(array))

    print("TEST".center(10, '-'))
    for size in [100, 1000, 10_000, 100_000, 1_000_000]:
        timeit_sort(size, msort, size)
