import os


class Tester:
    def __init__(self, task, path):
        self.task = task
        self.path = path

    def run_tests(self):
        test_counter = 0
        print("=== Start tests ===")
        while True:
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
        with open(out_file, 'r') as f:
            expect = f.read().rstrip()
        actual = self.task(data)
        return expect == actual
