def pow_iter(num, p):
    res = 1
    for i in range(p):
        res *= num
    return res


def fib_rec(n):
    if n <= 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    if n <= 2:
        return 1
    fib_1 = fib_2 = 1
    for i in range(2, n):
        fib_3 = fib_1 + fib_2
        fib_2, fib_1 = fib_3, fib_2
    return fib_2


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_count(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count


if __name__ == "__main__":
    print("Pow 3**2:", pow_iter(3, 2))
    print("Pow 4**3:", pow_iter(4, 3))
    print("Pow 5**1:", pow_iter(5, 1))

    print("Fib_rec 3:", fib_rec(3))
    print("Fib_rec 4:", fib_rec(4))
    print("Fib_rec 5:", fib_rec(5))

    print("Fib_iter 3:", fib_iter(3))
    print("Fib_iter 4:", fib_iter(4))
    print("Fib_iter 5:", fib_iter(5))

    print("Prime_count 10:", prime_count(10))
    print("Prime_count 100:", prime_count(100))
    print("Prime_count 1000:", prime_count(1000))
