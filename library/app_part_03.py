import sqlite3
from flask import Flask, g, render_template
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