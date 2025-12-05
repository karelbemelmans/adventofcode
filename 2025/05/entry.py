#!/usr/bin/env python3
from functools import reduce


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        fresh, ingredients = [line for line in fp.read().split("\n\n")]

    F = sorted(
        {(int(a), int(b)) for a, b in [rule.split("-") for rule in fresh.splitlines()]}
    )

    if p2:

        return sum(
            end - start + 1  # Calculate range size (inclusive)
            # Merge all the overlapping ranges into a new range
            for start, end in reduce(
                lambda m, x: (
                    # If ranges overlap or are adjacent (x[0] <= m[-1][1] + 1):
                    # Merge by extending the last range's end to max of both ends
                    m[:-1] + [[m[-1][0], max(m[-1][1], x[1])]]
                    if m and x[0] <= m[-1][1] + 1
                    # Otherwise, ranges don't overlap - add as separate range
                    else m + [x]
                ),
                F,  # Input: sorted list of (start, end) tuples
                [],  # Initial accumulator: empty list of merged ranges
            )
        )

    else:
        return sum(
            any(f[0] <= int(x) <= f[1] for f in F) for x in ingredients.splitlines()
        )


# Part 1
assert parse_file("example.txt") == 3
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 14
print("Part 2: ", parse_file("input.txt", True))
