#!/usr/bin/env python3


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        rules, lines = [line for line in fp.read().split("\n\n")]

    R = [(int(a), int(b)) for a, b in [rule.split("|") for rule in rules.splitlines()]]

    def valid(numbers):
        for i in range(len(numbers)):

            # Go over all numbers in this list and check if the order is correct
            for k in range(len(numbers)):

                # Before
                if k < i:
                    if not (numbers[k], numbers[i]) in R:
                        return False

                # After
                elif k > i:
                    if not (numbers[i], numbers[k]) in R:
                        return False

        return True

    T = 0
    for line in lines.splitlines():
        numbers = [int(num) for num in line.split(",")]

        if valid(numbers):
            T += numbers[int(len(numbers)/2)]

    return T


# Part 1
assert parse_file('example.txt') == 143
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('example.txt', True) == 31
# print("Part 2: ", parse_file('input.txt', True))
