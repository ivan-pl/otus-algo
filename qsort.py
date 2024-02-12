from typing import Sequence, Any


def qsort(array: Sequence[Any]) -> None:
    m = _split(array, 0, len(array) - 1)
    _qsort(array, 0, m - 1)
    _qsort(array, m, len(array) - 1)


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
    import random

    random.seed(47)
    arr = [random.randint(1, 20) for i in range(20)]
    print(arr)
    qsort(arr)
    print(arr)
