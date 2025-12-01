#!/usr/bin/env python3


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        steps = [(line[0], int(line[1:])) for line in fp.read().splitlines()]

    cur = 50
    direction = "R"
    hits = 0
    M = 100

    for step in steps:
        letter = step[0]
        number = step[1]

        if letter != direction:
            cur = (M - cur) % M
            direction = letter

        cur += number

        if p2:
            hits += cur // M
            cur = cur % M
        elif cur % M == 0:
            hits += 1

    print("Final counter: ", hits)
    return hits


# Part 1
assert parse_file("example.txt") == 3
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 6
assert parse_file("example2.txt", True) == 10
print("Part 2: ", parse_file("input.txt", True))
