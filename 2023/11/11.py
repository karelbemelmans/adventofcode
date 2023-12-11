#!/usr/bin/env python3

from itertools import combinations


def parse_file(file, diff=2):

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
    for i, row in enumerate(ER):
        for r, c, in [(r, c) for r, c in S if r > row+i*(diff-1)]:
            S.remove((r, c))
            S.add((r+(diff-1), c))

    # Add extra columns
    for i, col in enumerate(EC):
        for r, c, in [(r, c) for r, c in S if c > col+i*(diff-1)]:
            S.remove((r, c))
            S.add((r, c+(diff-1)))

    T = 0
    C = combinations(S, 2)
    for a, b in C:
        t = abs(a[0] - b[0]) + abs(a[1] - b[1])
        T += t

    return T


# Part 1
assert parse_file('test.txt') == 374
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', 10) == 1030
assert parse_file('test.txt', 100) == 8410
print("Part 2: ", parse_file('input.txt', 1000000))
