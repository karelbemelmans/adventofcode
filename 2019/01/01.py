#!/usr/bin/env python

with open('input.txt') as f:
    lines = [int(i) for i in f.readlines()]

print lines

def fuel_needed(x):
    fuel = (x / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_needed(fuel)

total = 0
for l in lines:
    print l
    fuel = fuel_needed(l)
    print " ->", fuel
    total += fuel

print total