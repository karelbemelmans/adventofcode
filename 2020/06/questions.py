#!/usr/bin/env python2

filename = "input.txt"

# We open the file and split
with open(filename, 'r') as f:
    groups = f.read().split('\n\n')


def process_member(member, answers):
    for x in member:
        answers[x] = True

def process_group(group):
    group_answers = {}
    for member in group.split('\n'):
        process_member(member, group_answers)
        print " -> member %s (%d)" % (member, len(member))

    return len(group_answers)

i = 0
total_count = 0
for group in groups:
    print "GROUP %d" % i
    count = process_group(group)
    print " -> Group count: %d" % count
    i += 1
    total_count += count

print ""
print "Total count: %d" % total_count
