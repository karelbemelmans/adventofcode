#!/usr/bin/env python3

from collections import deque, defaultdict
import re


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    total = 0
    for line in lines:

        if p2:
            # We don't need to encode, just count how much extra chars doing
            # the encoding would give us.
            # 2 fixed for the other quotes
            # then one per occurrence of \ and "
            total += 2+line.count('\\')+line.count('"')
        else:
            parsed = eval(line)
            total += abs(len(line) - len(parsed))

    return total


# Part 1
assert parse_file('test.txt') == 12
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 19
print("Part 2: ", parse_file('input.txt', True))
