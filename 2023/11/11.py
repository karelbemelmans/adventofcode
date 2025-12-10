#!/usr/bin/env python3

from itertools import combinations


def parse_file(file, diff=2):

    with open(file, "r") as fp:
        grid = [[char for char in line] for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])

    # We build up a list of points. This works better than parsing a grid for this thing.
    S = set()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "#":
                S.add((r, c))

    # Find empty rows and columns
    ER = [r for r in range(R) if all(grid[r][c] == "." for c in range(C))]
    EC = [c for c in range(C) if all(grid[r][c] == "." for r in range(R))]

    # Add extra rows and columns
    #
    # Since we use a set, this comes down to just moving points by a factor
    # for every extra row / column we add. We end up with the same number of
    # points in our set, their coords just have been changed.
    #
    # If prefer this approach over making the distance calculation more complex.
    #
    for i, row in enumerate(ER):
        for (
            r,
            c,
        ) in [(r, c) for r, c in S if r > row + i * (diff - 1)]:
            S.remove((r, c))
            S.add((r + (diff - 1), c))

    for i, col in enumerate(EC):
        for (
            r,
            c,
        ) in [(r, c) for r, c in S if c > col + i * (diff - 1)]:
            S.remove((r, c))
            S.add((r, c + (diff - 1)))

    # Return the sum of distances between all combinations of 2 points
    return sum(
        map(
            lambda p: abs(p[0][0] - p[1][0]) + abs(p[1][1] - p[0][1]),
            combinations(S, 2),
        )
    )


# Part 1
assert parse_file("test.txt") == 374
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test.txt", 10) == 1030
assert parse_file("test.txt", 100) == 8410
print("Part 2: ", parse_file("input.txt", 1000000))
