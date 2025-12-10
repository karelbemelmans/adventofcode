#!/usr/bin/env python3
import json
from collections import deque
from functools import cmp_to_key


# Exit codes:
#   -1 is done, with success
#    0 is continue
#    1 is done, with fail
def compare(a, b):
    # We start looking until we have a case where we need to return False

    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

        # In other cases we continue

    elif isinstance(a, list) and isinstance(b, list):
        L = min(len(a), len(b))
        for i in range(L):
            c = compare(a[i], b[i])
            if c == -1:
                return -1
            elif c == 1:
                return 1

        if len(a[L:]) == 0 and len(b[L:]) > 0:
            return -1

        elif len(b[L:]) == 0 and len(a[L:]) > 0:
            return 1

        # We continue
        else:
            return 0

    elif isinstance(a, int) and not isinstance(b, int):
        return compare([a], b)

    elif not isinstance(a, int) and isinstance(b, int):
        return compare(a, [b])


def parse_file(file, p2=False):

    if p2:
        with open(file, "r") as fp:
            data = [x.strip() for x in fp.read().splitlines()]

        # We can do this better...
        lines = []
        for line in data:
            if not line == "":
                lines.append(json.loads(line))

        # Add our markers
        lines.append([[2]])
        lines.append([[6]])

        # Some good old python library magic
        lines = sorted(lines, key=cmp_to_key(lambda p1, p2: compare(p1, p2)))

        # Find markers
        result = 1
        for i, p in enumerate(lines):
            if p == [[2]] or p == [[6]]:
                result *= i + 1

        return result

    else:
        with open(file, "r") as fp:
            pairs = [[y for y in x.split("\n")] for x in fp.read().split("\n\n")]

        result = 0
        for i, pair in enumerate(pairs):
            left, right = pair

            dl = json.loads(left)
            dr = json.loads(right)

            r = compare(dl, dr)
            if r == -1:
                result += i + 1

        return result


# Part 1
assert parse_file("test.txt") == 13
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 140
print("Part 2: ", parse_file("input.txt", True))
