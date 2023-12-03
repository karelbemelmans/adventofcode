#!/usr/bin/env python3

from collections import deque, defaultdict
from functools import reduce


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        G = [[char for char in line]
             for line in fp.read().splitlines()]

    T = []
    R = len(G)
    C = len(G[0])

    for r in range(R):
        current = ""
        valid = False

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
                            break

            # We move on to the next digit
            else:
                if valid:
                    T.append(int(current))
                current = ""
                valid = False

        # If the number was hitting the last point on a line
        if valid and current:
            T.append(int(current))
            current = ""
            valid = False

    S = reduce(lambda a, b: a+b, T)
    return S


# Part 1
assert parse_file('test.txt') == 4361
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
