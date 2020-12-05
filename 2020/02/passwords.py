#!/usr/bin/python

import re

input = "input.txt"

def check_passwords(input):

  # Read the input
  file = open(input, 'r')
  lines = file.readlines()
  file.close()

  i = 0
  count = 0
  while i < len(lines):
    searchObj = re.search( r'(\d+)-(\d+) (\w): (\w+)', lines[i], re.M|re.I)
    if searchObj:
      a = int(searchObj.group(1))
      b = int(searchObj.group(2))
      letter   = searchObj.group(3)
      password = searchObj.group(4)

      print "Match found: %d-%d %s: %s" % (a,b,letter,password)

      #if password_is_valid(a,b,letter,password):
      if password_is_valid2(a,b,letter,password):
        print "VALID!"
        count += 1
      else:
        print "not valid..."

    else:
      print "No match!!"

    i += 1

  print ""
  print "Valid passwords found: %d" % count

def password_is_valid(a,b,letter,password):
  count = password.count(letter)
  if (count >= a) and (count <= b):
    return 1
  else:
    return 0

def password_is_valid2(a,b,letter,password):
  match_a = password[a-1] == letter
  match_b = password[b-1] == letter

  # Basically a xor
  if (match_a and not match_b) or (not match_a and match_b):
    return True
  else:
    return False

check_passwords(input)
