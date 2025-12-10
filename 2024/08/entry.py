#!/usr/bin/env python3

from itertools import combinations


def calc_antinodes(grid, node, p2=False):
    antinodes = set()

    antennas = [x for x in grid if grid[x] == node]
    dim = int(max(p.real for p in grid)) + 1

    combs = combinations(antennas, 2)
    for x, y in combs:

        # In p2 we calculate the line between the antennas and find all the points
        if p2:
            v = y - x

            # Start at x, move in the direction of y
            for i in range(0, dim):
                p = x + i * v
                if p in grid:
                    antinodes.add(p)
                else:
                    break

            # Start at x, move away from y
            for i in range(0, dim):
                p = x - i * v
                if p in grid:
                    antinodes.add(p)
                else:
                    break

        # In p1 we calculate only 2 points and see if they are in the grid
        else:
            a = 2 * x - y
            b = 2 * y - x

            if a in grid:
                antinodes.add(a)
            if b in grid:
                antinodes.add(b)

    return antinodes


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        grid = {
            x + 1j * y: c
            for y, l in enumerate(fp.read().splitlines())
            for x, c in enumerate(l.strip())
        }

    T = set()

    freqs = set([grid[x] for x in grid if grid[x] != "."])
    for freq in freqs:
        antinodes = calc_antinodes(grid, freq, p2)
        T.update(antinodes)

    return len(T)


# Part 1
assert parse_file("example.txt") == 14
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 34
assert parse_file("example2.txt", True) == 9
print("Part 2: ", parse_file("input.txt", True))
