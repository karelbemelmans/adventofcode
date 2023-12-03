#!/usr/bin/env python3

from collections import deque, defaultdict


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        G = [[char for char in line]
             for line in fp.read().splitlines()]

    S = 0

    # Locations of all the gears we meet and the numbers that touched it
    # At the end we will filter our only the gears that touched with exactly 2 numbers
    T = defaultdict(list)

    R = len(G)
    C = len(G[0])

    for r in range(R):
        current = ""
        valid = False
        gear_location = None

        for c in range(C):
            char = G[r][c]

            if char.isnumeric():
                current += char

                # Check if this digit is valid
                for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1)]:
                    rr = r + x
                    cc = c + y
                    if (0 <= rr < R) and (0 <= cc < C):

                        # Anything NOT a point or a digit is considered a valid char
                        if not G[rr][cc] == "." and not G[rr][cc].isdigit():
                            valid = True

                        # Is this a gear location? Then we need to save that
                        if G[rr][cc] == "*":
                            gear_location = (rr, cc)

            # We move on to the next digit
            else:
                if valid:
                    S += int(current)
                if gear_location:
                    T[gear_location].append(int(current))
                current = ""
                valid = False
                gear_location = None

        # If the number was hitting the last point on a line
        # TODO: Fix this into the main loop
        if current:
            if valid:
                S += int(current)
            if gear_location:
                T[gear_location].append(int(current))
            current = ""
            valid = False
            gear_location = None

    if p2:
        S = 0
        for t in T:
            if len(T[t]) == 2:
                S += T[t][0] * T[t][1]

    return S


# Part 1
assert parse_file('test.txt') == 4361
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 467835
print("Part 2: ", parse_file('input.txt', True))
