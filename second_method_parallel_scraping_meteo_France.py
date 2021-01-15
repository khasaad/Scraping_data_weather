import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool

start_time = time.time()

dates = []
temperature = []
list_code = []
list_all_src = []

if __name__ == '__main__':

    base_url = 'https://www.historique-meteo.net/france/ile-de-france/'

    all_urls = list()


    def generate_urls():
        for u in range(1, 13):
            if u == 10 or u == 11 or u == 12:
                all_urls.append(base_url + str(2019) + '/' + str(u) + '/')
            else:
                all_urls.append(base_url + str(2019) + '/0' + str(u) + '/')


    def second_method_parallel_scraping(url):
        res = requests.get(url)
        if res.ok:
            soup = BeautifulSoup(res.text, 'html.parser')

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


    generate_urls()

    #  Sequential method
    # for url in all_urls:
    #     second_method_parallel_scraping(url)

    # *************************  Parallel method  *****************************************

    p = Pool(6)  # This “6” means that 6 URLs will be processed at the same time
    with p:
        p.map(second_method_parallel_scraping, all_urls)
        #  map function scrape with all_urls and Pool p will take care of executing each of them concurrently.

        #  terminate() is typically called when the parallelizable part of your main program is finished.
        p.terminate()

        #  join() is called to wait for the worker processes to terminate.
        p.join()
    #  ***********************************************************************************

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
df.to_csv('meteo_France_with_second_method_parallel_' + str(2019) + '.csv')

end_time = time.time()
print('Time taken : ' + str(end_time - start_time) + "sec")
