#Imports
import sqlite3
from flask import Flask, render_template, request, g

#Data-base assignment
DATABASE='./assignment3.db'

#The following 4 functions were attained from
#https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def get_db():
    db=getattr(g,'_database',None)
    if db is None:
        db=g._database=sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#Main
@app.route('/mark')
def get_marks():
    return 'E'
@app.route('/')
def root():
    db = get_db()
    db.row_factory = make_dicts

    marks = []
    for marks in query_db('select * from marks'):
        marks.append(mark)
    db.close()
    return render_template('index.html',mark=marks)