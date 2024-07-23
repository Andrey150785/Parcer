from selenium import webdriver as driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Использование ActionChains для выполнения последовательности действий

actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
actions.move_to_element(menu)  # Переместить курсор на элемент меню
actions.click(submenu)         # Кликнуть по подменю
actions.perform()              # Выполнить накопленные действия

# Методы ActionChains(driver)

actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
element = driver.find_element(By.ID, "draggable") # Находим необходимый элемент/тег

# Методы ActionChains(driver)
action = ActionChains(driver) # Создаём экземпляр класса ActionChains
element = driver.find_element(By.ID, "draggable") # Находим необходимый элемент/тег

action.perform(self) # Метод используется для выполнения всех сохраненных операций в экземпляре действия
# класса ActionChains. Запускает всю цепочку действий.
action.click(element) # Кликает по элементу.
action.click_and_hold(element) # Удерживает левую кнопку мыши на элементе.
action.context_click(element) # Используется для выполнения контекстного щелчка (щелчка правой кнопкой мыши) по элементу.
action.drag_and_drop(source, target) # Удерживает левую кнопку мыши на исходном элементе, затем перемещается
# к целевому элементу и отпускает кнопку мыши.
action.release(self, on_element=None)  # Метод release используется для отпускания удерживаемой кнопки мыши на элементе.
action.drag_and_drop_by_offset(source, xoffset, yoffset) # Удерживает левую кнопку мыши на исходном элементе,
# затем перемещается к заданному смещению и отпускает кнопку мыши.
action.key_down(value, element) # Отправляет только нажатие клавиши, не отпуская ее. Следует использовать
# только с клавишами-модификаторами (Control, Alt и Shift).
action.key_up(value, element) # Метод используется для отпускания нажатой клавиши с помощью метода key_down.
action.move_by_offset(xoffset, yoffset) # Позволяет перемещать курсор мыши на определенное расстояние
# от его текущего положения на экране.
# Это особенно полезно, когда вы хотите выполнить точное перемещение курсора без необходимости ссылаться
# на конкретный элемент на веб-странице.
action.move_to_element(to_element) # Метод используется для перемещения мыши в середину элемента.
action.move_to_element_with_offset(to_element, xoffset, yoffset) # Метод используется для перемещения мыши
# на смещение указанного элемента. Смещения относятся к верхнему левому углу элемента.
action.pause(seconds) # Метод паузы используется для приостановки всех входящих данных на указанное время в секундах.
# Метод паузы очень важен и полезен в случае выполнения какой-либо команды, для загрузки которой требуется какой-либо
# JavaScript, или в подобной ситуации, когда между двумя операциями есть временной промежуток.
action.send_keys(Keys.DOWN) # метод используется для отправки ключей текущему элементу в фокусе;
action.send_keys_to_element(element, *keys_to_send) # Метод используется для отправки
# нажатия клавиша текущему элементу в фокусе.
action.scroll(x, y, delta_x, delta_y, duration, origin=element) #  Выполняет скроллинг на элементе,
# где установлен курсор. Очень полезный скроллинг, позволяет прицельно скролить окна маленьких размеров;
action.reset_actions(self) # Метод очищает действия, которые уже сохранены локально и в ActionChains.
# Это один из наиболее часто используемых методов, так как после какой-либо операции
# необходимо сбросить экземпляр ActionChains для выполнения следующей операции.
action.scroll_by_amount(delta_x, delta_y) # Метод прокручивает на заданное количество,
# начало координат находится в верхнем левом углу области просмотра.
action.scroll_from_origin(scroll_origin, delta_x, delta_y) # Выполняет прокрутку на указанное
# расстояние на основе исходного положения.
action.scroll_to_element(element) # Метод предназначен для автоматического прокручивания страницы к указанному элементу.

# KEYES
from selenium.webdriver.common.keys import Keys # или from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Нажатие клавиши (Key down)
ActionChains(driver).key_down(Keys.SHIFT).send_keys("abc").perform()
# Отпускание клавиши (Key up)
ActionChains(driver).key_down(Keys.SHIFT).send_keys("a").key_up(Keys.SHIFT).send_keys("b").perform()



