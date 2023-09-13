def cnt1(num):
    cnt = 0
    while num > 0:
        cnt += num & 1
        num = num >> 1
    return cnt


def cnt2(num):
    cnt = 0
    while num > 0:
        num &= num - 1
        cnt += 1
    return cnt


BITS = []


def init_bits():
    global BITS
    BITS = [cnt2(i) for i in range(256)]


def cnt3(num):
    cnt = 0
    while num > 0:
        cnt += BITS[num & 255]
        num >>= 8
    return cnt


if __name__ == "__main__":
    print("cnt1: ", cnt1(770))  # 3
    print("cnt2: ", cnt2(770))  # 3
    init_bits()
    print("cnt3: ", cnt3(770))  # 3
