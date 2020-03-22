from app import board as board_module
from app import cards as cards_module
from app import market as market_module
from app import player as player_module
from app.cards import Deck
from app.board import Color
from app.player import Player

import random

base_deck = {
    "Soldier" : 3,
    "Noble" : 7
}

class Game:
    def __init__(self, ID, board, cards, market):
        self.ID = ID
        self.board = board
        self.cards = cards
        self.market = market
        self.players = dict()
        self.current_player = None

    def add_player(self, name, color):
        if not self.players:
            player_id = 1
        else:
            player_id = max([self.play.keys()]) + 1
        player = Player(player_id, name, color)
        self.players[player_id] = player
        for name in base_deck:
            card = self.cards.get_by_name(name)
            for x in range(base_deck[name]):
                player.add_card_to_deck(card)
        self.current_player = random.choice(list(self.players.keys()))
        return player_id

def new_game(id, deck_choices):
    board = board_module.load_board('app/board.csv')
    cards = cards_module.load_cards('app/cards.csv')

    market_cards = []
    for deck in deck_choices:
        market_cards += cards.get_by_deck(deck)
    random.shuffle(market_cards)
    num_priestesses = cards.get_by_name("Priestess of Lolth").count
    num_houseguards = cards.get_by_name("House Guard").count
    num_outcasts = cards.get_by_name("Insane Outcast").count if Deck.DEMON in deck_choices else 0

    market = market_module.Market(cards, market_cards, num_priestesses, num_houseguards, num_outcasts)
    game = Game(id, board, cards, market)
    return game