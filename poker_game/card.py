
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __toString__(self):
        if self.suit == "h":
            suit = "Hearts"
        elif self.suit == "c":
            suit = "Clubs"
        elif self.suit == "d":
            suit = "Diamonds"
        else: 
            suit = "Spades"
            
        return self.rank + "of" + suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getRankValue(self):
        if self.rank in "2345678910":
            return int(self.rank)
        elif self.rank == "J":
            return int(11)
        elif self.rank == "Q":
            return int(12)
        elif self.rank == "K":
            return int(13)
        return int(14)
