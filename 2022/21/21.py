#!/usr/bin/env python3

from collections import defaultdict


def parse(lines, p2=False):
    R = defaultdict(int)
    operations = ['+', '-', '*', '/']

    while True:
        for k, v in lines:

            # Is it a value? Then store it
            if any(v.count(o) for o in operations):
                a, op, b = v.split(" ")
                # Do we know a and b's value already?
                if R[a] and R[b]:
                    if op == '+':
                        R[k] = R[a] + R[b]
                    elif op == '-':
                        R[k] = R[a] - R[b]
                    elif op == '*':
                        R[k] = R[a] * R[b]
                    elif op == '/':
                        R[k] = R[a] // R[b]
            else:
                R[k] = int(v)

        if R['root']:
            return R['root']


def parse_file(file, p2=False):

    # Shape is a list of lists that contains pairs
    with open(file, 'r') as fp:
        lines = [[parts.strip() for parts in line.split(
            ":")] for line in fp.readlines()]

    return parse(lines, p2)


# Part 1
assert parse_file('test.txt') == 152
print("Part 1: ", parse_file('input.txt'))

# assert parse_file('test.txt', int(1e12), True) == 1514285714288
# print("Part 2: ", parse_file('input.txt', int(1e12), True))
