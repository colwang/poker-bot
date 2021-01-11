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

    def restart_game(self):
        
        self.card_pile = list()
        
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

        for suit in suits:
            for num in numbers:
                self.card_pile.append(card(num, suit))       

class player:

    def __init__(self, is_human, name, buy_in):

        if is_human:
            self.human = True

        self.money_balance = buy_in

        self.hand = []
        self.playing = True
        self.turn_done = False
        self.name = name

    def move(self, current_bet, min_raise, position):

        if self.human:
            
            valid_move = false
            bet_raise = current_bet

            while not valid_move:
                if current_bet == 0:
                    move = input("Check, Raise, or Fold (C/R/F):")
                else: 
                    move = input("Call, Raise, or Fold (C/R/F):")

                if move.lower == "c":
                    self.turn_done = True
                    self.money_balance -= current_bet
                    valid_move = True
                    if current_bet == 0:
                        print(self.name, "checked.")
                    else:
                        print(self.name, "called.")

                elif move.lower == "r":
                    bet_raise = input("What would you like to raise it to?")

                    while (bet_raised - current_bet) < min_raise:
                        bet_raise = input("Sorry, the minimum raise is " + str(min_raise) + ". What would you like to raise it to?")

                    self.money_balance -= bet_raise
                    valid_move = True
                    print(self.name, "raised to $", bet_raise)

                elif move.lower == "f":
                    self.turn_done = True
                    self.playing = False
                    valid_move = True
                    print(self.name, "folded.")

                else:
                    print("Please enter a valid move.")

                return bet_raise - current_bet, self.turn_done, self.playing




            

    
