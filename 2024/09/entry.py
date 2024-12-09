#!/usr/bin/env python3

from collections import deque


def checksum(data):
    T = 0

    i = 0
    for x in data:
        if not x == ".":
            T += i * x
            i += 1

    return T


def explode(data):

    # input:   12345
    # output: [0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]

    output = []

    id = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            for _ in range(x):
                output.append(id)
            id += 1
        else:
            for _ in range(x):
                output.append(".")

    return output


def compact(data):
    new = []
    Q = deque(data)

    # We loop over the string from the start
    # If we see an empty space, we pop an item off the end and replace it.
    while Q:
        item = Q.popleft()
        if item == "." and Q:

            # Find the first non-dot char from the end
            while Q:
                pop = Q.pop()
                if not pop == ".":
                    new.append(pop)
                    break
        else:
            new.append(item)

    return new


def parse_file(file, p2=False):

    with open(file, 'r') as fp:
        data = [int(char) for char in fp.readline().strip()]

    data = explode(data)

    data = compact(data)

    T = checksum(data)
    return T


# Part 1
assert parse_file('example2.txt') == 60
assert parse_file('example.txt') == 1928
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('example.txt', True) == 34
# print("Part 2: ", parse_file('input.txt', True))
