import random

class card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def get_score(self, scoreboard):
        # Scoreboard goes 2-10, J, Q, K, A, Clubs, Diamonds, Hearts, Spades

        if self.suit == "Clubs":
            scoreboard[13] += 1
        elif self.suit == "Diamonds":
            scoreboard[14] += 1
        elif self.suit == "Hearts":
            scoreboard[15] += 1
        else:
            scoreboard[16] += 1

        if self.number == "A":
            scoreboard[12] += 1
        elif self.number == "K":
            scoreboard[11] += 1
        elif self.number == "Q":
            scoreboard[11] += 1
        elif self.number == "J":
            scoreboard[11] += 1
        else:
            index = int(self.number) - 2
            scoreboard[index] += 1

    def __eq__(self, other):
        if self.number == other.number and self.suit == other.suit:
            return True
        else:
            return False

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
    
    def get_turn_river(self):

        turn = self.card_pile.pop(-1)

        return turn

    def deal_hand(self, players):

        for player in players:

            player.hand.append(self.card_pile.pop(-1))
            player.hand.append(self.card_pile.pop(-1))

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

        self.money_balance = int(buy_in)

        self.hand = list()
        self.hand_scoreboard = [0] * 17      # Goes 2-10, J, Q, K, A, Clubs, Diamonds, Hearts, Spades
        self.hand_ranking = [0] * 12         # Goes High Card, Pair, Two Pair, Three of a Kind, Straight, Flush
                                             # Full House, Four of a Kind, Straight Flush, Royal Flush, then the two card numbers
        self.playing = True
        self.turn_done = False
        self.name = name
        self.previous_bet = 0
        self.your_bet = 0

    def pay_blind(self, blind):
        self.money_balance -= blind
        self.previous_bet = blind

    def move(self, current_bet, min_raise):

        if self.human:
            
            self.turn_done = False
            valid_move = False

            print()
            print(self.name + ":")
            print("Your Balance:", self.money_balance)
            print("Your Hand:", self.hand)

            while not valid_move:
                if current_bet == 0:
                    move = input("Check, Raise, or Fold (C/R/F): ")
                else: 
                    move = input("Call, Raise, or Fold (C/R/F): ")

                if move.lower() == "c":
                    self.turn_done = True
                    self.your_bet = current_bet
                    self.money_balance -= (self.your_bet - self.previous_bet)
                    valid_move = True
                    if current_bet == 0:
                        print(self.name, "checked.")
                    else:
                        print(self.name, "called.")

                elif move.lower() == "r":
                    self.your_bet = int(input("What would you like to raise it to? "))

                    while (self.your_bet - current_bet) < min_raise:
                        self.your_bet = int(input("Sorry, the minimum raise is " + str(min_raise) + ". What would you like to raise the bet to? "))

                    while self.your_bet > self.money_balance:
                        self.your_bet = int(input("Sorry, your balance is currently " + str(self.money_balance) + ". What would you like to raise the bet to?"))

                    self.money_balance -= (self.your_bet - self.previous_bet)
                    min_raise = self.your_bet - current_bet
                    valid_move = True
                    print(self.name, "raised to $", self.your_bet)

                elif move.lower() == "f":
                    self.turn_done = True
                    self.playing = False
                    valid_move = True
                    print(self.name, "folded.")

                else:
                    print("Please enter a valid move.")

            previous_bet = self.previous_bet
            self.previous_bet = self.your_bet

            return previous_bet, self.your_bet, min_raise, self.turn_done, self.playing

    def __repr__(self):
        return self.name

