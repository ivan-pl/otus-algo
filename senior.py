from tester import Tester
from junior import pow_iter as power_iter, fib_iter, fib_rec, prime_count as jun_count_primes
from middle import power_b, power_mul, fib_gold, fib_matrix, count_primes, eratosthene


def test_power():
    parse_in = lambda data: [float(x) if '.' in x else int(x) for x in data.split('\n')]
    parse_out = float
    compare_results = lambda expect, actual: round(expect, 6) == round(actual, 6)
    power_funcs = [power_mul, power_b, power_iter]
    for power in power_funcs:
        tester = Tester(power, '3.Power', parse_in, parse_out, compare_results, 8)
        tester.run_tests()


def test_fib():
    fib_funcs = [fib_iter, fib_rec, fib_gold, fib_matrix]
    for fib in fib_funcs:
        tester = Tester(fib, '4.Fibo', int, int, test_count=6)
        tester.run_tests()


def test_primes():
    primes_funcs = [jun_count_primes, count_primes, eratosthene]
    for prime in primes_funcs:
        tester = Tester(prime, '5.Primes', int, int, test_count=8)
        tester.run_tests()


if __name__ == "__main__":
    test_power()
    test_fib()
    test_primes()
