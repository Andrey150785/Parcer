import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE score > 500 ORDER BY score DESC LIMIT 5")
    print(cur.fetchmany(3))
