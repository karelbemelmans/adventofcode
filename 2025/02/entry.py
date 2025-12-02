#!/usr/bin/env python3


def is_valid(s):

    # Cast our integer to a string
    s = str(s)
    l = len(s)

    # Uneven strings are always valid
    if l % 2 == 1:
        return True

    if s[0 : l // 2] == s[l // 2 :]:
        return False

    return True


def is_valid2(s):

    # Cast our integer to a string
    s = str(s)
    l = len(s)

    # Define the length borders of our patterns
    # A pattern can be as little as 1 char
    pattern_lmin = 1
    # And max the half length of the string
    pattern_lmax = l // 2

    # Go over all possible substring lengths
    for i in range(pattern_lmin, pattern_lmax + 1):

        # If pattern length is i, we have l // i as a length of our substring
        x = l // i

        p = s[0:i]

        # Glue the x occurences together, do they form the input string?
        if p * x == s:
            return False

    return True


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        data = fp.read()

    count = 0

    # Fun with python
    parts = [[int(x) for x in t.split("-")] for t in data.split(",")]

    for start, end in parts:
        for x in range(start, end + 1):
            if p2 and not is_valid2(x):
                print("invalid: ", x)
                count += x
            elif not is_valid(x):
                count += x

    return count


# Part 1
assert parse_file("example.txt") == 1227775554
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 4174379265
print("Part 2: ", parse_file("input.txt", True))
