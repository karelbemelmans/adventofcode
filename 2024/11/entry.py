#!/usr/bin/env python3


# Gold old dynamic programming cache
DP = {}


def blink(x, t):

    # Cached?
    if (x, t) in DP:
        return DP[(x, t)]

    # Done?
    if t == 0:
        T = 1

    # Parse our rules
    elif x == 0:
        T = blink(1, t-1)

    elif len(str(x)) % 2 == 0:
        sx = str(x)
        left = int(sx[:len(sx)//2])
        right = int(sx[len(sx)//2:])
        T = blink(left, t-1) + blink(right, t-1)

    else:
        T = blink(x*2024, t-1)

    DP[(x, t)] = T
    return T


def parse_file(input, count=6):
    numbers = [int(x) for x in input.split()]
    return sum(blink(n, count) for n in numbers)


# Part 1

assert parse_file('0 1 10 99 999', 1) == 7
assert parse_file('125 17', 6) == 22
assert parse_file('125 17', 25) == 55312
print("Part 1: ", parse_file('0 7 6618216 26481 885 42 202642 8791', 25))

# Part 2
print("Part 2: ", parse_file('0 7 6618216 26481 885 42 202642 8791', 75))
