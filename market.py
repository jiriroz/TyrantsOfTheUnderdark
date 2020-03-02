
class Market:
    """
    @param all_cards cards.Cards
    @param cards_in_deck list
    @param num_priestesses int
    @param num_house_guards int
    @param num_outcasts int
    """
    def __init__(self, all_cards, cards_in_deck, num_priestesses, num_house_guards, num_outcasts):
        self.all_cards = all_cards
        self.num_market_cards = 6
        self.market_cards = []
        self.cards_in_deck = cards_in_deck
        self.num_priestesses = num_priestesses
        self.num_house_guards = num_house_guards
        self.num_outcasts = num_outcasts
        self.cards_devoured = []

        for x in range(self.num_market_cards):
            self.market_cards.append(self.cards_in_deck.pop())

    def get_market_cards(self):
        return self.market_cards

    def draw_market_card(self, index):
        assert index < self.num_market_cards
        card = self.market_cards[index]
        self.market_cards[index] = None
        if len(self.cards_in_deck) > 0:
            self.market_cards[index] = self.cards_in_deck.pop()
        return card

    def get_num_priestesses(self):
        return self.num_priestesses

    def draw_priestess(self):
        if self.num_priestesses <= 0:
            raise ValueError('No more priestesses in the market')
        self.num_priestesses -= 1
        return self.all_cards.get_by_name('Priestess of Lolth')

    def get_num_house_guards(self):
        return self.num_house_guards

    def draw_house_guard(self):
        if self.num_house_guards <= 0:
            raise ValueError('No more house guards in the market')
        self.num_house_guards -= 1
        return self.all_cards.get_by_name('House Guard')

    def get_num_outcasts(self):
        return self.num_outcasts

    def draw_outcast(self):
        if self.num_outcasts <= 0:
            raise ValueError('No more outcasts in the market')
        self.num_outcasts -= 1
        return self.all_cards.get_by_name('Insane Outcast')

    def devour_card(self, card):
        self.cards_devoured.append(card)


if __name__ == '__main__':
    import cards
    import random
    all_cards = cards.load_cards('cards.csv')
    dragon = all_cards.get_by_deck(cards.Deck.DRAGON)
    demon = all_cards.get_by_deck(cards.Deck.DEMON)
    deck_cards = dragon + demon
    random.shuffle(dragon + demon)

    num_priestesses = all_cards.get_by_name('Priestess of Lolth').count
    num_house_guards = all_cards.get_by_name('House Guard').count
    num_outcasts = all_cards.get_by_name('Insane Outcast').count

    market = Market(all_cards, deck_cards, num_priestesses, num_house_guards, num_outcasts)

    print ("Market cards")
    for c in market.get_market_cards():
        print (c)
    print ("Draw card")
    print (market.draw_market_card(1))
    print ("Draw card")
    print (market.draw_market_card(5))
    print ("Market cards")
    for c in market.get_market_cards():
        print (c)
    print ("Draw priestess")
    print (market.draw_priestess())
    print ("Draw house guard")
    print (market.draw_house_guard())
    print ("Draw outcast")
    print (market.draw_outcast())
    print ("num priestesses = {} num guards = {} num outcasts = {}".format(
        market.get_num_priestesses(), market.get_num_house_guards(), market.get_num_outcasts()
    ))
