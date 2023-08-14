def spell_01(x: int, y: int) -> bool:
    return x > y


def spell_02(x: int, y: int) -> bool:
    return x == y


def spell_03(x: int, y: int) -> bool:
    return 24 - x == y


def spell_04(x: int, y: int) -> bool:
    return x < 30 - y


def spell_05(x: int, y: int) -> bool:
    return x * 0.5 == y or x * 0.5 - 0.5 == y


def spell_06(x: int, y: int) -> bool:
    return y <= 10 or x <= 10


def spell_07(x: int, y: int) -> bool:
    return y > 15 and x > 15


def spell_08(x: int, y: int) -> bool:
    return x * y == 0


def spell_09(x: int, y: int) -> bool:
    return x - 10 > y or x + 10 < y


def spell_10(x: int, y: int) -> bool:
    return x - 1 >= y >= x * 0.5 - 0.5


def spell_11(x: int, y: int) -> bool:
    return x == 1 or y == 1 or x == 23 or y == 23


def spell_13(x: int, y: int) -> bool:
    return -x + 19 < y < -x + 29


def main():
    for y in range(25):
        for x in range(25):
            print("#", end=" ") if spell_13(x, y) else print(".", end=" ")
        print()


if __name__ == "__main__":
    main()
