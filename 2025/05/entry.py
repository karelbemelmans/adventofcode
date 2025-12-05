#!/usr/bin/env python3
from functools import reduce


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        fresh, ingredients = [line for line in fp.read().split("\n\n")]

    F = sorted(
        {(int(a), int(b)) for a, b in [rule.split("-") for rule in fresh.splitlines()]}
    )
    T = 0

    if p2:

        # Merge all the overlapping ranges into a new range
        reduced = reduce(
            lambda m, x: (
                m[:-1] + [[m[-1][0], max(m[-1][1], x[1])]]
                if m and x[0] <= m[-1][1] + 1
                else m + [x]
            ),
            F,
            [],
        )

        T = sum(end - start + 1 for start, end in reduced)

    else:
        T = sum(
            any(f[0] <= int(x) <= f[1] for f in F) for x in ingredients.splitlines()
        )

    print(T)
    return T


# Part 1
assert parse_file("example.txt") == 3
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 14
print("Part 2: ", parse_file("input.txt", True))
