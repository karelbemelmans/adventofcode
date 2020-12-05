#!/usr/bin/env python

with open("input.txt") as f:
    content = [i.strip() for i in f.readlines()]


# The assignment is pretty simple because it actually is a perfect
# binary representation of numbers. So we just replace the chars with
# 0 or 1 and then process the items as base 2 (aka binary).
def decode_entry(code):
    row = int(code.replace('B', '1').replace('F', '0')[0:7], 2)
    col = int(code.replace('R', '1').replace('L', '0')[7:10], 2)
    return (row * 8) + col


max_id = 0
passes = []
for row in content:
    id = decode_entry(row)
    print "%s decodes to %d" % (row, id)

    max_id = max(max_id, id)
    passes.append(id)

print "Max id we found was: %d" % max_id

# We need to sort our list before we continue
passes.sort()

# We make a list of all the passes that are available
perfect = range(passes[0], passes[-1] + 1)

# Which one is missing from the passes list now?
print "The set of items missing from our list:"
print set(perfect) - set(passes)