import random
import board

NUM_IN_HAND = 5

class Player:
    def __init__(self, color, num_troops, num_spies):
        self.color = color
        self.hand = []
        self.deck = []
        self.discard_pile = []
        self.inner_circle = []
        self.trophy_hall = dict()
        for color in board.Color:
            self.trophy_hall[color] = 0
        self.num_troops = num_troops
        self.num_spies = num_spies

    def add_card_to_dicard_pile(self, card):
        self.discard_pile.append(card)

    def add_card_to_deck(self, card):
        self.deck.append(card)

    def get_hand(self):
        return self.hand

    def new_hand(self):   
        self.discard_pile.extend(self.hand)
        self.hand = []
        to_draw = min(NUM_IN_HAND, len(self.deck))
        self.hand = self.deck[:to_draw]
        self.deck = self.deck[to_draw:]
        if len(self.hand) < NUM_IN_HAND:
            self.deck = self.discard_pile
            self.discard_pile = []
            random.shuffle(self.deck)
            to_draw = min(NUM_IN_HAND - len(self.hand), len(self.deck))
            self.hand.extend(self.deck[:to_draw])
            self.deck = self.deck[to_draw:]

    def get_num_killed(color):
        return self.trophy_hall[color]

    def add_num_killed(color, count):
        self.trophy_hall[color] += count

if __name__ == '__main__':
    import cards
    player = Player(board.Color.BLUE, 20, 20)
    all_cards = cards.load_cards('cards.csv')
    dragon = all_cards.get_by_deck(cards.Deck.DRAGON)
    demon = all_cards.get_by_deck(cards.Deck.DEMON)
    deck_cards = dragon + demon
    random.shuffle(deck_cards)

    for x in range(7):
        player.add_card_to_deck(deck_cards[x])

    player.new_hand()
    print ("Hand")
    for c in player.get_hand():
        print (c)

    player.new_hand()
    print ("Hand")
    for c in player.get_hand():
        print (c)