class game:

    def __init__(self, small_blind, big_blind):

        self.game_deck = deck()
        self.game_deck.shuffle()

        self.small_blind = small_blind
        self.big_blind = big_blind
        self.game_board = list()
        self.game_pot = 0
        self.game_scoreboard = [0] * 17      # Goes 2-10, J, Q, K, A, Clubs, Diamonds, Hearts, Spades

        self.num_human_players = int(input("How many players? "))
        self.num_AI = int(input("How many AI? "))
        self.total_players = self.num_human_players + self.num_AI

        if self.total_players == 0:
            print("No players playing. Have a good day.")
        
        else:    

            # establishing players
            self.players = list()
            self.playing = [True] * (self.total_players) 

            for i in range(self.num_human_players):
                name = input("Player " + str(i + 1) + ", what is your name? ")
                amount_buy_in = input("How much would you like to buy in for? ")
                self.players.append(player(True, name, amount_buy_in))

            for i in range(self.num_AI):
                AI_name = "AI " + str(i + 1)
                self.players.append(player(False, AI_name, 1000))


            # establishing player order
            self.positions = list()
            for i in range(self.total_players):
                self.positions.append(i)
            random.shuffle(self.positions)

            player_positions = dict()
            for i in range(self.total_players):
                player_positions[self.positions[i]] = self.players[i]
            self.play_order = dict(sorted(player_positions.items()))

            # print(self.turn_order)

    def pre_flop(self):
        
        self.game_deck.deal_hand(self.players)
        for player in self.players:
            for card in player.hand:
                card.get_score(player.hand_scoreboard)

        print()
        print("Play order:", self.play_order)

        preflop_round_done = [False] * (self.total_players)

        self.play_order[0].pay_blind(self.small_blind)
        print(self.play_order[0].name, "paid small blind of", self.small_blind)
        self.game_pot += self.small_blind
        
        self.play_order[1].pay_blind(self.big_blind)
        print(self.play_order[1].name, "paid big blind of", self.big_blind)
        self.game_pot += self.big_blind
        
        current_bet = self.big_blind
        min_raise = self.big_blind - self.small_blind

        active_player = 1
        while False in preflop_round_done:
            
            active_player += 1
            if active_player >= self.total_players:
                active_player = active_player % self.total_players
            
            index = self.players.index(self.play_order[active_player])
            if preflop_round_done[index] or not self.playing[index]:
                continue

            print("Current Bet:", current_bet)
            print("Min Raise:", min_raise)
            print("Current Pot:", self.game_pot)
            previous_bet, bet_raise, min_raise, turn_done, playing = self.play_order[active_player].move(current_bet, min_raise)
            current_bet = bet_raise
            if playing:
                self.game_pot += bet_raise - previous_bet

            if not turn_done:
                preflop_round_done = [False] * (self.total_players)
                preflop_round_done[index] = True
                
                for i in range(self.total_players):
                    if not self.playing[i]:
                        preflop_round_done[i] = True
            else:
                preflop_round_done[index] = turn_done

            if not playing:
                self.playing[index] = playing
                if self.playing.count(True) < 2:
                    return False

        print()
        print("Preflop round done.")
        print()

        return True

    def flop(self):

        flop_1, flop_2, flop_3 = self.game_deck.get_flop()

        flop_1.get_score(self.game_scoreboard)
        flop_2.get_score(self.game_scoreboard)
        flop_3.get_score(self.game_scoreboard)

        self.game_board.append(flop_1)
        self.game_board.append(flop_2)
        self.game_board.append(flop_3)

        print("Flop:")
        print("----------------------------------------")
        print(self.game_board)
        
        flop_round_done = [False] * (self.total_players)
        for i in range(self.total_players):
            if not self.playing[i]:
                flop_round_done[i] = True

        current_bet = 0
        min_raise = 0

        active_player = -1
        while False in flop_round_done:
            
            active_player += 1
            if active_player >= self.total_players:
                active_player = active_player % self.total_players
            
            index = self.players.index(self.play_order[active_player])
            if flop_round_done[index] or not self.playing[index]:
                continue

            print("Current Bet:", current_bet)
            print("Min Raise:", min_raise)
            print("Current Pot:", self.game_pot)
            previous_bet, bet_raise, min_raise, turn_done, playing = self.play_order[active_player].move(current_bet, min_raise)
            current_bet = bet_raise
            if playing:
                self.game_pot += bet_raise - previous_bet

            if not turn_done:
                flop_round_done = [False] * (self.total_players)
                flop_round_done[index] = True
                
                for i in range(self.total_players):
                    if not self.playing[i]:
                        flop_round_done[i] = True
            else:
                flop_round_done[index] = turn_done
            
            if not playing:
                self.playing[index] = playing
                if self.playing.count(True) < 2:
                    return False

        print()
        print("Flop round done.")

        return True


    def turn_river(self):

        turn_river = self.game_deck.get_turn_river()
        turn_river.get_score(self.game_scoreboard)
        self.game_board.append(turn_river)

        if len(self.game_board) == 4:
            print("Turn:")
        else:
            print("River")
        print("----------------------------------------")
        print(self.game_board)
        
        round_done = [False] * (self.total_players)
        for i in range(self.total_players):
            if not self.playing[i]:
                round_done[i] = True

        current_bet = 0
        min_raise = 0

        active_player = -1
        while False in round_done:
            
            active_player += 1
            if active_player >= self.total_players:
                active_player = active_player % self.total_players
            
            index = self.players.index(self.play_order[active_player])
            if round_done[index] or not self.playing[index]:
                continue

            print("Current Bet:", current_bet)
            print("Min Raise:", min_raise)
            print("Current Pot:", self.game_pot)
            previous_bet, bet_raise, min_raise, turn_done, playing = self.play_order[active_player].move(current_bet, min_raise)
            current_bet = bet_raise
            if playing:
                self.game_pot += bet_raise - previous_bet

            if not turn_done:
                round_done = [False] * (self.total_players)
                round_done[index] = True

                for i in range(self.total_players):
                    if not self.playing[i]:
                        round_done[i] = True
            else:
                round_done[index] = turn_done
            
            if not playing:
                self.playing[index] = playing
                if self.playing.count(True) < 2:
                    return False

        print()
        if len(self.game_board) == 4:
            print("Turn round done.")
        else:
            print("River round done.")

        return True

    def determine_winner(self, reveal):

        if reveal:
            for player in self.players:

                for card in self.game_board:
                    player.hand.append(card)

                for i in range(17):
                    player.hand_scoreboard[i] += self.game_scoreboard[i]

                # check for straight
                for i in range(9):
                    if (player.hand_scoreboard[i] > 0 and player.hand_scoreboard[i + 1] > 0 and player.hand_scoreboard[i + 2] > 0 
                        and player.hand_scoreboard[i + 3] > 0 and player.hand_scoreboard[i + 4] > 0):

                        # check for flush with straight
                        for j in range(13, 16):
                            if player.hand_scoreboard[j] >= 5:
                                if j == 13:
                                    flush_suit = "Clubs"
                                elif j == 14:
                                    flush_suit = "Diamonds"
                                elif j == 15:
                                    flush_suit = "Hearts"
                                elif j == 16:
                                    flush_suit = "Spades"

                                # check for royal flush
                                if i == 8:
                                    royal_flush = [False] * 5
                                    if card("10", flush_suit) in player.hand:
                                        royal_flush[0] = True
                                    if card("J", flush_suit) in player.hand:
                                        royal_flush[1] = True
                                    if card("Q", flush_suit) in player.hand:
                                        royal_flush[2] = True
                                    if card("K", flush_suit) in player.hand:
                                        royal_flush[3] = True
                                    if card("A", flush_suit) in player.hand:
                                        royal_flush[4] = True

                                    if False not in royal_flush:
                                        player.hand_ranking[9] = 1

                                # check for straight flush
                                else:
                                    straight_flush = [False] * 5

                                    if i + 2 == 9:
                                        card_3_number = "J"
                                    else:
                                        card_3_number = str(i + 4)
                                    
                                    if i + 3 == 9:
                                        card_4_number = "J"
                                    elif i + 3 == 10:
                                        card_4_number = "Q"
                                    else:
                                        card_4_number = str(i + 5)
                                    
                                    if i + 4 == 9:
                                        card_5_number = "J"
                                    elif i + 4 == 10:
                                        card_5_number = "Q"
                                    elif i + 4 == 11:
                                        card_5_number = "K"
                                    else:
                                        card_5_number = str(i + 6)

                                    if card(str(i + 2), flush_suit) in player.hand:
                                        straight_flush[0] = True
                                    if card(str(i + 3), flush_suit) in player.hand:
                                        straight_flush[1] = True
                                    if card(card_3_number, flush_suit) in player.hand:
                                        straight_flush[2] = True
                                    if card(card_4_number, flush_suit) in player.hand:
                                        straight_flush[3] = True
                                    if card(card_5_number, flush_suit) in player.hand:
                                        straight_flush[4] = True

                                    if False not in straight_flush:
                                        player.hand_ranking[8] = 1

                        # has only straight
                        if player.hand_ranking[9] == 0 and player.hand_ranking[8] == 0:
                            player.hand_ranking[4] = 1

                # check for flush
                for i in range(13, 16):
                    if player.hand_scoreboard[j] >= 5:
                        player.hand_ranking[5] = 1

                pair_count = 0
                trips = False
                for i in range(13):

                    # 4 of a kind
                    if player.hand_scoreboard[i] == 4:
                        player.hand_ranking[7] = 1
                    elif player.hand_scoreboard[i] == 3:
                        trips = True
                    elif player.hand_scoreboard[i] == 2:
                        pair_count += 1
                    
                if trips and pair_count > 0:
                    player.hand_ranking[6] = 1
                elif trips:
                    player.hand_ranking[3] = 1
                elif pair_count > 1:
                    player.hand_ranking[2] = 1
                elif pair_count > 0:
                    player.hand_ranking[1] = 1
                else:
                    player.hand_ranking[0] = 1

                player.hand_ranking[10] = player.hand[0].number
                player.hand_ranking[11] = player.hand[1].number


        else:
            index = self.playing.index(True)
            print(self.players[index].name + " won the round with a pot of $" + str(self.game_pot) + ". Congrats!")



            






    
