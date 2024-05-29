import random


def generate_bingo_card():
    numbers = random.sample(range(1, 91), 24)

    numbers.sort()

    bingo_card = [[None] * 5 for _ in range(5)]

    counter = 0
    for row in range(5):
        for col in range(5):
            if row == 2 and col == 2:
                bingo_card[row][col] = 'BINGO!'
            else:
                bingo_card[row][col] = numbers[counter]
                counter += 1

    return bingo_card


def display_bingo_card(bingo_card):
    for row in bingo_card:
        print(" | ".join(str(cell).center(6) for cell in row))
        print("-" * 29)


bingo_card = generate_bingo_card()
display_bingo_card(bingo_card)
