#!/usr/bin/env python

import copy

with open("input.txt", "r") as fp:
    L = [list(x) for x in fp.read().splitlines()]

ON = set()

# We build our input set:
#   - we use a r(ow) and c(ol) grid here
#   - r(ow,) l(ine), c(olumn), ch(ar)
# ... and build the input into a map M we can use to run over.
#
# ON is a set of x,y,z, w coords that have the value #
#
for r, l in enumerate(L):
    for c, ch in enumerate(l):
        if ch == "#":
            ON.add((r, c, 0, 0))

# We now loop over this map 6 times to calculate the new values
# Brute force, let's see if this gets us there...
for _ in range(6):
    NEW_ON = set()

    # We set a hard boundary here because we know the grid grows by a fixed amount every time
    # 8x8 grid in 6 steps, grows to 14x14
    for x in range(-15, 15):
        for y in range(-15, 15):
            for z in range(-8, 8):
                for w in range(-8, 8):

                    nbr = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            for dz in [-1, 0, 1]:
                                for dw in [-1, 0, 1]:

                                    # We need to exclude ourselves
                                    if not (
                                        dx == 0 and dy == 0 and dz == 0 and dw == 0
                                    ):
                                        if (x + dx, y + dy, z + dz, w + dw) in ON:
                                            nbr += 1

                    if (x, y, z, w) in ON and nbr in [2, 3]:
                        NEW_ON.add((x, y, z, w))
                    elif (x, y, z, w) not in ON and nbr == 3:
                        NEW_ON.add((x, y, z, w))

    ON = NEW_ON

# The result is the number of items in ON
print(len(ON))
