#!/usr/bin/env python

X = 138241
Y = 674034

# My original functions for part 1
def has_adj_digit(x):
    s = str(x)
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True

    # If we get here there was no match
    return False


def never_decreases(x):
    s = str(x)

    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False

    # If we get here the numbers we were good
    return True


# I was kind of stuck with the confusing way of the assignment, but it can simply
# be read as "doubles but no tripples"
#
# Thanks to comments:
#   https://www.reddit.com/r/adventofcode/comments/e5y3gq/2019_day_4_which_of_these_two_topics_were_the_key/
#
# Just building a string and then checking if it appears in the input seems to be the easiest way to solve this
#
def hasDouble(n):
    n = str(n)

    for i in range(10):
        if str(i)*2 in n:
            return True
    return False


def hasDoubleAndNotTriple(n):
    n = str(n)

    for i in range(10):
        if str(i)*2 in n and not str(i)*3 in n:
            return True
    return False


# P1
results = []
for i in range(X,Y+1):
    if never_decreases(i) and hasDouble(i):
        results.append(i)

print len(results)


# P2
results = []
for i in range(X,Y+1):
    if never_decreases(i) and hasDoubleAndNotTriple(i):
        results.append(i)

print len(results)