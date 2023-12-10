#!/usr/bin/env python3


def connects(x, y, dir):
    d = None

    # Our start point matches with all pipes that connect with it
    if y == 'S':
        return True

    match x:

        # | is a vertical pipe connecting north and south.
        case '|':
            d = {
                (-1, 0): ['|', 'F', '7'],  # Up
                (1, 0):  ['|', 'J', 'L']  # Down
            }

        # - is a horizontal pipe connecting east and west.
        case '-':
            d = {
                (0, -1):  ['-', 'L', 'F'],  # Left
                (0, 1):  ['-', 'J', '7']  # Right
            }

        # L is a 90-degree bend connecting north and east.
        case 'L':
            d = {
                (-1, 0):  ['|', '7', 'F'],  # Up
                (0, 1):  ['-', 'J', '7']  # Righjt
            }

        # J is a 90-degree bend connecting north and west.
        case 'J':
            d = {
                (-1, 0): ['|', '7', 'F'],  # Up
                (0, -1): ['-', 'L', 'F']  # Left
            }

        # 7 is a 90-degree bend connecting south and west.
        case '7':
            d = {
                (1, 0):  ['|', 'L', 'J'],  # Down
                (0, -1):  ['-', 'L', 'F']  # Left
            }

        # F is a 90-degree bend connecting south and east.
        case 'F':
            d = {
                (1, 0): ['|', 'L', 'J'],  # Down
                (0, 1): ['-', 'J', '7']  # Right
            }

        # S connects with all pipes that connect with it
        case 'S':
            d = {
                (1, 0):  ['|', 'J', 'L'],  # Down
                (0, 1): ['-', 'J', '7'],  # Right
                (-1, 0): ['|', '7', 'F'],  # Up
                (0, -1): ['-', 'F', 'L']  # Left
            }

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

    current = S
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

    # Add S to the start of the path
    path = [S] + path

    # We have a circular path, so use halfway of it as the furthest point
    return len(path) // 2


# Part 1
assert parse_file('test.txt') == 4
assert parse_file('test-complex.txt') == 4
assert parse_file('test2.txt') == 8
assert parse_file('test2-complex.txt') == 8
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test3.txt', True) == 4
# assert parse_file('test4.txt', True) == 8
# print("Part 2: ", parse_file('input.txt', True))
