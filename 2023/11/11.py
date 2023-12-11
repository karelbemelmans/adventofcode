#!/usr/bin/env python3

from collections import deque, defaultdict
from itertools import combinations


def print_points(text, G):
    print(text)

    r_min = min([r for r, c in G])
    r_max = max([r for r, c in G])
    c_min = min([c for r, c in G])
    c_max = max([c for r, c in G])

    for r in range(r_min, r_max+1):
        row = ''
        for c in range(c_min, c_max+1):
            if (r, c) in G:
                row += '#'
            else:
                row += '.'
        print(row)
    print("")


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])

    # We build up a list of points. This works better than parsing a grid for this thing.
    S = set()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                S.add((r, c))

    # Find empty rows and columns
    ER = [r for r in range(R) if all(grid[r][c] == '.' for c in range(C))]
    EC = [c for c in range(C) if all(grid[r][c] == '.' for r in range(R))]

    # Add extra rows
    # Remember the offset when we select the old rows (+i)
    for i, row in enumerate(ER):
        R += 1
        for r, c, in [(r, c) for r, c in S if r > row+i]:
            S.remove((r, c))
            S.add((r+1, c))

    # Add extra columns
    for i, col in enumerate(EC):
        C += 1
        for r, c, in [(r, c) for r, c in S if c > col+i]:
            S.remove((r, c))
            S.add((r, c+1))

    # Does it look good at this point?
    print_points("Larger grid", S)

    # At this point we have S that contains all our points
    T = 0
    for a, b in combinations(S, 2):
        T += abs(a[0] - b[0]) + abs(a[1] - b[1])

    return T


# Part 1
assert parse_file('test.txt') == 374
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
