import os
# вывести переменные окружения
print(*os.environ, sep="\n")
# получить значение переменной
print(os.getenv("PWD"))
# получить рабочую директорию
print(os.getcwd())
# создать директрию
os.mkdir("files")
# вывести список файлов в текущей директории
print(os.listdir("."))

