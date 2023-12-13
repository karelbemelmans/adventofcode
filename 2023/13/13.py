#!/usr/bin/env python3

def find_reflections(grid, p2=False):

    R = len(grid)
    C = len(grid[0])

    # We look for mirrors in the vertical side first, so loop over columns
    # Our "pointer" is called c and means the place between column c-1 and c
    # So we can start our range at 1, skipping the first column, and go on to the last one
    for c in range(1, C):

        # The discrepancy between our column and the edge of the grid can be at most l
        l = min(c, C-c)

        # We keep a counter for all the errors we get, meaning the times a char
        # at position r,c is not the same as the one at r,C-c
        errors = 0

        # We scan per row, from top to bottom, going over all rows
        for r in range(R):

            # We check the left and right side of the column, with an increasing
            # offset that goes from 0 to l
            for i in range(l):

                # The coords of the mirror character
                cl = c-1-i
                cr = c+i

                # If it's not the same, we add an error and continue anyway
                if not grid[r][cl] == grid[r][cr]:
                    errors += 1

        # The result is now the column that has either 0 or 1 errors
        if errors == (1 if p2 else 0):
            return c

    # Rows. Same as above, but we loop over rows and scan columns
    for r in range(1, R):
        l = min(r, R-r)

        errors = 0
        for c in range(C):
            for i in range(l):
                rl = r-1-i
                rr = r+i
                if not grid[rl][c] == grid[rr][c]:
                    errors += 1

        if errors == (1 if p2 else 0):
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
