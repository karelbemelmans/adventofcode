#!/usr/bin/env python3

import heapq


def nr_of_paths(G, start, end):

    Q = [(0, *start)]
    count = 0

    while Q:
        l, r, c = heapq.heappop(Q)

        # We reached the end? Done.
        if (r, c) == end:
            count += 1
            continue

        # We can only go in 4 directions, no diagonals
        for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
            a, b = r, c

            # Take a step
            a = a+dr
            b = b+dc

            # Is the next point one step up from the previous?
            if (a, b) in G and G[a, b] == G[r, c] + 1:
                heapq.heappush(Q, (l+1, a, b))

    return count


def parse_file(file, p2=False):

    # We like complex numbers now.
    with open(file, 'r') as fp:
        G = {(i, j): int(c) for i, row in enumerate(fp.read().splitlines())
             for j, c in enumerate(row.strip())}

    starts = [x for x in G if G[x] == 0]
    ends = [x for x in G if G[x] == 9]

    T = 0

    # Simple counting the nr of paths from all starts to all ends
    for s in starts:
        for e in ends:

            # In p2 we look at the nr of paths
            if p2:
                T += nr_of_paths(G, s, e)

            # In p1 we only look if there is a path possible
            else:
                T += 1 if nr_of_paths(G, s, e) else 0

    return T


# Part 1
assert parse_file('example.txt') == 36
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 81
print("Part 2: ", parse_file('input.txt', True))
