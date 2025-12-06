#!/usr/bin/env python3
from functools import reduce


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    print(lines)
    # Last row is the operators
    operators = lines.pop()
    print(operators)

    T = 0

    current = None
    numbers = []
    for i, op in enumerate(operators):
        # print(i, op)

        # We meet a new operator?
        if not op == "":
            current = op

        # We have an empty line?
        print(line[i])

        num = ""
        for j, line in enumerate(lines):
            print(line[i])
            num += line[i]

        print(num)
        numbers.append(int(num))
        print("new column")

    print(numbers)

    print(T)
    return T


# Part 2
assert parse_file("example.txt", True) == 3263827
print("Part 2: ", parse_file("input.txt", True))
