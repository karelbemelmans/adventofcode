#!/usr/bin/env python3

import sys

# Give our directions a nice name
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# All possible connect pieces for each direction
DIR = {
    UP: ["|", "7", "F"],
    LEFT: ["-", "F", "L"],
    RIGHT: ["-", "J", "7"],
    DOWN: ["|", "J", "L"],
}


def poly_area(p):
    """
    This function calculates the area of a polygon given a list of points

    https://en.wikipedia.org/wiki/Shoelace_formula
    """
    return 0.5 * abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in segments(p)))


def segments(p):
    """
    This function is a helper function that turns a list into a list of tuples:

    Single value:
    Input:   ['a', 'b', 'c', 'd']
    Returns: [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]

    2D tuples:
    Input:   [('a', 'a'), ('b', 'b'), ('c', 'c')]
    Output:  [(('a', 'a'), ('b', 'b')), (('b', 'b'), ('c', 'c')), (('c', 'c'), ('a', 'a'))]
    """
    return zip(p, p[1:] + [p[0]])


def connects(x, y, dir):
    d = None

    # Our start point matches with all pipes that connect with it
    if y == "S":
        return True

    # The symbols our first char can match with
    match x:
        case "|":
            d = [UP, DOWN]
        case "-":
            d = [LEFT, RIGHT]
        case "L":
            d = [UP, RIGHT]
        case "J":
            d = [UP, LEFT]
        case "7":
            d = [DOWN, LEFT]
        case "F":
            d = [DOWN, RIGHT]
        case "S":
            d = [UP, DOWN, LEFT, RIGHT]

    # We match if we have a direction list AND the item is in that list
    return dir in d and y in DIR[dir]


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        grid = [[char for char in line] for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])

    # Find S as starting node
    S = None
    for r in range(R):
        for c in range(C):
            match grid[r][c]:
                case "S":
                    S = (r, c)
                    break

    # Current position
    current = S

    # Path of all visited nodes in our circular path
    path = [S]
    outline = 0

    done = False
    while not done:

        # When are we done?
        if len(path) > 1 and current == S:
            break

        r = current[0]
        c = current[1]

        # Look around in all directions
        for dr, dc in [UP, DOWN, LEFT, RIGHT]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C:
                if (
                    connects(grid[r][c], grid[rr][cc], (dr, dc))
                    and not (rr, cc) in path
                ):
                    current = (rr, cc)
                    path.append((rr, cc))
                    outline += 1
                    break
        # If we have no more connections, we are done
        else:
            done = True

    # p2: Find isolated points
    if p2:
        T = int(poly_area(path)) - len(path) // 2 + 1
        return T

    # We have a circular path, so use halfway of it as the furthest point
    else:
        T = outline // 2 + 1
        return T


def main():
    # Part 1
    assert parse_file("test.txt") == 4
    assert parse_file("test-complex.txt") == 4
    assert parse_file("test2.txt") == 8
    assert parse_file("test2-complex.txt") == 8
    print("Part 1: ", parse_file("input.txt"))

    # Part 2
    assert parse_file("test3.txt", True) == 4
    assert parse_file("test4.txt", True) == 8
    print("Part 2: ", parse_file("input.txt", True))


if __name__ == "__main__":
    sys.exit(main())
