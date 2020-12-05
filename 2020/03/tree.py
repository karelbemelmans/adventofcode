#!/usr/bin/env python

filename = "input.txt"

with open(filename) as f:
    content = [i.strip() for i in f.readlines()]

def count_trees(content, add_x, add_y):
    print "Running taverse: %d to right, %d down" % (add_x, add_y)

    trees = 0
    pos_x = 0
    pos_y = 0

    rows = len(content)
    cols = len(content[0])

    #print "Rows: %d, Cols: %d" % (rows, cols)
    while pos_y < rows:
        #print "POS: X: %d, Y: %d, Content: %s" % (pos_x, pos_y, content[pos_y][pos_x])

        if content[pos_y][pos_x] == "#":
            trees += 1

        pos_x  = (pos_x + add_x) % (cols)
        pos_y += add_y

    return trees


traverses = [(1,1), (3,1), (5,1), (7,1), (1,2)]
product = 1
for t in traverses:
    trees = count_trees(content, t[0], t[1])
    print "  -> Trees: %d" % trees
    product *= trees

print "Product: %d" % product