#/usr/bin/env python

# My script works for all the samle inputs, but not
# for the actual puzzle input because it's a naive
# loop that increments with 1 and that will take forever
# to find a solution in this case.
#
# Like usual Jonathan Paulson has the answer here:
# https://www.youtube.com/watch?v=x40aLK9KjYQ
#
#

with open('sample.txt', 'r') as fp:
    lines = fp.read().splitlines()

busses = [x for x in lines[1].split(',')]
print busses

conditions = []
for i, b in enumerate(busses):
    if not b == 'x':
        conditions.append((i, b))
print conditions

time = 1
while True:
    time += 1

    for i, b in conditions:
        success = True
        b = int(b)

        # Is there a bus at time+i ?
        if not (time + i) % b == 0:
            # We did not have a good match so we break
            success = False
            break

    if success:
        print "Success at time ", time
        break

