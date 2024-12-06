#!/usr/bin/env python3

from itertools import combinations


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])
    cur = None
    visited = set()
    blockers = set()

    # TODO: This is a bit ugly
    rotations = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find the guard
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '^':
                cur = ((r, c), (-1, 0))
                visited.add((r, c))
                break

    while True:
        # Do a next step
        rr, cc = cur[0][0] + cur[1][0], cur[0][1] + cur[1][1]

        # Out of bounds? Then we are done
        if rr < 0 or rr >= R or cc < 0 or cc >= C:
            break

        # Turning point?
        elif grid[rr][cc] == '#':
            cur = (cur[0], rotations[(rotations.index(cur[1]) + 1) % 4])

        else:
            visited.add((rr, cc))
            cur = ((rr, cc), cur[1])

    if p2:
        return len(blockers)
    else:
        return len(visited)


# Part 1
assert parse_file('example.txt') == 41
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 6
# print("Part 2: ", parse_file('input.txt', True))
