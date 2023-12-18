#!/usr/bin/env python3

DIR = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def show_set(S, p2=False):
    min_r = min(r for r, _ in S)
    max_r = max(r for r, _ in S)
    min_c = min(c for _, c in S)
    max_c = max(c for _, c in S)

    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if (r, c) in S:
                if (r, c) in S:
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                print('.', end='')
        print()
    print()


def floodFill(G, r,  c):
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
    G.add((r, c))

    # While the queue is not empty i.e. the whole component having prevC color is not colored with newC color
    while queue:

        # Dequeue the front node
        cur = queue.pop()

        # Check if the adjacent pixels are valid
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr, cc = cur[0] + d[0], cur[1] + d[1]
            if not (rr, cc) in G and not d == (0, 0):
                G.add((rr, cc))
                queue.append((rr, cc))


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [[piece for piece in line.split(' ')]
                 for line in fp.read().splitlines()]

    S = set()

    # Pointer coords
    p = (0, 0)

    # Build up our set of points
    for line in lines:
        d = int(code[-1]) if p2 else line[0]
        l = int(code[1:-1], 16) if p2 else int(line[1])

        # 0 means R, 1 means D, 2 means L, and 3 means U.
        match d:
            case 0 | 'R':
                d = DIR['R']
            case 1 | 'D':
                d = DIR['D']
            case 2 | 'L':
                d = DIR['L']
            case 3 | 'U':
                d = DIR['U']

        # End point of our line
        end = (p[0] + l * d[0], p[1] + l * d[1])

        # We add every point along the way
        for i in range(1, l+1):
            rr, cc = p[0] + (i * d[0]), p[1] + (i * d[1])
            S.add((rr, cc))

        # Our new pointer location
        p = (rr, cc)

    show_set(S)

    floodFill(S, 1, 1)

    show_set(S)

    T = len(S)
    print("Score: ", T)
    return T


# Part 1
assert parse_file('test.txt') == 62
# print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 952408144115
# print("Part 2: ", parse_file('input.txt', True))
