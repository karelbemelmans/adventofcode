# Flash a point on the grid
def flash_point(grid, r, c, flashed):
    R = len(grid)
    C = len(grid[0])

    # Has this point already flashed? Then we skip it.
    if [r,c] in flashed:
        return

    # Add this point to our list of flashed points
    flashed.append([r, c])

    # Increase points around this one
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr = r + dr
            cc = c + dc
            if not (dr == 0 and dc == 0) and (0 <= rr < R) and (0 <= cc < C):
                grid[rr][cc] += 1

                # Did we make this point go above 9? Then it will also flash, if it has not flashed already this run
                if grid[rr][cc] > 9:
                    flash_point(grid, rr, cc, flashed)


def parse_grid(grid, steps, run=1, flashes=0, p2=False):

    # Did we do enough runs in p1?
    if not p2 and run > steps:
        return flashes

    R = len(grid)
    C = len(grid[0])

    flashed = []

    # First we boost every point by 1
    for r in range(R):
        for c in range(C):
            grid[r][c] += 1

    # Then check for flashes
    # This function will recurse on points that also flashed from this action
    for r in range(R):
        for c in range(C):
            if grid[r][c] > 9:
                flash_point(grid, r, c, flashed)

    # Reset all flashed points to 0 and continue
    for r, c in flashed:
        grid[r][c] = 0

    # Did we reach the p2 goal?
    if p2 and len(flashed) == R*C:
        return run

    # Otherwise we recurse this grid for the next step
    return parse_grid(grid, steps, run+1, flashes + len(flashed), p2)


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        grid = [[int(char) for char in line] for line in fp.read().splitlines()]

    if p2:
        return parse_grid(grid, 0, 1, 0, True)
    else:
        return parse_grid(grid, 100)


# Part 1
assert parse_file('test.txt') == 1656
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 195
print("Part 2: ", parse_file('input.txt', True))
