import csv

from enum import Enum

class Deck(Enum):
    STARTER = 1
    CORE = 2
    DROW = 3
    ELEMENTAL = 4
    DEMON = 5
    DRAGON = 6

class Aspect(Enum):
    OBEDIENCE = 1
    MALICE = 2
    CONQUEST = 3
    GUILE = 4
    AMBITION = 5

class Card:
    def __init__(self):
        self.ID = None
        self.name = None
        self.deck = None
        self.aspect = None
        self.cost = None
        self.deckVP = None
        self.innerCircleVP = None
        self.count = None
    def __str__(self):
        return 'ID={} name={} deck={} aspect={} cost={} deckVP={} innerCircleVP={} count={}'.format(
            self.ID, self.name, self.deck, self.aspect, self.cost, self.deckVP, self.innerCircleVP, self.count
        )

class Cards:
    def __init__(self):
        self.cards = dict()
        self.cards_by_name = dict()
    def __str__(self):
        s = ''
        for ID in self.cards:
            s += str(self.cards[ID])
            s += '\n'
        return s

    def add(self, card):
        self.cards[card.ID] = card
        self.cards_by_name[card.name] = card

    def get_by_name(self, name):
        if name not in self.cards_by_name:
            raise ValueError("Card {} doesn't exist".format(name))
        return self.cards_by_name[name]

    def get_by_deck(self, deck):
        return [self.cards[id] for id in self.cards if self.cards[id].deck == deck]

def load_cards(cards_file):
    def intOrNone(val):
        if val == '':
            return None
        return int(val)
    rows = []
    with open(cards_file) as f:
        rows = [row for row in csv.DictReader(f, delimiter=',')]

    cards = Cards()
    for row in rows:
        card = Card()
        card.ID = int(row['ID'])
        card.name = row['Name']
        card.deck = Deck[row['Deck'].upper()]
        if row['Aspect'] == '':
            card.aspect = None
        else:
            card.aspect = Aspect[row['Aspect'].upper()]
        card.cost = intOrNone(row['Cost'])
        card.deckVP = intOrNone(row['DeckVP'])
        card.innerCircleVP = intOrNone(row['InnerCircleVP'])
        card.count = intOrNone(row['Count'])
        cards.add(card)
    return cards

if __name__ == '__main__':
    cards = load_cards('cards.csv')
    print (cards)