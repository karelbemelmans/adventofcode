#!/usr/bin/env python3

from collections import deque, defaultdict


def find_reflections(grid, p2=False):

    R = len(grid)
    C = len(grid[0])

    # Columns
    for c in range(1, C):
        l = min(c, C-c)

        errors = 0
        for r in range(R):
            for i in range(0, l):
                cl = c-1-i
                cr = c+i
                if not grid[r][cl] == grid[r][cr]:
                    errors += 1

        if p2:
            if errors == 1:
                return c
        elif errors == 0:
            return c

    # Row
    for r in range(1, R):
        l = min(r, R-r)

        errors = 0
        for c in range(C):
            for i in range(0, l):
                rl = r-1-i
                rr = r+i
                if not grid[rl][c] == grid[rr][c]:
                    errors += 1

        if p2:
            if errors == 1:
                return r * 100
        elif errors == 0:
            return r * 100

    return 0


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        blocks = [block for block in fp.read().split("\n\n")]

    # Reflected columns and rows counter
    T = 0
    for block in blocks:
        grid = [[char for char in line] for line in block.splitlines()]

        # Find reflected columns
        T += find_reflections(grid, p2)

    return T


# Part 1
assert parse_file('test.txt') == 5
assert parse_file('test2.txt') == 400
assert parse_file('test3.txt') == 405
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 300
assert parse_file('test2.txt', True) == 100
assert parse_file('test3.txt', True) == 400
print("Part 2: ", parse_file('input.txt', True))
