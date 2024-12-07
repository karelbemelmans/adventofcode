#!/usr/bin/env python3

from itertools import product
from collections import deque


# This is probably very ugly, but it works for now. 
def calculate(numbers):
    Q = deque(numbers)
    
    # First number
    T = Q.popleft()

    op = None
    
    # Walk through the list by popping the first element and checking 
    # if it's an operator or a number.
    while Q:
        x = Q.popleft()
        if x in ['+', '*']:
            op = x
        else:
            if op == '+':
                T += x
            elif op == '*':
                T *= x

    return T
    

def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    pairs = [(int(a), [int(x) for x in b.split()]) for a, b in (line.strip().split(':') for line in lines)]
    
    T = 0
    for total, numbers in pairs:
        
        # All possible combintations of operators for a list of numbers of this length
        for ops in product('+*', repeat=len(numbers)-1):
        
            # We merge both the numbers and operators list into one list
            merged = sum(zip(numbers, list(ops)+[0]), ())[:-1]
            t = calculate(merged)
            if t == total:
                T += t
                break
        
    return T
        

# Part 1
assert parse_file('example.txt') == 3749
print("Part 1: ", parse_file('input.txt'))

# Part 2
# assert parse_file('example.txt', True) == 31
# print("Part 2: ", parse_file('input.txt', True))
