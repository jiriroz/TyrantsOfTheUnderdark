import board as board_module
import cards as cards_module


class Game:
    def __init__(self, board, cards):
        self.board = board
        self.cards = cards


def new_game():
    board = board_module.load_board('board.csv')
    cards = cards_module.load_cards('cards.csv')
    game = Game(board, cards)