from utility import timeit_sort


def shell(array):
    N = len(array)
    gap = int(N / 2)
    while gap >= 1:
        for j in range(gap, N):
            for i in range(j, gap - 1, -gap):
                if array[i - gap] < array[i]:
                    break
                array[i - gap], array[i] = array[i], array[i - gap]
        gap >>= 1
    return array


def form_hibbard_gaps(N):
    gaps = []
    k = 1
    gap = 1
    while gap < N:
        gaps.append(gap)
        gap = (2 << k) - 1
        k += 1
    return gaps[::-1]


def shell_hibbard(array):
    N = len(array)
    for gap in form_hibbard_gaps(N):
        for j in range(gap, N):
            for i in range(j, gap - 1, -gap):
                if array[i - gap] < array[i]:
                    break
                array[i - gap], array[i] = array[i], array[i - gap]
    return array


def form_sedgewick_gaps(N):
    gaps = []
    k = 1
    gap = 1
    while gap < N:
        gaps.append(gap)
        gap = 4 ** k + 3 * 2 ** (k - 1) + 1
        k += 1
    return gaps[::-1]


def shell_sedgewick(array):
    N = len(array)
    for gap in form_sedgewick_gaps(N):
        for j in range(gap, N):
            for i in range(j, gap - 1, -gap):
                if array[i - gap] < array[i]:
                    break
                array[i - gap], array[i] = array[i], array[i - gap]
    return array


if __name__ == "__main__":
    for size in (100, 1_000, 10_000, 100_000, 1_000_000):
        timeit_sort(size, shell)

    for size in (100, 1_000, 10_000, 100_000, 1_000_000):
        timeit_sort(size, shell_hibbard)

    for size in (100, 1_000, 10_000, 100_000, 1_000_000):
        timeit_sort(size, shell_sedgewick)
