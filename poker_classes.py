import random

class card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return self.number + " of " + self.suit

    def __repr__(self):
        return str(self)

class deck:

    def __init__(self):

        self.card_pile = list()
        
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

        for suit in suits:
            for num in numbers:
                self.card_pile.append(card(num, suit))

    def get_size(self):

        return len(self.card_pile)

    def shuffle(self):

        random.shuffle(self.card_pile)

    def get_flop(self):

        flop_1 = self.card_pile.pop(-1)
        flop_2 = self.card_pile.pop(-1)       
        flop_3 = self.card_pile.pop(-1)

        return flop_1, flop_2, flop_3
    
    def get_turn(self):

        turn = self.card_pile.pop(-1)

        return turn

    def get_river(self):

        river = self.card_pile.pop(-1)

        return river

    def deal_hand(players):

        for player in players:

            player.hand.append(self.card_pile.pop(-1), self.card_pile.pop(-1))