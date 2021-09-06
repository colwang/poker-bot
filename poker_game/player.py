from Poker.poker_game.deck import *


class Player:
    """
    Initializes a Player in the poker game
    """
    def __init__(self, name, buy_in, is_human):
        
        self.name = name
        self.balance = int(buy_in)
        self.is_human = is_human
        self.hand = list()
        self.total_bet = 0
        self.prev_bet = 0
        self.all_in = False

    """
    Adds the card to the Players hand
    """
    def add_hand(self, card):
        self.hand.append(card)

    """
    Gets the Players hand

    @ return array of 2 cards
    """
    def get_hand(self):
        return self.hand


    """
    Handles the Player's move input
    """
    def get_player_move(self, prev_bet):
        player_move = ""
        if self.is_human:
            valid_move = False
            if prev_bet == 0: 
                player_move = input("Previous bet is 0. Check, Bet, or Fold? (Enter C/B/F): ")
                while not valid_move:
                    if player_move in "cCbBfF":
                        valid_move = True
                    else:
                        player_move = input("""Please enter valid move. Previous bet is 0. 
                                               Check, Bet, or Fold? (Enter C/B/F): """)
            else:
                player_move = input("Previous bet is " + str(prev_bet) + 
                                    ". Call, Raise, or Fold? (Enter C/R/F): ")
                while not valid_move:
                    if player_move in "cCrRfF":
                        valid_move = True
                    else:
                        player_move = input("Please enter valid move. Previous bet is " 
                                            + str(prev_bet) + ". Call, Raise, or Fold? (Enter C/R/F): ")
        return player_move

    """
    Implements calling
    """
    def call_bet(self, bet):
        # making sure the player has the funds to call the full bet
        if (self.balance - bet) < 0:
            self.total_bet += self.balance
            self.prev_bet = self.balance
            self.balance = 0
            self.all_in = True
        else: 
            self.total_bet += bet
            self.prev_bet = 0
            self.balance -= bet

        print(self.name + " called the bet of " + str(bet))

    """
    Implements raising
    """
    def raise_bet(self, bet, min_raise):
        raise_amount = input("What would you like to raise it to?")
        # forcing the player to make at least the min raise
        if (raise_amount - bet) < min_raise:
            raise_amount = bet + min_raise
        # making sure the player has the funds for the raise
        if raise_amount > self.balance:
            raise_amount = self.balance
        
        self.total_bet += raise_amount
        self.balance -= raise_amount

        print(self.name + " raised to " + str(raise_amount)) 
