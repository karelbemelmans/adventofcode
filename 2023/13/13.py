#!/usr/bin/env python3

from collections import deque, defaultdict


def find_reflections(grid):
    print(grid)

    R = len(grid)
    C = len(grid[0])
    print(R, C)

    # Columns
    print("Checking columns")
    for c in range(1, C):

        # Length of the reflection, decided by the column
        l = min(c, C-c)
        print("Column", c, l)

        mirror = True
        for r in range(R):
            print("Row: ", r)

            for i in range(0, l):
                cl = c-1-i
                cr = c+i
                print(r, cl, r, cr, grid[r][cl], grid[r][cr])
                if not grid[r][cl] == grid[r][cr]:
                    mirror = False
                    break

        if mirror:
            return c

    # Row
    print("Checking rows")
    for r in range(1, R):

        # Length of the reflection, decided by the column
        l = min(r, R-r)
        print("Row", r, l)

        mirror = True
        for c in range(C):
            print("Column: ", c)

            for i in range(0, l):
                rl = r-1-i
                rr = r+i
                if not grid[rl][c] == grid[rr][c]:
                    mirror = False
                    break

        if mirror:
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
        T += find_reflections(grid)

    # To summarize your pattern notes, add up the number of columns to the left
    # of each vertical line of reflection; to that, also add 100 multiplied by
    # the number of rows above each horizontal line of reflection.
    print("Score: ", T)
    return T


# Part 1
assert parse_file('test.txt') == 5
assert parse_file('test2.txt') == 400
assert parse_file('test3.txt') == 405
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
