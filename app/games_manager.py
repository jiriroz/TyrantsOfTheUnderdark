from app import game

all_games = dict()
top_id = 0

def new_game():
    global top_id
    top_id += 1
    all_games[top_id] = game.new_game(top_id)
    return top_id