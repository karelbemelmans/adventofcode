#!/usr/bin/env python3

letters = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [line for line in fp.read().splitlines()]

    T = 0
    for line in lines:
        if p2:
            new_line = ""

            # Find the first digit
            current_word = ""
            for char in line:
                if char.isdigit():
                    new_line += char
                    break
                else:
                    current_word += char
                    for letter in letters:
                        if letter in current_word:
                            new_line += letters[letter]
                            break
                    else:
                        continue
                    break

            # Findt the last digit
            current_word = ""
            for char in reversed(line):
                if char.isdigit():
                    new_line += char
                    break
                else:
                    current_word = char + current_word
                    for letter in letters:
                        if letter in current_word:
                            new_line += letters[letter]
                            break
                    else:
                        continue
                    break

            line = new_line

        digits = [x for x in line if x.isdigit()]
        T += int(digits[0] + digits[-1])

    return T


# Part 1
assert parse_file('test.txt') == 142
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test2.txt', True) == 281
print("Part 2: ", parse_file('input.txt', True))
