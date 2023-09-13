from bitcount import cnt2 as bit_count
from tester import Tester
import os
import math


def rook(position: int):
    row = math.floor(position / 8)
    col = position % 8

    K = 1 << position
    K_y = 0x101010101010101 << col
    K_x = 0xff << 8 * row

    M = K_x ^ K_y
    M &= 0xffffffffffffffff
    return bit_count(M), int(M)


if __name__ == "__main__":
    path = os.path.join('0.BITS', '3.Bitboard - Ладья')


    def parse_out(string: str):
        return tuple(int(s) for s in string.split('\n'))


    tester = Tester(rook, path, int, parse_out)
    tester.run_tests()
