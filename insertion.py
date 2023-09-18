from numpy import random
from utility import timeit_sort


def insertion_sort(array):
    for j in range(1, len(array)):
        for i in range(j, 0, -1):
            if array[i] < array[i - 1]:
                array[i - 1], array[i] = array[i], array[i - 1]
            else:
                break
    return array


if __name__ == "__main__":
    for size in (100, 1_000, 10_000):
        timeit_sort(size, insertion_sort)
