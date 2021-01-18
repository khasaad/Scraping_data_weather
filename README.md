<!DOCTYPE html>
<html>
<body>

<h3> Bibliothèques utiliséés:</h3> Pandas, Beautifulsoup, matplotlib, numpy, threading, multiprocessing , os, time, math <br/>
<ol>
  
  <li>Partie scraping: </li>
  <ul>
    <li>scraping data twitter: LDLC </li>
    <li>scraping data météo from site:  https://www.historique-meteo.net/france/ile-de-france/ </li>
    <ul>
      <li>Partie sequential</li>
      Il contient 2 scripts python: <br/>
      <ul>
        <li>sequential_scraping_meteo.py </li>
        Il contient une fonction (sequential_scraping()) qui fait le scraping data météo (Dans le output il faut choisir l'année souhaitée) <br/>
        <li> Dict_sequential_scraping_meteo.py </li> 
        Il uilise le script "sequential_scraping_meteo.py " pour faire un tableau csv qui contient le data et le donne automatiquement le nom avec l'année précisée
        </ul>
     
      <li>Partie sequential avec détails</li>
      Cette partie fait scraping data météo avec détails (degré température minimale, maximale, moyenne, condition de météo (pire:0, mauvaise:1, moyenne:2, bonne:3)) en île-de-         France. <br/>
      Il contient 2 scripts python:
      <ul>
        <li>sequential_scraping_weather_France_with_details.py</li>
        Il contient une fonction (scraping_detail()) qui fait le scraping data météo avec détails (Dans le output il faut choisir l'année souhaitée)
        <li>Dict_sequential_scraping_weather_France_with_details.py</li>
         Il uilise le script "Dict_sequential_scraping_weather_France_with_details.py " pour faire un tableau csv qui contient le data et le donne automatiquement le nom avec            l'année précisée
      </ul>
      <li>Partie parallèle</li>
      Cette partie fait scraping data météo en île-de-France par deux méthodes parallèles du site: https://www.historique-meteo.net/france/ile-de-france/ <br/>
      Il contient deux scripts python: <br/>
      <ul>
        <li>parallel_scraping_meteo_France.py</li> 
        Il utilise threading library, on choisit toujours 2*cores qui égale 16 threading. Dans le output il faut choisir l'année souhaitée et le donne automatiquement le nom             du fichier csv avec l'année précisée.
        <li>second_method_parallel_scraping_meteo_France.py</li> 
        Il utilise multiprocessing library avec module Pool and map function.
      </ul>
    </ul>
    
  </ul>
  <li>partie visualisation</li>
  Cette partie contient un script python:<br/>
  visualisation.py:  <br/>
  Il contient deux fonctions: 
  <ul>
  <li>correlation_between_temperature_and_tweets(df, year='2018', month='08'):</li>
  Elle visualise la corrélation entre température et tweets en utilisant matplotlib library.
  <li>show_temperature_same_months_in_18_19_20(month='01'):</li>
  Elle visualise la température pendant un mois souhaitée pour les années 2018, 2019 et 2020 dans le même graphe.
  </ul>
 
</ol>

                 
</body>
</html>
