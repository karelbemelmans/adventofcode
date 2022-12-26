#!/usr/bin/env python3

from collections import deque, defaultdict


def parse_file(file, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]


# Part 1
assert parse_file('test.txt') == x
print("Part 1: ", parse_file('input.txt'))

# assert parse_file('test.txt', True) == 58
# print("Part 2: ", parse_file('input.txt', True))
