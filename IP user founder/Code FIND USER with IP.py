import requests
from pyfiglet import Figlet
import folium

def getinfo_byIP(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        data = {
            '[IP]': response.get('query'),
            '[Internet provider]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Zip]': response.get('zip'),
            '[Latitude]': response.get('lat'),
            '[Longitude]': response.get('lon'),
        }
        for key, values in data.items():
            print(f'{key}: {values}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('Connection failed - check connection or IP adress')

def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP info'))
    ip = input('Enter a target IP adress: ')

    getinfo_byIP(ip=ip)

if __name__ == '__main__':
    main()


