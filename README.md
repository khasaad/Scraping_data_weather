<!DOCTYPE html>
<html>
<body>
  <h3> Bibliothèques utiliséés:</h3> Pandas, Beautifulsoup, matplotlib, seaborn, numpy, threading, multiprocessing , os, time, math <br/><br/>
  Il contient 2 parties: <br/><br/> 
    <ul>
    <li>Partie scraping: </li> 	
	<ul>
	<li>scraping data twitter: LDLC </li>
	<ul>
         <li>scrap_twitter.py: </li>
                  fichier .py qui exécute une commande ILC dans le terminal avec snscrape, une bibliothèque permettant le scraping de twitter selon des paramètres définis par l’utilisateur via l’API twitter. </br>
          → LDLC_tweet.csv (les 17000 derniers tweets afin d’avoir 3 ans de données)
          <B>notes</B>: installer snscrape via « pip install git+https://github.com/JustAnotherArchivist/snscrape.git » afin d’obtenir la version développeur qui permet d’obtenir des infos depuis les tweets plutôt que depuis l’url des tweets.
          <li>csv_edit.py: </li>
           édition de « LDLC_tweet.csv » pour éliminer les informations inutiles, en ajouter, réduire le poids et mettre en forme.</br>
          →best_tweets.csv (sélection des tweets les plus like)</br>
          →reply_tweet.csv (sélection des tweets ayant eu le plus de réponses)</br>
          →LDLC_tweets_edited.csv (version édité des tweets)</br>
          →LDLC_tweets_edited_light.csv (version plus légère, sans le commentaire du tweet)
          <li>csv_merge.py: </li>
          concaténation des fichiers « météo_France-2020.csv, météo_France-2019.csv, météo_France-2018.csv ». Mise en forme du dataframe résultant.</br>
          Chargement du fichier « LDLC_tweets_edited_light.csv », mise en forme.</br>
          Merge des 2 dataframes afin d’avoir les tweets en relation avec la météo.</br>
          Print() de différentes données afin de remplir la slide 9.</br>
          →LDLC_tweets_media.csv ( dataframe pour la création des graphs média)</br>
          →meteo_tweets.csv (dataframe tweets + météo de janvier 2018 à novembre 2020)
          <li>profiling.py: </li>
          profiling de « meteo_tweets.csv »</br>
		      →rapport-tweets.html</br>
		      →graph slide 4 </br>
          <li>chart_bar_weather.py: </li>
          création de graph depuis « meteo_tweets.csv ».</br>
			    →slide 15
          <li>chart_pie_media.py & chart_ bar_media.py:  </li>
          création de graph depuis « LDLC_tweets_media.csv »</br>
						→slide 18
	</ul>
        </ul>
      <ul>
        <li>scraping data météo from site:  https://www.historique-meteo.net/france/ile-de-france/ </li>
          <ul>
            <li>Partie sequential</li>
            Il contient 2 scripts python: <br/>
            <ul>
              <li>sequential_scraping_meteo.py </li>
              Il contient une fonction (sequential_scraping()) qui fait le scraping data météo (Dans le output il faut choisir l'année souhaitée) <br/>
              <li> Dict_sequential_scraping_meteo.py </li>
              Il uilise le script "sequential_scraping_meteo.py " pour faire un tableau csv qui contient le data et le donne automatiquement le nom avec l'année précisée.
            </ul>
            <li>Partie sequential avec détails</li>
            Cette partie fait scraping data météo avec détails (degré température minimale, maximale, moyenne, condition de météo (pire:0, mauvaise:1, moyenne:2, bonne:3))                  en île-de-France. <br/>
         Il contient 2 scripts python:
            <ul>
              <li>sequential_scraping_weather_France_with_details.py</li>
              Il contient une fonction (scraping_detail()) qui fait le scraping data météo avec détails (Dans le output il faut choisir l'année souhaitée)
              <li>Dict_sequential_scraping_weather_France_with_details.py</li>
              Il uilise le script "Dict_sequential_scraping_weather_France_with_details.py " pour faire un tableau csv qui contient le data et le donne automatiquement le nom avec l'année précisée.
            </ul>
            <li>Partie parallèle</li>
            Cette partie fait scraping data météo en île-de-France par deux méthodes parallèles du site: https://www.historique-meteo.net/france/ile-de-france/ <br/>
                Il contient deux scripts python: <br/>
            <ul>
              <li>parallel_scraping_meteo_France.py</li> 
              Il utilise threading library, on choisit toujours 2*cores qui égale 16 threading. Dans le output il faut choisir l'année souhaitée et le donne automatiquement le nom du fichier csv avec l'année précisée.
              <li>second_method_parallel_scraping_meteo_France.py</li> 
              Il utilise multiprocessing library avec module Pool and map function.
            </ul>
          </ul>
      </ul>
    <li>partie visualisation</li>
    Cette partie contient un script python:<br/>
    visualisation.py:  <br/>
    Il contient deux fonctions et il faut utiliser les fichiers qui sortent de la fonction "Dict_sequential_scraping_weather_France_with_details.py" pour l'année 2018-2019-2020 et de la code "twitter_ldlc.py". 
  <ul>
    <li>correlation_between_temperature_and_tweets(df, year='2018', month='08'):</li>
    Elle visualise la corrélation entre température et tweets en utilisant matplotlib library.
     <li>show_temperature_same_months_in_18_19_20(month='01'):</li>
    Elle visualise la température pendant un mois souhaitée pour les années 2018, 2019 et 2020 dans le même graphe.
  </ul>
  </ol>
  
</body>
</html> 
