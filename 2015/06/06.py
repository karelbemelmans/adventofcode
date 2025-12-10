#!/usr/bin/env python3

from collections import deque, defaultdict
from functools import reduce


def parse(lines, p2=False):

    G = defaultdict(int)

    for line in lines:
        words = line.split(" ")

        if words[0] == "turn":
            m = words[1]
            r1, c1 = words[2].split(",")
            r2, c2 = words[4].split(",")

        elif words[0] == "toggle":
            m = words[0]
            r1, c1 = words[1].split(",")
            r2, c2 = words[3].split(",")

        r1 = int(r1)
        c1 = int(c1)
        r2 = int(r2)
        c2 = int(c2)

        assert r2 >= r1
        assert c2 >= c1

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):

                # Turn on if not on already
                if m == "on":
                    if p2:
                        G[(r, c)] += 1
                    else:
                        G[(r, c)] = 1

                # Turn off if it was on
                elif m == "off":
                    if p2:
                        G[(r, c)] = max(0, G[(r, c)] - 1)
                    else:
                        G[(r, c)] = 0

                # Toggle
                else:
                    if p2:
                        G[(r, c)] += 2
                    else:
                        G[(r, c)] = (G[(r, c)] + 1) % 2

    # Return the number of lights we have on
    r = reduce(lambda a, b: a + b, G.values())
    return r


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    return parse(lines, p2)


# Part 1
assert parse_file("test.txt") == 1000000
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test4.txt", True) == 1
assert parse_file("test5.txt", True) == 2000000
print("Part 2: ", parse_file("input.txt", True))
