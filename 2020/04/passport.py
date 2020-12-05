#!/usr/bin/env python

import re

filename = "input.txt"

with open(filename) as f:
    content = [i.strip() for i in f.readlines()]

# Check if a passport is valid
def check_passport(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    parsed = parse_passport(passport)
    print parsed

    # 1. Check if we have all required fields
    for r in required:
        # Did we find a missing field? Then fail
        if r not in parsed.keys():
            print " -> Found a missing field (%s), invalid!" % r
            return False

    # 2. Check for the actual valid field values
    for p in parsed.keys():
        #print "Checking field: %s" % p

        if p == "byr":
            if not re.match(r'\d{4}$', parsed[p]):
                print " -> Not a number: %s" % parsed[p]
                return False
            if int(parsed[p]) < 1920 or int(parsed[p]) > 2002:
                print " -> Outside of allowed data range: %s" % parsed[p]
                return False

        elif p == "iyr":
            if not re.match(r'\d{4}$', parsed[p]):
                print " -> Not a number: %s" % parsed[p]
                return False
            if int(parsed[p]) < 2010 or int(parsed[p]) > 2020:
                print " -> Outside of allowed data range: %s" % parsed[p]
                return False

        elif p == "eyr":
            if not re.match(r'\d{4}$', parsed[p]):
                print " -> Not a number: %s" % parsed[p]
                return False
            if int(parsed[p]) < 2020 or int(parsed[p]) > 2030:
                print " -> Outside of allowed data range: %s" % parsed[p]
                return False

        elif p == "hgt":
            matches = re.match(r'(\d*)(cm|in)$', parsed[p])
            if not matches:
                print " -> Not a height valid input: %s" % parsed[p]
                return False

            if matches.group(2) == "cm" and (int(matches.group(1)) < 150 or int(matches.group(1)) > 193):
                print " -> Not a height valid input in cm: %s" % parsed[p]
                return False

            if matches.group(2) == "in" and (int(matches.group(1)) < 59 or int(matches.group(1)) > 76):
                print " -> Not a height valid input in inches: %s" % parsed[p]
                return False

        elif p == "hcl":
            if not re.match(r'#[0-9a-f]{6}$', parsed[p]):
                print " -> Not a valid color code: %s" % parsed[p]
                return False

        elif p == "ecl":
            allowed_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if parsed[p] not in allowed_eye_colors:
                print " -> Not a valid eye color: %s" % parsed[p]
                return False

        elif p == "pid":
            if not re.match(r'\d{9}$', parsed[p]):
                print " -> Not a valid passport number: %s" % parsed[p]
                return False

    # If we reach this phase we had no validation errors so we can return success
    print " -> Valid passport!"
    return True


# We parse a string into an array of values
def parse_passport(passport):
    parsed = {}

    pieces = re.findall(r'\w+:#?\w+', passport)
    for p in pieces:
        matches = re.match(r'(\w+):(#?\w+)', p)
        if matches:
            parsed[matches.group(1)] = matches.group(2)

    return parsed


total_passports = 0
valid_passports = 0

row_counter = 0
total_rows = len(content)

passport = ""
for row in content:
    passport += row + " "

    if row == "" or row_counter == (len(content) - 1):
        total_passports += 1
        if check_passport(passport):
            valid_passports += 1
        passport = ""

    row_counter += 1

print "Scanned passports: %d - Valid passports: %d" % (total_passports, valid_passports)
