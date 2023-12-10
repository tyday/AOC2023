from Card import Card
from helper.FileHelper import file_helper

def part_two(cards):
    winning_cards = [0 for card in cards]
    # print(winning_cards)
    for i in range(len(cards)):
        card = cards[i]
        card_numb = card.card_number
        # print(card_numb)
        number_of_clones = winning_cards[i]
        if len(card.numbers_that_won) > 0:
            for j in range(len(card.numbers_that_won)):
                winning_cards[card_numb + j] += 1 + number_of_clones
    # print(winning_cards)
    clone_total = 0
    for i in range(len(cards)):
        card = cards[i]
        val = 1
        val += winning_cards[i]
        clone_total += val
    print(clone_total)
    return clone_total


def part_one(cards):
    part_one_total = 0
    for card in cards:
        print(f'Card #{card.card_number}:Points: {card.get_part1_points()} -- {card.numbers_that_won}')
        part_one_total += card.get_part1_points()
    return part_one_total

def main(filename):
    data = file_helper(filename)

    cards = []
    for line in data:
        cards.append(Card(line))
    part_one_total = part_one(cards)
    print(f"Part one total: {part_one_total}")
    part_two(cards)


if __name__ == '__main__':
    main("data.txt")