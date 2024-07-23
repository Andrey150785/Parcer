# Если необходимо получить значение value="" мы напишем следующий код.

from selenium import webdriver
from selenium.webdriver.common.by import By

with (webdriver.Chrome() as browser):
    browser.get('http://parsinger.ru/selenium/5/5.html')
    checkbox = browser.find_elements(By.CLASS_NAME, 'check')
    for item in checkbox:
        print(item.get_attribute('value'))

# найти текст или его часть
browser.find_element(By.PARTIAL_LINK_TEXT, "Посетить мой")
browser.find_element(By.LINK_TEXT, "Посетить мой профиль")

# By.ID – Поиск элемента по уникальному идентификатору(id). Этот метод очень быстрый и надежный, но требует, чтобы у
# элемента был атрибут id.
element = browser.find_element(By.ID, "some_id")

# By.CSS_SELECTOR – Поиск элемента или элементов, используя селекторы CSS.
# Это гибкий и мощный метод, который может выразить сложные критерии поиска
elements = browser.find_elements(By.CSS_SELECTOR, ".some_class")
# 1. По тегу:
browser.find_element(By.CSS_SELECTOR, 'div')  # Найти первый div-элемент
# 2. По идентификатору:
browser.find_element(By.CSS_SELECTOR, '#element_id')  # Найти элемент с определенным идентификатором
# 3. По классу:
browser.find_element(By.CSS_SELECTOR, '.class_name')  # Найти элемент с определенным классом
# 4. По атрибуту:
browser.find_element(By.CSS_SELECTOR, 'div span')  # Найти span-элемент, вложенный в div
# 5. По вложенности:
browser.find_element(By.CSS_SELECTOR, 'div span')  # Найти span-элемент, вложенный в div
# 6. По псевдоклассам:
browser.find_element(By.CSS_SELECTOR, 'input:checked')  # Найти выбранный (checked) элемент input
# 7. По подстроке атрибута:
browser.find_element(By.CSS_SELECTOR, '[attribute_name*="partial_value"]')  # Найти элемент с атрибутом, содержащим указанную подстроку
# 8. По началу атрибута:
browser.find_element(By.CSS_SELECTOR, '[attribute_name^="prefix"]')  # Найти элемент с атрибутом, начинающимся с указанного префикса
# 9. По концу атрибута:
browser.find_element(By.CSS_SELECTOR, '[attribute_name$="suffix"]')  # Найти элемент с атрибутом, заканчивающимся указанным суффиксом
# 10. Комбинированный поиск:
browser.find_element(By.CSS_SELECTOR, 'div#element_id.class_name')  # Комбинированный поиск по тегу, идентификатору и классу


# By.XPATH – Поиск элемента с помощью языка XPath. Позволяет создать более сложные запросы, но он менее читаемый,
# возможно работать будет медленнее, чем прочие методы
element = browser.find_element(By.XPATH, "//div[@attribute='value']")
# 1. По абсолютному пути:
browser.find_element(By.XPATH, '/html/body/div[1]/span')  # Найти элемент по абсолютному пути
# 2. По относительному пути:
browser.find_element(By.XPATH, '//div/span')  # Найти элемент по относительному пути
# 3. По атрибуту:
browser.find_element(By.XPATH, '//*[@attribute_name="value"]')  # Найти элемент с определенным атрибутом и значением
# 4. По тексту элемента:
browser.find_element(By.XPATH, '//*[text()="Text Content"]')  # Найти элемент по тексту внутри него
# 5. По частичному тексту элемента:
browser.find_element(By.XPATH, '//*[contains(text(), "Partial Text")]')  # Найти элемент по частичному тексту внутри него
# 6. По индексу:
browser.find_element(By.XPATH, '(//div/span)[2]')  # Найти второй элемент, соответствующий заданному пути
# 7. По вложенности:
browser.find_element(By.XPATH, '//div/span')  # Найти span-элемент, вложенный в div
# 8. Используя логические операторы (AND, OR):
browser.find_element(By.XPATH, '//input[@type="text" and @name="username"]')  # Найти input-элемент с типом "text" и именем "username"
# 9. Используя псевдоклассы:
browser.find_element(By.XPATH, '//input[@checked]')  # Найти выбранный (checked) элемент input
# 10. Используя функции:
browser.find_element(By.XPATH, '//div[starts-with(@class, "prefix")]')  # Найти div-элемент, у которого класс начинается с указанного префикса

