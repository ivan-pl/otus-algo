from utility import timeit_sort


def bubble_sort(array):
    for j in range(len(array), 0, -1):
        for i in range(1, j):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
    return array


def bubble_sort_2(array):
    for j in range(len(array), 0, -1):
        is_sorted = True
        for i in range(1, j):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                is_sorted = False
        if is_sorted:
            break
    return array


if __name__ == "__main__":
    for size in (100, 1_000, 10_000):
        timeit_sort(size, bubble_sort)
