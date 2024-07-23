# импортируйте необходимое
import threading

# импортируйте необходимое
import threading

# создайте функцию перехватчика исключений
def custom_hook(args):
    exc_type, exc_value, exc_traceback, exc_thread = args
    if exc_type.__name__ == "TypeError":
        print(f"{exc_thread.name}, {exc_type.__name__}, {exc_value}")
    if exc_type.__name__ == "ValueError":
        print(f"{exc_thread.name}, {exc_type.__name__}, {exc_value}")
    else:
        with open('custom_errors.txt', 'w', encoding='utf-8') as file:
            file.write(f"{exc_thread.name}, {exc_type.__name__}, {exc_value}\n")

# переопределите функцию threading.excepthook
threading.excepthook = custom_hook

def test_1():
    raise TypeError("Type")

def test_2():
    raise ValueError("Value")

def test_3():
    raise ZeroDivisionError("some error")

def test_4():
    raise SyntaxError("some error")

for function in (test_1, test_2, test_3, test_4):
    threading.Thread(target=function).start()

