#!/usr/bin/env python3

# I guess part 2 was more difficult in 2015 when CPU's were a bit less
# powerfull than my M1 Mac currently.

import hashlib


def parse(secret, p2=False):

    i = 0
    while True:
        str = f"%s%i" % (secret, i)
        enc = hashlib.md5(str.encode("utf-8")).hexdigest()

        if p2 and enc[0:6] == "000000":
            return i
        elif not p2 and enc[0:5] == "00000":
            return i

        i += 1


# Part 1
assert parse("abcdef") == 609043
assert parse("pqrstuv") == 1048970
print("Part 1: ", parse("iwrupvqb"))
print("Part 2: ", parse("iwrupvqb", True))
