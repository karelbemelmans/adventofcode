#!/usr/bin/env python3

from collections import deque, defaultdict

ORDER = ['soil', 'fertilizer', 'water',
         'light', 'temperature', 'humidity', 'location']


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        blocks = [block for block in fp.read().split("\n\n")]

    S = [int(x) for x in blocks[0].split(": ")[1].split()]

    # Find the locations for every seed
    L = float("inf")

    for seed in S:
        for block in blocks[1:]:
            for line in block.splitlines()[1:]:
                dest, src, l = [int(x) for x in line.split(" ")]

                d = seed - src
                if d in range(l):
                    seed = dest + d
                    break

                # If not, seed remains the same

        L = min(L, seed)

    return L


# Part 1
assert parse_file('test.txt') == 35
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 46
# print("Part 2: ", parse_file('input.txt', True))
