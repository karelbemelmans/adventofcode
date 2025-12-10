#!/usr/bin/env python3

from itertools import product
from collections import deque


def match(numbers, total):
    Q = deque(numbers)
    T = Q.popleft()

    while Q:
        # Did we already overshoot our target?
        if T > total:
            return False

        op = Q.popleft()
        x = Q.popleft()

        match op:
            case "+":
                T += x
            case "*":
                T *= x
            case "||":
                T = int(f"%d%d" % (T, x))

    return T == total


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    # Gotta do it all in one line!
    pairs = [
        (int(a), [int(x) for x in b.split()])
        for a, b in (line.strip().split(":") for line in lines)
    ]

    if p2:
        operators = ["+", "*", "||"]
    else:
        operators = ["+", "*"]

    T = 0
    for total, numbers in pairs:

        # All possible combintations of operators for a list of numbers of this length
        for ops in product(operators, repeat=len(numbers) - 1):

            # We merge both the numbers and operators list into one list.
            # This could potentially blow up but it's fine for this problem.

            merged = sum(zip(numbers, list(ops) + [0]), ())[:-1]
            if match(merged, total):
                T += total
                break

    return T


# Part 1
assert parse_file("example.txt") == 3749
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 11387
print("Part 2: ", parse_file("input.txt", True))
