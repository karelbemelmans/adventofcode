#!/usr/bin/env python

input = [2, 0, 1, 9, 5, 19]
#input = [0, 3, 6]

#T = 10
#T = 2020
T = 30000000

numbers = {}

# Optimization 1:
# - We only need to keep the 2 last positions of each number, so
#   we create a function that cleans up numbers for us every time
#   we add something new to them.
#
def add_and_clean(number, pos):
    if not number in numbers:
        numbers[number] = [(pos)]
    else:
        # Take the last entry
        prev = numbers[number][-1]

        # Make the new entry that value + our new one
        numbers[number] = [prev, pos]
        #print number, numbers


# Optimization 2:
# - Remove the actual storing of all items we looked at into spoken
#   We dont really care about that list since we keep a history of when
#   we spoke the last 2 ones already. And the output of the T-th spot is simply
#   the value of the last number we had in "number" stored.


number = None
for i in range(T):
    if i < len(input):
        number = input[i]

        # We note at which place this number appeared
        add_and_clean(number, i)

    else:

        # Was that the first time we saw that number?
        if len(numbers[number]) == 1:
            number = 0

        else:
            # The turn before we spoke this number, i-i
            # The turn before that we look at the last number in numbers[number]
            prev = numbers[number][-1]
            pprev = numbers[number][-2]
            number = prev - pprev

        # Log that we spoke this number and at which spot
        add_and_clean(number, i)


print number

