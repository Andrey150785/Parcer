import sqlite3

with sqlite3.connect("log_and_pass.db") as database:
    cursor = database.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users
    (login TEXT,
    password TEXT)
    """)
    database.commit()
    change = input("Вход или регистрация? 1 | 2: ")
    while change not in ('1', '2'):
        # некорректный ввод на старте
        print("Выберите один из двух вариантов:\n1: вход\n2: регистрация\nВаш выбор")
        change = input("Вход или регистрация? 1 | 2: ")
    if  change == "1":
        # выбрал вход (авторизацию в системе)
        login = input("Login: ")
        cursor.execute(f"SELECT login FROM users WHERE login = '{login}'")
        if not cursor.fetchone() is None: # Логин в системе зарегистрирован, далее проверяется пароль
            password = input("Password: ")
            cursor.execute(f"SELECT login, password FROM users WHERE login = '{login}'")
            if cursor.fetchone()[1] == password: # Проверяется верность пароля для существующего логина
                print("Вы вошли в систему!") # Пароль верный - вошли в систему
            else:
                print('Неверный пароль!') # Пароль неверный
        else: # Пользователь с введенным логином не найден в системе
            print("Пользователь не найден!")
    elif change == '2':
        # Регистрация нового пользователя в системе
        inp_login = input("Login: ")
        # Проверка наличия введенного логина в базе данных пользователей
        cursor.execute(f"SELECT login FROM users WHERE login = '{inp_login}'")
        if cursor.fetchone() is None: # Если пользователь с введенным логином не найден в системе
            inp_password = input("Password: ")
            # Создается новый пользователь с введенной парой логин-пароль
            cursor.execute(f"INSERT INTO users VALUES(?,?)", (inp_login, inp_password))
            # Обновляем базу
            database.commit()
        else: # Проверка при регистрации на уникальность введенного логина
            print("Такой пользователь уже зарегистрирован в системе!")