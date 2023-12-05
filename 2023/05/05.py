#!/usr/bin/env python3

from collections import deque, defaultdict

ORDER = ['soil', 'fertilizer', 'water',
         'light', 'temperature', 'humidity', 'location']


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        blocks = [block for block in fp.read().split("\n\n")]

    seeds = [int(x) for x in blocks[0].split(": ")[1].split()]

    # Parse the input information
    X = defaultdict(list)
    for i, block in enumerate(blocks[1:]):
        for j, line in enumerate(block.splitlines()):
            if j > 0:
                dest, src, l = [int(x) for x in line.split(" ")]
                X[ORDER[i]].append((dest, src, l))

    # Find the locations for every seed
    L = float("inf")
    for seed in seeds:
        x = seed
        for order in ORDER:
            table = X[order]

            for t in table:
                if t[1] <= x < t[1]+t[2]:
                    x = t[0] + (x - t[1])
                    break

            # If not, x remains the same

        L = min(L, x)

    return L


# Part 1
assert parse_file('test.txt') == 35
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
