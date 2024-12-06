#!/usr/bin/env python3

import copy


def walk(G, start, p2=False):
    visited = set()
    visited_dir = set()

    visited.add(start[0])
    visited_dir.add(start)

    R = len(G)
    C = len(G[0])
    cur = start

    rotations = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    k = 0
    while True and k < 10000:
        k += 1

        # Do a next step
        rr, cc = cur[0][0] + cur[1][0], cur[0][1] + cur[1][1]

        # Out of bounds? Then we are done
        if rr < 0 or rr >= R or cc < 0 or cc >= C:
            break

        # Turning point?
        elif G[rr][cc] == '#':
            cur = (cur[0], rotations[(rotations.index(cur[1]) + 1) % 4])

        # We are ok to step forward
        else:
            # Are we on a loop? Then we are done for p2.
            if p2 and ((rr, cc), cur[1]) in visited_dir:
                return p2, True

            visited.add((rr, cc))
            visited_dir.add(((rr, cc), cur[1]))

            # Set new curser
            cur = ((rr, cc), cur[1])

    if p2:
        return p2, False
    else:
        return p2, visited


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    start = None

    R = len(grid)
    C = len(grid[0])

    # Find the guard
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '^':
                start = ((r, c), (-1, 0))
                break

    _, path = walk(grid, start)

    # p1 we return the length of the path
    if not p2:
        return len(path)

    if p2:
        T = 0

        # This is a brute force solution where we put up a new blocket on
        # every possible location and see if the path turns into a loop.

        for r in range(R):
            for c in range(C):

                # We only add a wall if the point was on the path from p1
                if grid[r][c] == '.' and (r, c) in path:

                    # Deepcopy is important here to make a complete copy of the grid
                    new_grid = copy.deepcopy(grid)
                    new_grid[r][c] = '#'
                    _, is_loop = walk(new_grid, start, True)

                    if is_loop:
                        T += 1

        return T


# Part 1
assert parse_file('example.txt') == 41
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 6
print("Part 2: ", parse_file('input.txt', True))
