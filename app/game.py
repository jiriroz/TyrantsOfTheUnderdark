from app import board as board_module
from app import cards as cards_module
from app import market as market_module
from app import player as player_module
from app.cards import Deck
from app.board import Color

import random

base_deck = {
    "Soldier" : 3,
    "Noble" : 7
}

class PlayerChoice:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Game:
    def __init__(self, ID, board, cards, market):
        self.ID = ID
        self.board = board
        self.cards = cards
        self.market = market
        self.players = dict()
        self.current_player = None

    def add_player(self, player):
        self.players[player.ID] = player

def new_game(id, player_choices):
    board = board_module.load_board('app/board.csv')
    cards = cards_module.load_cards('app/cards.csv')

    decks = random.sample([Deck.DROW, Deck.DEMON, Deck.DRAGON, Deck.ELEMENTAL], 2)
    market_cards = cards.get_by_deck(decks[0]) + cards.get_by_deck(decks[1])
    random.shuffle(market_cards)
    num_priestesses = cards.get_by_name("Priestess of Lolth").count
    num_houseguards = cards.get_by_name("House Guard").count
    num_outcasts = cards.get_by_name("Insane Outcast").count if Deck.DEMON in decks else 0

    market = market_module.Market(cards, market_cards, num_priestesses, num_houseguards, num_outcasts)
    game = Game(id, board, cards, market)

    player_id = 0
    for c in player_choices:
        player = player_module.Player(player_id, c.name, c.color, 40, 5)        
        game.add_player(player)
        player_id += 1
        for name in base_deck:
            card = cards.get_by_name(name)
            for x in range(base_deck[name]):
                player.add_card_to_deck(card)

    game.current_player = random.choice(list(game.players.keys()))
    return game