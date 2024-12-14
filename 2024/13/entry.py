#!/usr/bin/env python3

import sys
import re

MAX = 100
A_COST = 3
B_COST = 1

# p1: Very naive approach


def match(x, y, t):
    for i in range(MAX+1):
        for j in range(MAX+1):
            if (x[0]*i + y[0]*j == t[0]) and (x[1]*i + y[1]*j == t[1]):
                return i * A_COST + j * B_COST

    return False


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        machines = [[line for line in machine.splitlines()] for machine in fp.read().split("\n\n")]

    T = 0
    for m in machines:

        a = [int(x[2:]) for x in m[0][10:].split(', ')]
        b = [int(x[2:]) for x in m[1][10:].split(', ')]
        prize = [int(x[2:]) for x in m[2][7:].split(', ')]

        t = match(a, b, prize)
        if t:
            T += t

    return T


def main():
    # Part 1
    assert parse_file('example.txt') == 480
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    # assert parse_file('example.txt', True) == 80
    # print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
