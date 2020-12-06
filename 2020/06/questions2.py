#!/usr/bin/env python2

filename = "input.txt"

# We open the file and split
with open(filename, 'r') as f:
    groups = f.read().split('\n\n')


# We simply use the sec.intersection() function to determine
# which items are in common between 2 strings. We can do this
# in a recursive way over all members.
def process_group(group):
    intersect = False

    i = 0
    for member in group.split('\n'):
        if i == 0:
            intersect = set(member)
        else:
            intersect = intersect.intersection(member)
        i += 1

    return len(intersect)

i = 1
total_count = 0
for group in groups:
    print "GROUP %d" % i
    count = process_group(group)
    print " -> Group count: %d" % count
    i += 1
    total_count += count

print ""
print "Total count: %d" % total_count
