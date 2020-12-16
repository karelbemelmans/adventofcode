#!/usr/bin/env python

import re
from itertools import permutations

my_ticket = [79,193,53,97,137,179,131,73,191,139,197,181,67,71,211,199,167,61,59,127]

with open('input.sample', 'r') as fp:
    lines = fp.read().splitlines()

with open('ranges.sample', 'r') as fp:
    ranges = fp.read().splitlines()


# Return True if there is at least one range that is valid
def is_valid(n, R):
    for min, max in R:
        if min <= n <= max:
            return True
    return False


R  = [] # This contains ranges as pairs
RR = {} # This contains ranges as pairs with the key being the field they match with


# We build up R and RR
for r in ranges:
    matches = re.match(r'(.*): (\d+)\-(\d+) or (\d+)\-(\d+)', r)
    if matches:
        field = matches.group(1)
        r1 = (int(matches.group(2)), int(matches.group(3)))
        r2 = (int(matches.group(4)), int(matches.group(5)))
        R.append(r1)
        R.append(r2)

        RR[field] = (r1, r2)

# We filter our input tickets to only have valid tickets
valid_tickets = []
for l in lines:
    numbers = [int(x) for x in l.split(',')]

    valid = True
    for n in numbers:
        if not is_valid(n, R):
            valid = False
            break

    if valid:
        valid_tickets.append(numbers)

# We look for an order of the fields where all the values for each ticket gives a valid solution
# We have 20 fields, so would have 20! possible permutations...

winner = None
for fields in permutations(RR.keys()):
    print "FIELDS: ", fields

    matched = True

    # We loop over all fields in this order where we match field with position i
    i = 0
    for f in fields:

        # Go over all tickets
        for t in valid_tickets:

            # Look at field i in this ticket now, and see if we match the rules for field f
            if not is_valid(t[i], RR[f]):
                matched = False
                break

        i += 1

    if matched:
        winner = fields
        print "Winning field:", winner
        break


# Now go over our ticket to produce the actual output required for P2
RES = 1
for i, f in enumerate(winner):
    if f.startswith('departure'):
        RES *= my_ticket[i]

    i += 1

print RES
