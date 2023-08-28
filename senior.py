from tester import Tester
from junior import pow_iter as power_iter
from middle import power_b, power_mul

if __name__ == "__main__":
    # Testing Power
    parse_in = lambda data: [float(x) if '.' in x else int(x) for x in data.split('\n')]
    parse_out = float
    compare_results = lambda expect, actual: round(expect, 6) == round(actual, 6)
    power_funcs = [power_mul, power_b, power_iter]
    for power in power_funcs:
        tester_power = Tester(power, '3.Power', parse_in, parse_out, compare_results)
        tester_power.run_tests()
