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
        count = [0] * 13

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

            repeats.add(rank)
            count[rank - 2] += 1

        flush = False
        straight = False
        quads = False
        trips = False
        num_pairs = 0
        firstKeyCard = 0
        secondKeyCard = 0
        kicker = -1

        for i in range(12, -1, -1):
            # searches for quads
            if count[i] == 4:
                quads = True
                firstKeyCard = i
            # searches for trips
            elif count[i] == 3:
                trips = True
                firstKeyCard = i
            # searches for pairs
            elif count[i] == 2:
                num_pairs += 1
                if trips and num_pairs == 1:
                    secondKeyCard = i
                elif num_pairs == 1:
                    firstKeyCard = i
                elif num_pairs == 2:
                    secondKeyCard = i
            # searches for kicker
            elif count[i] == 1:
                if kicker == -1:
                    kicker = i
                    

        # checks for flushes
        if hearts >= 5 or clubs >= 5 or diamonds >= 5 or spades >= 5:
            flush = True

        # checks for straights
        cardRanks = [0] * 14
        for card in repeats:
            cardRanks[card.getRankValue() - 1] = 1
        if cardRanks[13] == 1:
            cardRanks[0] = 1

        consecutiveCards = 0
        startOfStraight = 0
        for i in range(14):
            if cardRank[i] >= 1:
                consecutiveCards += 1
            elif consecutiveCards >= 5:
                straight = True
                break
            else:
                consecutiveCards = 0
                startOfStraight = i + 1
        if consecutiveCards >= 5:
            straight = True

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

        # checks for royal and straight flush
        if flush and straight:
            if 10 in straightCards and 11 in straightCards and 12 in straightCards and 13 in straightCards and 14 in straightCards:
                hand_score = ROYAL_FLUSH_HAND_SCORE
            else:
                hand_score = STRAIGHT_FLUSH_BASE_HAND_SCORE + startOfStraight

        # checks for quads
        elif quads:
            hand_score = FOUR_OF_A_KIND_BASE_HAND_SCORE + firstKeyCard

        # checks for full house
        elif trips and num_pairs >= 1:
            hand_score = FULL_HOUSE_BASE_HAND_SCORE + 12 * firstKeyCard + secondKeyCard
        
        # checks for flush
        # THIS IS GONNA BE THE TRUE DOOZY

        # checks for straight
        elif straight:
            hand_score = STRAIGHT_BASE_HAND_SCORE + startOfStraight

        # checks for trips
        elif trips:
            hand_score = THREE_OF_A_KIND_BASE_HAND_SCORE + firstKeyCard
        
        # checks for two pairs
        elif num_pairs >= 2:
            hand_score = TWO_PAIR_BASE_HAND_SCORE + 12 * firstKeyCard + secondKeyCard

        # checks for one pair
        elif num_pairs == 1:
            hand_score = ONE_PAIR_BASE_HAND_SCORE + firstKeyCard

        # checks for high card
        elif num_pairs == 1:
            hand_score = HIGH_CARD_BASE_HAND_SCORE + kicker