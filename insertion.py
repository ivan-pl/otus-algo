from utility import timeit_sort


def insertion_sort(array):
    for j in range(1, len(array)):
        for i in range(j, 0, -1):
            if array[i] < array[i - 1]:
                array[i - 1], array[i] = array[i], array[i - 1]
            else:
                break
    return array


def insertion_shift_sort(array):
    for j in range(1, len(array)):
        k = array[j]
        i = j - 1
        while i >= 0 and array[i] > k:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = k
    return array


def binary_search(key, array, low, high):
    if high <= low:
        if key > array[low]:
            return low + 1
        return low
    mid = int((low + high) / 2)
    if key >= array[mid]:
        return binary_search(key, array, mid + 1, high)
    return binary_search(key, array, low, mid - 1)


def insertion_binary_sort(array):
    for j in range(1, len(array)):
        k = array[j]
        i = j - 1
        p = binary_search(k, array, 0, i)
        while i >= p:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = k
    return array


if __name__ == "__main__":
    for size in (100, 1_000, 10_000):
        timeit_sort(size, insertion_sort)

    for size in (100, 1_000, 10_000):
        timeit_sort(size, insertion_shift_sort)

    for size in (100, 1_000, 10_000):
        timeit_sort(size, insertion_binary_sort)