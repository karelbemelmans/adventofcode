#!/usr/bin/env python3
from functools import cmp_to_key


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        rules, lines = [line for line in fp.read().split("\n\n")]

    R = [(int(a), int(b)) for a, b in [rule.split("|") for rule in rules.splitlines()]]

    def valid(numbers):
        for i in range(len(numbers)):

            # Go over all numbers in this list and check if the order is correct
            for k in range(len(numbers)):

                # Before
                if k < i and not (numbers[k], numbers[i]) in R:
                    return False

                # After
                elif k > i and not (numbers[i], numbers[k]) in R:
                    return False

        return True

    def correct(numbers):
        return sorted(numbers, key=cmp_to_key(lambda a, b: 1 if (a, b) in R else -1))

    T = 0
    for line in lines.splitlines():
        numbers = [int(num) for num in line.split(",")]

        if p2:
            if not valid(numbers):
                corrected = correct(numbers)
                T += corrected[int(len(corrected)/2)]

        else:
            if valid(numbers):
                T += numbers[int(len(numbers)/2)]

    return T


# Part 1
assert parse_file('example.txt') == 143
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 123
print("Part 2: ", parse_file('input.txt', True))
