import itertools


def find(n: int) -> int:
    if n < 1:
        return 0

    sum_count_arr = [1]
    for i in range(n):
        count_arr = []
        for j in range(10):
            count_arr.append([0] * j + sum_count_arr)
        sum_count_arr = [sum(i) for i in itertools.zip_longest(*count_arr, fillvalue=0)]

    return sum([x * x for x in sum_count_arr])


if __name__ == "__main__":
    n = 4
    print(find(n))
