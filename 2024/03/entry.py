#!/usr/bin/env python3

import re


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        data = fp.read()

    T = 0
    if p2:
        DO = True
        matches = re.findall(r"(mul|do|don't)\(((\d+,\d+)*?)\)", data)
        for m in matches:
            if m[0] == "mul" and DO:
                a, b = m[1].split(",")
                T += int(a) * int(b)
            elif m[0] == "do":
                DO = True
            elif m[0] == "don't":
                DO = False
    else:
        matches = re.findall(r"mul\((\d+),(\d*)\)", data)
        T = sum([int(a) * int(b) for a, b in matches])

    return T


# Part 1
assert parse_file("example.txt") == 161
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example2.txt", True) == 48
print("Part 2: ", parse_file("input.txt", True))
