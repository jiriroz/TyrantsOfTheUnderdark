import board as board_module
import cards as cards_module


class Game:
    def __init__(self, ID, board, cards):
        self.ID = ID
        self.board = board
        self.cards = cards
        self.players = dict()

    def add_player(self, player):
        self.players[player.ID] = player

def new_game():
    board = board_module.load_board('board.csv')
    cards = cards_module.load_cards('cards.csv')
    game = Game(board, cards)