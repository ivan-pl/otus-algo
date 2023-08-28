import os


class Tester:
    def __init__(self, task, path, parse_in=None, parse_out=None, compare_results=None, test_count=None):
        self.task = task
        self.path = path
        self.parse_in = parse_in
        self.parse_out = parse_out
        self.compare_results = compare_results
        self.test_count = test_count

    def run_tests(self):
        test_counter = 0
        print(f"=== Start tests for {self.task.__name__} ===")
        while True:
            if self.test_count and test_counter > self.test_count: break
            in_file = os.path.join(self.path, f'test.{test_counter}.in')
            out_file = os.path.join(self.path, f'test.{test_counter}.out')
            if not os.path.isfile(in_file) or not os.path.isfile(out_file):
                break
            print(f'Test #{test_counter}:\t{self.__run_test(in_file, out_file)}')
            test_counter += 1
        print("=== End tests ===")

    def __run_test(self, in_file, out_file):
        with open(in_file, 'r') as f:
            data = f.read().rstrip()
            if self.parse_in:
                data = self.parse_in(data)
        with open(out_file, 'r') as f:
            expect = f.read().rstrip()
            if self.parse_out:
                expect = self.parse_out(expect)
        actual = self.task(*data) if isinstance(data, list) else self.task(data)
        if self.compare_results:
            result = self.compare_results(expect, actual)
        else:
            result = expect == actual
        if not result:
            print(f'Expect: {expect!r}\tActual: {actual!r}')
        return result
