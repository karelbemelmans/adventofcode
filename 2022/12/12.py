#!/usr/bin/env python3

import networkx as nx


def print_grid(grid):
    R = len(grid)
    for r in range(R):
        print(grid[r])


def parse_grid(grid, p2=False):
    R = len(grid)
    C = len(grid[0])

    G = nx.DiGraph()

    S = False
    E = False

    # Find S and E
    # This can probably be done more efficiently
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                S = (r, c)
                grid[r][c] = "a"
            elif grid[r][c] == "E":
                E = (r, c)
                grid[r][c] = "z"

    # Add the edges
    for r in range(R):
        for c in range(C):
            G.add_node((r, c), pos=[r, c])

            # Every point has an edge to another point up and down, left and right
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                rr = r + dr
                cc = c + dc
                if (0 <= rr < R) and (0 <= cc < C):
                    # We only add an edge if the step is not too big
                    weight = ord(grid[rr][cc]) - ord(grid[r][c])
                    if weight <= 1:
                        G.add_edge((r, c), (rr, cc), weight=1)

    starts = []
    if p2:
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "a":
                    starts.append((r, c))
    else:
        starts = [S]

    # Take a good default for the max
    L = R * C

    for s in starts:
        try:
            path = nx.dijkstra_path(G, s, E, weight="weight")
            L = min(L, len(path))
        except:
            do = False

    # We need to remove one edge since we are already on the start so the
    # node (0,0) does not need to be counted in path
    return L - 1


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        grid = [[char for char in line] for line in fp.read().splitlines()]

    return parse_grid(grid, p2)


# Part 1
assert parse_file("test.txt") == 31
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test.txt", True) == 29
print("Part 2: ", parse_file("input.txt", True))
