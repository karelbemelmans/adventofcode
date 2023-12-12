#!/usr/bin/env python3

# Global cache to speed up the process
cache = {}


def generate_lines(springs: str, pattern: list[int]) -> int:
    global cache
    key = hash(springs + str(pattern))

    # Cache hit?
    if key in cache.keys():
        return cache[key]

    # Are we done with the iteration?
    if not pattern:
        return '#' not in springs

    T = 0
    for pos in range(len(springs) - sum(pattern[1:]) + len(pattern[1:]) - pattern[0] + 1):
        possible = '.' * pos + '#' * pattern[0] + '.'

        for spring, possible_spring in zip(springs, possible):
            if spring != possible_spring and spring != '?':
                break
        else:
            T += generate_lines(springs[len(possible):], pattern[1:])

    cache[key] = T
    return T


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [[pairs for pairs in line.split()]
                 for line in fp.read().splitlines()]

    T = 0
    for springs, b in lines:
        pattern = [int(n) for n in b.split(',')]

        # This seems to be the most Python-ish way to do this
        if p2:
            springs = "?".join([springs] * 5)
            pattern = pattern*5

        T += generate_lines(springs, pattern)

    return T


# Part 1
assert parse_file('test.txt') == 1
assert parse_file('test2.txt') == 21
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 1
assert parse_file('test2.txt', True) == 525152
print("Part 2: ", parse_file('input.txt', True))
