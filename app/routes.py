from flask import render_template, redirect, url_for, request
from app import app
from app import games_manager

@app.route('/newgame')
def newgame():
    game_id = games_manager.new_game()
    return redirect(url_for('game', id=game_id))

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jiri'}
    return render_template('index.html', user=user)


@app.route('/game/<int:id>')
def game(id):
    game = games_manager.get_game(id)
    if game == None:
        return "Game ID {} doesn't exist"
    
