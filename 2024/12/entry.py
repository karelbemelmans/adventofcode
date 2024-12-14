#!/usr/bin/env python3

import sys


def edge(ps, p2=False):
    P = {(p, d) for d in (+1, -1, +1j, -1j) for p in ps if p+d not in ps}

    if p2:
        return P - {(p+d*1j, d) for p, d in P}
    else:
        return P


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        grid = {i+j*1j: c for i, row in enumerate(fp.read().splitlines())
                for j, c in enumerate(row.strip())}

    sets = {p: {p} for p in grid}

    # Build up our regions in the grid
    for p in grid:
        for n in p+1, p-1, p+1j, p-1j:
            if n in grid and grid[p] == grid[n]:
                sets[p] |= sets[n]
                for x in sets[p]:
                    sets[x] = sets[p]

    sets = {tuple(s) for s in sets.values()}

    return sum((len(s) * len(edge(s, p2)) for s in sets))


def main():
    # Part 1
    assert parse_file('example.txt') == 140
    assert parse_file('example2.txt') == 772
    assert parse_file('example3.txt') == 1930
    print("Part 1: ", parse_file('input.txt'))

    # Part 2
    assert parse_file('example.txt', True) == 80
    assert parse_file('example3.txt', True) == 1206
    print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
