nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,      31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54}
vall = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}
suits = {1: "♤", 2: "♡", 3: "♧", 4: "♢"}


class Card:
    def __init__(self, nums, suit, vall):
        self.nums = nums[nums]
        self.vall = vall[vall]
        self.suit = suits[suit]

    # def show(self):
    #     print(f'{self.suit}{self.name}')


card_1 = Card(8, 3)
card_2 = Card(12, 2)

deck = {}
i = nums
for suit in suits:
    for number in nums:
        deck.update({i: Card(number, suit)})
        i += 1

deck[4].show()
