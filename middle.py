import math


def power_b(num, p):
    if p == 0:
        return 1
    if p == 1:
        return num
    if p % 2 == 0:
        x = power_b(num, p / 2)
        return x * x
    return num * power_b(num, p - 1)


def power_mul(num, p):
    if p == 0:
        return 1
    if p == 1:
        return num
    res = num
    cur_p = 1
    next_p = 2
    while next_p <= p:
        res *= res
        cur_p = next_p
        next_p *= 2
    for i in range(cur_p, p):
        res *= num
    return res


def fib_gold(n):
    fi = (1 + math.sqrt(5)) / 2
    return round(math.pow(fi, n) / math.sqrt(5))


class Matrix:
    @staticmethod
    def mul(m1: list[list], m2: list[list]) -> list[list]:
        if len(m1[0]) != len(m2):
            raise Exception("M1 doesn't correspond M2")
        cols = len(m2[0])
        rows = len(m1)
        result = [[None] * cols for _ in range(rows)]
        for x in range(cols):
            for y in range(rows):
                col = m1[y]
                row = [l[x] for l in m2]
                result[y][x] = sum([i1 * i2 for i1, i2 in zip(col, row)])
        return result

    @staticmethod
    def power(m, p):
        if len(m) != len(m[0]):
            raise Exception("The matrix must be square")
        if p == 0:
            raise Exception("P must be >= 1")
        if p == 1:
            return m
        if p % 2 == 0:
            x = Matrix.power(m, p / 2)
            return Matrix.mul(x, x)
        return Matrix.mul(m, Matrix.power(m, p - 1))


def fib_matrix(n):
    if n <= 2:
        return 1
    return Matrix.power([[1, 1], [1, 0]], n - 1)[0][0]


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = math.floor(math.sqrt(num))
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
    return True


def count_primes(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count


if __name__ == "__main__":
    print("Pow_b 3**2:", power_b(3, 2))
    print("Pow_b 4**3:", power_b(4, 3))
    print("Pow_b 5**1:", power_b(5, 1))

    print("Pow_mul 3**2:", power_mul(3, 2))
    print("Pow_mul 4**3:", power_mul(4, 3))
    print("Pow_mul 5**1:", power_mul(5, 1))

    print("Fib_gold 3:", fib_gold(3))
    print("Fib_gold 4:", fib_gold(4))
    print("Fib_gold 5:", fib_gold(5))

    m1 = [[4, 2], [9, 0]]
    m2 = [[3, 1], [-3, 4]]
    print("Matrix mul :", Matrix.mul(m1, m2), "Expected:", [[6, 12], [27, 9]])

    m1 = [[2, 1], [-3, 0], [4, -1]]
    m2 = [[5, -1, 6], [-3, 0, 7]]
    print("Matrix mul :", Matrix.mul(m1, m2), "Expected:", [[7, -2, 19], [-15, 3, -18], [23, -4, 17]])

    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matrix pow 2:", Matrix.power(m, 2), "Expected:", [[30, 36, 42], [66, 81, 96], [102, 126, 150]])

    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matrix pow 3:", Matrix.power(m, 3), "Expected:", [[468, 576, 684], [1062, 1305, 1548], [1656, 2034, 2412]])

    print("Fib_matrix 3:", fib_matrix(3))
    print("Fib_matrix 4:", fib_matrix(4))
    print("Fib_matrix 5:", fib_matrix(5))

    print("count_primes 1:", count_primes(10))
    print("count_primes 2:", count_primes(100))
    print("count_primes 3:", count_primes(1000))
