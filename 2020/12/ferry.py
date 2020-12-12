#!/usr/bin/env python2

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()

COMPAS = ['E', 'S', 'W', 'N']
dir = 'E'
x = 0
y = 0

for l in lines:
    cmd = l[0]
    value = int(l[1:])

    print "Command: %s, Value: %d" % (cmd, value)

    if cmd == 'N':
        y += value

    elif cmd == 'S':
        y -= value

    elif cmd == 'E':
        x += value

    elif cmd == 'W':
        x -= value

    elif cmd == 'L' or cmd == 'R':
        t = value / 90

        # If we turn left, we need to go the other way in the compas directions
        if cmd == 'L':
            t *= -1

        # Which way are we pointing to right now?
        cur = COMPAS.index(dir)

        # New direction we are facing in
        dir = COMPAS[(cur + t) % 4]

    elif cmd == 'F':
        if dir == 'N':
            y += value

        elif dir == 'S':
            y -= value

        elif dir == 'E':
            x += value

        elif dir == 'W':
            x -= value

print x, y, abs(x) + abs(y)