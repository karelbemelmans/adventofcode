#!/usr/bin/env python3

from collections import deque, defaultdict


def weight(G):

    R = len(G)
    C = len(G[0])

    T = 0
    for r in range(R):
        w = R-r
        for c in range(C):
            if G[r][c] == 'O':
                T += w

    return T


def sort_rocks(L):

    # If there are no rocks we can return L as-is
    if not L.count('O'):
        return L

    # Split out string into pieces separated by '#'
    pieces = L.split('#')
    N = []

    # Parse these pieces indivually
    for p in pieces:

        # We can simply sort our list because:
        #  - O comes before . in the ASCII table
        #  - There are no # in the string
        P = sorted(list(p), reverse=True)
        N.append(P)

    # ... and then glue them back togetehr with '#' as separator
    S = N[0]
    for i in range(1, len(N)):
        S += ['#'] + N[i]

    return S


# This function tilts north
def tilt(G):

    # Create an empty new grid
    N = [['.' for char in line] for line in G]

    R = len(G)
    C = len(G[0])

    # We look over each column
    for c in range(C):

        # We sort this column and place it in the new grid
        sorted = sort_rocks("".join([G[r][c] for r in range(R)]))
        for r in range(R):
            N[r][c] = sorted[r]

    return N


def parse_file(file, p2=False, cycles=1):

    with open(file, 'r') as fp:
        G = tuple(tuple(char for char in line)
                  for line in fp.read().splitlines())

    if p2:
        CACHE = {}

        t = 0
        while t < cycles:
            t += 1
            # Each cycle tilts it 4 times
            for _ in range(4):
                G = tilt(G)
                G = tuple(zip(*G[::-1]))

            # If we have seen this grid before we can calculate the cycle length
            if G in CACHE:
                cycle_length = t-CACHE[G]
                amt = (cycles-t)//cycle_length
                t += amt * cycle_length

            CACHE[G] = t

    else:
        G = tilt(G)

    # Calculate the total weight after tilting
    T = weight(G)
    return T


# Part 1
assert parse_file('test-final.txt') == 136
assert parse_file('test.txt') == 136
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True, 10**9) == 64
print("Part 2: ", parse_file('input.txt', True, 10**9))
