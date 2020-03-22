from app import game
import pickle
from pathlib import Path
import uuid

all_games = dict()
temp_hold_id = set()

def get_next_id():
    # I know, this doesn't really scale
    # Also this is NOT thread safe
    while True:
        id = str(uuid.uuid1())
        if id in all_games or id in temp_hold_id:
            continue
        temp_hold_id.add(id)
        return id

def load_games():
    games_path = Path(__file__).parent.absolute() / 'games'
    for g in games_path.rglob('*.pickle'):
        with open(g, 'rb') as f:
            game = pickle.load(f)
            all_games[game.ID] = game

def new_game(id, deck_choices):
    all_games[id] = game.new_game(id, deck_choices)
    temp_hold_id.discard(id)
    save_game(all_games[id])
    return all_games[id]

def get_game(id):
    if id not in all_games:
        return None
    return all_games[id]
    
def save_game(game):
    game_path = Path(__file__).parent.absolute() / 'games' / 'game{}.pickle'.format(game.ID)
    with open(game_path, "wb") as f:
        pickle.dump(game, f)

# This should really run in a proper startup sequence
load_games()