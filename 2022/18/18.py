#!/usr/bin/env python3

from collections import defaultdict
from functools import reduce


def parse(dice, p2=False):
    S = defaultdict(int)

    # Build up our dict of dice and how much sides they have exposed
    # We start with every dice have 6 sides exposed
    for d in dice:
        S[(d[0], d[1], d[2])] = 6

    DIR = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for d in dice:

        # Look at neighbours in 1 directions
        for (x, y, z) in DIR:
            xx = d[0] + x
            yy = d[1] + y
            zz = d[2] + z

            # Is there a dice on this side? Then we reduce our counter
            if (xx, yy, zz) in S:
                S[(d[0], d[1], d[2])] -= 1

    return reduce(lambda a, b: a+b, S.values())


def parse_file(file, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, 'r') as fp:
        dice = [
            [int(part) for part in line.strip().split(",")]
            for line in fp.readlines()
        ]

    return parse(dice)


# Part 1
assert parse_file('test.txt') == 64
print("Part 1: ", parse_file('input.txt'))

# assert parse_file('test.txt', True) == 1514285714288
# print("Part 2: ", parse_file('input.txt', True))
