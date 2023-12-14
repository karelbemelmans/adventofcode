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
    pieces = "".join(L).split('#')
    N = []

    # Parse these pieces indivually
    for p in pieces:
        P = list(p)
        rocks = P.count('O')

        for i in range(len(P)):

            # An immutable rock
            if P[i] == '#':
                continue

            # A valid spot to place a rock?
            elif P[i] in ['.', 'O'] and rocks:
                P[i] = 'O'
                rocks -= 1

            # We have a rock but we placed all our rocks? It becomes empty now
            elif not rocks:
                P[i] = '.'

        N.append(P)

    # ... and then glue them back togetehr with '#' as separator
    S = N[0]
    for i in range(1, len(N)):
        S += ['#'] + N[i]

    return S


def tilt(G, dir='N'):

    # Create an empty new grid
    N = [['.' for char in line] for line in G]

    R = len(G)
    C = len(G[0])

    # We look over each column
    for c in range(C):

        # We sort this column and place it in the new grid
        sorted = sort_rocks([G[r][c] for r in range(R)])
        for r in range(R):
            N[r][c] = sorted[r]

    return N


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        G = [[char for char in line] for line in fp.read().splitlines()]

    G = tilt(G, 'N')
    T = weight(G)

    return T


# Part 1
assert parse_file('test-final.txt') == 136
assert parse_file('test.txt') == 136
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
