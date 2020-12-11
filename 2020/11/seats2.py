#!/usr/bin/env python2

import copy

with open('input.txt', 'r') as fp:
    lines = list([list(x) for x in fp.read().splitlines()])

# Little helper function to debug the lines
def print_lines(lines, count = 0):
    for row in lines:
        for char in row:
            print char,
        print ""
    print ""


# Helper function since we have an array of arrays
# This could probably be written as a oneliner somehow
def count_seats(lines):
    count = 0
    for line in lines:
        count += line.count('#')
    return count


# Count how may visible neighbours a position has
# This is very explicit code and most like can be optimized later...
def count_occupied_neighbours(x, y, lines):
    occupied = 0

    rows = len(lines)
    cols = len(lines[0])

    # print " Left"
    for z in range(y-1, -1, -1):
        if lines[x][z] == 'L':
            break

        elif lines[x][z] == '#':
            occupied += 1
            break

    # print " Right"
    for z in range(y+1, cols):
        if lines[x][z] == 'L':
            break

        elif lines[x][z] == '#':
            occupied += 1
            break

    # print " Up"
    for z in range(x-1, -1, -1):
        if lines[z][y] == 'L':
            break

        elif lines[z][y] == '#':
            occupied += 1
            break

    # print " Down"
    for z in range(x+1, rows):
        if lines[z][y] == 'L':
            break

        elif lines[z][y] == '#':
            occupied += 1
            break

    xx = x
    for z in range(y-1, -1, -1):
        xx -= 1

        # Out of bounds
        if z < 0 or xx < 0:
            break

        if lines[xx][z] == 'L':
            break

        elif lines[xx][z] == '#':
            occupied += 1
            break

    # print " Diagonal Right Up"
    xx = x
    for z in range(y+1, cols):
        xx -= 1

        # Out of bounds
        if xx < 0:
            break

        if lines[xx][z] == 'L':
            break

        elif lines[xx][z] == '#':
            occupied += 1
            break

    # print " Diagonal Left Down"
    xx = x
    for z in range(y-1, -1, -1):
        xx += 1

        # Out of bounds
        if z <0 or xx >= rows:
            break

        if lines[xx][z] == 'L':
            break

        elif lines[xx][z] == '#':
            occupied += 1
            break

    # print " Diagonal Right Down"
    xx = x
    for z in range(y+1, cols):
        xx += 1

        # Out of bounds
        if xx >= rows:
            break

        if lines[xx][z] == 'L':
            break

        elif lines[xx][z] == '#':
            occupied += 1
            break

    return occupied


count = 0
while True:

    # Assume we have no changed unless we make some
    changed = False

    # We need to do a deepcode since this is an array of arrays
    oldLines = copy.deepcopy(lines)

    for i in range(len(oldLines)):
        for j in range(len(oldLines[i])):
            state = oldLines[i][j]

            occupied = count_occupied_neighbours(i, j, oldLines)
            if state == 'L':
                if occupied == 0:
                    state = '#'

            elif state == '#':
                if occupied >= 5:
                    state = 'L'

            # Save the new value
            lines[i][j] = state

            # Log if this was a change or not
            if not state == oldLines[i][j]:
                changed = True

    count += 1

    # We didnt swap anything? Then we are done.
    if not changed:
        break


print "We ended after: ", count
print "Occupied seats: ", count_seats(lines)