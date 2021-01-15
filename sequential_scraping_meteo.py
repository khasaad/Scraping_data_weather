import requests
from bs4 import BeautifulSoup
import numpy as np


dates = []
temperature = []
list_code = []
list_all_src = []


year = input('add the year: ')


def sequential_scraping():
    for w in np.arange(1, 13):
        if w == 10 or w == 11 or w == 12:
            url = 'https://www.historique-meteo.net/france/ile-de-france/' + str(year) + '/' + str(w) + '/'
        else:
            url = 'https://www.historique-meteo.net/france/ile-de-france/' + str(year) + '/0' + str(w) + '/'

        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')

            # findAll(name, attrs, recursive, text, limit, **kwargs)
            table = soup.find(name="table", attrs={"class": "table table-striped table-bordered"})
            tbody = table.find('tbody').find_all('tr')

            code = []
            for i in range(len(tbody)):
                for j in tbody[i]:
                    if str(j).startswith('<td><b>'):
                        dates.append(str(j)[7:17])
                    elif j.find('small'):
                        new_string = str(j.find('small')).replace('<br/>', ',')
                        comma = new_string.find(',')
                        temperature.append(new_string[7: comma])
                    if j.find_all('img'):
                        for img in j.find_all('img'):
                            src = img['src']
                            list_all_src.append(src)
                            val = src[61:64]
                            code.append(val)
            list_code.append(code)
