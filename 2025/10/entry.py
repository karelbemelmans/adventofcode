#!/usr/bin/env python3


def str_to_int(s):
    return int(s[::-1].replace("#", "1").replace(".", "0"), 2)


def bin_to_int(bits):
    return sum(1 << b for b in bits)


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        lines = fp.read().splitlines()

    T = 0
    for line in lines:
        parts = line.split()

        # We convert our input to base 10 numbers
        target = str_to_int(parts[0].replace("[", "").replace("]", ""))
        buttons = [bin_to_int(eval(b[:-1] + ",)")) for b in parts[1:-1]]

        s = set([0])

        # Use an XOR operation to "press" the button
        # Pressing a button twice returns the lights to the original position again
        while target not in s:
            s = {a ^ b for a in s for b in buttons}
            T += 1

    return T


# Part 1
assert parse_file("example.txt") == 7
print("Part 1: ", parse_file("input.txt"))

# Part 2
# assert parse_file("example.txt", p2=True) == 24
# print("Part 2: ", parse_file("input.txt", p2=True))
