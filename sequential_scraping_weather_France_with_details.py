import requests
from bs4 import BeautifulSoup
import numpy as np


dates = []
temperature = []
temperature_min = []
temperature_max = []
temperature_average = []

list_code = []
new_list_code = []
list_all_src = []
list_weather_condition = []

year = input('add the year: ')


def scraping_detail():
    for w in np.arange(1, 13):
        try:
            if w == 10 or w == 11 or w == 12:
                url = 'https://www.historique-meteo.net/france/ile-de-france/' + str(year) + '/' + str(w) + '/'
            else:
                url = 'https://www.historique-meteo.net/france/ile-de-france/' + str(year) + '/0' + str(w) + '/'

            response = requests.get(url)

            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')

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
                            slash = new_string.find('°C/')
                            temperature_min.append(new_string[7:slash])
                            temperature_max.append(new_string[slash + 3:comma - 2])
                            average = (int(new_string[slash + 3:comma - 2]) + int(new_string[7:slash])) / 2
                            temperature_average.append(average)
                            temperature.append(new_string[7: comma])

                        if j.find_all('img'):
                            for img in j.find_all('img'):
                                src = img['src']
                                list_all_src.append(src)
                                val = src[61:64]
                                code.append(val)
                list_code.append(code)

        except Exception as e:
            print(str(e))
