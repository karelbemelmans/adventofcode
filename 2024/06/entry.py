#!/usr/bin/env python3

from itertools import combinations


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])
    start = None

    # TODO: This is a bit ugly
    rotations = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find the guard
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '^':
                start = ((r, c), (-1, 0))
                break

    def walk(grid, start, p2=False):
        visited = set()
        visited_dir = set()

        visited.add(start[0])
        visited_dir.add(start)

        cur = start

        k = 0
        while True and k < 10000:
            k += 1
            # Do a next step
            rr, cc = cur[0][0] + cur[1][0], cur[0][1] + cur[1][1]

            # Out of bounds? Then we are done
            if rr < 0 or rr >= R or cc < 0 or cc >= C:
                break

            # Turning point?
            elif grid[rr][cc] == '#':
                cur = (cur[0], rotations[(rotations.index(cur[1]) + 1) % 4])

            else:
                # Are we on a loop?
                if p2 and ((rr, cc), cur[1]) in visited_dir:
                    print("visited_dir: ", visited_dir)
                    return False

                visited.add((rr, cc))
                visited_dir.add(((rr, cc), cur[1]))
                cur = ((rr, cc), cur[1])

        print(visited, len(visited))
        return len(visited)

    if p2:
        T = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.':
                    print("New blocker at: ", r, c)

                    new_grid = grid.copy()
                    new_grid[r][c] = '#'
                    if not walk(new_grid, start, True):
                        T += 1

        print("T: ", T)
        return T

    else:
        return walk(grid, start)


# Part 1
# assert parse_file('example.txt') == 41
# print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 6
# print("Part 2: ", parse_file('input.txt', True))
