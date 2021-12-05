#!/usr/bin/env python3

import re

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()

# Make an empty grid of size RxR
def make_grid(R=1000):
    G = [ [0]*R for i in range(R)]
    return G


# Print our grid, used during testin mainly
def print_grid(G):
    print ("GRID:")
    for R in range(len(G)):
        for C in range(len(G[0])):
            print (G[C][R], end='')
        print ("")


# Mark a point on the grid, increasing the value by 1
def mark_point(G, x, y, verbose=False):
    if verbose:
        print (" - mark", x, y)
    G[x][y] += 1


# Parse a line of our input file. Simple regex
def parse_line(G, line):
    matches = re.match(r'(\d*),(\d*) -> (\d*),(\d*)$', line)
    if matches:

        # TODO: This can probably be a smarter one liner?
        x1 = int(matches.group(1))
        y1 = int(matches.group(2))
        x2 = int(matches.group(3))
        y2 = int(matches.group(4))

        # Horizontal line+
        if y1 == y2:
            start = x1
            end = x2
            if x1 > x2:
                start = x2
                end = x1
            for x in range(start, end+1):
                mark_point(G, x, y1)

        # Vertical line?
        elif x1 == x2:
            start = y1
            end = y2
            if y1 > y2:
                start = y2
                end = y1
            for y in range(start, end+1):
                mark_point(G, x1, y)

        # Diagonal line, we need to do a bit more math
        else:
            # How many steps our diagonal line has?
            steps = abs(x1 - x2) + 1

            # See which direction we go in
            if x2 > x1:
                diff_x = 1
            else:
                diff_x = -1

            if y2 > y1:
                diff_y = 1
            else:
                diff_y = -1

            # Take our steps starting from (x1,y1)
            for i in range(steps):
                mark_point(G, x1+(diff_x*i), y1+(diff_y*i))


# Calculate the actual result score of our grid
def filter_overlap(grid, number):
    count = 0

    # TODO: Can we reduce our grid in a single oneliner?
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > number:
                count += 1
    return count


# Main loop, we assume our input grid is big enough for this case
G = make_grid(1000)
for line in lines:
    parse_line(G, line)

#print_grid(G)

print ("Nr of overlapping points: ", filter_overlap(G, 1))
