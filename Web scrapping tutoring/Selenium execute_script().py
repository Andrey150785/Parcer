window.scrollBy(X, Y) # прокрутит страницу вниз на заданное число пикселей по x и y.
# X - смещение в пикселях по горизонтали;
# Y - смещение в пикселях по вертикали.
browser.execute_script("window.scrollBy(0,5000)")

return document.body.scrollHeight # вернёт значение высоты основного элемента на странице — body.
height = browser.execute_script("return document.body.scrollHeight")

window.innerHeight # используется для получения высоты видимой области.
window.innerWidth # для получения ширины видимой области.
height = browser.execute_script("return window.innerHeight")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") # прокрутить страницу до самого низа, до последнего пикселя

.execute_script("return arguments[0].scrollIntoView(true);", element) # прокручивает родительский контейнер элемента таким образом, чтобы element, для которого вызывается scrollIntoView, был виден пользователю.
.execute_script("window.open('http://parsinger.ru', 'tab2');") # создаст новую вкладку в браузере с именем "tab2".
.execute_script("return document.body.scrollHeight") # вернёт значение высоты элемента <body>.
.execute_script("return window.innerHeight") # вернёт значение высоты окна браузера.
.execute_script("return window.innerWidth") # вернёт значение ширины окна браузера.
.execute_script("window.scrollBy(X, Y)") # прокрутит документ на заданное число пикселей по осям X и Y.
# X — смещение в пикселях по горизонтали.
# Y — смещение в пикселях по вертикали.

.execute_script("alert('Ура Selenium')") # вызывает модальное окно Alert.
.execute_script("return document.title;") # возвращает title открытого документа.
.execute_script("return document.documentURI;") # возвращает URL документа.
.execute_script("return document.readyState;") # возвращает состояние загрузки страницы; вернёт "complete", если страница загрузилась.
.execute_script("return document.anchors;") # возвращает список всех якорей на странице.
[x.tag_name for x in browser.execute_script("return document.anchors;")] # этот код позволяет получить список всех тегов с якорями. Очень полезная инструкция, особенно если при скроллинге элемент для "зацепления" не найден.
.execute_script("return document.cookie;") # возвращает строку, содержащую все cookies документа, разделённые точкой с запятой.
.execute_script("return document.domain;") # возвращает домен текущего документа.
.execute_script("return document.forms;") # возвращает список всех форм на странице.
.execute_script("window.scrollTo(x-coord, y-coord);") # прокручивает документ до указанных координат:
# x-coord — позиция по горизонтальной оси, которая будет отображена вверху
# y-coord — позиция по вертикальной оси, которая будет отображена вверху слева.
.execute_script("return document.getElementsByClassName('container');") # возвращает список всех элементов с классом 'container'.
.execute_script("return document.getElementsByTagName('container');") # возвращает список всех элементов с тегом 'container'.
.execute_script("return document.getElementById('some-id');") #  возвращает элемент с указанным ID 'some-id'.