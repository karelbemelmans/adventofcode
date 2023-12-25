#!/usr/bin/env python3

import sys
import networkx as nx


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = (line.split(": ") for line in fp.read().splitlines())

    # Build our Graph
    G = nx.Graph()
    [G.add_edge(a, b) for a, l in lines for b in l.split(' ')]

    # networkx is awesome
    cutsets = list(nx.minimum_edge_cut(G))
    if len(cutsets) == 3:
        G.remove_edges_from(cutsets)
        x = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
        return x[0] * x[1]


def main():
    # Part 1
    assert parse_file('test.txt') == 54
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    # assert parse_file('test.txt', True) == 0
    # print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
