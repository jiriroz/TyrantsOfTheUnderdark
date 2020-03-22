from flask import render_template, redirect, url_for, request, session
from app import app
from app import games_manager
from app.board import Color
from app.cards import Deck
from app.forms import PlayerSetupForm
import random

@app.route('/newgame')
def newgame():
    gameid = games_manager.get_next_id()
    return redirect(url_for('gamesetup', gameid=gameid))

@app.route('/gamesetup/<int:gameid>',  methods=['GET', 'POST'])
def gamesetup(gameid):
    player_form = PlayerSetupForm()
    if player_form.validate_on_submit():

        game = games_manager.get_game(gameid)
        if game is None:
            decks = random.sample([Deck.DROW, Deck.DEMON, Deck.DRAGON, Deck.ELEMENTAL], 2)
            game = games_manager.new_game(gameid, decks)

        name = player_form.name.data
        col = Color(player_form.color.data)
        player_id = game.add_player(name, col)

        if 'active_games' not in session:
            session['active_games'] = dict()
    
        session['active_games'][str(gameid)] = {'player_id' : str(player_id)}
        session.modified = True
        return redirect(url_for('gamedebug', id=gameid))
    
    return render_template('game_setup.html', player_form=player_form)


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
    return render_template('game_debug.html', game=game)
    
@app.route('/game/<int:id>')
def game(id):
    game = games_manager.get_game(id)
    if game == None:
        return "Game ID {} doesn't exist".format(id)
    return render_template('game.html', game=game)