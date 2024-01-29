from typing import Sequence

"""
P = (x - 1) / 2
L = 2x + 1
R = 2x + 2
"""


def heapify(arr: Sequence[int], root: int, size: int) -> None:
    L = 2 * root + 1
    R = 2 * root + 2
    X = root
    if L < size and arr[L] > arr[X]:
        X = L
    if R < size and arr[R] > arr[X]:
        X = R
    if X == root:
        return
    arr[X], arr[root] = arr[root], arr[X]
    heapify(arr, X, size)


def heap_sort(arr: Sequence[int]) -> Sequence[int]:
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))
    for i in range(len(arr) - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)
    return arr


if __name__ == "__main__":
    from numpy import random
    from utility import timeit_sort

    print('SHOW RESULT'.center(10, '-'))
    array = random.randint(0, 10, 10)
    print(array)
    print(heap_sort(array))

    print("TEST".center(10, '-'))
    for size in [100, 1000, 10_000, 100_000, 1_000_000]:
        timeit_sort(size, heap_sort, size)
