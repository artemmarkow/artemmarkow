import requests
from bs4 import BeautifulSoup
from time import sleep

list_hrefs = []

headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.837 YaBrowser/23.9.4.837 Yowser/2.5 Safari/537.36'}

for count in range(1, 2):

    sleep(1)
    url = f'https://quotes.toscrape.com/page/{count}'

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, 'lxml')

    data = soup.findAll('div', class_='quote')

    for item in data:

        # quote = item.find('span', class_='text').text
        # author = item.find('small', class_='author').text
        href = 'https://quotes.toscrape.com' + item.find('a').get('href')
        list_hrefs.append(href)
        # info = quote + '\n' + author + '\n' + href + '\n'

for hrefs in list_hrefs:

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, 'lxml')

    data = soup.find('div', class_='author-details')

    name = data.find('h3', class_='author-title').text
    born_date = data.find('span', class_='author-born-date').text
    born_location = data.find('span', class_='author-born-location').text
    print(f'{name} was born in {born_location} in {born_date}')
