import threading

import requests
from time import perf_counter


sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

headers_stor = {}  # Храним здесь заголовки
start = perf_counter()
sum_ex_time = 0

def task(site, ex_time):
    start_tmp = perf_counter()
    headers_stor[site] = requests.get(site).headers  # получаем заголовки и формируем словарь
    delta = perf_counter() - start_tmp
    print(site, delta)
    ex_time += delta

threads = [threading.Thread(target=task, args=(source, sum_ex_time)) for source in sources]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()


print(f"completed in {perf_counter()-start} seconds")  # Считаем общее время выполнения всех запросов
print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности
print(*headers_stor.items(), sep="\n")  # Выводим наши заголовки