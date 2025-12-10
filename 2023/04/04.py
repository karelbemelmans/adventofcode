#!/usr/bin/env python3

from collections import deque, defaultdict
import math


def score(i):
    if i == 0:
        return 0
    else:
        return 2 ** (i - 1)


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    S = 0

    # Amount of times we've processed a card
    T = defaultdict(int)

    # Process cards
    for i, line in enumerate(lines):

        T[i] += 1

        card, data = line.split(": ")
        winners, numbers = data.split(" | ")

        W = [int(x) for x in winners.split()]
        N = [int(x) for x in numbers.split()]

        matches = len(set(W) & set(N))
        S += score(matches)

        for j in range(matches):
            T[i + 1 + j] += T[i]

    if p2:
        return sum(T.values())
    else:
        return S


# Part 1
assert parse_file("test.txt") == 13
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test.txt", True) == 30
print("Part 2: ", parse_file("input.txt", True))
