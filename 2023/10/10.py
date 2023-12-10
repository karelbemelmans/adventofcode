#!/usr/bin/env python3

from collections import deque, defaultdict
import networkx as nx


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        grid = [[char for char in line]
                for line in fp.read().splitlines()]

    R = len(grid)
    C = len(grid[0])

    G = nx.Graph()
    S = None

    # Add all valid nodes
    for r in range(R):
        for c in range(C):
            match grid[r][c]:
                case 'S':
                    S = (r, c)
                    G.add_node((r, c))

                case '|', '-', 'L', 'J', '7', 'F':
                    G.add_node((r, c))

    # Find edges we need to add
    for r in range(R):
        for c in range(C):

            d = []  # directions and valid types per direction
            match grid[r][c]:

                # | is a vertical pipe connecting north and south.
                case '|':
                    d = [(-1, 0, ['L', 'J']), (1, 0, ['F', '7'])]

                # - is a horizontal pipe connecting east and west.
                case '-':
                    d = [(0, -1, ['L', 'F']), (0, 1, ['J', '7'])]

                # L is a 90-degree bend connecting north and east.
                case 'L':
                    d = [(-1, 0, ['|', '7', 'F']), (0, 1, ['-', 'J', '7'])]

                # J is a 90-degree bend connecting north and west.
                case 'J':
                    d = [(-1, 0, ['|', '7', 'F']), (0, -1, ['-', 'L', 'F'])]

                # 7 is a 90-degree bend connecting south and west.
                case '7':
                    d = [(1, 0, ['|', 'L', 'J']), (0, -1, ['-', 'L', 'F'])]

                # F is a 90-degree bend connecting south and east.
                case 'F':
                    d = [(1, 0, ['|', 'L', 'J']), (0, 1, ['-', 'J', '7'])]

                # S connects with all pipes that connect with it
                case 'S':
                    d = [
                        (1, 0, ['|', 'J', 'L']),  # Down
                        (0, 1, ['-', 'J', '7']),  # Right
                        (-1, 0, ['|', '7', 'F']),  # Up
                        (0, -1, ['-', 'F', 'L'])  # Left
                    ]

            for dr, dc, types in d:
                if 0 <= r + dr < R and 0 <= c + dc < C:
                    rr = r + dr
                    cc = c + dc

                    # We only add nodes that actually connect to this pipe
                    if grid[rr][cc] in types:
                        G.add_edge((r, c), (rr, cc))

    print(G)
    print(G.edges)

    # Find the longest path starting from S
    T = 0
    for node in G.nodes:
        print(node)
        paths = nx.all_simple_paths(G, S, node, cutoff=None)
        for p in paths:
            print("- ", p)
            T = max(T, len(p))

    print(T)
    return T


# Part 1
assert parse_file('test.txt') == 4
assert parse_file('test2.txt') == 4
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
