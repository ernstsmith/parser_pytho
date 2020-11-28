from bs4 import BeautifulSoup
import requests
import csv

FILENAME = 'parse_01.csv'


def save():
    with open(FILENAME, 'a', newline="") as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(
            f"{comp['image'],comp['name'],comp['description']}")


def parse():
    HOST = 'https://www.shimadzu.eu'
    URL = 'https://www.shimadzu.eu/liquid-chromatograph-mass-spectrometry'
    HEADERS = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
               }
    response = requests.get(URL, HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='unit image-col-set')
    comps = []

    for item in items:
        comps.append(
            {
                'image': HOST + item.find('img').get('src'),
                'name': item.find('figcaption', class_='image-col-set-description').find('h3').find('a').get_text(),
                'description': item.find('div', class_='image-col-set-description-text').find('div').get_text(),
            })
        global comp
        for comp in comps:
            print(f"{comp['image'],comp['name'],comp['description']}")
            save()


parse()
