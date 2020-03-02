

class Actions:
    def __init__(self, all_cards):
        self.all_cards = all_cards
        self.actions = dict()

    def add(self, card_name, action):
        card_id = self.all_cards.get_by_name(card_name).ID
        self.actions[card_id] = action

    def get(self, ID):
        return self.actions[ID]

from action_defs import *

def load_actions(all_cards):
    actions = Actions(all_cards)
    for name in actions_mappings:
        actions.add(name, actions_mappings[name])
    return actions

if __name__ == '__main__':
    import cards
    all_cards = cards.load_cards('cards.csv')
    actions = load_actions(all_cards)
