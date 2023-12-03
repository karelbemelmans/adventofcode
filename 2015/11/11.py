#!/usr/bin/env python3

from collections import deque, defaultdict


def next_password(string):
    '''
    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; if it was z, it wraps around to a, and 
    repeat with the next letter to the left until one doesn't wrap around.
    '''

    # Do we need to cover this case where the password gets longer?
    if string == "":
        return "a"

    start = ord('a')
    end = ord('z')

    x = string[-1]
    new = ord(x) + 1

    if new > end:
        return next_password(string[0:-1]) + chr(start)
    else:
        return string[0:-1] + chr(new)


def meets_requirements(string):
    '''
    Passwords must include one increasing straight of at least three letters, 
    like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    '''

    p1 = False
    p2 = False
    p3 = 0

    start = ord('a')
    end = ord('z')

    for x in range(start, end-1):
        match = chr(x) + chr(x+1) + chr(x+2)
        if match in string:
            p1 = True
            break

    '''
    Passwords may not contain the letters i, o, or l, as these letters can be 
    mistaken for other characters and are therefore confusing.
    '''
    banned = set(['i', 'o', 'l'])
    if not any(x in banned for x in string):
        p2 = True

    '''
    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    '''
    for x in range(start, end+1):
        if chr(x)*2 in string:
            p3 += 1

    return p1 and p2 and p3 >= 2


def parse_string(string, p2=False):

    while True:
        string = next_password(string)
        if meets_requirements(string):
            return string


# Part 1
assert parse_string('abcdefgh') == "abcdffaa"
p1 = parse_string('hxbxwxba')
print("Part 1: ", p1)

# Part 2
print("Part 2: ", parse_string(p1))
