#!/usr/bin/env python3

letters = ['one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    T = 0
    for line in lines:

        numbers = []

        for i, char in enumerate(line):
            if char.isdigit():
                numbers.append(char)

            if p2:
                # We check all the digits we want to scan for
                for d, val in enumerate(letters):
                    # We make substrings from i to the end of the line and check for matches
                    if line[i:].startswith(val):
                        numbers.append(str(d + 1))

        T += int(numbers[0] + numbers[-1])

    return T


# Part 1
assert parse_file('test.txt') == 142
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test2.txt', True) == 281
print("Part 2: ", parse_file('input.txt', True))
