#!/usr/bin/env python3

from collections import deque, defaultdict
from collections import Counter


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    splits = 0
    paths = Counter()

    for line in lines:
        for i, c in enumerate(line.strip()):
            match c:
                case "S":
                    paths[i] = 1
                case "^":
                    if i in paths:
                        splits += 1
                        paths[i - 1] += paths[i]
                        paths[i + 1] += paths[i]
                        del paths[i]

    if p2:
        return paths.total()
    else:
        return splits


# Part 1
assert parse_file("example.txt") == 21
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 40
print("Part 2: ", parse_file("input.txt", True))
