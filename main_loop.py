from cards import deck, card_map, Player

def start():
    n_players = 4
    start_money = 10
    players = [Player(start_money) for _ in range(n_players)]
    serve(players, deck, 5)
    return players

def serve(players, cards, n_cards):
    for player in players:
        player.take_cards(cards, n_cards)


if __name__ == '__main__':
    players = start()
    for player in players:
        p_cards = [str(card_map[card]) for card in player.cards]
        print(p_cards)

    last = [str(card_map[card]) for card in deck]

    print('last cards', last)

    print(len(last))

    print([str(i) for i in card_map.values()])

    print(deck)
