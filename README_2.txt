Slide google : https://docs.google.com/presentation/d/1WA6l8bBAvUmFnGiNW4qu3X53quZC02TX6PCtFiPwAV4/edit#slide=id.gb61c4ecbd6_1_0

Bibliothèques : os, pandas, pandas_profiling, matplotlib.pyplot, seaborn

scrap_twitter.py : fichier .py qui exécute une commande ILC dans le terminal avec snscrape, une              			bibliothèque permettant le scraping de twitter selon des paramètres définis par l’utilisateur via l’API twitter.
			→ LDLC_tweet.csv (les 17000 derniers tweets afin d’avoir 3 ans de données)

notes : installer snscrape via « pip install git+https://github.com/JustAnotherArchivist/snscrape.git »
	afin d’obtenir la version développeur qui permet d’obtenir des infos depuis les tweets plutôt que depuis l’url des tweets.

csv_edit.py : édition de « LDLC_tweet.csv » pour éliminer les informations inutiles, en ajouter, réduire le poids et mettre en forme.
		→best_tweets.csv (sélection des tweets les plus like)
		→reply_tweet.csv (sélection des tweets ayant eu le plus de réponses)
		→LDLC_tweets_edited.csv (version édité des tweets)
		→LDLC_tweets_edited_light.csv (version plus légère, sans le commentaire du tweet)

csv_merge.py : concaténation des fichiers « météo_France-2020.csv, météo_France-2019.csv, météo_France-2018.csv ». Mise en forme du dataframe résultant.
		Chargement du fichier « LDLC_tweets_edited_light.csv », mise en forme.
		Merge des 2 dataframes afin d’avoir les tweets en relation avec la météo.
		Print() de différentes données afin de remplir la slide 9.
		→LDLC_tweets_media.csv ( dataframe pour la création des graphs média)
		→meteo_tweets.csv (dataframe tweets + météo de janvier 2018 à novembre 2020)

profiling.py : profiling de « meteo_tweets.csv »
		→rapport-tweets.html
		→graph slide 4

chart_bar_weather.py : création de graph depuis « meteo_tweets.csv ».
			→slide 15

chart_pie_media.py & chart_ bar_media.py : création de graph depuis « LDLC_tweets_media.csv »
						→slide 18
		
