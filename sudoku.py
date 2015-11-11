import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from board import Board
from solver import solve_board

app = Flask(__name__)

#configuation
DATABASE = os.path.join(app.root_path, 'flaskr.db')
DEBUG = True
SECRET_KEY = 'development key'

app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db(): 
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()
    
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
        
@app.route('/', methods=['GET', 'POST'])
def solve_puzzle():
    result = None
    board_list = [0]*81
    if request.method == 'POST':
        res_list = request.form.getlist('val1')
        
        for i in range(0, 81):
          v = res_list[i]
          if v:
            board_list[i] = int(v)
        result = board_list
        
        board_to_solve = Board(board_list)
        solved_board = solve_board(board_to_solve)
        
        result = solved_board
        return render_template('result.html', result=result)
        
    return render_template('solver.html', result=result)
        
if __name__ == '__main__':
    app.run()