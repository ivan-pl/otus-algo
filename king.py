from bitcount import cnt2 as bit_count
from tester import Tester
import os


def king(position: int):
    K = 1 << position
    Ka = 0xfefefefefefefefe & K
    Kh = 0x7f7f7f7f7f7f7f7f & K
    M = (
            Ka << 7 | K << 8 | Kh << 9 |
            Ka >> 1 | Kh << 1 |
            Ka >> 9 | K >> 8 | Kh >> 7
    )
    M &= 0xffffffffffffffff
    return bit_count(M), int(M)


if __name__ == "__main__":
    path = os.path.join('0.BITS', '1.Bitboard - Король')


    def parse_out(string: str):
        return tuple(int(s) for s in string.split('\n'))


    tester = Tester(king, path, int, parse_out)
    tester.run_tests()
