import pandas as pd
from sequential_scraping_weather_France_with_details import *
import time

start_time = time.time()
scraping_detail()

pire = ['thunderstorms', 'snow and thunderstorms', 'partly cloudy and thunderstorms', 'fog and snow']
mauvaise = ['totally fog', 'continuous moderate rain', 'snow', 'rain and snow', 'sun and thunderstorms']
moyenne = ['totally cloudy', 'partly fog', 'light drizzle', 'light rain and sun',
           'rain_snow light and sun', 'light snow and sun', 'lightly snow']
bonne = ['partly cloudy', 'sunny']

#  This dictionary contains the keys of weather condition and the values which
weather_condition = {'partly cloudy': '116', 'totally cloudy': {'119', '122'}, 'partly fog': '143',
                     'totally fog': '248',
                     'light drizzle': {'266', '263', '314'}, 'continuous moderate rain': {'284', '296', '302', '308'},
                     'snow': '338',
                     'partly cloudy and thunderstorms': '386',
                     'light rain and sun': {'305', '176', '353', '299', '293'},
                     'sunny': '113', 'rain_snow light and sun': {'356', '362'}, 'snow and thunderstorms': '395',
                     'fog and snow': '230', 'light snow and sun': '371', 'rain and snow': '320', 'thunderstorms': '389',
                     'lightly snow': '332', 'sun and thunderstorms': '200'}

for element in list_all_src:
    code_element = element[61:64]
    for cw in weather_condition:
        if code_element in weather_condition[cw]:
            list_weather_condition.append(cw)
        else:
            continue

composite_list_weather_numeric = []
for e, wea in enumerate(list_weather_condition):
    if wea in pire:
        wea = 0
        composite_list_weather_numeric.append(wea)
    elif wea in mauvaise:
        wea = 1
        composite_list_weather_numeric.append(wea)
    elif wea in moyenne:
        wea = 2
        composite_list_weather_numeric.append(wea)
    elif wea in bonne:
        wea = 3
        composite_list_weather_numeric.append(wea)
    else:
        print('Not exist')

composite_list_weather = [list_weather_condition[x:x + 5] for x in range(0, len(list_weather_condition), 5)]

composite_list_weather_num = [composite_list_weather_numeric[x:x + 5] for x in
                              range(0, len(composite_list_weather_numeric), 5)]

composite_list = [temperature[x:x + 5] for x in range(0, len(temperature), 5)]
composite_list_temperature_min = [temperature_min[y:y + 5] for y in range(0, len(temperature_min), 5)]
composite_list_temperature_max = [temperature_max[z:z + 5] for z in range(0, len(temperature_max), 5)]
composite_list_temperature_avg = [temperature_average[v:v + 5] for v in range(0, len(temperature_average), 5)]

paris_weather = []
for par in composite_list_weather_num:
    paris_weather.append(par[0])

paris = []
for par in composite_list:
    paris.append(par[0])

paris_min = []
for par_min in composite_list_temperature_min:
    paris_min.append(par_min[0])

paris_max = []
for par_max in composite_list_temperature_max:
    paris_max.append(par_max[0])

paris_avg = []
for par_avg in composite_list_temperature_avg:
    paris_avg.append(par_avg[0])

versailles_weather = []
for ver in composite_list_weather_num:
    versailles_weather.append(ver[1])

versailles = []
for ver in composite_list:
    versailles.append(ver[1])

versailles_min = []
for ver_min in composite_list_temperature_min:
    versailles_min.append(ver_min[1])

versailles_max = []
for ver_max in composite_list_temperature_max:
    versailles_max.append(ver_max[1])

versailles_avg = []
for ver_avg in composite_list_temperature_avg:
    versailles_avg.append(ver_avg[1])

melun_weather = []
for mel in composite_list_weather_num:
    melun_weather.append(mel[2])

melun = []
for mel in composite_list:
    melun.append(mel[2])

melun_min = []
for mel_min in composite_list_temperature_min:
    melun_min.append(mel_min[2])

melun_max = []
for mel_max in composite_list_temperature_max:
    melun_max.append(mel_max[2])

melun_avg = []
for mel_avg in composite_list_temperature_avg:
    melun_avg.append(mel_avg[2])

fontainebleau_weather = []
for fon in composite_list_weather_num:
    fontainebleau_weather.append(fon[3])

fontainebleau = []
for fon in composite_list:
    fontainebleau.append(fon[3])

fontainebleau_min = []
for fon_min in composite_list_temperature_min:
    fontainebleau_min.append(fon_min[3])

fontainebleau_max = []
for fon_max in composite_list_temperature_max:
    fontainebleau_max.append(fon_max[3])

fontainebleau_avg = []
for fon_avg in composite_list_temperature_avg:
    fontainebleau_avg.append(fon_avg[3])

cergy_weather = []
for cer in composite_list_weather_num:
    cergy_weather.append(cer[4])

cergy = []
for cer in composite_list:
    cergy.append(cer[4])

cergy_min = []
for cer_min in composite_list_temperature_min:
    cergy_min.append(cer_min[4])

cergy_max = []
for cer_max in composite_list_temperature_max:
    cergy_max.append(cer_max[4])

cergy_avg = []
for cer_avg in composite_list_temperature_avg:
    cergy_avg.append(cer_avg[4])

meteo = dict()

meteo['Date'] = dates

meteo['Paris'] = paris
meteo['Paris_weather'] = paris_weather
meteo['Paris_min'] = paris_min
meteo['Paris_max'] = paris_max
meteo['Paris_avg'] = paris_avg

meteo['Versailles'] = versailles
meteo['Versailles_weather'] = versailles_weather
meteo['Versailles_min'] = versailles_min
meteo['Versailles_max'] = versailles_max
meteo['Versailles_avg'] = versailles_avg

meteo['Melun'] = melun
meteo['Melun_weather'] = melun_weather
meteo['Melun_min'] = melun_min
meteo['Melun_max'] = melun_max
meteo['Melun_max'] = melun_max

meteo['Fontainebleau'] = fontainebleau
meteo['Fontainebleau_weather'] = fontainebleau_weather
meteo['Fontainebleau_min'] = fontainebleau_min
meteo['Fontainebleau_max'] = fontainebleau_max
meteo['Fontainebleau_avg'] = fontainebleau_avg

meteo['Cergy'] = cergy
meteo['Cergy_weather'] = cergy_weather
meteo['Cergy_min'] = cergy_min
meteo['Cergy_max'] = cergy_max
meteo['Cergy_avg'] = cergy_avg

df = pd.DataFrame(meteo)

# saving the dataframe
df.to_csv('meteo_France-' + str(year) + '.csv')


end_time = time.time()
print('Time taken : ' + str(end_time - start_time) + " sec")
