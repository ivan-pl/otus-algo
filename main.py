import time
from myarray import SingleArray, FactorArray, VectorArray
import random

random.seed(49)


def test_arr(arr, total, comment=''):
    start_time = time.time()
    for i in range(total):
        index = random.randint(0, i)
        arr.add(i, index)
    print(f'Add {arr.__class__.__name__} {comment} total={total}:\t{time.time() - start_time:.2f} seconds')
    start_time = time.time()
    for i in range(total - 1, -1, -1):
        index = random.randint(0, i)
        arr.remove(index)
    print(f'Remove {arr.__class__.__name__} {comment} total={total}:\t{time.time() - start_time:.2f} seconds')


if __name__ == "__main__":
    # for total in (1_000, 10_000, 100_000):
    #     single_arr = SingleArray()
    #     test_arr(single_arr, total)

    # for total in (1_000, 10_000, 100_000):
    #     vector_arr = VectorArray()
    #     test_arr(vector_arr, total, "vector=10")

    # for total in (1_000, 10_000, 100_000):
    #     vector_arr = VectorArray(dtype=int, vector=100)
    #     test_arr(vector_arr, total, "vector=100")

    # for total in (1_000, 10_000, 100_000):
    #     factor_arr = FactorArray()
    #     test_arr(factor_arr, total, "factor=0.3")

    for total in (1_000, 10_000, 100_000):
        factor_arr = FactorArray(dtype=int, factor=0.5)
        test_arr(factor_arr, total, "factor=0.5")
