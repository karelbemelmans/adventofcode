from pprint import pprint
from collections import defaultdict

# Inspired by https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/7.py
#
# The key learning was: when adding size, add them to all the directories
#                       in the current path up to the root. This way we do not
#                       need to do a 2nd run.


def parse_lines(lines):

    # dir path is the key in S, value is the size of the dir and below
    S = defaultdict(int)
    P = []

    for line in lines:
        words = line.strip().split(" ")

        if words[1] == "cd":
            # We go one dir back
            if words[2] == "..":
                P.pop()

            # We go one level deeper
            else:
                P.append(words[2])

        elif words[1] == "ls":
            continue

        elif words[0] == "dir":
            continue

        # Otherwise it's file
        else:
            size = int(words[0])

            # Add to all parents
            for i in range(1, len(P) + 1):
                S["/".join(P[:i])] += size

    return S


def parse_file(file, p2=False):
    with open(file, "r") as fp:
        lines = [x for x in fp.read().splitlines()]

    S = parse_lines(lines)

    max = 70000000 - 30000000
    total = S["/"]
    need = total - max

    # Find the min between the values and something big
    if p2:
        big = 1e9
        for p, size in S.items():
            if size >= need:
                big = min(big, size)
        return big

    else:
        total = 0
        for p, size in S.items():
            if size <= 100000:
                total += size
        return total


assert parse_file("test.txt") == 95437
print("Part 1: ", parse_file("input.txt"))

assert parse_file("test.txt", True) == 24933642
print("Part 2: ", parse_file("input.txt", True))
