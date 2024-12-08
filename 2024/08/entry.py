#!/usr/bin/env python3

from itertools import product, combinations
from collections import deque


def calc_antinodes(grid, node, p2=False):
    antinodes = set()

    # Find all the antennas with the same frequency
    antennas = [x for x in grid if grid[x] == node]

    # Maximum dimension of the grid
    dim = int(max(p.real for p in grid)) + 1

    # We need more than 1 antenna to calculate antinodes
    if len(antennas) <= 1:
        return antinodes

    # Pair up antennas and calculate the antinodes:
    combs = combinations(antennas, 2)
    for x, y in combs:

        # In p2 we calculate the line between the antennas and find all the points
        if p2:

            # Vector of the direction between the antennas
            v = y - x

            # Start at x, move in the direction of y
            for i in range(0, dim):
                p = x + i*v
                if p in grid:
                    antinodes.add(p)
                else:
                    break

            # Start at x, move away from y
            for i in range(0, dim):
                p = x - i*v
                if p in grid:
                    antinodes.add(p)
                else:
                    break

        # In p1 we calculate only 2 points and see if they are in the grid
        else:
            # Simple math to calculate the antinodes
            a = 2*x - y
            b = 2*y - x

            if a in grid:
                antinodes.add(a)
            if b in grid:
                antinodes.add(b)

    return antinodes


def parse_file(file, p2=False):

    # Let's do this one with complex numbers as in 2023 day 23
    # Seeing how we need to do distance calculations that should make it very easy for us...
    with open(file, 'r') as fp:
        grid = {x+1j*y: c for y, l in enumerate(fp.read().splitlines()) for x, c in enumerate(l.strip())}

    # Unique coordinates of the antinodes
    T = set()

    freqs = set([grid[x] for x in grid if grid[x] != '.'])
    for freq in freqs:
        antinodes = calc_antinodes(grid, freq, p2)
        T.update(antinodes)

    return len(T)


# Part 1
assert parse_file('example.txt') == 14
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 34
print("Part 2: ", parse_file('input.txt', True))
