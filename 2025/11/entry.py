#!/usr/bin/env python3

import sys
import networkx as nx


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        lines = (line.split(": ") for line in fp.read().splitlines())

    # Build our Graph
    G = nx.DiGraph()
    [G.add_edge(a, b) for a, l in lines for b in l.split(" ")]

    # networkx is awesome
    P = nx.all_simple_paths(G, "you", "out", cutoff=None)
    return len(list(P))


# Part 1
assert parse_file("example.txt") == 5
print("Part 1: ", parse_file("input.txt"))

# Part 2
# assert parse_file('test.txt', True) == 0
# print("Part 2: ", parse_file('input.txt', True))
