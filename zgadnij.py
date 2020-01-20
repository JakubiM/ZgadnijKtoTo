# -*- coding: utf-8 -*-
# ZgadnijKtoTO/zgadnij.py
from flask import Flask, request, jsonify, redirect, url_for
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import InputRequired
import sys
from random import randint
from copy import deepcopy
from player import Player

import characters
from attributes import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

Player1 = Player("Gracz1")
Player2 = Player("Gracz2")
Player1.chars = deepcopy(characters.characters)
Player2.chars = deepcopy(characters.characters)
Player1.char = characters.characters[randint(0, 23)]
Player2.char = characters.characters[randint(0, 23)]
print(getattr(Player1.char, 'Sex'))
turn = Player1


class Form(FlaskForm):
    att = SelectField('att', choices=Att)
    typ = SelectField('typ', choices=[], validators=[InputRequired()])
    yesno = SelectField('yesno', choices=[('yes', 'Tak'), ('no', 'Nie')])
    askchar = SelectField('askchar', choices=[
                          (x.name, x.name) for x in turn.chars])


@app.route('/')
def index():
    global Player1, Player2, turn
    Player1 = Player("Gracz1")
    Player2 = Player("Gracz2")
    Player1.chars = deepcopy(characters.characters)
    Player2.chars = deepcopy(characters.characters)
    Player1.char = characters.characters[randint(0, 23)]
    Player2.char = characters.characters[randint(0, 23)]
    turn = Player1
    return render_template('index.html')


@app.route('/player1', methods=['POST', 'GET'])
def player1():
    if request.method == 'POST':
        clicked_chars = request.form.getlist('mycheckbox')
        for ch in clicked_chars:
            for chars in turn.chars:
                if ch == chars.name:
                    chars.visibility = not chars.visibility
    return render_template('player1.html', chars=turn.chars, p_char=turn.char, turn=turn.name, quest=turn.getQuestion())


@app.route('/question', methods=['POST', 'GET'],)
def question():
    form = Form()
    if request.method == 'POST':
        turn.quest_att = form.att.data
        return redirect(url_for('question2'))
    return render_template('question.html', form=form)


@app.route('/question2', methods=['POST', 'GET'])
def question2():
    form = Form()
    form.typ.choices = [(x.name, x.value)
                        for x in getattr(sys.modules[__name__], turn.quest_att)]
    if request.method == 'POST':
        turn.quest_typ = form.typ.data
        return redirect(url_for('change'))
    return render_template('question2.html', form=form)


@app.route('/zgadnij', methods=['POST', 'GET'])
def zgadnij():
    global turn
    form = Form()
    form.askchar.choices = [
        (x.name, x.name) for x in turn.chars if x.visibility == True]
    if request.method == 'POST':
        if turn == Player1:
            turn = Player2
        else:
            turn = Player1
        if turn.char.name == form.askchar.data:
            return render_template('koniec.html', tekst='Wygrywasz')
        else:
            return render_template('koniec.html', tekst='Przegrywasz')
    return render_template('zgadnij.html', form=form)


@app.route('/change', methods=['POST', 'GET'])
def change():
    global turn
    form1 = Form()
    if request.method == 'POST':
        turn.request = form1.yesno.data
        if turn == Player1:
            turn = Player2
        else:
            turn = Player1
        return redirect(url_for('player1'))

    pytanie = turn.getQuestAtt() + ", " + turn.getQuestTyp()

    if turn == Player1:
        wyswietl = Player2
    else:
        wyswietl = Player1

    return render_template('change.html', form=form1, pytanie=pytanie, turn=wyswietl)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)
