import requests
from random import choice
from requests.exceptions import Timeout


url = 'http://httpbin.org/user-agent'

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)

# time.sleep(randint(1,5))
# try:
#     response = requests.get("http://example.com", timeout=1)
# except Timeout:
#     print("The request timed out")