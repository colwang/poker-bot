from poker_classes import *


poker_game = game(5,10)

reveal = False

if poker_game.pre_flop():
    if poker_game.flop():
        if poker_game.turn_river():
            if poker_game.turn_river():
                print("Game Done")
                reveal = True
                
poker_game.determine_winner(reveal)

