#!/usr/bin/env python3


# The forklifts can only access a roll of paper if there are fewer
# than four rolls of paper in the eight adjacent positions.
def can_access(grid, p):
    directions = (1 + 1j, 1, 1 - 1j, 0 + 1j, 0 - 1j, -1 + 1j, -1, -1 - 1j)

    # Find all neighbours of p
    P = {p + d for d in directions if p + d in grid}

    return len(P) < 4


def parse_file(file, p2=False):

    # We use imaginary numbers to create an (x,y) grid
    # This allows us to easily add up points
    with open(file, "r") as fp:
        grid = {
            x + 1j * y: c
            for y, l in enumerate(fp.read().splitlines())
            for x, c in enumerate(l.strip())
        }

    # Keep only the points where we have a roll
    rolls = [x for x in grid if grid[x] == "@"]
    start = len(rolls)

    if p2:
        while True:

            changes = False
            for r in rolls:
                if can_access(rolls, r):
                    rolls.remove(r)
                    changes = True

            if not changes:
                return start - len(rolls)

    else:
        return sum(can_access(rolls, r) for r in rolls)


# Part 1
assert parse_file("example.txt") == 13
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 43
print("Part 2: ", parse_file("input.txt", True))
