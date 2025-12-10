#!/usr/bin/env python3

from collections import deque

OUT = set()
IN = set()


def reaches_outside(P, x, y, z, p2=False):
    if (x, y, z) in OUT:
        return True
    if (x, y, z) in IN:
        return False
    SEEN = set()
    Q = deque([(x, y, z)])
    while Q:
        x, y, z = Q.popleft()
        if (x, y, z) in P:
            continue
        if (x, y, z) in SEEN:
            continue
        SEEN.add((x, y, z))
        if len(SEEN) > (5000 if p2 else 0):
            for p in SEEN:
                OUT.add(p)
            return True
        Q.append((x + 1, y, z))
        Q.append((x - 1, y, z))
        Q.append((x, y + 1, z))
        Q.append((x, y - 1, z))
        Q.append((x, y, z + 1))
        Q.append((x, y, z - 1))
    for p in SEEN:
        IN.add(p)
    return False


def solve(P, p2=False):
    OUT.clear()
    IN.clear()
    ans = 0
    for x, y, z in P:
        if reaches_outside(P, x + 1, y, z, p2):
            ans += 1
        if reaches_outside(P, x - 1, y, z, p2):
            ans += 1
        if reaches_outside(P, x, y + 1, z, p2):
            ans += 1
        if reaches_outside(P, x, y - 1, z, p2):
            ans += 1
        if reaches_outside(P, x, y, z + 1, p2):
            ans += 1
        if reaches_outside(P, x, y, z - 1, p2):
            ans += 1
    return ans


def parse_file(file, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    # Cubes
    P = set()
    for line in lines:
        x, y, z = line.split(",")
        x, y, z = int(x), int(y), int(z)
        P.add((x, y, z))

    if p2:
        return solve(P, True)
    else:
        return solve(P)


# Part 1
assert parse_file("test.txt") == 64
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 58
print("Part 2: ", parse_file("input.txt", True))
