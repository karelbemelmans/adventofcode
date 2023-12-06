#!/usr/bin/env python3

from collections import deque, defaultdict
from functools import reduce


def parse_file(file, p2=False):

    times, distances = open(file).read().splitlines()

    times = list(map(int, times.split(":")[1].split()))
    distances = list(map(int, distances.split(":")[1].split()))

    # Turn our list into one big number
    if p2:
        times = [int(reduce(lambda a, b: str(a)+str(b), times))]
        distances = [int(reduce(lambda a, b: str(a)+str(b), distances))]

    winners = defaultdict(int)
    for i in range(len(times)):
        for j in range(times[i]):
            d = (times[i] - j) * j

            if d > distances[i]:
                winners[i] += 1

    return reduce(lambda a, b: a*b, winners.values())


# Part 1
assert parse_file('test.txt') == 288
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 71503
print("Part 2: ", parse_file('input.txt', True))
