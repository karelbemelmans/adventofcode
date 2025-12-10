#!/usr/bin/env python3
import re


# Is this point covered by a sensor in our list?
def valid(x, y, S):
    for sx, sy, d in S:
        dxy = abs(x - sx) + abs(y - sy)
        if dxy <= d:
            return False
    return True


def parse_lines(lines, n, p2=False):

    S = set()
    B = set()

    # Build up our list of sensors and beacons
    # We store the hamming distance with the sensor
    for line in lines:
        matches = re.match(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$",
            line,
        )
        if matches:
            s = (int(matches.group(1)), int(matches.group(2)))
            b = (int(matches.group(3)), int(matches.group(4)))
            h = abs(s[0] - b[0]) + abs(s[1] - b[1])

            S.add((s[0], s[1], h))
            B.add((b[0], b[1]))

    if p2:
        # Theory from reddit:
        #
        # - If there is only one possible position for another beacon, it must be distance d+1 from some beacon
        # - If not, we could find an adjacent position that is possible.
        for sx, sy, d in S:

            # check all points that are d+1 away from (sx,sy):
            # - we loop over dx
            # - adjust dy so that distance is always d+1
            for dx in range(d + 2):
                dy = (d + 1) - dx
                for signx, signy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    x = sx + (dx * signx)
                    y = sy + (dy * signy)
                    if not (0 <= x <= n and 0 <= y <= n):
                        continue
                    assert abs(x - sx) + abs(y - sy) == d + 1
                    if valid(x, y, S):
                        return x * 4000000 + y

    else:
        total = 0
        for x in range(-int(1e7), int(1e7)):
            if not valid(x, n, S) and (x, n) not in B:
                total += 1
        return total


def parse_file(file, y, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, "r") as fp:
        lines = [x for x in fp.read().splitlines()]

    return parse_lines(lines, y, p2)


# Part 1
assert parse_file("test.txt", 10) == 26
print("Part 1: ", parse_file("input.txt", 2000000))

assert parse_file("test.txt", 20, True) == 56000011
print("Part 2: ", parse_file("input.txt", 4000000, True))
