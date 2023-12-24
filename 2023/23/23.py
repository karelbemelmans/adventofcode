#!/usr/bin/env python3
#
# Solution from: https://www.reddit.com/r/adventofcode/comments/18oy4pc/comment/keodhrv/?utm_source=share&utm_medium=web2x&context=3
#
# First time I see someone use complex numbers: https://docs.python.org/2/library/functions.html#complex
# I guess this is a very easy hack to represent a 2D grid

import sys
from collections import deque, defaultdict

NDIRS = {'>': 1, '^': -1j, '<': -1, 'v': 1j}
def n4(p): return [p - 1j, p - 1, p + 1, p + 1j]


def find_adjacent(start, grid, terminals, ndirs):
    adj, q = [], [(start, 0, {start})]
    while q:
        p, l, seen = q.pop(0)
        if p in terminals and p != start:
            adj.append((p, l))
            continue

        neighbors = [n for n in n4(p) if n in grid and n not in seen and grid[n] != '#']
        if len(neighbors) > 1 and p != start:
            adj.append((p, l))
            continue

        for n in neighbors:
            if ndirs and grid[n] in NDIRS and n + NDIRS[grid[n]] != p:
                q.append((n + NDIRS[grid[n]], l+2, seen | {n, n+NDIRS[grid[n]]}))
            elif grid[n] == '.' or not ndirs:
                q.append((n, l+1, seen | {n}))
    return adj


# Transforms our grid to a graph of nodes and edges
def build_graph(grid, start, end, ndirs):
    graph, seen, q = defaultdict(list), set(), [start]
    while q:
        p = q.pop()
        if p in seen:
            continue
        seen.add(p)
        for n, l in find_adjacent(p, grid, [start, end], ndirs):
            graph[p].append((n, l))
            if n not in seen:
                q.append(n)

    return graph


# Find the longest path in a graph
def longest_path(graph, start, end):
    longest, q = 0, [(start, 0, {start})]
    while q:
        p, l, seen = q.pop()
        if p == end:
            longest = max(longest, l)
            continue
        for n, nl in graph[p]:
            if n not in seen:
                q.append((n, l+nl, seen | {n}))
    return longest


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        grid = {x+1j*y: c for y, l in enumerate(open(file).readlines()) for x, c in enumerate(l.strip())}

    start, end = 1, max(p.real for p in grid) - 1 + 1j*max(p.imag for p in grid)

    # p2 is the same question except the slope limitations are turned off
    # This will give us a much larger graph
    graph = build_graph(grid, start, end, False if p2 else True)
    return longest_path(graph, start, end)


def main():
    # Part 1
    assert parse_file('test.txt') == 94
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    assert parse_file('test.txt', True) == 154
    print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
