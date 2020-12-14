#!/usr/bin/env python

import re

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()


def mask_pos(mask, value):
    P = ['']
    value = list(format(value, '036b'))

    # We build up multiple lists at the same time
    for i in range(len(mask)):
        for j in range(len(P)):
            if mask[i] == '0':
                P[j] += value[i]

            elif mask[i] == '1':
                P[j] += '1'

            elif mask[i] == 'X':
                # We add an extra entry with a 0
                P.append(P[j] + '0')
                # And the other ones we extended with a 1
                P[j] += '1'

#    for p in P:
#        print " -> ", p, int(p, 2)

    return P

reg = {}
mask = None
for l in lines:

    if l.startswith('mask'):
        mask = l.split(' = ')[1]

    elif l.startswith('mem'):
        m = re.match(r'^mem\[(\d*)\] = (\d*)$', l)
        if m:
            pos = int(m.group(1))
            value = int(m.group(2))

            for p in mask_pos(mask, pos):
                reg[p] = value

sum = 0
for k, v in reg.items():
    sum += v

print sum