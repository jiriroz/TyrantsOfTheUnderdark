from app import game

all_games = dict()
top_id = 0

def new_game(player_choices):
    global top_id
    top_id += 1
    all_games[top_id] = game.new_game(top_id, player_choices)
    return top_id

def get_game(id):
    if id not in all_games:
        return None
    return all_games[id]