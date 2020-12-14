#!/usr/bin/env python

import re

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()


def apply_mask(mask, value):
    value = list(format(value, '036b'))

    for i, m in enumerate(mask):
        if not m == 'X':
            value[i] = m

    return int("".join(value), 2)

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

            reg[pos] = apply_mask(mask, value)

sum = 0
for k, v in reg.items():
    sum += v

print sum