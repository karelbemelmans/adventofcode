#!/usr/bin/env python3


def draw_line(a, b):
    line = []

    dx = a[0] - b[0]
    dy = a[1] - b[1]

    l = max(abs(dx), abs(dy))
    for i in range(l+1):
        aa = b[0]+i*(1 if dx > 0 else (-1 if dx < 0 else 0))
        bb = b[1]+i*(1 if dy > 0 else (-1 if dy < 0 else 0))
        line.append((aa, bb))

    return line


def parse_shapes(shapes):
    R = set()

    for shape in shapes:
        for i in range(len(shape)-1):
            line = draw_line(shape[i], shape[i+1])
            R.update(line)

    return R


def sand_flows(rocks, start):

    # High deep is too deep?
    floor = max(r[1] for r in rocks) + 2

    # Take some high number which we will most likely not reach
    for t in range(1000000):

        rock = start

        while True:

            if rock[1] + 1 >= floor:
                return t

            if (rock[0], rock[1]+1) not in rocks:
                rock = (rock[0], rock[1]+1)
            elif (rock[0]-1, rock[1]+1) not in rocks:
                rock = (rock[0]-1, rock[1]+1)
            elif (rock[0]+1, rock[1]+1) not in rocks:
                rock = (rock[0]+1, rock[1]+1)
            else:
                break

        if rock == (500, 0):
            print(t+1)
            break

        rocks.add(rock)


def parse_file(file, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, 'r') as fp:
        shapes = [
            [
                [
                    int(x) for x in line.split(",")
                ]
                for line in row.split(" -> ")
            ]
            for row in fp.read().splitlines()
        ]

    rocks = parse_shapes(shapes)

    return sand_flows(rocks, (500, 0))


# Part 1
assert parse_file('test.txt') == 24
print("Part 1: ", parse_file('input.txt'))

# assert parse_file('test.txt', True) == 140
# print("Part 2: ", parse_file('input.txt', True))
