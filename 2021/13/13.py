from collections import defaultdict
from functools import reduce


# Helper function to visualize our points on a grid
def print_grid(points):
    # Notice our input is different from our usual r,c

    # Calculate the bounds of our grid
    R = reduce(max, [x[1] for x in points]) + 1
    C = reduce(max, [x[0] for x in points]) + 1

    for r in range(R):
        for c in range(C):
            if [c, r] in points:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def parse_grid(grid, instruction):
    what, fold = instruction.split("=")
    fold = int(fold)
    new = []

    # Remember our coords are c,r
    # We are changing r here
    for r, c in grid:
        # Fold up
        if what == "fold along y" and c > fold:
            c = fold - (c - fold)

        # Fold left
        elif what == "fold along x" and r > fold:
            r = fold - (r - fold)

        if not [r, c] in new:
            new.append([r, c])

    return new


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        dots, actions = [x for x in fp.read().split("\n\n")]

    grid = [[int(char) for char in line.split(",")] for line in dots.splitlines()]
    instructions = [x for x in actions.splitlines()]

    if not p2:
        grid = parse_grid(grid, instructions[0])
        return len(grid)

    else:
        for i in instructions:
            grid = parse_grid(grid, i)

        print("End grid:")
        print_grid(grid)

        # We'll just have to manually read that code from the screen :)


# Part 1
assert parse_file('test.txt') == 17
print("Part 1: ", parse_file('input.txt'))

# Part 2
print("Part 2: ", parse_file('input.txt', True))
