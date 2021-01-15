from sequential_scraping_meteo import *
import pandas as pd
from datetime import datetime

start_time = datetime.now()

sequential_scraping()

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
df.to_csv('meteo_France-' + str(year) + '.csv')


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
