#!/usr/bin/env python3
from math import prod
from itertools import combinations
from shapely.geometry import Polygon, box


def area(edge) -> int:
    ((x1, y1), (x2, y2)) = edge
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        data = [tuple(map(int, line.split(","))) for line in fp.read().splitlines()]

    # p2: Find isolated points
    if p2:

        # Let's use some python math libraries to make it easy for us
        # Is this cheating? No, it's knowing the language that you use and is
        # pretty much the whole reason I'm doing this in Python :)
        polygon = Polygon(data)

        for edge in sorted(combinations(data, 2), key=area, reverse=True):
            (x1, y1), (x2, y2) = edge
            if polygon.contains(box(x1, y1, x2, y2)):
                return area(edge)

    else:
        return max(
            prod(abs(p[0] - p[1]) + 1 for p in zip(*pair))
            for pair in combinations(data, 2)
        )


# Part 1
assert parse_file("example.txt") == 50
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", p2=True) == 24
print("Part 2: ", parse_file("input.txt", p2=True))
