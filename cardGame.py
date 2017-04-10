import random

class Card(object):
    """Class holding members and methods of Card"""
    def __init__(self, suit, val):
        """Initialize object of Card class"""
        self.suit = suit
        self.value = val

    def show(self):
        """Prints/Shows card"""
        # print "{} of {}".format(self.value, self.suit)

        if self.value in range(2, 11):
            print "{} of {}".format(self.value, self.suit)
        else:
            if self.value == 1:
                print "{} of {}".format("Ace", self.suit)
            elif self.value == 11:
                print "{} of {}".format("Jack", self.suit)
            elif self.value == 12:
                print "{} of {}".format("Queen", self.suit)
            else:
                print "{} of {}".format("King", self.suit)



class Deck(object):
    """Class holding members and methods of Deck"""
    def __init__(self):
        """Initialize object of Deck class"""
        self.cards = []
        self.build()

    def build(self):
        """Builds a deck"""
        for _suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for _card in range(1, 14):
                self.cards.append(Card(_suit, _card))

    def show(self):
        """Shows all cards in deck"""
        for _card in self.cards:
            _card.show()

    def shuffle(self):
        """Shuffles cards in deck"""
        for _idx in range(len(self.cards)-1, 0, -1):
            _rand_idx = random.randint(0, _idx)
            self.cards[_idx], self.cards[_rand_idx] = self.cards[_rand_idx], self.cards[_idx]

    def draw(self):
        """draws the last card from deck"""
        return self.cards.pop()


class Player(object):
    """Class holding members and methods of Deck"""
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, _deck):
        """appends a card from deck to the hand"""
        self.hand.append(_deck.draw())
        return self

    def show_hand(self):
        """"shows cards in hand"""
        for card in self.hand:
            card.show()

# card = Card("Hearts", 6)
# card.show()
# DECK = Deck()
# DECK.shuffle()

# BOB = Player("bob")
# BOB.draw(DECK).draw(DECK)
# BOB.show_hand()

# card = deck.draw()
# card.show()