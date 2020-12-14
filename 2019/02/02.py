#!/usr/bin/env python

with open('input.txt') as f:
    lines = [int(i) for i in f.read().split(',')]


# Replace values
lines[1] = 12
lines[2] = 2
print "INPUT", lines

i = 0
while i < len(lines):

    print i, lines

    # Program is done
    if lines[i] == 99:
        break

    elif lines[i] == 1:
        lines[lines[i+3]] = lines[lines[i+1]] + lines[lines[i+2]]
        i += 4

    elif lines[i] == 2:
        lines[lines[i+3]] = lines[lines[i+1]] * lines[lines[i+2]]
        i += 4

    # If we had no valid opcode we just move on 1 step
    else:
        i += 1

print lines[0]

