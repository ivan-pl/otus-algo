from tester import Tester
from tickets import find

if __name__ == "__main__":
    tester = Tester(find, '1.Tickets')
    tester.run_tests()
