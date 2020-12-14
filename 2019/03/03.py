#!/usr/bin/env python
#
# I did not know how to do this in a structured way, so I looked at Jonathan Paulson's solution:
# https://www.youtube.com/watch?v=tMPQp60q9GA

with open('input.txt') as f:
    lines = [x for x in f.read().split('\n')]

# You have to leave Python's ease of parsing input data
A,B = [x.split(',') for x in lines]

# N
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

# We make a set of every point that the wire passes on the grid
def get_points(list):
    points = set()
    x = 0
    y = 0

    for move in list:
        dir = move[0]
        val = int(move[1:])

        assert dir in ['L', 'R', 'U', 'D']
        for _ in range(val):
            x += DX[dir]
            y += DY[dir]
            points.add((x, y))

    return points

PA = get_points(A)
PB = get_points(B)

# This is the intersection of points, so were the wires cross each other
both = PA&PB

# Simply run the min() function for every item in both
ans = min([abs(x) + abs(y) for (x,y) in both])
print ans


