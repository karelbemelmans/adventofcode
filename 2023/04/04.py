#!/usr/bin/env python3

from collections import deque, defaultdict
import math


def score(i):
    if i < 2:
        return i
    else:
        return 2 * score(i-1)


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    S = 0
    C = {}

    # Parse cards
    for line in lines:
        card, data = line.split(': ')
        _, id = card.split()
        C[int(id)] = data

    # Process cards
    for id in C.keys():
        data = C[id]
        winners, numbers = data.split(' | ')

        W = set([int(x) for x in winners.split()])
        N = set([int(x) for x in numbers.split()])

        matches = len(N.intersection(W))
        S += score(matches)

    return S


# Part 1
assert parse_file('test.txt') == 13
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 30
# print("Part 2: ", parse_file('input.txt', True))
