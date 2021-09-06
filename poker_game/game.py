from Poker.poker_game.player import *

class game:
    
    """
    Initializes a poker game with the specified blinds
    """
    def __init__(self, small_blind, big_blind):
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.players = []
        
        self.pot = 0
        self.previous_bet = 0
        self.min_raise = 0

        self.game_board = []

    """
    Adds players to the poker game
    """
    def add_player(self):
        name = input("What is the player's name?")
        buy_in = input("What is the player's buy-in?")
        human_input = input("Is the player human")
        is_human = (human_input in "yesYes")

        self.player.append(player(name, buy_in, is_human))

    """
    Deals the flop (three cards)
    """
    def deal_flop(self, game_deck): 
        self.game_board.append(game_deck.get_flop)

    """
    Deals the turn (one card)
    """
    def deal_turn(self, game_deck): 
        self.game_board.append(game_deck.get_turn)

    """
    Deals the river (one card)
    """
    def deal_turn(self, game_deck): 
        self.game_board.append(game_deck.get_river)

    """
    Implements a full round of betting
    """
    def betting_round(self): 
        self.game_board.append(game_deck.get_river)
 