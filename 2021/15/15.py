import networkx as nx
from collections import defaultdict


# Helper function to visualize our points on a grid
def print_grid(grid):
    R = len(grid)
    for r in range(R):
        print(grid[r])


def blow_up(grid, times=5):
    R = len(grid)
    C = len(grid[0])

    # We make a new, empty, bigger grid
    new = [[0] * (C * times) for _ in range(R * times)]

    for r in range(R):
        for c in range(C):
            new[r][c] = grid[r][c]

            # Every point gets added times-1 in each direction
            for i in range(0, times):
                rr = r + (R * i)
                for j in range(0, times):
                    cc = c + (C * j)

                    # Ugly, but i works?
                    value = (grid[r][c] + i + j) % 9
                    if value == 0:
                        value = 9

                    new[rr][cc] = value

    return new


def parse_grid(grid, p2=False):
    R = len(grid)
    C = len(grid[0])

    G = nx.DiGraph()

    # Add all our nodes to the graph
    for r in range(R):
        for c in range(C):
            G.add_node((r, c), pos=[r, c])

    # Add the edges
    for r in range(R):
        for c in range(C):

            # Every point has an edge to another point up and down
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                rr = r + dr
                cc = c + dc
                if not (dr == 0 and dc == 0) and (0 <= rr < R) and (0 <= cc < C):
                    weight = grid[rr][cc]
                    G.add_edge((r, c), (rr, cc), weight=weight)

    path = nx.dijkstra_path(G, 0, R * C - 1, weight="weight")
    return nx.path_weight(G, path, weight="weight")


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        grid = [[int(char) for char in line] for line in fp.read().splitlines()]

    # Blow up our grid?
    if p2:
        grid = blow_up(grid)

    weight = parse_grid(grid)
    return weight


# Part 1
assert parse_file('test.txt') == 40
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('mini.txt', True) == 37
assert parse_file('test.txt', True) == 315
print("Part 2: ", parse_file('input.txt', True))
