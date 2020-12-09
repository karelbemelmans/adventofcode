#!/usr/bin/env python2

with open('input.txt', 'r') as fp:
    lines = list([int(x) for x in fp.read().splitlines()])


def valid(number, data):
    i = 0
    while i < len(data):
        j = 0
        while j < len(data):
            if not i == j and data[i] + data[j] == number:
                # print "Match found: %d = %s + %s" % (number, data[i], data[j])
                return True
            j += 1
        i += 1
    return False


def findRange(number, data):
    i = 0
    while i < len(data):
        inc = 0
        items = []
        j = i
        while j < len(data):
            inc += data[j]
            items.append(data[j])
            if inc == number:
                return sorted(items)
            j += 1
        i += 1
    return False


i = 25
while i < len(lines):

    number = int(lines[i])
    set = lines[i-25:i]

    if not valid(number, set):
        print "Bad number found: %s" % lines[i]

        items = findRange(number, lines)
        if items:
            print items[0] + items[-1]
            break

    i += 1