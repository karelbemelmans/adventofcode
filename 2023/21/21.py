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

    Q = [start]
    for i in range(steps):
        print(i)

        QQ = set()
        for (r, c) in Q:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc
                if not (nr, nc) in S:
                    QQ.add((nr, nc))

        # Q = deepcopy(QQ)
        Q = QQ
        print(len(Q), Q)

    show_set(S, Q)

    T = len(Q)
    print("T: ", T)
    return T


def main():
    # Part 1
    assert parse_file('test.txt', 6) == 16
    print("Part 1: ", parse_file('input.txt', 64))

    # Part 2
    # assert parse_file('test.txt', True) == 0
    # print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
