#!/usr/bin/env python3
from functools import reduce
from collections import deque, defaultdict
from operator import add, mul


def parse_file(file):
    with open(file, "r") as fp:
        rows = [line.split() for line in fp.read().splitlines()]

    # Last row is the operators
    operators = rows.pop()

    # Swap columns and rows
    numbers = list(zip(*rows))

    # Use sum() with operator functions for cleaner code
    op_func = {"+": add, "*": mul}

    return sum(
        reduce(op_func[operators[i]], map(int, n)) for i, n in enumerate(numbers)
    )


def parse_file2(file):
    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    # We transpose the input so we get empty lines to separate the blocks
    transpose = list(zip(*lines))

    # Split our big list of items into smaller blocks we can combine later
    blocks = defaultdict(list)
    i = 0
    for t in transpose:
        if all(x == " " for x in t):
            i += 1
            continue

        blocks[i].append(t)

    T = 0

    # Blocks are numbers we need to process together
    for i in blocks:

        # Last item of first list item is the operator
        operator = blocks[i][0][-1]

        # Glue back the numbers using list comprehension
        numbers = [int("".join(b[:-1])) for b in blocks[i]]

        # Use operator functions for cleaner code
        op_func = {"+": add, "*": mul}
        T += reduce(op_func[operator], numbers)

    return T


# Part 1
assert parse_file("example.txt") == 4277556
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file2("example.txt") == 3263827
print("Part 2: ", parse_file2("input.txt"))
