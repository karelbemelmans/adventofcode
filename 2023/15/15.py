#!/usr/bin/env python3

from collections import deque, defaultdict


def do_hash(str):
    cur = 0

    for char in str:
        cur += ord(char)
        cur *= 17
        cur %= 256

    return cur


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        pieces = [line for line in fp.read().splitlines()][0].split(",")

    cur = 0

    for p in pieces:
        cur += do_hash(p)

    print("Score:", cur)
    return cur


# Part 1
assert parse_file('hash.txt') == 52
assert parse_file('test.txt') == 1320
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
