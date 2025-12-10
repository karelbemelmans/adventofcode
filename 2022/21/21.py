#!/usr/bin/env python3

from collections import defaultdict


def parse(lines, p2=False):

    low = 0
    high = 10000000000000

    while True:
        j = (low + high) // 2
        print(low, high, j)

        R = defaultdict(int)
        R["humn"] = j

        left = ""
        right = ""

        i = 0
        while i < len(lines):
            i += 1
            for k, v in lines:

                if k == "root":
                    left, _, right = v.split(" ")

                # p2 ignores humn
                if p2 and k == "humn":
                    continue

                # Operation
                if any(v.count(o) for o in ["+", "-", "*", "/"]):
                    a, op, b = v.split(" ")

                    if R[a] and R[b]:
                        if op == "+":
                            R[k] = R[a] + R[b]
                        elif op == "-":
                            R[k] = R[a] - R[b]
                        elif op == "*":
                            R[k] = R[a] * R[b]
                        elif op == "/":
                            R[k] = R[a] // R[b]

                # A literal value
                else:
                    R[k] = int(v)

            if not p2 and R["root"]:
                return R["root"]

        diff = R[left] - R[right]
        # print("diff", left, right, R[left], R[right], diff)
        if p2 and diff == 0:
            print("p2 result found:", R["humn"])
            return R["humn"]
        elif diff < 0:
            low = j + 1
        else:
            high = j - 1


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        lines = [
            [parts.strip() for parts in line.split(":")] for line in fp.readlines()
        ]

    return parse(lines, p2)


# Part 1
assert parse_file("test.txt") == 152
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 301
# print("Part 2: ", parse_file('input.txt', True))
