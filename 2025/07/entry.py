#!/usr/bin/env python3

from collections import deque


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        grid = {
            x + 1j * y: c
            for y, l in enumerate(fp.read().splitlines())
            for x, c in enumerate(l.strip())
        }

    # Real moves from left to right
    # Imag moves up and down

    # Find the start
    start = [k for k in grid if grid[k] == "S"][0]

    Q = set([start])
    splits = set()

    while Q:
        cur = Q.pop()
        print(cur)
        nxt = cur + 1j

        # We can move down
        if nxt in grid and grid[nxt] == ".":
            Q.add(nxt)

        elif nxt in grid and grid[nxt] == "^":
            left = nxt - 1
            right = nxt + 1
            print(left, right)

            Q.add(left)
            Q.add(right)

            # Mark where a beam was split
            splits.add(cur)

    print(len(splits))
    print(splits)
    return len(splits)


# Part 1
assert parse_file("example.txt") == 21
print("Part 1: ", parse_file("input.txt"))

# Part 2
# assert parse_file("example.txt", True) == 6
# print("Part 2: ", parse_file("input.txt", True))
