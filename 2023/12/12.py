#!/usr/bin/env python3

from collections import deque, defaultdict
from itertools import groupby, permutations, product


def spring_matches_pattern(springs, pattern):
    m = len(pattern) - 1
    i = 0
    for k, g in groupby(springs):

        l = len(list(g))  # nr of times this char occurs in this block
        if k == "#":
            if i > m:
                return False

            if l != pattern[i]:
                return False
            i += 1
    else:
        # We only return if we had the exact amount of matches needed for the pattern
        if i == len(pattern):
            return True


def replace_chars(input, chars):
    new = ""
    for i, c in enumerate(input):
        if c == '?':
            new += chars.popleft()
        else:
            new += c

    # Did we replace all chars needed?
    assert (len(chars) == 0)
    return new


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        lines = [[pairs for pairs in line.split()]
                 for line in fp.read().splitlines()]

    T = 0
    for springs, b in lines:
        t = 0
        pattern = [int(n) for n in b.split(',')]

        if p2:
            springs += ('?' + springs)*4
            pattern = pattern*5

        print("LINE: ", springs, pattern)

        # Count nr of questionmarks in the input
        c = springs.count('?')

        # Generate all possible combinations of . and # of length c
        P = [deque(n, maxlen=c) for n in
             [''.join(seq) for seq in
              product(".#", repeat=c)]]

        print("Possible combinations: ", len(P))
        for p in P:
            new = replace_chars(springs, p)
            if spring_matches_pattern(new, pattern):
                t += 1
        print("score: ", t)
        T += t

    print("SOLUTION: ", T)
    return T


# Part 1
# assert parse_file('test.txt') == 5
# assert parse_file('test2.txt') == 21
# print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test2.txt', True) == 525152
# print("Part 2: ", parse_file('input.txt', True))
