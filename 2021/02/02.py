#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()


H = 0
D = 0
A = 0

for line in lines:
    parts = line.split()

    if parts[0] == 'forward':
        H += int(parts[1])
        D += (A * int(parts[1]))

    elif parts[0] == 'down':
        A += int(parts[1])

    elif parts[0] == 'up':
        A -= int(parts[1])


print (H * D)
