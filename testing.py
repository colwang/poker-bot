from poker_classes import *

A_spades = card("A", "Spades")
print(A_spades)

game_deck = deck()
print(game_deck.get_size())

print(game_deck.card_pile[45:])
# print ([str(card) for card in game_deck.card_pile[45:]])

game_deck.shuffle()
print(game_deck.card_pile[45:])
