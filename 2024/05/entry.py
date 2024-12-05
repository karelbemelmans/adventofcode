#!/usr/bin/env python3


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        rules, lines = [line for line in fp.read().split("\n\n")]

    R = [(int(a), int(b)) for a, b in [rule.split("|") for rule in rules.splitlines()]]

    def valid(numbers):
        for i in range(len(numbers)):
            print(i, numbers[i])

            # Before
            # After

        return True

    T = 0
    for line in lines.splitlines():
        numbers = [int(num) for num in line.split(",")]
        print(numbers)

        if valid(numbers):
            T += numbers[int(len(numbers)/2)]

    print("T: ", T)
    return T


# Part 1
assert parse_file('example.txt') == 143
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('example.txt', True) == 31
# print("Part 2: ", parse_file('input.txt', True))
