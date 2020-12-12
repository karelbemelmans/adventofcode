#!/usr/bin/env python2

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()

COMPAS = ['E', 'S', 'W', 'N']
dir = 'E'
x = 0
y = 0
way_x = 10
way_y = 1

for l in lines:
    cmd = l[0]
    value = int(l[1:])

    print "Command: %s, Value: %d" % (cmd, value)

    if cmd == 'N':
        way_y += value

    elif cmd == 'S':
        way_y -= value

    elif cmd == 'E':
        way_x += value

    elif cmd == 'W':
        way_x -= value

    elif cmd == 'L' or cmd == 'R':
        t = value / 90

        # R90 and L270 have the same effect
        if (cmd == 'R' and t == 1) or (cmd == 'L' and t == 3):
            t_x = way_y
            t_y = way_x * -1

            way_x = t_x
            way_y = t_y

        # R270 and L90 have the same effect
        if (cmd == 'R' and t == 3) or (cmd == 'L' and t == 1):
            t_x = way_y * -1
            t_y = way_x

            way_x = t_x
            way_y = t_y

        # R120 and L120 are the same
        elif t == 2:
            way_x *= -1
            way_y *= -1

    elif cmd == 'F':
        x += way_x * value
        y += way_y * value


    print " -> x, y", x, y
    print " -> way_x, way, y", way_x, way_y

print x, y, abs(x) + abs(y)