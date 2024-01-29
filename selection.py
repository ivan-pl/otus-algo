from typing import Sequence


def find_max(arr: Sequence[int], to: int) -> int:
    max_ind = arr[0]
    for i in range(0, to + 1):
        if arr[i] > arr[max_ind]:
            max_ind = i
    return max_ind


def selection_sort(arr: Sequence[int]) -> Sequence[int]:
    for i in range(len(arr) - 1, 0, -1):
        max_ind = find_max(arr, i)
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
    return arr


if __name__ == "__main__":
    from numpy import random
    from utility import timeit_sort

    print('SHOW RESULT'.center(10, '-'))
    array = random.randint(0, 10, 10)
    print(array)
    print(selection_sort(array))

    print("TEST".center(10, '-'))
    for size in [1000, 10_000, 100_000, 1_000_000]:
        timeit_sort(size, selection_sort, size)
