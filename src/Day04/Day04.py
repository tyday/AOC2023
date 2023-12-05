from Card import Card
from helper.FileHelper import file_helper

def part_two(cards):
    winning_cards = [0 for card in cards]
    print(winning_cards)
    # for card in cards

def part_one(cards):
    part_one_total = 0
    for card in cards:
        print(f'Card #{card.card_number}:Points: {card.get_part1_points()} -- {card.numbers_that_won}')
        part_one_total += card.get_part1_points()
    print(f"Part one total: {part_one_total}")

def main(filename):
    data = file_helper(filename)

    cards = []
    for line in data:
        cards.append(Card(line))
    # part_one(cards)
    part_two(cards)


if __name__ == '__main__':
    main("testdata.txt")