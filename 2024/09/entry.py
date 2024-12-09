#!/usr/bin/env python3

from itertools import combinations


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    T = 0
    return T


# Part 1
assert parse_file('example.txt') == 1928
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('example.txt', True) == 34
# print("Part 2: ", parse_file('input.txt', True))
