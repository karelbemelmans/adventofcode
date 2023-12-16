#!/usr/bin/env python3

from collections import deque


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        G = tuple(tuple(char for char in line)
                  for line in fp.read().splitlines())

    R = len(G)
    C = len(G[0])

    T = 0

    if p2:
        # Generate any edge node as a start point
        start = [(0, c, 'S') for c in range(C)] + \
                [(R-1, c, 'N') for c in range(C)] + \
                [(r, 0, 'E') for r in range(R)] + \
                [(r, C-1, 'W') for r in range(R)]
    else:
        start = [(0, 0, 'E')]

    for S in start:

        B = deque([S])

        # Set of points that have been energized, including the direction
        # We will filter out the direction later
        E = set()

        while True:

            # No more beams to process?
            if len(B) == 0:
                break

            # Get the current beam
            r, c, d = B.popleft()

            # If we have been here before, we end this beam
            #
            # The direction is important, because we can have two beams pass through
            # the same point but with different directions!
            if (r, c, d) in E:
                continue

            E.add((r, c, d))

            # Look at which point we are current at
            match G[r][c]:
                case '.':
                    pass

                case '/':
                    if d == 'N':
                        d = 'E'
                    elif d == 'E':
                        d = 'N'
                    elif d == 'S':
                        d = 'W'
                    elif d == 'W':
                        d = 'S'

                case '\\':
                    if d == 'N':
                        d = 'W'
                    elif d == 'E':
                        d = 'S'
                    elif d == 'S':
                        d = 'E'
                    elif d == 'W':
                        d = 'N'

                case '-':
                    if d == 'N' or d == 'S':
                        # Our beam splits into two beams
                        B.append((r, c, 'E'))
                        B.append((r, c, 'W'))
                        continue

                case '|':
                    if d == 'E' or d == 'W':
                        # Our beam splits into two beams
                        B.append((r, c, 'N'))
                        B.append((r, c, 'S'))
                        continue

            # Move to the next spot
            if d == 'N':
                r -= 1
            elif d == 'S':
                r += 1
            elif d == 'W':
                c -= 1
            elif d == 'E':
                c += 1

            # Add the new beam to the list if the spot is valid
            if 0 <= r < R and 0 <= c < C:
                B.append((r, c, d))

        # We need to filter our the direction.
        # Can probably be done with a python oneliner
        S = set()
        for r, c, _ in E:
            S.add((r, c))

        T = max(T, len(S))

    return T


# Part 1
assert parse_file('test.txt') == 46
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 51
print("Part 2: ", parse_file('input.txt', True))
