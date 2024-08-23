from get_card_info import get_info_N1
from get_card_links import get_content

table = []
URL = "https://novosibirsk.n1.ru/search/?rubric=flats&deal_type=sell&metro=2353440%2C2353441%2C2353442%2C2353443%2C2353444%2C2353445%2C2353446%2C2353447&metro_time=10&rooms=1&is_newbuilding=false&total_area_min=30&total_area_max=50&release_date_min=2000&floor_not_first=true&floors_count_min=10"

for card in get_content(URL):
    print(card)
    print(get_info_N1(card))