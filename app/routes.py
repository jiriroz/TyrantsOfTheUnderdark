from flask import render_template, redirect, url_for, request
from app import app
from app import games_manager
from app.game import PlayerChoice
from app.board import Color

@app.route('/newgame')
def newgame():
    player_choices = [PlayerChoice("Jiri", Color.ORANGE), PlayerChoice("Bareesh", Color.BLUE), PlayerChoice("Reuben", Color.RED)]
    game_id = games_manager.new_game(player_choices)
    return redirect(url_for('game', id=game_id))

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jiri'}
    return render_template('index.html', user=user)


@app.route('/gamedebug/<int:id>')
def gamedebug(id):
    game = games_manager.get_game(id)
    if game == None:
        return "Game ID {} doesn't exist".format(id)
    return render_template('gamedebug.html', game=game)
    
@app.route('/game/<int:id>')
def game(id):
    game = games_manager.get_game(id)
    if game == None:
        return "Game ID {} doesn't exist".format(id)
    return render_template('game.html', game=game)