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

      # We skip over ourselves
      if i == j:
        print "Nothing"

      elif a + b == 2020:
        print "FOUND THEM: %d, %d, %d" % (a,b,a*b)
        return

      j += 1

    i += 1

print "Here are the winners and their product:"
find2020(input)
