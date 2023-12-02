#!/usr/bin/env python3

from collections import deque, defaultdict


def look_and_say_string(string):
    R = []
    current = None
    count = 0

    for char in string:

        # We are still in the same char? Add 1 to counter
        if current:
            if char == current:
                count += 1

            else:
                R.append(str(count))
                R.append(current)
                current = char
                count = 1

        else:
            current = char
            count = 1

    # Last step is adding the current
    R.append(str(count))
    R.append(current)

    return R


def parse_string(string, times=40, p2=False):

    for i in range(times):
        string = look_and_say_string(string)

    return len(string)


# Part 1
assert parse_string('1', 1) == 2
assert parse_string('11', 1) == 2
assert parse_string('21', 1) == 4
assert parse_string('1211', 1) == 6
assert parse_string('111211', 1) == 6
assert parse_string('1', 4) == 6
print("Part 1: ", parse_string('3113322113', 40))

# Part 2
print("Part 1: ", parse_string('3113322113', 50))
