#!/usr/bin/env python3


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
        for l in L:
            print(l)

        # Add a zero to our last list
        L[-1].append(0)
        L.reverse()

        for i in range(len(L)-1):
            new = L[i+1][-1] + L[i][-1]
            L[i+1].append(new)

        s = L[-1][-1]
        print("score: ", s)
        S += s

    return S


# Part 1
assert parse_file('test.txt') == 114
assert parse_file('test2.txt') == (-12 - 93)
assert parse_file('test3.txt') == -9295
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
