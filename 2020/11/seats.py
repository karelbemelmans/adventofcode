#!/usr/bin/env python2

import copy

with open('input.txt', 'r') as fp:
    lines = list([list(x) for x in fp.read().splitlines()])

# Little helper function to debug the lines
def print_lines(lines, count = 0):
    print "PASS: ", count
    for row in lines:
        for char in row:
            print char,
        print ""
    print ""


def count_seats(lines):
    count = 0
    for line in lines:
        count += line.count('#')
    return count


# We keep this list until nothing has changed
count = 0
while True:

    # Assume we have no changed unless we make some
    changed = False

    # We need to do a deepcode since this is an array of arrays
    oldLines = copy.deepcopy(lines)
    for i in range(len(oldLines)):
        for j in range(len(oldLines[i])):
            state = oldLines[i][j]

            #print "Looking at cell: (%d, %d)" % (i, j)
            #print " Current state: ", state

            if state == 'L':
                #print "  Cell is emtpy, looking at neighbours..."

                isolated = True
                for x in (i-1, i, i+1):
                    for y in (j-1, j, j+1):

                        # Make sure we only target in bound cells
                        if not (x == i and y == j) and (x >= 0 and x < len(oldLines)) and (y >= 0 and y < len(oldLines[i])):

                            #print "   Investigating cell (%d,%d): %s" % (x, y, oldLines[x][y])
                            if oldLines[x][y] == '#':
                                isolated = False

                if isolated:
                    state = '#'

            elif state == '#':
                #print "  Cell is occupied, looking at neighbours..."

                occupied = 0
                for x in (i-1, i, i+1):
                    for y in (j-1, j, j+1):

                        # Make sure we only target in bound cells
                        if not (x == i and y == j) and (x >= 0 and x < len(oldLines)) and (y >= 0 and y < len(oldLines[i])):

                            #print "   Investigating cell (%d,%d): %s" % (x, y, oldLines[x][y])
                            if oldLines[x][y] == '#':
                                occupied += 1

                if occupied >= 4:
                    state = 'L'

            # Save the new value
            #print " New state: ", state
            lines[i][j] = state

            # Log if this was a change or not
            if not state == oldLines[i][j]:
                changed = True

    count += 1
    #print_lines(lines, count)

    # We didnt swap anything? Then we are done.
    if not changed:
        break

print "We ended after: ", count
print "Occupied seats: ", count_seats(lines)