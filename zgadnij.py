# -*- coding: utf-8 -*-
# ZgadnijKtoTO/zgadnij.py

from flask import Flask, request
from flask import render_template
import characters
import attributes

app = Flask(__name__)

player1_chars = list(characters.characters)
player2_chars = list(characters.characters)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/player1', methods = ['POST', 'GET'])
def player1():
    if request.method == 'POST':
        clicked_chars = request.form.getlist('mycheckbox')
        for ch in clicked_chars:
            for chars in player1_chars:
                if ch == chars.name:
                    chars.visibility = not chars.visibility
                    print (chars.name, chars.visibility)
    return render_template('player1.html', chars = player1_chars, attributes=attributes.Attributes)

@app.route('/player2', methods = ['POST', 'GET'])
def player2():
    if request.method == 'POST':
        clicked_chars = request.form.getlist('mycheckbox')
        for ch in clicked_chars:
            for chars in player2_chars:
                if ch == chars.name:
                    chars.visibility = not chars.visibility
                    print (chars.name, chars.visibility)
    return render_template('game.html', chars = player2_chars)




@app.route('/game', methods = ['POST', 'GET'])
def game():
    if request.method == 'POST':
        clicked_chars = request.form.getlist('mycheckbox')
        for ch in clicked_chars:
            for chars in player1_chars:
                if ch == chars.name:
                    chars.visibility = not chars.visibility
                    print (chars.name, chars.visibility)
    return render_template('game.html', chars = player1_chars)


if __name__ == '__main__':
    app.run(debug=True)
