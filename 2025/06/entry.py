#!/usr/bin/env python3
from functools import reduce


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        rows = [x for x in [line.split() for line in fp.read().splitlines()]]

    # Last row is the operators
    operators = rows.pop()

    # Swap columns and rows
    numbers = list(zip(*rows))

    if p2:
        print(numbers)

    # Reduce the rows with the correct operator
    T = 0
    for i, n in enumerate(numbers):
        n = map(int, n)
        if operators[i] == "+":
            T += reduce(lambda x, y: x + y, n)
        else:
            T += reduce(lambda x, y: x * y, n)

    return T


# Part 1
assert parse_file("example.txt") == 4277556
print("Part 1: ", parse_file("input.txt"))
