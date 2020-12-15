#!/usr/bin/env python

import re

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()


def mask_pos(mask, value):
    # P will be a list of strings that value gets because of the floating X part
    # If there is no X in the mask, this will be one item only.
    P = ['']
    value = list(format(value, '036b'))

    for i in range(len(mask)):
        for j in range(len(P)):
            if mask[i] == '0':
                P[j] += value[i]

            elif mask[i] == '1':
                P[j] += '1'

            elif mask[i] == 'X':
                # In this case we add new items to our list:
                #   - we add new entries to our list with a 0 at the end
                #   - the current entries we extend with a 1 at the end
                P.append(P[j] + '0')
                P[j] += '1'

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