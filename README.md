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
        Il utilise threading library, on choisit toujours 2*cores qui égale 16 threading. Dans le output il faut choisir l'année souhaitée et le donne automatiquement le nom             du fichier csv avec l'année précisée
      </ul>

    </ul>
  </ul>
  <li>partie visualisation</li>
</ol>

                 
</body>
</html>
