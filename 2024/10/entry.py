#!/usr/bin/env python3

import heapq


def trailhead(G, start, end):

    Q = [(0, *start)]
    S = set()

    while Q:
        l, r, c = heapq.heappop(Q)

        # We reached the end? Done.
        if (r, c) == end:
            return True

        if (r, c) in S:
            continue

        S.add((r, c))

        # We can only go in 4 directions, no diagonals
        for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
            a, b = r, c

            # Take a step
            a = a+dr
            b = b+dc

            # Is the next point one step up from the previous?
            if (a, b) in G and G[a, b] == G[r, c] + 1:
                heapq.heappush(Q, (l+1, a, b))

    return False


def parse_file(file, p2=False):

    # Different appreach with tuples for a grid
    # End point can simply by selected with using max(G)
    with open(file, 'r') as fp:
        G = {(i, j): int(c) for i, row in enumerate(fp.read().splitlines())
             for j, c in enumerate(row.strip())}

    print(G)

    starts = [x for x in G if G[x] == 0]
    ends = [x for x in G if G[x] == 9]
    print(starts, ends)

    T = 0
    for s in starts:
        print("Start: ", s)
        t = 0
        for e in ends:

            if trailhead(G, s, e):
                t += 1

        print("This point has paths: ", t)
        T += t

    print("T", T)
    return T


# Part 1
assert parse_file('example2.txt') == 1
assert parse_file('example.txt') == 36
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 8
# print("Part 2: ", parse_file('input.txt', True))
