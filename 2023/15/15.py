#!/usr/bin/env python3

from collections import deque, defaultdict


def do_hash(str):
    cur = 0

    for char in str:
        cur += ord(char)
        cur *= 17
        cur %= 256

    return cur


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        pieces = [line for line in fp.read().splitlines()][0].split(",")

    # Let's get p1 out of the way
    if not p2:
        return sum(map(do_hash, pieces))

    # p2
    BOXES = defaultdict(list)

    for p in pieces:

        if p.count("="):
            box, val = p.split("=")
            val = int(val)
            cur = do_hash(box)

            # If there is already a lens in the box with the same label, replace the old lens with the new lens:
            # remove the old lens and put the new lens in its place, not moving any other lenses in the box.
            for i in range(0, 10):
                if (box, i) in BOXES[cur]:
                    BOXES[cur] = [
                        x if x != (box, i) else (box, val) for x in BOXES[cur]
                    ]
                    break

            # If there is not already a lens in the box with the same label, add the lens to the box immediately behind
            # any lenses already in the box. Don't move any of the other lenses when you do this. If there aren't any
            # lenses in the box, the new lens goes all the way to the front of the box.
            else:
                BOXES[cur].append((box, val))

        elif p.count("-"):
            box, _ = p.split("-")
            cur = do_hash(box)
            for i in range(0, 10):
                if (box, i) in BOXES[cur]:
                    BOXES[cur].remove((box, i))
                    break

    # Calculate p2 score
    T = 0
    for box in BOXES:
        for i, slot in enumerate(BOXES[box]):
            T += (box + 1) * (i + 1) * slot[1]
    return T


# Part 1
assert parse_file("hash.txt") == 52
assert parse_file("test.txt") == 1320
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert parse_file("test.txt", True) == 145
print("Part 2: ", parse_file("input.txt", True))
