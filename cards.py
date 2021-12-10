import random

numbers = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}
suits = {1: "♤", 2: "♡", 3: "♧", 4: "♢"}


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.name = numbers[number]
        self.suit = suits[suit]

    def show(self):
        print(f'{self.suit}{self.name}')

    def __str__(self):
        return f'{self.suit}{self.name}'


class Player:
    def __init__(self, money):
        self.cards = []
        self.money = money

    def append(self, card):
        self.cards.append(card)

    def do_step(self, cards):
        step = []
        for card in cards:
            j = self.cards.pop(card)
            step.append(j)
        return step

    def take_cards(self, deck, n_cards):
        for _ in range(n_cards):
            self.cards.append(deck.pop(0))


card_map = {}
i = 1
for suit in suits:
    for number in numbers:
        card_map.update({i: Card(number, suit)})
        i += 1


def get_deck():
    card_deck = [i for i in range(1, 53)]
    random.shuffle(card_deck)
    return card_deck
deck = get_deck()