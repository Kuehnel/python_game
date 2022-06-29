import sqlite3
from datetime import date


def create_db():
    db_conn = sqlite3.connect('highscore.db')
    c = db_conn.cursor()

    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='highscore' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] != 1:
        c.execute('''CREATE TABLE highscore
                      (date text, score integer)''')

        db_conn.commit()


def insert_highscore(score):
    db_conn = sqlite3.connect('highscore.db')
    c = db_conn.cursor()

    c.execute("INSERT INTO highscore VALUES (?,?)", (date.today(), score))

    db_conn.commit()


def get_highscore_list():
    db_conn = sqlite3.connect('highscore.db')

    result = []

    data = db_conn.execute("SELECT * FROM highscore ORDER BY score DESC LIMIT 10")

    for row in data:
        result.append([row[0], str(row[1])])

    return result
