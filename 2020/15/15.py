#!/usr/bin/env python

input = [2, 0, 1, 9, 5, 19]
T = 2020

numbers = {}
spoken = []

number = None
for i in range(T):
    print "Turn ", i+1

    if i < len(input):
        print " - The i spoken number: ", input[i]
        number = input[i]

        # We log that we spoke this number
        spoken.append(number)

        # We note at which place this number appeared
        numbers[number] = [(i)]

    else:

        # The last spoken number is in the parameter "number"
        # The previous position is i-i
        if number in spoken:
            print "  - We have seen this number before: ", number

            # Was that the first time we saw that number?
            if len(numbers[number]) == 1:
                print "    ... and it was the first time, so we speak 0"
                number = 0

            else:
                # The turn before we spoke this number, i-i
                # The turn before that we look at the last number in numbers[number]
                prev = numbers[number][-1]
                print "    - Previous time spoken: ", prev
                pprev = numbers[number][-2]
                print "    - Time before that spoken: ", pprev
                number = prev - pprev
                print "    - New number: ", number

            # Log that we spoke this number and at which spot
            spoken.append(number)
            if not number in numbers:
                numbers[number] = [(i)]
            else:
                numbers[number].append(i)


        else:
            print "  - We have NOT seen this number before: ", number

            # We say the number 0 now
            spoken.append(0)

            # We log that we have said the number 0 at this position
            numbers[0] = list(i)


print spoken[T-1]

