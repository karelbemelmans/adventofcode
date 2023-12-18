#!/usr/bin/env python3

from collections import deque, defaultdict
import random

DIR = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

default_color = "#000000"


def show_set(S, p2=False):
    min_r = min(r for r, _ in S)
    max_r = max(r for r, _ in S)
    min_c = min(c for _, c in S)
    max_c = max(c for _, c in S)

    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if (r, c) in S:
                if p2:
                    print(S[(r, c)], end='')
                else:
                    if not S[(r, c)] == default_color:
                        print('#', end='')
                    else:
                        print('.', end='')
            else:
                print('.', end='')
        print()
    print()


def floodFill(G, r,  c, prevC, newC):
    min_r = min(r for r, _ in G)
    max_r = max(r for r, _ in G)
    min_c = min(c for _, c in G)
    max_c = max(c for _, c in G)

    R = max_r - min_r
    C = max_c - min_c

    queue = []

    # Append the position of starting
    # pixel of the component
    queue.append((r, c))

    # Color the pixel with the new color
    G[(r, c)] = newC

    # While the queue is not empty i.e. the whole component having prevC color is not colored with newC color
    while queue:

        # Dequeue the front node
        cur = queue.pop()

        # Check if the adjacent pixels are valid
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = cur[0] + d[0]
            cc = cur[1] + d[1]
            if (rr, cc) in G and not d == (0, 0):
                if G[(rr, cc)] == prevC:
                    G[(rr, cc)] = newC
                    queue.append((rr, cc))


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [[piece for piece in line.split(' ')]
                 for line in fp.read().splitlines()]

    S = {}

    # Build up our set of points
    p = (0, 0)
    for line in lines:
        d, l, color = DIR[line[0]], int(line[1]), line[2][1:-1]
        for _ in range(1, l+1):
            rr, cc = p[0] + d[0], p[1] + d[1]
            S[(rr, cc)] = color if p2 else "#"
            p = (rr, cc)

    # Give all the other points a color as well
    min_r = min(r for r, _ in S)
    max_r = max(r for r, _ in S)
    min_c = min(c for _, c in S)
    max_c = max(c for _, c in S)

    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if not (r, c) in S:
                S[(r, c)] = default_color

    print("Set before closing:")
    show_set(S, p2)

    floodFill(S, 1, 1, default_color, "#")

    print("Set after closing:")
    show_set(S, p2)

    T = len([color for color in S.values() if color == "#"])
    print("Score: ", T)
    return T


# Part 1
assert parse_file('test.txt') == 62
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
