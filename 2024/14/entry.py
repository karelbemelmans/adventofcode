#!/usr/bin/env python3

import sys


def print_robots_grid(X, Y, robots):
    for y in range(Y):
        for x in range(X):
            if (x, y) in robots:
                l = robots.count((x, y))
                print(l, end="")
            else:
                print(".", end="")
        print()


def parse_file(file, X, Y, p2=False):

    with open(file, 'r') as fp:
        positions = [[tuple([int(y) for y in x[2:].split(",")]) for x in line.split(" ")]
                     for line in fp.read().splitlines()]

    print_robots_grid(X, Y, [x[0] for x in positions])

    for p, v in positions:
        print(p, v)

    T = 0
    return T


def main():
    # Part 1
    assert parse_file('example.txt', 11, 7) == 480
    print("Part 1: ", parse_file('input.txt', 101, 103))

    # Part 2
    print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
