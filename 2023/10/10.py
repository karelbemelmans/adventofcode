#!/usr/bin/env python3

from collections import deque, defaultdict
import networkx as nx

DIR = {
    (-1, 0): 'Up',
    (1, 0): 'Down',
    (0, -1): 'Left',
    (0, 1): 'Right'
}


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

                case '|' | '-' | 'L' | 'J' | '7' | 'F':
                    G.add_node((r, c))

    # Find edges we need to add
    for r in range(R):
        for c in range(C):

            d = []  # directions and valid types per direction
            match grid[r][c]:

                # | is a vertical pipe connecting north and south.
                case '|':
                    d = [
                        (-1, 0, ['|', 'F', '7']),  # Up
                        (1, 0, ['|', 'J', 'L'])  # Down
                    ]

                # - is a horizontal pipe connecting east and west.
                case '-':
                    d = [
                        (0, -1, ['-', 'L', 'F']),  # Left
                        (0, 1, ['-', 'J', '7'])  # Right
                    ]

                # L is a 90-degree bend connecting north and east.
                case 'L':
                    d = [
                        (-1, 0, ['|', '7', 'F']),  # Up
                        (0, 1, ['-', 'J', '7'])  # Righjt
                    ]

                # J is a 90-degree bend connecting north and west.
                case 'J':
                    d = [
                        (-1, 0, ['|', '7', 'F']),  # Up
                        (0, -1, ['-', 'L', 'F'])  # Left
                    ]

                # 7 is a 90-degree bend connecting south and west.
                case '7':
                    d = [
                        (1, 0, ['|', 'L', 'J']),  # Down
                        (0, -1, ['-', 'L', 'F'])  # Left
                    ]

                # F is a 90-degree bend connecting south and east.
                case 'F':
                    d = [
                        (1, 0, ['|', 'L', 'J']),  # Down
                        (0, 1, ['-', 'J', '7'])  # Right
                    ]

                # S connects with all pipes that connect with it
                case 'S':
                    d = [
                        (1, 0, ['|', 'J', 'L']),  # Down
                        (0, 1, ['-', 'J', '7']),  # Right
                        (-1, 0, ['|', '7', 'F']),  # Up
                        (0, -1, ['-', 'F', 'L'])  # Left
                    ]

            for dr, dc, types in d:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < R and 0 <= cc < C:

                    # We only add nodes that actually connect to this pipe
                    if grid[rr][cc] in types:
                        G.add_edge((r, c), (rr, cc))

    # Print the grid
    # for r in range(R):
    #     for c in range(C):
    #         try:
    #             l = nx.dijkstra_path_length(G, S, (r, c))
    #             if l > 9:
    #                 l = 'X'
    #             print(l, end='')
    #         except nx.NetworkXNoPath:
    #             print(".", end='')

    #     print("")

    # print(G)
    # print(G.nodes)
    # print(G.edges)

    # Find the longest path starting from S
    T = 0
    longest = None
    for node in G.nodes:
        try:
            l = nx.dijkstra_path_length(G, S, node)
            T = max(T, l)
        except nx.NetworkXNoPath:
            continue

    if p2:
        print(longest, len(longest) - 1)

    else:
        return T


# Part 1
assert parse_file('test.txt') == 4
assert parse_file('test-complex.txt') == 4

assert parse_file('test2.txt') == 8
assert parse_file('test2-complex.txt') == 8

print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('test3.txt', True) == 4
# assert parse_file('test4.txt', True) == 8
# print("Part 2: ", parse_file('input.txt', True))
