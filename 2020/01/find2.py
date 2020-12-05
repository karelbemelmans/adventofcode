#!/usr/bin/python
#
#

input = "input.txt"

def find2020(input):

  # Read the input
  file = open(input, 'r+')
  lines = file.readlines()
  file.close()

  i = 0
  while i < len(lines):
    a = int(lines[i])
    print "Number %d: %d" % (i,a)

    j = 0
    while j < len(lines):
      b = int(lines[j])

      k = 0
      while k < len(lines):
        c = int(lines[k])

        # We skip over ourselves
        if i == j or j == k or i == k:
          print "Nothing"

        elif a + b + c == 2020:
          print "FOUND THEM: %d, %d, %d, %d" % (a,b,c,a*b*c)
          return

        k += 1
      j += 1
    i += 1

print "Here are the winners and their product:"
find2020(input)
