#!/usr/bin/env python
#
# I did not know how to do this in a structured way, so I looked at Jonathan Paulson's solution:
# https://www.youtube.com/watch?v=tMPQp60q9GA
#
# What changed from the first part:
#
# - We need to save the length of every wire at every steps we take
#   So instead of saving just the points in a set, we now make a dict that has the coords as key
#   and the value is the length it took to get there.
#   After that we can just intersect again and look at the minimum of the sum of the intersect points

with open('input.txt') as f:
    lines = [x for x in f.read().split('\n')]

# You have to leave Python's ease of parsing input data
A,B = [x.split(',') for x in lines]

# N
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

# We make a set of every point that the wire passes on the grid
def get_points(list):
    points = {}
    x = 0
    y = 0
    length = 0

    for move in list:
        dir = move[0]
        val = int(move[1:])

        assert dir in ['L', 'R', 'U', 'D']
        for _ in range(val):
            x += DX[dir]
            y += DY[dir]
            length += 1
            if (x,y) not in points:
                points[(x,y)] = length

    return points

PA = get_points(A)
PB = get_points(B)

# This is the intersection of points, so were the wires cross each other
both = set(PA.keys()) & set(PB.keys())

ans = min(PA[p] + PB[p] for p in both)
print ans


