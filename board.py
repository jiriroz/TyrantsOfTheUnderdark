


class Board:
    sites = dict()


class Site:
    adj = []
    capacity = -1
    troops = dict()
    spies = dict()
    isBlack = False
    vpPerTurn = 0
    influencePerTurn = 0
    vpEndGame = 0
    isRoute = False
    name = ''
    ID = 0
    graphicalMetadata = dict()