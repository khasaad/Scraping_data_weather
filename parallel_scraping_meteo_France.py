import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import threading
import math
import time


start_time = time.time()

dates = []
temperature = []
list_code = []
list_all_src = []


year = input('add the year: ')


def parallel_scraping(start, end):
    for w in np.arange(start, end):
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


thread_count = 16   # Put your thread count here (usually 2*cores)
link_count = 12
thread_list = []

for t in range(thread_count):
    start = math.floor(t * link_count/thread_count) + 1
    print(t, start)
    end = math.floor((t+1) * link_count/thread_count) + 1
    print(t, end)
    thread_list.append(threading.Thread(target=parallel_scraping, args=(start, end)))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()


composite_list = [temperature[x:x + 5] for x in range(0, len(temperature), 5)]

paris = []
for par in composite_list:
    paris.append(par[0])

versailles = []
for ver in composite_list:
    versailles.append(ver[1])

melun = []
for mel in composite_list:
    melun.append(mel[2])

fontainebleau = []
for fon in composite_list:
    fontainebleau.append(fon[3])

cergy = []
for cer in composite_list:
    cergy.append(cer[4])

meteo = dict()

meteo['Date'] = dates
meteo['Paris'] = paris
meteo['Versailles'] = versailles
meteo['Melun'] = melun
meteo['Fontainebleau'] = fontainebleau
meteo['Cergy'] = cergy

df = pd.DataFrame(meteo)

# saving the dataframe
df.to_csv('meteo_France_with_parallel_method-' + str(year) + '.csv')

end_time = time.time()
print('Time taken : ' + str(end_time - start_time) + "sec")
