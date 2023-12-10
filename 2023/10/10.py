#!/usr/bin/env python3

from matplotlib.path import Path


def connects(x, y, dir):
    d = None

    # Our start point matches with all pipes that connect with it
    if y == 'S':
        return True

    match x:

        case '|':
            d = {
                (-1, 0): ['|', 'F', '7'],  # Up
                (1, 0):  ['|', 'J', 'L']  # Down
            }

        case '-':
            d = {
                (0, -1):  ['-', 'L', 'F'],  # Left
                (0, 1):  ['-', 'J', '7']  # Right
            }

        case 'L':
            d = {
                (-1, 0):  ['|', '7', 'F'],  # Up
                (0, 1):  ['-', 'J', '7']  # Right
            }

        case 'J':
            d = {
                (-1, 0): ['|', '7', 'F'],  # Up
                (0, -1): ['-', 'L', 'F']  # Left
            }

        case '7':
            d = {
                (1, 0):  ['|', 'L', 'J'],  # Down
                (0, -1):  ['-', 'L', 'F']  # Left
            }

        case 'F':
            d = {
                (1, 0): ['|', 'L', 'J'],  # Down
                (0, 1): ['-', 'J', '7']  # Right
            }

        case 'S':
            d = {
                (1, 0):  ['|', 'J', 'L'],  # Down
                (0, 1): ['-', 'J', '7'],  # Right
                (-1, 0): ['|', '7', 'F'],  # Up
                (0, -1): ['-', 'F', 'L']  # Left
            }

    # We match if we have a direction list AND the item is in that list
    return dir in d and y in d[dir]


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])

    # Find S as starting node
    S = None
    for r in range(R):
        for c in range(C):
            match grid[r][c]:
                case 'S':
                    S = (r, c)

    # Current position
    current = S

    # Path of all visited nodes in our circular path
    path = [S]

    done = False
    while not done:

        # When are we done?
        if len(path) > 1 and current == S:
            break

        r = current[0]
        c = current[1]

        # Look around in all directions
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C:
                if connects(grid[r][c], grid[rr][cc], (dr, dc)) and not (rr, cc) in path:
                    current = (rr, cc)
                    path.append((rr, cc))
                    break
        # If we have no more connections, we are done
        else:
            done = True

    # We have a circular path, so use halfway of it as the furthest point
    if not p2:
        return len(path) // 2

    # p2: Find isolated points
    # matplotlib.path makes this ridiculously easy :)
    T = 0
    p = Path(path)
    for r in range(R):
        for c in range(C):
            if (r, c) in path:
                continue
            if p.contains_point((r, c)):
                T += 1

    return T


# Part 1
assert parse_file('test.txt') == 4
assert parse_file('test-complex.txt') == 4
assert parse_file('test2.txt') == 8
assert parse_file('test2-complex.txt') == 8
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test3.txt', True) == 4
assert parse_file('test4.txt', True) == 8
print("Part 2: ", parse_file('input.txt', True))
