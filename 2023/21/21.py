#!/usr/bin/env python3

import sys
from collections import deque, defaultdict
from copy import deepcopy


def show_set(S, Q):
    R = max(r for r, c in S)
    C = max(c for r, c in S)

    for r in range(R+1):
        for c in range(C+1):
            if (r, c) in Q:
                print('O', end='')
            elif (r, c) in S:
                print('#', end='')
            else:
                print('.', end='')
        print()


def parse_file(file, steps=6, p2=False):

    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])

    # We build up a list of points. This works better than parsing a grid for this thing.
    S = set()
    start = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                S.add((r, c))
            if grid[r][c] == 'S':
                start = (r, c)

    Q = set([start])
    for i in range(steps):

        QQ = set()
        for (r, c) in Q:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc

                # Normalize coords and look if those are on the input grid
                xnr = nr % R
                xnc = nc % C

                if not (xnr, xnc) in S:
                    QQ.add((nr, nc))

        Q = deepcopy(QQ)
        print(i, len(Q))

    show_set(S, Q)

    T = len(Q)
    print("T: ", T)
    return T


def main():
    # Part 1
    assert parse_file('test.txt', 6) == 16
    print("Part 1: ", parse_file('input.txt', 64))

    # Part 2
    assert parse_file('test.txt', 6, True) == 16
    assert parse_file('test.txt', 10, True) == 50
    assert parse_file('test.txt', 50, True) == 1594
    assert parse_file('test.txt', 100, True) == 6536
    assert parse_file('test.txt', 500, True) == 167004
    # assert parse_file('test.txt', 1000, True) == 668697
    # assert parse_file('test.txt', 5000, True) == 16733044
    # print("Part 2: ", parse_file('input.txt', 26501365, True))


if __name__ == "__main__":
    sys.exit(main())
