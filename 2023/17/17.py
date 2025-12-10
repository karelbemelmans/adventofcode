#!/usr/bin/env python3

import heapq


# Your basic A* search, but with a twist.
# This comes back every year, so good I had some older code to reuse.
#
# # Python's heapq does a lot of the heavy lifting for us \o/
#
def minimal_heat(G, start, end, least, most):

    Q = [(0, *start, 0, 0)]
    S = set()

    while Q:
        heat, r, c, pr, pc = heapq.heappop(Q)

        # We reached the end? Done.
        if (r, c) == end:
            return heat

        if (r, c, pr, pc) in S:
            continue

        S.add((r, c, pr, pc))

        # Can't go forward or backward, only turn.
        for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {(pr, pc), (-pr, -pc)}:
            a, b, h = r, c, heat

            for i in range(1, most + 1):
                a = a + dr
                b = b + dc

                if (a, b) in G:
                    h += G[a, b]
                    if i >= least:
                        heapq.heappush(Q, (h, a, b, dr, dc))


def parse_file(file, p2=False):

    # Different appreach with tuples for a grid
    # End point can simply by selected with using max(G)
    with open(file, "r") as fp:
        G = {
            (i, j): int(c)
            for i, row in enumerate(fp.read().splitlines())
            for j, c in enumerate(row.strip())
        }

    if p2:
        return minimal_heat(G, (0, 0), max(G), 4, 10)
    else:
        return minimal_heat(G, (0, 0), max(G), 1, 3)


# Part 1
assert parse_file("test.txt") == 102
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test.txt", True) == 94
assert parse_file("test2.txt", True) == 71
print("Part 2: ", parse_file("input.txt", True))
