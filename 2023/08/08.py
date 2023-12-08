#!/usr/bin/env python3

from collections import deque, defaultdict


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        instructions, lines = [line for line in fp.read().split("\n\n")]

    P = {}
    for line in lines.splitlines():
        a, b = line.split(' = ')
        P[a] = (b[1:4], b[6:9])

    print("instructions", instructions, len(instructions))
    print("P", P)

    cur = "AAA"
    end = "ZZZ"

    i = 0
    while True and i < 100000:
        print("step: ", i)
        print("- cur: ", cur)
        dir = instructions[i % len(instructions)]
        print("- dir: ", dir)

        cur = P[cur][0 if dir == 'L' else 1]
        print("- new: ", cur)
        if cur == end:
            return i + 1

        # Make sure we rotate around
        i += 1


# Part 1
assert parse_file('test.txt') == 2
assert parse_file('test2.txt') == 6
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
