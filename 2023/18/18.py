#!/usr/bin/env python3

DIR = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def segments(p):
    '''
    This function is a helper function that turns a list into a list of tuples:

    Input:   ['a', 'b', 'c', 'd']
    Returns: [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
    '''
    return zip(p, p[1:] + [p[0]])


def poly_area(p):
    '''
    This function calculates the area of a polygon given a list of points
    '''
    return 0.5 * abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in segments(p)))


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [[piece for piece in line.split(' ')]
                 for line in fp.read().splitlines()]

    # Pointer coords
    p = (0, 0)

    # Corners
    S = []
    outline = 0

    # Build up our set of points
    for line in lines:
        d = int(line[2][-2:-1]) if p2 else line[0]
        l = int(line[2][2:-2], 16) if p2 else int(line[1])

        # 0 means R, 1 means D, 2 means L, and 3 means U.
        match d:
            case 0 | 'R':
                d = DIR['R']
            case 1 | 'D':
                d = DIR['D']
            case 2 | 'L':
                d = DIR['L']
            case 3 | 'U':
                d = DIR['U']

        # End point of our line
        p = (p[0] + l * d[0], p[1] + l * d[1])
        outline += l
        S.append(p)

    T = int(poly_area(S)) + outline // 2 + 1
    return T


# Part 1
assert parse_file('test.txt') == 62
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 952408144115
print("Part 2: ", parse_file('input.txt', True))
