"""
Utils
-----
Something about utils.py
"""
import sqlite3
from flask import Flask

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'this should be a secret random string'

connection = sqlite3.connect('../database.db')

c = connection.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS urls(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            original_url TEXT NOT NULL,
            clicks INTEGER NOT NULL DEFAULT 0
        )''')


def get_db_connection():
    conn = sqlite3.connect('../database.db')
    conn.row_factory = sqlite3.Row
    return conn
