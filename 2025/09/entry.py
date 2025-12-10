#!/usr/bin/env python3
import math
from itertools import product


# We need to add 1 to every dimensation because we need to include both "rows"
def surface(pair):
    return math.prod(abs(x - y) + 1 for x, y in zip(*pair))


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        nodes = [tuple(map(int, line.split(","))) for line in fp.read().splitlines()]

    squares = sorted(
        (p for p in product(nodes, nodes) if p[0] < p[1]), key=surface, reverse=True
    )

    return surface(squares[0])


# Part 1
assert parse_file("example.txt") == 50
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", p2=True) == 24
print("Part 2: ", parse_file("input.txt", p2=True))
