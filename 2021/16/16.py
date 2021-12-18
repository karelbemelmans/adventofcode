# This was a difficult one, I had to borrow some inspiration from fellow coders.

# Our p1 counter, we use this as a global because we don't want to pass it around the whole time
p1 = 0


def parse_bits(bits, i, indent):
    global p1

    version = int(bits[i: i + 3], 2)
    type_ = int(bits[i + 3: i + 6], 2)
    p1 += version

    # Literal
    if type_ == 4:
        # Move our pointer 6 positions down since we read version and type
        i += 6
        str = ""
        while True:
            str += bits[i + 1: i + 5]
            i += 5
            if bits[i - 5] == '0':
                number = int(str, 2)
                return number, i

    # Operator
    else:
        # First bit contains the length type id
        len_id = int(bits[i + 6], 2)
        vs = []

        if len_id == 0:
            # The first 15 bits are the total length of the package
            len_bits = int(bits[i + 7: i + 7 + 15], 2)

            # Move our pointer:
            #   7 bits because of the header and length type id,
            #   15 because of the length field
            start_i = i + 7 + 15

            i = start_i
            while True:
                v, next_i = parse_bits(bits, i, indent + 1)
                vs.append(v)

                i = next_i
                if next_i - start_i == len_bits:
                    break

        # If the length type ID is 1, then the next 11 bits are a number that represents the number of
        # sub-packets immediately contained by this packet.
        else:
            n_packets = int(bits[i + 7:i + 7 + 11], 2)

            # Move our pointer:
            #   7 bits because of the header and length type id
            #   11 because of the number of packages number
            i += 7 + 11

            # We need to parse a set amount of packages
            for t in range(n_packets):
                v, next_i = parse_bits(bits, i, indent + 1)
                vs.append(v)
                i = next_i

        # Parse the operator types
        if type_ == 0:
            return sum(vs), i
        elif type_ == 1:
            ans = 1
            for v in vs:
                ans *= v
            return ans, i
        elif type_ == 2:
            return min(vs), i
        elif type_ == 3:
            return max(vs), i
        elif type_ == 5:
            return (1 if vs[0] > vs[1] else 0), i
        elif type_ == 6:
            return (1 if vs[0] < vs[1] else 0), i
        elif type_ == 7:
            return (1 if vs[0] == vs[1] else 0), i
        else:
            assert False, type_


def parse_string(input, p2=False):
    global p1

    # Convert our hexadecimal input to a binary string
    bits = "".join([format(int(char, 16), "04b") for char in input])

    # Run some basic checks if our bits parsing makes sense
    assert len(bits) % 4 == 0
    assert len(bits) == 4 * len(input)

    p1 = 0
    value, next_i = parse_bits(bits, 0, 0)

    if p2:
        return value
    else:
        return p1


def parse_file(file, p2=False):
    with open(file, 'r') as fp:
        input = fp.read()
    return parse_string(input, p2)


# Part 1
assert parse_string('D2FE28') == 6

assert parse_string('38006F45291200') == 9

# 8A004A801A8002F478 represents:
# - an operator packet (version 4)
#   - which contains an operator packet (version 1)
#     - which contains an operator packet (version 5)
#       - which contains a literal value (version 6)
assert parse_string('8A004A801A8002F478') == 16

# 620080001611562C8802118E34 represents:
# - an operator packet (version 3)
#   - which contains two sub-packets;
#     - each sub-packet is an operator packet that contains two literal values.
assert parse_string('620080001611562C8802118E34') == 12

# C0015000016115A2E0802F182340 has the same structure as the previous example, but the outermost packet uses a
# different length type ID. This packet has a version sum of 23.
assert parse_string('C0015000016115A2E0802F182340') == 23

# A0016C880162017C3686B18A3D4780 is:
# - an operator packet that contains
#   - an operator packet that contains
#     - an operator packet that contains
#       - five literal values;
assert parse_string('A0016C880162017C3686B18A3D4780') == 31

print("Part 1: ", parse_file('input.txt'))
print("Part 2: ", parse_file('input.txt', True))
