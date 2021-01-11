from poker_classes import *


game_deck = deck()

small_blind = input("What is small blind?")
big_blind = input("What is big blind?")

num_human_players = int(input("How many players?"))
num_AI = int(input("How many AI?"))


# establishing players
players = list()

for i in range(num_human_players):
    name = input("Player " + str(i + 1) + ", what is your name?")
    amount_buy_in = input("How much would you like to buy in for?")
    players.append(player(True, name, amount_buy_in)

for i in range(num_AI):
    AI_name = "AI " + str(i + 1)
    players.append(player(False, AI_name, 1000))


# establishing player order
positions = list()
for i in range(num_human_players + num_AI):
    positions.append(i)
random.shuffle(positions)

player_positions = dict()
for i in range(num_human_players + num_AI):
    player_positions[positions[i]] = players[i] 


# starting game
want_to_play = True
while want_to_play:
    game_deck.deal_hand(players)
