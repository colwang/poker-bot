import random
from Poker.poker_game.player import *

class Deck: 
    """
    Initializes a new standard deck with 52 cards
    """
    def __init__(self):
        self.deck = []
        suits = ["h", "c", "d", "s"]
        ranks = list(range(2, 10)) + list("J", "Q", "K", "A")

        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.deck.append(card)

    """
    Shuffles the deck
    """
    def shuffle(self):
        random.shuffle(self.deck)

    """
    Draws a card from the deck and removes it from the preexisting deck

    @param number of cards you want to draw
    @return an array of size number of cards from the top of the deck
    """
    def draw(self, number):
        cards = []
        for i in range(number):
            cards.append(self.deck.pop(0))

        return cards

    """
    Begins the game of poker by drawing the river

    @return an array of the 3 cards that form the flop
    """
    def get_flop(self):
        burn = self.draw(1)
        flop = self.draw(3)
        return flop
    
    """
    Continues the second round of poker by drawing the turn

    @return an array of 1 card for the turn
    """
    def get_turn(self):
        burn = self.draw(1)
        turn = self.draw(1)
        return turn
    
    """
    Finishes the last action of poker by drawing the river

    @return an array of 1 card for the river
    """
    def get_river(self):
        burn = self.draw(1)
        river = self.draw(1)
        return river
    

    """
    Deals cards from the top of the deck to form the players hands

    @param an array of Player objects
    """
    def deal_hands(self, arr_of_players):
        for i in range(2):
            for player in arr_of_players:
                player.add_hand(self.draw(1))
