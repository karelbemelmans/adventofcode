#!/usr/bin/env python3

def blink(numbers):
    new = []

    """
    - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
        - The left half of the digits are engraved on the new left stone, 
        - and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
   """

    for n in numbers:
        if n == 0:
            new.append(1)
        elif len(str(n)) % 2 == 0:
            new.append(int(str(n)[:len(str(n))//2]))
            new.append(int(str(n)[len(str(n))//2:]))
        else:
            new.append(n * 2024)

    return new


def parse_file(input, count=0, p2=False):
    numbers = [int(x) for x in input.split()]

    print(numbers)

    for i in range(count):
        numbers = blink(numbers)
        print("i: ",  numbers)

    T = len(numbers)
    return T


# Part 1

assert parse_file('0 1 10 99 999', 1) == 7
assert parse_file('125 17', 6) == 22
assert parse_file('125 17', 25) == 55312
print("Part 1: ", parse_file('0 7 6618216 26481 885 42 202642 8791', 25))

# Part 2
# assert parse_file('example.txt', True) == 11387
# print("Part 2: ", parse_file('input.txt', True))
