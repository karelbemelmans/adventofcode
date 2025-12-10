#!/usr/bin/env python3
#
# https://www.reddit.com/r/adventofcode/comments/18o7014/comment/kefvjex/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
#
# I spent quite a time writing a very long and explicit process
# This code does the same but in a much much more elegant Python way...

import sys
import numpy as np


def drop(stack, skip=None):

    # Our input does not go beyond 12,12 for x,y so we can assume this box size
    peaks = np.zeros((12, 12))
    falls = 0

    for i, (u, v, w, x, y, z) in enumerate(stack):
        if i == skip:
            continue

        peak = peaks[u:x, v:y].max()
        peaks[u:x, v:y] = peak + z - w

        stack[i] = u, v, peak, x, y, peak + z - w
        falls += peak < w

    return not falls, falls


def parse_file(file, p2=False):

    # We load our numbers into a numpy array
    # e.g the test input will be:
    #
    # [[1 0 1 1 2 1]
    #  [0 0 2 2 0 2]
    #  [0 2 3 2 2 3]
    #  [0 0 4 0 2 4]
    #  [2 0 5 2 2 5]
    #  [0 1 6 2 1 6]
    #  [1 1 8 1 1 9]]
    #
    stack = np.fromregex(file, r"\d+", [("", int)]).reshape(-1, 6).astype(int)

    # We sort the input on ascending z value and add 1 to the x,y,z values
    stack = stack[stack[:, 2].argsort()] + [0, 0, 0, 1, 1, 1]
    print("After sorting: ")
    print(stack)

    # We then perform an initial drop to get all the pieces of our "jenga tower"
    # to fall into their correct places.
    drop(stack)
    print("After initial drop: ")
    print(stack)

    # Perform another drop with skipping a block every time
    # Output is nr of blocks that fall and nr. of blocks that do not fall
    res = np.sum([drop(stack.copy(), skip=i) for i in range(len(stack))], axis=0)
    return res[1 if p2 else 0]


def main():
    # Part 1
    assert parse_file("test.txt") == 5
    # print("Part 1: ", parse_file('input.txt'))

    # Part 2
    # assert parse_file('test.txt', True) == 7
    # print("Part 2: ", parse_file('input.txt', True))


if __name__ == "__main__":
    sys.exit(main())
