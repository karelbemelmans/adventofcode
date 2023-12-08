#!/usr/bin/env python3

import numpy as np


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        instructions, lines = [line for line in fp.read().split("\n\n")]

    P = {}
    for line in lines.splitlines():
        a, b = line.split(' = ')
        # Ugly, but it works since our input is all 3 char strings...
        P[a] = (b[1:4], b[6:9])

    # Find our start nodes
    S = [x for x in P if x[2] == 'A'] if p2 else ['AAA']

    # A list of how many steps it took for every start node to reach the end
    L = []

    for node in S:
        cur = node

        i = 0
        while True:
            dir = instructions[i % len(instructions)]
            cur = P[cur][0 if dir == 'L' else 1]

            if (p2 and cur[2] == 'Z') or cur == 'ZZZ':
                L.append(i+1)
                break

            i += 1

    # least common multiple
    S = np.lcm.reduce(L)
    return S


# Part 1
assert parse_file('test.txt') == 2
assert parse_file('test2.txt') == 6
print("Part 1: ", parse_file('input.txt'))


# Part 2
assert parse_file('test3.txt', True) == 6
print("Part 2: ", parse_file('input.txt', True))
