

class Turn:
    def __init__(self, player, actions):
        self.player = player
        self.actions = actions
        self.cards_played = []
        self.current_card = None

    def play_card(self, card_index):
        if card_index >= len(self.player.get_hand()):
            raise ValueError('Card index out of range')
        elif card_index in self.cards_played:
            raise ValueError('Card was already played')
        if self.current_card != None:
            self.cards_played.append(self.current_card)
        self.current_card = card_index
        card = self.player.get_hand()[card_index]
        print ("Playing card", card)
        return self.actions.get(card.ID)

