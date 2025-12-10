#!/usr/bin/env python3

import sys
from collections import deque, defaultdict


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    return 0


def main():
    # Part 1
    assert parse_file("test.txt") == 0
    print("Part 1: ", parse_file("input.txt"))

    # Part 2
    assert parse_file("test.txt", True) == 0
    print("Part 2: ", parse_file("input.txt", True))


if __name__ == "__main__":
    sys.exit(main())
