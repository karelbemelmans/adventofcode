#!/usr/bin/env python3

# A nice string is one with all of the following properties:
#
#  - It contains at least three vowels (aeiou only), like aei, xazegov, or
#    aeiouaeiouaeiou.
#  - It contains at least one letter that appears twice in a row, like xx,
#    abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#  - It does not contain the strings ab, cd, pq, or xy, even if they are part
#    of one of the other requirements.


def nice_p1(s):

    # A set helps us with unique letters
    S = set(s)

    # Banned strings appear?
    if any(x in s for x in ["ab", "cd", "pq", "xy"]):
        return False

    # Contains 3 vowels
    # Lots of other options: for, map
    if len([char for char in s if char in ["a", "e", "i", "o", "u"]]) < 3:
        return False

    # Double string with any of the chars in the string
    if not any([i * 2 in s for i in S]):
        return False

    return True


# Now, a nice string is one with all of the following properties:
#
#  - It contains a pair of any two letters that appears at least twice in the string
#    without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa,
#    but it overlaps).
#  - It contains at least one letter which repeats with exactly one letter between
#    them, like xyx, abcdefeghi (efe), or even aaa.


def nice_p2(s):
    c1 = False
    c2 = False

    # Is there a substring in s that appear more than once?
    if any([s.count(s[i : i + 2]) > 1 for i in range(len(s) - 2)]):
        c1 = True

    # Condition 2
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            c2 = True
            break

    return c1 and c2


def parse(lines, p2=False):
    N = 0

    for line in lines:
        if p2:
            if nice_p2(line):
                N += 1
        else:
            if nice_p1(line):
                N += 1

    return N


def parse_file(file, p2=False):

    with open(file, "r") as fp:
        lines = [line for line in fp.read().splitlines()]

    return parse(lines, p2)


# Part 1
assert nice_p1("ugknbfddgicrmopn") == True
assert nice_p1("aaa") == True
assert nice_p1("jchzalrnumimnmhp") == False
assert nice_p1("haegwjzuvuyypxyu") == False
assert nice_p1("dvszwmarrgswjxmb") == False
print("Part 1: ", parse_file("input.txt"))

# Part 2
assert nice_p2("qjhvhtzxzqqjkmpb") == True
assert nice_p2("xxyxx") == True
assert nice_p2("uurcxstgmygtbstg") == False
assert nice_p2("ieodomkazucvgmuy") == False
print("Part 2: ", parse_file("input.txt", True))
