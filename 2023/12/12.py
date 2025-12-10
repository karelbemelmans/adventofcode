#!/usr/bin/env python3

from functools import cache


@cache
def dp(springs, pattern):
    T = 0

    # Are we done with the iteration?
    if not pattern:
        return 1 if "#" not in springs else 0

    # Generate possible values for the current iteration
    for pos in range(
        len(springs) - sum(pattern[1:]) + len(pattern[1:]) - pattern[0] + 1
    ):
        possible = "." * pos + "#" * pattern[0] + "."

        for spring, possible_spring in zip(springs, possible):
            if spring != possible_spring and spring != "?":
                break
        else:
            T += dp(springs[len(possible) :], pattern[1:])

    return T


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        lines = [[pairs for pairs in line.split()] for line in fp.read().splitlines()]

    T = 0
    for springs, b in lines:

        # We need a tuple here because of the use of @cache
        # A tuple is immutable, a list item is not immutable
        pattern = tuple(int(n) for n in b.split(","))

        # This seems to be the most Python-ish way to do this
        if p2:
            springs = "?".join([springs] * 5)
            pattern = pattern * 5

        T += dp(springs, pattern)

    return T


# Part 1
assert parse_file("test.txt") == 1
assert parse_file("test2.txt") == 21
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test.txt", True) == 1
assert parse_file("test2.txt", True) == 525152
print("Part 2: ", parse_file("input.txt", True))
