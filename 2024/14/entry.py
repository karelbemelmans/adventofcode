#!/usr/bin/env python3

import sys


def score(X, Y, robots):
    T = 1

    # Top left
    T *= sum([robots.count((x, y)) for x in range(0, X // 2) for y in range(0, Y//2)])

    # Top right
    T *= sum([robots.count((x, y)) for x in range(X // 2, X) for y in range(0, Y//2)])

    # Bottom left
    T *= sum([robots.count((x, y)) for x in range(0, X // 2) for y in range(Y//2 + 1, Y)])

    # Bottom right
    T *= sum([robots.count((x, y)) for x in range(X // 2 + 1, X) for y in range(Y//2 + 1, Y)])

    return T


def print_robots_grid(X, Y, robots):
    for y in range(Y):
        for x in range(X):
            if (x, y) in robots:
                l = robots.count((x, y))
                print(l, end="")
            else:
                print(".", end="")
        print()


def parse_file(file, X, Y, S=10, p2=False):

    with open(file, 'r') as fp:
        robots = [[tuple([int(y) for y in x[2:].split(",")]) for x in line.split(" ")]
                  for line in fp.read().splitlines()]

    # print_robots_grid(X, Y, [x[0] for x in robots])

    # Loop over robots
    for i in range(len(robots)):

        # Loop for S seconds
        for s in range(1, S+1):
            # print("Second: ", s)

            # TODO: Write this a bit more readable
            robots[i][0] = ((robots[i][0][0] + robots[i][1][0]) % X, (robots[i][0][1] + robots[i][1][1]) % Y)

    # Final state
    print_robots_grid(X, Y, [x[0] for x in robots])

    T = score(X, Y, [x[0] for x in robots])

    print("T: ", T)
    return T


def main():
    # Part 1
    # assert parse_file('example2.txt', 11, 7, 10) == 12
    assert parse_file('example.txt', 11, 7, 100) == 12
    print("Part 1: ", parse_file('input.txt', 101, 103, 100))

    # Part 2
    # print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
