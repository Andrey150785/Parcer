import sqlite3

with sqlite3.connect("log_and_pass.db") as database:
    cursor = database.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users
    (login TEXT,
    password TEXT)
    """)
    if input("Вход или регистрация? 1 | 2: ") == 1:
        login = input("Login: ")
        cursor.execute(f""""SELECT login FROM users WHERE login = {login}""")
        if not cursor.fetchone() is None:
            password = input("Password: ")
            cursor.execute(f"""SELECT login, password FROM users WHERE login = {login}""")
            if cursor.fetchone()[1] == password:
                print("Вы вошли в систему!")
            else:
                print('Неверный пароль!')
        else:
            print("Пользователь не найден!")
    else:
        inp_login = input("Login: ")
        inp_password = input("Password: ")

        cursor.execute(f"SELECT login FROM users WHERE login = '{inp_login}'")
        if cursor.fetchone() is None:
            cursor.execute(f"""INSERT INTO users VALUES(?,?)""", (inp_login, inp_password))
        else:
            print("Такой пользователь уже зарегистрирован в системе!")