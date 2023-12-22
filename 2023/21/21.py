#!/usr/bin/env python3
#
# Inspiration from the whole Reddit thread about quadratic numbers
#
# Final solution comes from:
# - https://github.com/WinslowJosiah/adventofcode/blob/main/aoc2023/day21/__init__.py
# - https://github.com/mebeim/aoc/blob/master/2023/original_solutions/day21.py

import sys
from collections import deque, defaultdict
from math import ceil


def count_paths(start, R, C, steps, S):

    T = 0
    visited = set()
    Q = deque([(0, start)])

    while Q:

        cost, node = Q.popleft()

        # Already visited before? Continue
        if node in visited:
            continue

        # Add node to our list
        visited.add(node)

        # If the current path's parity is the same as the parity of the specified path length
        if cost % 2 == steps % 2:

            # This path can be reached in the specified number of steps
            #  We can do this because all paths between any two tiles will have the same parity.
            T += 1

        # Don't explore further if path becomes longer than specified path length
        if cost >= steps:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = node[0] + dr
            nc = node[1] + dc

            # If this neighbor is not a wall
            if (nr % R, nc % C) in S:
                continue

            # Append this neighbor to the queue
            Q.append((cost + 1, (nr, nc)))

    return T


def parse_file(file, steps=6, p2=False):

    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])

    # We build up a list of points. This works better than parsing a grid for this thing.
    S = set()
    start = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                S.add((r, c))
            if grid[r][c] == 'S':
                start = (r, c)

    T = 0
    if p2:

        # Make sure our assumption of a middle point is right
        assert start is not (R//2, C//2)
        assert C == R

        n = steps // C
        a, b, c = (
            count_paths(start, R, C, s * C + (C // 2), S)
            for s in range(3)
        )

        T = a + n * (b - a + (n - 1) * (c - b - b + a) // 2)

    else:
        T = count_paths(start, R, C, steps, S)

    return T


def main():

    # Part 1
    assert parse_file('test.txt', 6) == 16
    assert parse_file('test.txt', 50) == 1594
    assert parse_file('test.txt', 100) == 6536
    print("Part 1: ", parse_file('input.txt', 64))

    # Part 2
    # The formula for p2 only works for this specific input number
    # because it's a quadratic number sequence
    #
    # See: https://www.radfordmathematics.com/algebra/sequences-series/difference-method-sequences/quadratic-sequences.html
    #
    print("Part 2: ", parse_file('input.txt', 26501365, True))


if __name__ == "__main__":
    sys.exit(main())
