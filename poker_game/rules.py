HIGH_CARD_BASE_HAND_SCORE = 1
ONE_PAIR_BASE_HAND_SCORE = 15
TWO_PAIR_BASE_HAND_SCORE = 26
THREE_OF_A_KIND_BASE_HAND_SCORE = 184
STRAIGHT_BASE_HAND_SCORE = 195
FLUSH_HAND_SCORE = 205
FULL_HOUSE_BASE_HAND_SCORE = 206
FOUR_OF_A_KIND_BASE_HAND_SCORE = 362
STRAIGHT_FLUSH_BASE_HAND_SCORE = 375
ROYAL_FLUSH_HAND_SCORE = 384

def rules(board, arr_of_players):
    player_hands = []
    for player in arr_of_players:
        player_hands.append(player.get_hand)
    
    for hand in player_hands:
        inPlay = board + hand
        hand_score = 0

        hearts = 0
        clubs = 0
        diamonds = 0
        spades = 0
        repeats = set()
        count = {}

        for card in inPlay:
            rank = card.getRank()
            suit = card.getSuit()
            
            # counts number of cards per suit
            if suit == "h":
                hearts += 1
            elif suit == "c":
                clubs += 1
            elif suit == "d":
                diamonds += 1
            else:
                spades += 1
            
            # checks for repeats and how many of those repeats there are
            if card in repeats:
                if rank in count:
                    count[rank] += 1
                else:
                    count[rank] = 2
            else:
                repeats.add(rank)
        
        flush = False
        straight = False

        # checks for flushes
        if hearts >= 5 or clubs >=5 or diamonds >= 5 or spades >= 5:
            flush = True
        
        # checks for straights
        cardRanks = []
        for card in repeats:
            cardRanks.append(getRankValue())
        if 14 in cardRanks:
            cardRanks.append(1)
        cardRanks.sort()

        consecutiveCards = 0
        lastRank = -1
        straightCards = []
        for rank in cardRanks:
            if lastRank + 1 == rank:
                consecutiveCards += 1
                straightCards.append(rank)
            else:
                consecutiveCards = 0
                straightCards = []
            lastRank = rank
        
        """
        Hand Rankings
        For this, a hearts flush is equivalent to a spades flush
        Eights-full-of-threes is greater than sevens-full-of-aces

        12 possible high card (1-12)
        13 possible one pair (13-25)
        13 * 12 = 156 possible two pairs (26-181)
        13 possible three-of-a-kind (182-194)
        10 possible straights (195-204)
        1 possible flush (205)
        13 * 12 = 156 possible full houses (206-361)
        13 possible four-of-a-kind (362-374)
        9 possible straight flushes (375-383)
        1 possible royal flush (384)

        Total: 384 possible rankings 
        """

        # checks for royal flush
        if flush and straight:
            if 10 in straightCards and 11 in straightCards and 12 in straightCards and 13 in straightCards and 14 in straightCards:
                hand_score = ROYAL_FLUSH_HAND_SCORE
            



        




