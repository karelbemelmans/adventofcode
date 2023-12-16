#!/usr/bin/env python3

from collections import deque, defaultdict


def show_grid(G):
    for line in G:
        print(''.join(line))
    print()


def show_set(S):
    min_r = min(r for r, _ in S)
    max_r = max(r for r, _ in S)
    min_c = min(c for _, c in S)
    max_c = max(c for _, c in S)

    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if (r, c) in S:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        G = tuple(tuple(char for char in line)
                  for line in fp.read().splitlines())

    R = len(G)
    C = len(G[0])

    # List of beams. Every beam has a coordinate and a direction
    # We start with a beam at 0,0 pointing East
    B = deque([(0, 0, 'E')])

    # Set of points that have been energized
    E = set()

    i = 0
    while True:
        i += 1

        # No more beams to process?
        if len(B) == 0:
            break

        # Get the current beam
        r, c, d = B.popleft()

        # If we have been here before, we end this beam
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

        # print("  - Moving beam", r, c, d)

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

    S = set()
    for r, c, _ in E:
        S.add((r, c))

    T = len(S)
    return T


# Part 1
assert parse_file('test.txt') == 46
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
