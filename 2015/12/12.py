#!/usr/bin/env python3

from json import loads


def n(j, p2=False):
    if type(j) == int:
        return j

    if type(j) == list:
        return sum([n(j, p2) for j in j])

    if type(j) != dict:
        return 0

    if p2 and 'red' in j.values():
        return 0

    return n(list(j.values()), p2)


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    S = 0
    for line in lines:
        data = loads(line)
        S += n(data, p2)

    return S


# Part 1
assert parse_file('test.txt') == 6+6+3+3+0+0
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test2.txt', True) == 6+4+0+6
print("Part 2: ", parse_file('input.txt', True))
