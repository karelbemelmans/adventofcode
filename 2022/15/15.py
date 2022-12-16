#!/usr/bin/env python3
import re


def print_grid(G):
    e = 10

    # Calculate the bounds of our grid
    R_0 = min([r for r, c in G]) - e
    R_1 = max([r for r, c in G]) + e
    C_0 = min([c for r, c in G]) - e
    C_1 = max([c for r, c in G]) + e

    print(R_0, R_1, C_0, C_1)

    for c in range(C_0, C_1):
        for r in range(R_0, R_1):
            if (r, c) in G:
                print("x", end="")
            else:
                print(".", end="")
        print("")


# Is this point covered by a sensor in our list?
def valid(x, y, S):
    for (sx, sy, d) in S:
        dxy = abs(x-sx)+abs(y-sy)
        if dxy <= d:
            return False
    return True


def parse_lines(lines, y,  p2=False):

    S = set()
    B = set()

    # Build up our list of sensors and beacons
    # We store the hamming distance with the sensor
    for line in lines:
        matches = re.match(
            r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$', line)
        if matches:
            s = (int(matches.group(1)), int(matches.group(2)))
            b = (int(matches.group(3)), int(matches.group(4)))
            h = abs(s[0]-b[0]) + abs(s[1]-b[1])

            S.add((s[0], s[1], h))
            B.add((b[0], b[1]))

    total = 0
    for x in range(-int(1e7), int(1e7)):
        if not valid(x, y, S) and (x, y) not in B:
            total += 1

    return total


def parse_file(file, y, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    return parse_lines(lines, y, p2)


# Part 1
assert parse_file('test.txt', 10) == 26
print("Part 1: ", parse_file('input.txt', 2000000))

# assert parse_file('test.txt', True) == 56000011
# print("Part 2: ", parse_file('input.txt', True))
