#!/usr/bin/env python3

from collections import deque


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    S = 0
    for nr, line in enumerate(lines):
        values = [int(x) for x in line.split(' ')]
        L = [values]

        done = False
        while not done:
            new = []

            for i in range(len(values)-1):
                diff = values[i+1] - values[i]
                new.append(diff)

            values = new
            L.append(values)

            # Are we done?
            if sum(values) == 0:
                done = True

        # At this point we have L with a list of all the differences up to 0
        # Now work the other way around and count up

        # Add a zero to our last list and reverse it for easier parsing
        L[-1].append(0)
        L.reverse()

        # deque so we can add items to the front later one
        L = [deque(l) for l in L]

        for i in range(len(L)-1):
            # New item at the end
            end = L[i+1][-1] + L[i][-1]
            L[i+1].append(end)

            # New item at the front
            start = L[i+1][0] - L[i][0]
            L[i+1].appendleft(start)

        S += L[-1][0] if p2 else L[-1][-1]

    return S


# Part 1
assert parse_file('test.txt') == 114
assert parse_file('test2.txt') == (-12 - 93)
assert parse_file('test3.txt') == -9295
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 2
print("Part 2: ", parse_file('input.txt', True))
