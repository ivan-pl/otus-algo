from bitcount import cnt2 as bit_count
from tester import Tester
import os


def knight(position: int):
    K = 1 << position
    Ka = 0xfefefefefefefefe & K
    Kb = 0xfcfcfcfcfcfcfcfc & K
    Kg = 0x3f3f3f3f3f3f3f3f & K
    Kh = 0x7f7f7f7f7f7f7f7f & K
    M = (
            Ka << 15 | Kh << 17 |
            Kb << 6 | Kg << 10 |
            Kb >> 10 | Kg >> 6 |
            Ka >> 17 | Kh >> 15
    )
    M &= 0xffffffffffffffff
    return bit_count(M), int(M)


if __name__ == "__main__":
    path = os.path.join('0.BITS', '2.Bitboard - Конь')


    def parse_out(string: str):
        return tuple(int(s) for s in string.split('\n'))


    tester = Tester(knight, path, int, parse_out)
    tester.run_tests()
