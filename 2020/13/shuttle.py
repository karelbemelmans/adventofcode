#/usr/bin/env python

with open('input.txt', 'r') as fp:
    lines = fp.read().splitlines()

T = int(lines[0])
busses = [int(x) for x in lines[1].split(',') if not x == 'x']

winner = 0
diff = -1
for b in busses:
    next = (T / b) * (b) + b
    d = next - T

    if diff < 0:
        diff = d
        winner = b
    elif d < diff:
        diff = d
        winner = b

print winner * diff