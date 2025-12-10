#!/usr/bin/env python3

from itertools import groupby


def look_and_say_string(string):
    s = ""
    for k, g in groupby(string):
        s += str(len(list(g))) + str(k)
    return s


def parse_string(string, times=40, p2=False):
    for _ in range(times):
        string = look_and_say_string(string)
    return len(string)


# Part 1
assert parse_string("1", 1) == 2
assert parse_string("11", 1) == 2
assert parse_string("21", 1) == 4
assert parse_string("1211", 1) == 6
assert parse_string("111211", 1) == 6
assert parse_string("1", 4) == 6
print("Part 1: ", parse_string("3113322113", 40))

# Part 2
print("Part 2: ", parse_string("3113322113", 50))
