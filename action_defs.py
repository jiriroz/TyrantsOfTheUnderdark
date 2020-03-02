import subactions as sa
from board import Color

# CORE

def soldier(game_state):
    return sa.Attack(1).play()

def noble(game_state):
    yield sa.Influence(1).play()

# DROW

def blackguard(game_state):
    return sa.Choice(sa.Attack(2), sa.Assasinate())

def bounty_hunter(game_state):
    return sa.Attack(3)

def master_of_melee(game_state):
    return sa.Choice(sa.Deploy(4), sa.SupplantAnywhere(Color.WHITE))

def spellspinner(game_state):
    return sa.Choice(sa.PlaceSpy(), sa.ReturnSpy().then(sa.SupplantAtPreviousSite()))

# DRAGON

def red_dragon(game_state):
    return sa.Supplant().then(sa.ReturnSpy().then(GainVPForEachSiteUnderTotalControl(1)))
    

actions_mappings = {
    'Soldier' : soldier,
    'Noble' : noble,
    'Blackguard' : blackguard,
    'Bounty Hunter' : bounty_hunter,
    'Master of Melee-Magthere' : master_of_melee,
    'Spellspinner', spellspinner
}