from app import game
import pickle
from pathlib import Path

all_games = dict()
top_id = 0

def load_games():
    games_path = Path(__file__).parent.absolute() / 'games'
    for g in games_path.rglob('*.pickle'):
        with open(g, 'rb') as f:
            game = pickle.load(f)
            all_games[game.ID] = game
            top_id = game.ID


# This function is NOT thread safe
def new_game(player_choices):
    global top_id
    top_id += 1
    all_games[top_id] = game.new_game(top_id, player_choices)
    game_path = Path(__file__).parent.absolute() / 'games' / 'game{}.pickle'.format(top_id)
    with open(game_path, "wb") as f:
        pickle.dump(all_games[top_id], f) 
    return top_id

def get_game(id):
    if id not in all_games:
        return None
    return all_games[id]


# This should really run in a proper startup sequence
load_games()