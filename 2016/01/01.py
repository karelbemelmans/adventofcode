#!/usr/bin/env python3

from collections import deque, defaultdict


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        cmds = [cmd for cmd in fp.read().split(", ")]

    # Our grid:
    # r,c (rows, columns)
    # 0,0 is top left

    d = (-1, 0)
    p = (0, 0)
    V = set(p)

    for cmd in cmds:
        if cmd[0] == 'R':
            d = (d[1], -d[0])
        else:
            d = (-d[1], d[0])

        steps = int(cmd[1:])
        for i in range(steps):
            if p in V and p2:
                return abs(p[0]) + abs(p[1])
            V.add(p)
            p = (p[0] + d[0], p[1] + d[1])

    return abs(p[0]) + abs(p[1])


# Part 1
assert parse_file('test.txt') == 12
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test2.txt', True) == 4
print("Part 2: ", parse_file('input.txt', True))
