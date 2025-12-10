#!/usr/bin/env python3


def draw_line(a, b):
    line = []

    dx = a[0] - b[0]
    dy = a[1] - b[1]

    l = max(abs(dx), abs(dy))
    for i in range(l + 1):
        aa = b[0] + i * (1 if dx > 0 else (-1 if dx < 0 else 0))
        bb = b[1] + i * (1 if dy > 0 else (-1 if dy < 0 else 0))
        line.append((aa, bb))

    return line


def parse_shapes(shapes):
    R = set()

    for shape in shapes:
        for i in range(len(shape) - 1):
            line = draw_line(shape[i], shape[i + 1])
            R.update(line)

    return R


def sand_flows(rocks, p2=False):

    # We need to set a cap, p2's floor is good for p1 as well
    start = (500, 0)
    floor = max(r[1] for r in rocks) + 2

    # p2 needs a floor. Seems easy enough to just add it as actual rocks
    if p2:
        x_min = min(r[0] for r in rocks) - 2000
        x_max = max(r[0] for r in rocks) + 2000
        for x in range(x_min, x_max):
            rocks.add((x, floor))

    # Take some high number which we will most likely not reach
    for t in range(100000):

        rock = start

        while True:

            # p1 is done when we start to go past the floor
            if rock[1] + 1 >= floor and not p2:
                return t

            if (rock[0], rock[1] + 1) not in rocks:
                rock = (rock[0], rock[1] + 1)
            elif (rock[0] - 1, rock[1] + 1) not in rocks:
                rock = (rock[0] - 1, rock[1] + 1)
            elif (rock[0] + 1, rock[1] + 1) not in rocks:
                rock = (rock[0] + 1, rock[1] + 1)
            else:
                break

        # In p2 our end point is when we did not find any more rocks
        # to advance to, so our start is our end point
        if rock == start:
            return t + 1

        # We add sand as rocks because it does not matter what the material
        # is, as long as we know it's not an air spot.
        rocks.add(rock)


def parse_file(file, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, "r") as fp:
        shapes = [
            [[int(x) for x in line.split(",")] for line in row.split(" -> ")]
            for row in fp.read().splitlines()
        ]

    rocks = parse_shapes(shapes)
    return sand_flows(rocks, p2)


# Part 1
assert parse_file("test.txt") == 24
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 93
print("Part 2: ", parse_file("input.txt", True))
