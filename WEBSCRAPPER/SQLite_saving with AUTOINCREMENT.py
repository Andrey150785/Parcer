import sqlite3 as sq
from get_card_info import result

# SQL & csv saving attributes. Сохранить информацию в базу данных SQLite и файл CSV:

with sq.connect('database.db') as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS flats (
    flat_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Количество_комнат INTEGER, 
    Улица TEXT, 
    №_дома TEXT, 
    Площадь INTEGER, 
    Этаж INTEGER, 
    Этажей_в_доме INTEGER, 
    Цена INTEGER, 
    Дата_публикации TEXT,
    Количество_просмотров INTEGER, 
    Декларация TEXT, 
    Описание TEXT, 
    Собственность TEXT, 
    Год_постройки TEXT, 
    Материал_стен TEXT, 
    Агентство TEXT,
    Продавец TEXT, 
    Телефон TEXT, 
    Ссылка TEXT
    )""")
    cur.execute("""INSERT INTO flats (Количество_комнат, 
    Улица, 
    №_дома, 
    Площадь, 
    Этаж, 
    Этажей_в_доме, 
    Цена, 
    Дата_публикации,
    Количество_просмотров, 
    Декларация, 
    Описание, 
    Собственность, 
    Год_постройки, 
    Материал_стен, 
    Агентство,
    Продавец, 
    Телефон, 
    Ссылка) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", result)
    conn.commit()
    cur.execute("""SELECT * FROM flats""")
    print(cur.fetchall())