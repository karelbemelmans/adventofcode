
def find_basin(grid, r, c, marked = []):
    R = len(grid)
    C = len(grid[0])

    # We add the current point to the list if it's not in there already
    if not [r,c] in marked:
        marked.append([r,c])

    # Look around this spot and see if there are spots we need to mark
    # If we do, then recurse our algorithm and build a bigger marked list.

    # We only check in vertical or horizontal directions
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        rr = r + d[0]
        cc = c + d[1]

        if (0 <= rr < R) and (0 <= cc < C):
            value = grid[rr][cc]
            if value < 9 and not [rr, cc] in marked:
                find_basin(grid, rr, cc, marked)

    return marked

def parse_grid(grid, p2=False):
    R = len(grid)
    C = len(grid[0])

    result = 0
    basins = []
    for r in range(R):
        for c in range(C):

            # Is this a low point+
            smaller = True

            # We only check in vertical or horizontal directions
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (0 <= r+x < R) and (0 <= c+y < C):
                    if grid[r][c] >= grid[r+x][c+y]:
                        smaller = False

            # Current point is a low point
            if smaller:
                if p2:
                    # Check for basin points around this point r,c
                    points = find_basin(grid, r, c, [])

                    # Add the size of this basin to our list
                    basins.append(len(points))

                else:
                    result += (grid[r][c] + 1)

    if p2:
        # Find the three largest basins and multiply their sizes together
        basins = sorted(basins, reverse=True)
        return basins[0] * basins[1] * basins[2]

    else:
        return result

def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        grid = [[int(char) for char in line] for line in fp.read().splitlines()]

    return parse_grid(grid, p2)

# Part 1
assert parse_file('test.txt') == 15
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 1134
print("Part 2: ", parse_file('input.txt', True))
