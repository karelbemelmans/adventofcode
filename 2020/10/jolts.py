#!/usr/bin/env python2

with open('input.txt', 'r') as fp:
    lines = list([int(x) for x in fp.read().splitlines()])


lines.append(0)
lines.sort()
lines.append(max(lines)+3)
print lines

# Part 1
diffs = {}
i = 0
while i < len(lines) - 1:
    diff = lines[i+1] - lines[i]

    if not diff in diffs:
        diffs[diff] = 1
    else:
        diffs[diff] += 1

    i += 1

print diffs[1] * diffs[3]

# Part 2
#
# Pretty much a textbook example

# We need a cache since we will get asked the same results tons of times and this saves us compute time
cache = {}

def recurse(i):

    # If we are at the end, we are done
    if i == len(lines)-1:
        return 1

    # Cached result?
    if i in cache:
        return cache[i]

    total = 0
    # We need to count the possible ways to get to the end of the lines now from our position i
    # We do this buy going to the direct steps j, as long as they are valid and then just add
    # the steps needed to go from j to the end of the line.
    j = i + 1
    while j < len(lines):
        if lines[j] - lines[i] <= 3:
            total += recurse(j)
        j += 1

    cache[i] = total
    return total

print recurse(0)