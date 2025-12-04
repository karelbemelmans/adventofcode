#!/usr/bin/env python3


def can_access(rolls_set, p):
    directions = (1 + 1j, 1, 1 - 1j, 0 + 1j, 0 - 1j, -1 + 1j, -1, -1 - 1j)

    # Count neighbors that are rolls
    neighbor_count = sum(1 for d in directions if (p + d) in rolls_set)

    return neighbor_count < 4


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        grid = {
            x + 1j * y: c
            for y, l in enumerate(fp.read().splitlines())
            for x, c in enumerate(l.strip())
        }

    # Use a set for O(1) lookups and removals
    rolls = {x for x in grid if grid[x] == "@"}
    start = len(rolls)

    if p2:
        i = 0
        while True:
            # print("run: %d, length of rolls: %d" % (i, len(rolls)))
            i += 1

            # Find all removable rolls in current iteration
            to_remove = {r for r in rolls if can_access(rolls, r)}

            if not to_remove:
                return start - len(rolls)

            # Remove all at once
            rolls -= to_remove

    else:
        return sum(can_access(rolls, r) for r in rolls)


# Part 1
assert parse_file("example.txt") == 13
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 43
print("Part 2: ", parse_file("input.txt", True))
