#!/usr/bin/env python3
import math
from itertools import product


def distance(pair):
    return sum((x - y) ** 2 for x, y in zip(*pair)) ** 0.5


def find(p, n):
    while n != p[n]:
        p[n] = p[p[n]]
        n = p[n]
    return n


def parse_file(file, c=10, p2=False):
    with open(file, "r") as fp:
        nodes = [tuple(map(int, line.split(","))) for line in fp.read().splitlines()]

    # pairs of edges, sorted by distance asc
    edges = sorted((p for p in product(nodes, nodes) if p[0] < p[1]), key=distance)

    # product of our nodes
    p = {n: n for n in nodes}

    if p2:
        clusters = len(nodes)

        for u, v in edges:
            if (r1 := find(p, u)) != (r2 := find(p, v)):
                p[r2] = r1
                if (clusters := clusters - 1) == 1:
                    return u[0] * v[0]

    else:
        s = {n: 1 for n in nodes}

        for u, v in edges[:c]:
            if (r1 := find(p, u)) != (r2 := find(p, v)):
                p[r2] = r1
                s[r1] += s[r2]
                s[r2] = 0

        return (S := sorted(s.values()))[-1] * S[-2] * S[-3]


# Part 1
assert parse_file("example.txt", c=10) == 40
print("Part 1: ", parse_file("input.txt", c=1000))

# Part 2
assert parse_file("example.txt", p2=True) == 25272
print("Part 2: ", parse_file("input.txt", p2=True))
