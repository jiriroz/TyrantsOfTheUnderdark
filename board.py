import csv
from enum import Enum

class Color(Enum):
    WHITE = 1
    RED = 2
    BLACK = 3
    ORANGE = 4
    BLUE = 5

class Board:
    sites = dict()

    def __str__(self):
        s = ''
        for id in self.sites:
            s += str(self.sites[id]) + '\n'
        return s

class Site:
    def __init__(self):
        self.ID = None
        self.name = ''
        self.adj = []
        self.capacity = -1
        self.troops = dict()
        self.spies = dict()
        self.isBlack = False
        self.vpPerTurn = 0
        self.vpEndGame = 0
        self.influencePerTurn = 0
        self.isRoute = False
        self.graphicalMetadata = dict()

    def __str__(self):
        return ("ID={} name={} adj={} capacity={} troops={} spies={} isBlack={} vpPerTurn={} vpEndGame={} influencePerTurn={} isRoute={}".format(
            self.ID, self.name, str(self.adj), self.capacity, str(self.troops), str(self.spies), self.isBlack, self.vpPerTurn,
            self.vpEndGame, self.influencePerTurn, self.isRoute
        ))

def load_board():
    rows = []
    with open('board.csv') as f:
        rows = [row for row in csv.DictReader(f, delimiter=',')]

    board = Board()
    for row in rows:
        site = Site()
        site.ID = int(row['ID'])
        site.name = row['Name']
        site.isRoute = bool(int(row['isRoute']))
        site.capacity = int(row['capacity'])
        site.isBlack = bool(int(row['isBlack']))
        site.vpPerTurn = int(row['vpPerTurn'])
        site.vpEndGame = int(row['vpEndGame'])
        site.influencePerTurn = int(row['influencePerTurn'])
        for color in Color:
            site.troops[color] = 0
        site.troops[Color.WHITE] = int(row['numWhiteTroops'])
        site.adj = [int(x) for x in row['neighborIDs'].split(',')]
        board.sites[site.ID] = site
    return board
        
board = load_board()
print (board)
