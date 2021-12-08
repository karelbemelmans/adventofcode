from collections import defaultdict


def parse_line(line, counter, p2=False):
    start, end = line.split(" | ")
    global original

    # p2: Map
    if p2:
        words = start.split(" ")
        patterns = defaultdict(list)
        new_dict = {}

        # Part 1: Process the obvious ones
        #         Map all the words into an array grouped by word length
        for word in words:
            l = len(word)

            # We have 4 numbers that we can already map to the new_dict
            # Number 1
            if l == 2:
                patterns[1] = list(word)
                new_dict[1] = "".join(sorted(word))

            # Number 7
            elif l == 3:
                patterns[7] = list(word)
                new_dict[7] = "".join(sorted(word))

            # Number 4
            elif l == 4:
                patterns[4] = list(word)
                new_dict[4] = "".join(sorted(word))

            # Number 8
            elif l == 7:
                patterns[8] = list(word)
                new_dict[8] = "".join(sorted(word))

            # The 6 next ones we will look at more closely later, for now we just group them

            # Length 5: 2, 3, 5
            elif l == 5:
                patterns[235].append(list("".join(sorted(word))))

            # Length 6: 0, 6, 9
            elif l == 6:
                patterns[69].append(list("".join(sorted(word))))

        # Part 2
        #
        # We measure the amount of differences between digits we know and digits we not know yet.
        # For every check we can single out one and then continue with the rest.

        ################################################################################################################
        # Words of length 5

        ## Pattern 2 - Pattern 4 = 3 lines difference  <--  we look for this one
        ## Pattern 3 - Pattern 4 = 2 lines difference
        ## Pattern 5 - Pattern 4 = 2 lines difference
        for pattern in patterns[235]:
            diff = set(pattern) - set(patterns[4])
            if len(diff) == 3:
                new_dict[2] = "".join(sorted(pattern))
                patterns[235].remove(pattern)

        ## Pattern 3 - Pattern 7 = 2 lines difference   <--  we look for this one
        ## Pattern 5 - Pattern 7 = 3 lines difference
        assert len(patterns[235]) == 2
        for pattern in patterns[235]:
            diff = set(pattern) - set(patterns[7])
            if len(diff) == 2:
                new_dict[3] = "".join(sorted(pattern))
                patterns[235].remove(pattern)

        # We have one number left now, that is 5
        assert len(patterns[235]) == 1
        new_dict[5] = "".join(patterns[235][0])

        ################################################################################################################
        # Words of length 6

        ## Pattern 0 - Pattern 4 = 3 lines difference
        ## Pattern 6 - Pattern 4 = 3 lines difference
        ## Pattern 9 - Pattern 4 = 2 lines difference  <--  we look for this one
        for pattern in patterns[69]:
            diff = set(pattern) - set(patterns[4])
            if len(diff) == 2:
                new_dict[9] = "".join(sorted(pattern))
                patterns[69].remove(pattern)

        ## Pattern 0 - Pattern 5 = 2 lines difference
        ## Pattern 6 - Pattern 5 = 1 line difference  <--  we look for this one
        assert len(patterns[69]) == 2
        for pattern in patterns[69]:
            diff = set(pattern) - set(list(new_dict[5]))
            if len(diff) == 1:
                new_dict[6] = "".join(sorted(pattern))
                patterns[69].remove(pattern)

        # We have one number left now, that is 0
        assert len(patterns[69]) == 1
        new_dict[0] = "".join(patterns[69][0])

        # Make sure we got all 10 at this point
        assert len(new_dict) == 10

        # Now use our new_dict to translate the codes into digits and return it as a number.
        words = end.split(" ")
        number = ""
        for word in words:
            word = "".join(sorted(word))
            if word in new_dict.values():
                n = list(new_dict.keys())[list(new_dict.values()).index(word)]
                number += f"{n}"

        return int(number)

    # P1
    else:
        for word in end.split(" "):
            if len(word) in [2, 4, 3, 7]:
                counter[len(word)] += 1


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    counter = defaultdict(int)
    count = 0
    for line in lines:
        if p2:
            count += parse_line(line, counter, True)
        else:
            parse_line(line, counter)

    if p2:
        return count
    else:
        return sum(counter.values())


# Part 1
assert parse_file('test.txt') == 26
print("Part 1: ", parse_file('input.txt'))

# Part 2
assert parse_file('test.txt', True) == 61229
print("Part 2: ", parse_file('input.txt', True))
