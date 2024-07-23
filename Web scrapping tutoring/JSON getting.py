import requests

dictionary = {}

url = 'https://parsinger.ru/4.6/1/res.json'
response = requests.get(url=url).json()

for i in response:
    dictionary[i['categories']] = dictionary.get(i['categories'], 0) + int(i['article']) * int(i['description']['rating'])

print(dictionary)

