from selenium import webdriver
from selenium.webdriver.common.by import By

with (webdriver.Chrome() as browser):
    browser.get('http://parsinger.ru/selenium/5/5.html')
    checkbox = browser.find_elements(By.CLASS_NAME, 'check')
    for item in checkbox:
        print(item.get_attribute('value'))

# Навигация по истории браузера
webdriver.back() # С помощью этого метода вы можете вернуться на предыдущую страницу, как
# если бы нажали стрелочку "назад" в браузере.
webdriver.forward() # Аналогично предыдущему, но перемещает вперёд по истории браузера.
webdriver.refresh() # Этот метод обновляет текущую страницу, как если бы вы нажали кнопку обновления в браузере.
# Работа со скриншотами
webdriver.get_screenshot_as_file("../file_name.jpg") # Сохраняет скриншот страницы в файл по указанному пути.
# Возвращает True если всё прошло успешно, и False при ошибках ввода-вывода.
webdriver.save_screenshot("file_name.jpg") # Сохраняет скриншот в папке с проектом.
webdriver.get_screenshot_as_png() # Возвращает скриншот в виде двоичных данных (binary data),
# которые можно передать или сохранить в файл в конструкторе with/as;
webdriver.get_screenshot_as_base64() # Возвращает скриншот в виде строки в кодировке Base64.
# Удобно для встроенных изображений в HTML.

# Откытие и закрытие страниц и браузера
webdriver.get("http://example_url.ru") # Открывает указанный URL в браузере.
webdriver.quit() # Закрывает все вкладки и окна, завершает процесс драйвера, освобождает ресурсы.
webdriver.close() # Закрывает только текущую вкладку.

# Исполнение JavaScript
webdriver.execute_script("script_code") # Выполняет JavaScript код на текущей странице.
webdriver.execute_async_script("script_code" , *args ) # Асинхронно выполняет JavaScript код.
# Удобно для работы с AJAX и промисами.
browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");') # открыть новую вкладку
browser.execute_script("return document.title;") # получить имя вкладки, т.е. её title

# Время ожидания
webdriver.set_page_load_timeout() # Устанавливает таймаут на загрузку страницы.
# Выбрасывает исключение, если время вышло.

# Поиск элементов
webdriver.find_element(By.ID, 'example_id') # Возвращает первый найденный элемент по заданному локатору.
webdriver.find_elements(By.ID, 'example_id') # Возвращает список всех элементов, соответствующих локатору.

# Работа с окном браузера
webdriver.get_window_position() # Возвращает словарь с текущей позицией окна браузера ({'x': 10, 'y': 50}).
webdriver.maximize_window() # Разворачивает окно на весь экран.
webdriver.minimize_window() # Сворачивает окно.
webdriver.fullscreen_window() # Переводит окно в полноэкранный режим, как при нажатии F11.
webdriver.get_window_size() # Возвращает размер окна в виде словаря ({'width': 945, 'height': 1020}).
webdriver.set_window_size(800,600) # Устанавливает новый размер окна.

# Работа с cookies
webdriver.get_cookies() # Возвращает список всех cookies.
webdriver.get_cookie(name_cookie) # Возвращает конкретную cookie по имени.
webdriver.add_cookie(cookie_dict) # Добавляет новую cookie к вашему текущему сеансу;
webdriver.delete_cookie(name_cookie) # Удаляет cookie по имени.
webdriver.delete_all_cookies() # удаляет все файлы cookie в рамках текущего сеанса;
# Состав куки
# "name" — устанавливает имя cookie-файла;
# "value" — устанавливает значение cookie; это значение может либо идентифицировать пользователя, либо содержать любую другую служебную информацию;
# "expires" и "max-age" — определяют срок жизни cookie; после истечения этого срока, cookie будет удалён из памяти браузера. Если не указывать эти значения, содержимое cookie будет удалено после закрытия браузера;
# "path" — указывает путь к директории на сервере, для которой будут доступны cookie. Чтобы cookie были доступны по всему домену, необходимо указать "/";
# "domain" — хранит в себе информацию о домене или поддомене, которые имеют доступ к этой cookie. Если необходимо, чтобы cookie были доступны по всему домену и всем поддоменам, указывается базовый домен, например, www.example.ru;
# "secure" — указывает серверу, что cookie должны передаваться только по защищённому HTTPS-соединению;
# "httponly"— этот параметр запрещает доступ к cookie посредством API браузера document.cookie. Предотвращает кражу cookie посредством XSS-атак. Если флаг установлен в True, вы сможете получить доступ к этой cookie только через браузер, в том числе и через Selenium;
# "samesite"— ограничивает передачу cookie между сайтами и предотвращает кражу cookie посредством XSS-атак. Имеет три состояния:
#         SameSite=None — на передачу cookie нет никаких ограничений;
#         SameSite=Lax — разрешает передачу только безопасным HTTP-методам;
#         SameSite=Strict или SameSite — самое строгое состояние, которое запрещает отправку cookie на другие сайты.

# Ожидание элементов
webdriver.implicitly_wait(10) # Устанавливает неявное ожидание на поиск элементов или выполнение команд.
webdriver.WebDriverWait(driver, timeout).until(condition)

# Работа с элементами
element.click() # Симулирует клик по элементу.
element.send_keys("text") # Вводит текст в текстовое поле. Очень полезно для автоматизации ввода данных.
element.clear() # Очищает текстовое поле.
element.is_displayed() # Проверяет, отображается ли элемент на странице.
element.is_enabled() # Проверяет, доступен ли элемент для взаимодействия (например, не заблокирован).
element.is_selected() # Проверяет, выбран ли элемент (актуально для радиокнопок и чекбоксов).
element.get_attribute("attribute") # Возвращает значение указанного атрибута элемента.
element.text # Возвращает текст элемента.
element.submit() # Отправляет форму, в которой находится элемент.

# Фреймы
webdriver.switch_to.frame("frame_name") # Переключает фокус на указанный фрейм.
webdriver.switch_to.default_content() # Возвращает фокус на основное содержимое страницы, выходя из фрейма.

# JavaScript Alerts
webdriver.switch_to.alert # Переключает фокус на всплывающее окно JavaScript.
webdriver.switch_to.frame(iframe) # Переключает фокус на iframe
webdriver.page_source # Мы переключились на iframe и теперь iframe - это driver.
# Возвращает исходный HTML код текущей страницы, который в этом контексте является содержимым iframe

webdriver.current_window_handle # возвращает дескриптор текущей вкладки;
webdriver.window_handles # возвращает список всех дескрипторов открытых вкладок;
webdriver.switch_to.window(window_handles[0]) # переключает фокус между вкладками.
browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");') # Открыть вкладку в одном браузере