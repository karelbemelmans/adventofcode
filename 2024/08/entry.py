#!/usr/bin/env python3

from itertools import product, combinations
from collections import deque


def print_grid(grid):
    dim = int(max(p.real for p in grid)) + 1

    for y in range(dim):
        print(''.join(grid[x+1j*y] for x in range(dim)))


def calc_antinodes(grid, node):
    antinodes = set()

    # Find all the antennas with the same frequency
    antennas = [x for x in grid if grid[x] == node]

    # We need more than 1 antenna to calculate antinodes
    if len(antennas) <= 1:
        return antinodes

    # Pair up antennas and calculate the antinodes:
    #
    #  In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency
    #  - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas
    #  with the same frequency, there are two antinodes, one on either side of them.

    combs = combinations(antennas, 2)
    for x, y in combs:

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
    with open(file, 'r') as fp:
        grid = {x+1j*y: c for y, l in enumerate(fp.read().splitlines()) for x, c in enumerate(l.strip())}

    # Will contain coordinates of the antennas
    T = set()

    # Get the unique antennas in the grid
    # Loop over them and calculate the antinodes

    unique = set([grid[x] for x in grid if grid[x] != '.'])
    for a in unique:
        nodes = calc_antinodes(grid, a)
        T.update(nodes)

    print("Total antinodes: ", len(T))
    return len(T)


# Part 1
assert parse_file('example.txt') == 14
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('example.txt', True) == 11387
# print("Part 2: ", parse_file('input.txt', True))
