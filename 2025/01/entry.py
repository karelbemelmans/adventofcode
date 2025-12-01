#!/usr/bin/env python3


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    # Read lines into pairs of integers
    steps = [(line[0], int(line[1:]) for line in lines]
    print((steps)
    

    if p2:
        return sum([a * second.count(a) for a in first])
    else:
        return sum([abs(first[i] - second[i]) for i in range(0, len(pairs))])


# Part 1
assert parse_file("example.txt") == 11
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 31
print("Part 2: ", parse_file("input.txt", True))
