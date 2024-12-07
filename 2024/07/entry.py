#!/usr/bin/env python3

from itertools import product
from collections import deque


# This is probably very ugly, but it works for now. 
def calculate(numbers, operators):
    Q = deque(numbers)
    
    # First number
    T = Q.popleft()

    op = None
    
    # Walk through the list by popping the first element and checking 
    # if it's an operator or a number.
    while Q:
        x = Q.popleft()
        if x in operators:
            op = x
        else:
            if op == '+':
                T += x
            elif op == '*':
                T *= x
            elif op == '||':
                T = int(f"%d%d" % (T,x))

    return T
    

def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    # Gotta do it all in one line!
    pairs = [(int(a), [int(x) for x in b.split()]) for a, b in (line.strip().split(':') for line in lines)]
    
    if p2: 
        operators = ['+', '*', '||']
    else:
        operators = ['+', '*']
    
    T = 0
    for total, numbers in pairs:
        
        # All possible combintations of operators for a list of numbers of this length
        for ops in product(operators, repeat=len(numbers)-1):
        
            # We merge both the numbers and operators list into one list
            # Brute force, but it works for now :)
            
            merged = sum(zip(numbers, list(ops)+[0]), ())[:-1]
            t = calculate(merged, operators)
            if t == total:
                T += t
                break
        
    return T
        

# Part 1
assert parse_file('example.txt') == 3749
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('example.txt', True) == 11387
print("Part 2: ", parse_file('input.txt', True))
