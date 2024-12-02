#!/usr/bin/env python3

from itertools import combinations


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [[int(a) for a in line.split()] for line in fp.read().splitlines()]

    SAFE = 0
    for line in lines:

        # In p2 we take combations of size one less than the length of the line
        if p2:
            combs = combinations(line, len(line) - 1)
        else:
            combs = [line]

        for row in combs:

            # convert to list, as combiation returns a tuple
            row = list(row)

            # First: Check if the row is sorted or reverse sorted
            S = (row == sorted(row) or row == sorted(row, reverse=True))

            # Second: Check if the difference between each element is in the range 1-3
            I = True
            for i in range(0, len(row) - 1):
                if not abs(row[i] - row[i+1]) in range(1, 4):
                    I = False

            # If both conditions are met, increment SAFE and move on to the next line
            if S and I:
                SAFE += 1
                break

    return SAFE


# Part 1
assert parse_file('example.txt') == 2
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 4
print("Part 2: ", parse_file('input.txt', True))
