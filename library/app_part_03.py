import sqlite3
from flask import Flask, g, render_template, request
from . import config

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

@app.before_request
def before_request():
    print("Connecting to DB")
    g.db = connect_db()

@app.route('/')
def hello_world():
    cursor = g.db.execute("""
    SELECT p.id, p.name, c.name 
    FROM person p INNER JOIN country c on p.country_id = c.id;
    """)
    mathematicians_dict = [dict(id = row[0], name = row[1], country=row[2]) for row in cursor.fetchall()]
    return render_template('database/mathematician.html', persons = mathematicians_dict)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        # show the use of inheritance
        return render_template('inheritance/form.html')
    elif request.method == 'POST':
        kwargs = {
            'achievement': request.form['achievement'],
            'year': request.form['year'],
            'person': request.form['person'],
            'secret_key': request.form['SECRET_KEY'],
            'submit_value': request.form['submit']
        }
        return render_template('forms/form_result.html', **kwargs)