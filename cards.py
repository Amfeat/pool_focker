numbers = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}
suits = {1: "♤", 2: "♡", 3: "♧", 4: "♢"}


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.name = numbers[number]
        self.suit = suits[suit]

    def show(self):
        print(f'{self.suit}{self.name}')


card_1 = Card(8,3)
card_2 = Card(12,2)

deck = {}
i = 1
for suit in suits:
    for number in numbers:
        deck.update({i: Card(number, suit)})
        i += 1

deck[4].show()
