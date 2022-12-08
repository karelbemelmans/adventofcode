# Pretty much a copy/paste from 2021 day 09

from collections import defaultdict


def parse_grid(grid, p2=False):
    R = len(grid)
    C = len(grid[0])

    result = 0
    edges = 0

    for r in range(R):
        for c in range(C):
            visible = True

            # Trees on the edge are always visible
            if (r in [0, (R-1)]) or (c in [0, (C-1)]):
                edges += 1

            else:
                # We only check in vertical or horizontal directions
                # A tree is visible if _ALL_ of the other trees between it and
                # an edge of the grid are shorter than it.

                # Nr of directions we are not visible from
                count = 0

                # Directions we are looking in
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:

                    # We look in increasing radius around our point
                    for l in range(1, max(R, C)):
                        rr = r + l*x
                        cc = c + l*y

                        if (0 <= rr < R) and (0 <= cc < C):

                            # Is this tree taller than us? Then it blocks our sights
                            if grid[rr][cc] >= grid[r][c]:
                                count += 1
                                break

                # Not visible from all directions?
                if count == 4:
                    visible = False

            # Current point is a low point
            if visible:
                result += 1

    return result


def parse_grid2(grid, p2=False):
    R = len(grid)
    C = len(grid[0])

    m = 0

    for r in range(R):
        for c in range(C):

            # Trees on the edge give always 0, so we skip them
            if (r in [0, (R-1)]) or (c in [0, (C-1)]):
                continue

            # We keep the 4 distance scores in this dict
            distance = defaultdict(int)

            # Directions we are looking in
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:

                distance[(x, y)] = 0

                # To measure the viewing distance from a given tree, look up, down, left, and right from that tree;
                # stop if you reach an edge or at the first tree that is the same height or taller than the tree
                # under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

                for l in range(1, max(R, C)):
                    rr = r + l*x
                    cc = c + l*y

                    if (0 <= rr < R) and (0 <= cc < C):
                        distance[(x, y)] += 1
                        # We hit a tree that ends our measuring, but still gives 1 score
                        if grid[rr][cc] >= grid[r][c]:
                            break

            score = distance[(1, 0)] * distance[(0, 1)] * \
                distance[(-1, 0)] * distance[(0, -1)]
            m = max(m, score)

    return m


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        grid = [[int(char) for char in line]
                for line in fp.read().splitlines()]

    if p2:
        return parse_grid2(grid)
    else:
        return parse_grid(grid)


# Part 1
assert parse_file('test.txt') == 21
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 8
print("Part 2: ", parse_file('input.txt', True))
