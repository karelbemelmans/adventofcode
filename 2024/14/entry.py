#!/usr/bin/env python3

import sys


def we_have_a_tree(robots):
    # Thanks to the reddit tip: "We probably have a tree if there is only max 1 robot per position"
    # This means all the items in our list have to be unique, for which we use a set()
    return len(robots) == len(set(robots))


def score(X, Y, robots):
    TL = sum([robots.count((x, y)) for x in range(0, X // 2) for y in range(0, Y // 2)])
    TR = sum(
        [robots.count((x, y)) for x in range(X // 2 + 1, X) for y in range(0, Y // 2)]
    )
    BL = sum(
        [robots.count((x, y)) for x in range(0, X // 2) for y in range(Y // 2 + 1, Y)]
    )
    BR = sum(
        [
            robots.count((x, y))
            for x in range(X // 2 + 1, X)
            for y in range(Y // 2 + 1, Y)
        ]
    )

    return TL * TR * BL * BR


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

    with open(file, "r") as fp:
        robots = [
            [tuple([int(y) for y in x[2:].split(",")]) for x in line.split(" ")]
            for line in fp.read().splitlines()
        ]

    S = 1
    while True:

        # Move all our robots
        for i in range(len(robots)):
            robots[i][0] = (
                (robots[i][0][0] + robots[i][1][0]) % X,
                (robots[i][0][1] + robots[i][1][1]) % Y,
            )

        if p2:
            if we_have_a_tree([x[0] for x in robots]):
                print_robots_grid(X, Y, [x[0] for x in robots])
                return S

        else:
            if S == 100:
                return score(X, Y, [x[0] for x in robots])

        S += 1


def main():
    # Part 1
    assert parse_file("example.txt", 11, 7) == 12
    print("Part 1: ", parse_file("input.txt", 101, 103))

    # Part 2
    print("Part 2: ", parse_file("input.txt", 101, 103, True))


if __name__ == "__main__":
    sys.exit(main())
