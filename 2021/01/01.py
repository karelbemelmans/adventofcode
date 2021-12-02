#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    lines = list([int(x) for x in fp.read().splitlines()])

# Part 1
increased = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        increased += 1

print (increased)

# Part 2
increased = 0
for i in range(3, len(lines)):
    A = (lines[i-1] + lines[i-2] + lines[i-3])
    B = (lines[i] + lines[i-1] + lines[i-2])
    if B > A:
        increased += 1

print (increased)
