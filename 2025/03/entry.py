#!/usr/bin/env python3


def max_single_digit_index(bank):
    return bank.index(str(max(int(b) for b in bank)))


def max_joltage(bank, remaining):
    if remaining == 0:
        return ""

    # The largest 12-digit number is simply the largest of the all but the last 11 digits,
    # followed by the largest 11-digit number of the remaining digits.
    index = max_single_digit_index(bank[: 1 + len(bank) - remaining])

    # number + recursive result on the rest of the string
    return bank[index] + max_joltage(bank[index + 1 :], remaining - 1)


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        banks = [line for line in fp.read().splitlines()]

    C = 12 if p2 else 2

    return sum(int(max_joltage(bank, C)) for bank in banks)


# Part 1
assert parse_file("example.txt") == 357
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("example.txt", True) == 3121910778619
print("Part 2: ", parse_file("input.txt", True))