# Поиск по полному совпадению текста
# Этот XPath выберет кнопку с текстом "Купить".
//button[text() = "Купить"]

# Поиск по частичному совпадению текста
# Этот XPath выберет все элементы p, в которых содержится текст "Артикул".
//p[contains(text(), "Артикул")]

# Поиск по полному совпадению атрибута
# Этот XPath выберет все ссылки, у которых атрибут href равен "https://example.com".
//a[@href = "https://example.com"]

# Поиск по частичному совпадению атрибута
# Этот XPath выберет все элементы li с классом, который частично совпадает с "item".
//li[contains(@class , "item")]

# Переход к дочерним элементам
# Здесь мы находим все дочерние элементы div с id='parent'.
//div[@id='parent']/child::*

# Переход к родительскому элементу
# Этот запрос вернет родительский элемент div с id='child'.
//div[@id = 'child']/parent::*

# Переход к следующему соседнему элементу
# Этот запрос вернет все следующие соседние элементы после div с id='prev_sibling'.
//div[@id = 'prev_sibling']/following-sibling::*

# Переход к предыдущему соседнему элементу
# Этот запрос вернет все предыдущие соседние элементы перед div с id='next_sibling'.
//div[@id = 'next_sibling']/preceding-sibling::*

# Переход к конкретному дочернему элементу
# Этот запрос вернет первый дочерний элемент p у div с id='parent'.
//div[@id = 'parent']/child::p[1]

# Поиск по вложенным элементам
# Этот запрос вернет все элементы span, являющиеся потомками div с id='ancestor'.
//div[@id = 'ancestor']//child::span

# Поиск первого дочернего элемента
# Этот запрос вернет первые дочерние элементы для всех div.
//div/*[1]

# Поиск последнего дочернего элемента
# Здесь мы находим последние дочерние элементы для всех div.
//div/*[last()]

# Поиск по порядковому номеру
# Этот запрос вернет третий элемент li в каждом ul.
//ul/li[position() = 3]

# Поиск элементов, имеющих дочерние элементы
# Этот запрос вернет все div, которые имеют хотя бы одного потомка.
//div[count(*) > 0]

# Поиск элементов на определенной глубине
# Этот запрос вернет все элементы p, находящиеся на четвертом уровне вложенности.
//*/*/*/*[name() = 'p']

# By.NAME – Поиск элемента по атрибуту name. Метод подходит для форм
element = browser.find_element(By.NAME, "username")
# By.TAG_NAME – Поиск элемента по названию тега HTML. Полезен, если нужно выбрать на страницу все изображения, например
images = browser.find_elements(By.TAG_NAME, "img")
# By.CLASS_NAME – Поиск элемента или элементов по классу. Полезен, если у элементов есть общий класс.
buttons = browser.find_elements(By.CLASS_NAME, "btn")
# By.LINK_TEXT – Поиск элемента по точному тексту ссылки. Удобно, когда текст уникален
element = browser.find_element(By.LINK_TEXT, "Continue")
# By.PARTIAL_LINK_TEXT – Поиск элемента по частичному тексту ссылки.Удобно, когда точный текст
# ссылки неизвестен или динамичен.
element = browser.find_element(By.PARTIAL_LINK_TEXT, "Cont")
# ввести текст в поле (в поле формы)
input_form = browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
.get_attribute('some_attribute') # для получения атрибутов, например, href у ссылок.
browser.find_element(By.TAG_NAME, "a").get_attribute("href")

