from copy import deepcopy


def print_grid(grid, title=""):
    print("GRID: ", title)
    for i in range(len(grid)):
        print("".join([x for x in grid[i]]))
    print("")


def move_grid(grid):
    R = len(grid)
    C = len(grid[0])
    moved = False

    # We make a new, empty, bigger grid
    new = deepcopy(grid)

    # First we move the > cucumbers
    for r in range(R):
        for c in range(C):
            if grid[r][c] == ">":
                cc = (c + 1) % C

                # Is there room to move?
                if grid[r][cc] == ".":
                    moved = True
                    new[r][cc] = ">"
                    new[r][c] = "."

    # Our input state is the state after all the ones above moved
    grid = deepcopy(new)
    new = deepcopy(grid)

    # Then we move the v cucumbers
    for c in range(C):
        for r in range(R):
            if grid[r][c] == "v":
                rr = (r + 1) % R

                # Is there room to move?
                if grid[rr][c] == ".":
                    moved = True
                    new[r][c] = "."
                    new[rr][c] = "v"

    return moved, new


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        grid = [[char for char in line] for line in fp.read().splitlines()]

    moved = True
    i = 0
    while moved:
        moved, grid = move_grid(grid)
        i += 1

    return i


# Part 1
# assert parse_file('sample.txt') == 0
assert parse_file("test.txt") == 58
print("Part 1: ", parse_file("input.txt"))

# Part 2
# assert parse_file('test2.txt', True) == 2758514936282235
# print("Part 2: ", parse_file('input.txt', True))
