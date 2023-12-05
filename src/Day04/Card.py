class Card:

    def __init__(self, card = None):
        self.card_number = None
        self.winning_numbers = []
        self.numbers = []
        self.numbers_that_won = []

        if card:
            self.import_card(card)

    def import_card(self, card_text):
        self.card_number = int(card_text.strip().split(':')[0].split()[1])
        sections = card_text.strip().split(':')[1].strip().split('|')
        self.winning_numbers = [a.strip() for a in sections[0].strip().split()]
        self.numbers = [a.strip() for a in sections[1].strip().split()]

        for n in self.numbers:
            if n in self.winning_numbers:
                self.numbers_that_won.append(n)

    def get_part1_points(self):
        if len(self.numbers_that_won) == 0:
            return 0
        elif len(self.numbers_that_won) == 1:
            return 1
        else:
            points = 1
            for i in range(len(self.numbers_that_won) - 1):
                points *= 2
            return points