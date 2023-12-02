#!/usr/bin/env python3

import re

from itertools import permutations
from collections import defaultdict


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    cities = set()
    distances = defaultdict(int)

    # Parse the input
    for line in lines:
        m = re.match(r"(.*) to (.*) = (\d*)$", line)
        if m:
            A = m.group(1)
            B = m.group(2)
            l = int(m.group(3))

            cities.add(A)
            cities.add(B)

            distances[(A, B)] = l

    # Permutations, beause why not?
    T = float("inf")
    for p in permutations(cities):
        l = 0

        i = 0
        while i < len(p)-1:
            if distances[p[i], p[i+1]]:
                l += distances[p[i], p[i+1]]
            else:
                l += distances[p[i+1], p[i]]
            i += 1

        T = min(T, l)

    return T


# Part 1
assert parse_file('test.txt') == 605
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
