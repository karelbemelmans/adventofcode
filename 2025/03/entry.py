#!/usr/bin/env python3


def find_highest_number(s):
    # Find the highest number in the list
    m = 0
    pos = None
    for i, b in enumerate(s):
        if int(b) > m:
            m = int(b)
            pos = i

    return m, pos


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        banks = [line for line in fp.read().splitlines()]

    T = 0

    for bank in banks:
        m, pos = find_highest_number(bank)

        # Find the other C-1 numbers
        # Find the highest number right of it
        if pos == len(bank) - 1:
            sub = bank[0:pos]
            n, _ = find_highest_number(sub)
            res = n * 10 + m

        # Find the highest number left of it
        else:
            sub = bank[pos + 1 :]
            n, _ = find_highest_number(sub)
            res = m * 10 + n

        T += res

    return T


# Part 1
assert parse_file("example.txt") == 357
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 3121910778619
print("Part 2: ", parse_file("input.txt", True))
