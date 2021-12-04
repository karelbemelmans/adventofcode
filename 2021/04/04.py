#/usr/bin/env python

with open('input.txt', 'r') as fp:
    lines = fp.read().split('\n\n')

NUMBERS = lines[0].split(',')
CARDS = lines[1:]

# The score of the winning board can now be calculated.
# Start by finding the sum of all unmarked numbers on that board
def bingo_score(input, draw):
    print("winning draw: ", draw)

    # Turn our into into a dimensional array
    card = [x.split() for x in input.split("\n")]
    print("winner card: ", card)

    # Flatten our array
    flat = [item for sublist in card for item in sublist]

    # Diff
    unused = list(set(flat) - set(draw))
    print("unused numbers: ", unused)

    # Sum and multiple with last number
    return sum([int(x) for x in unused]) * int(draw[-1])

def has_bingo(input, draw):

    # Turn our input into into a dimensional array
    card = [x.split() for x in input.split("\n")]
    rows = len(card)
    cols = len(card[0])

    # Check horizontal
    for row in range(rows):
        if all(x in draw for x in card[row]):
            return True

    # Check vertical
    for col in range(cols):
        # Build up a list with this column's numbers
        c = [card[r][col] for r in range(rows)]
        if all(x in draw for x in c):
            return True

    return False

# Part 1: First board to win
winner = False
for n in range(len(NUMBERS)):
    if winner:
        break

    # We take a longer set of input every time until we have a winner
    draw = NUMBERS[0:n+1]

    # Check if our cards have a winner with this draw
    for card in CARDS:
        if has_bingo(card, draw):
            winner = True
            print ("Winner card: ")
            print(bingo_score(card, draw))
            break

# Part 2: Last board to win
winners = 0
initial_cards = len(CARDS)

for n in range(len(NUMBERS)):

    # We take a longer set of input every time until we have a winner
    draw = NUMBERS[0:n+1]

    # Check if our cards have a winner with this draw
    for card in CARDS:
        if has_bingo(card, draw):
            winners += 1
            print ("winners so far: ", winners)

            # Remove this card from CARDS
            CARDS.remove(card)

            # Was this the last card of our board? Then we have a winner
            if winners == initial_cards:
                print ("The last winner card: ")
                print(bingo_score(card, draw))
