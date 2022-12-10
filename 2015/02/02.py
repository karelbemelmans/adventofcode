def paper(l, w, h):
    p = 2*l*w + 2*w*h + 2*h*l

    # Find the 2 smallest ones using a set
    s = [l, w, h]
    s = sorted(s)
    p += s[0]*s[1]

    return p


def ribbon(l, w, h):
    s = [l, w, h]
    s = sorted(s)
    p = 2*s[0] + 2*s[1]
    p += l*w*h

    return p


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        lines = [x for x in fp.read().splitlines()]

    T = 0

    for line in lines:
        words = [int(x) for x in line.split("x")]

        if p2:
            T += ribbon(words[0], words[1], words[2])
        else:
            T += paper(words[0], words[1], words[2])

    return T


assert parse_file('test.txt') == 58
print("Part 1: ", parse_file('input.txt'))

assert parse_file('test.txt', True) == 34
print("Part 2: ", parse_file('input.txt', True))
