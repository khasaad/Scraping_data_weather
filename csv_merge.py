import pandas as pd
import numpy as np
from datetime import datetime as dt

# chargement csv meteo
df_meteo = pd.read_csv('meteo_France-2020.csv')
print(df_meteo.info(verbose=False))
df_meteo_2 = pd.read_csv('meteo_France-2019.csv')
print(df_meteo_2.info(verbose=False))
df_meteo_3 = pd.read_csv('meteo_France-2018.csv')
print(df_meteo_3.info(verbose=False))

df_meteo_all = pd.concat([df_meteo, df_meteo_2, df_meteo_3])
print(df_meteo_all)

df_meteo_all = df_meteo_all.drop(columns=['Versailles', 'Versailles_weather', 'Versailles_min', 'Versailles_max',\
                                  'Versailles_avg', 'Melun', 'Melun_weather', 'Melun_min', 'Melun_max',\
                                  'Fontainebleau', 'Fontainebleau_weather', 'Fontainebleau_min', 'Fontainebleau_max',
                                  'Fontainebleau_avg', 'Cergy', 'Cergy_weather', 'Cergy_min', 'Cergy_max',\
                                  'Cergy_avg', 'Paris', 'Unnamed: 0'])
df_meteo_all['Date'] = pd.to_datetime(df_meteo_all['Date'], format='%d/%m/%Y')
df_meteo_all['Date'] = df_meteo_all['Date'].dt.strftime('%d/%m/%Y')
df_meteo_all = df_meteo_all.rename(columns={'Date': 'date'})

df_meteo_all.to_csv('verif_meteo.csv', index=False)

# chargement csv tweets version light
df_tweets = pd.read_csv('LDLC_tweets_edited_light.csv')

# ajout colonnes tweetCount, reactions
df_tweets['tweetCount'] = 1
df_tweets['reactions'] = df_tweets['replyCount'] + df_tweets['likeCount'] +\
                         df_tweets['retweetCount'] + df_tweets['quoteCount']


# somme reactions en fonction du media
df_tweets_media = df_tweets.drop(columns=['id', 'lang', 'time', 'contest', 'date'])
df_tweets_media = df_tweets_media.groupby('mediaType').sum()
# df_tweets_media = df_tweets_media.sum()

# sauvegarde csv
df_tweets_media.to_csv('LDLC_tweets_media.csv')

# print(df_tweets_media.info)
# print("\n")
# print(df_tweets_media)

# preparation merge
df_tweets = df_tweets.drop(columns=['id', 'lang', 'mediaType', 'time'])
df_tweets['date'] = pd.to_datetime(df_tweets['date'], format='%Y-%m-%d')
df_tweets['date'] = df_tweets['date'].dt.strftime('%d/%m/%Y')
df_tweets = df_tweets[['tweetCount', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'reactions',\
                       'contest', 'date']]

# infos des datasets
# print(df_meteo.info(verbose=False))
# print("\n")
# print(df_tweets.info(verbose=False))
# print("\n")

# somme des reactions en fonction de la date
df_tweets_count = df_tweets.groupby('date').sum()

# creation de nouvelles colonnes moyennes
df_tweets_count['replyAvg'] = df_tweets_count.apply(lambda row: (row.replyCount / row.tweetCount), axis=1)
df_tweets_count['replyAvg'] = df_tweets_count.replyAvg.round(1)
df_tweets_count['retweetAvg'] = df_tweets_count.apply(lambda row: (row.retweetCount / row.tweetCount), axis=1)
df_tweets_count['retweetAvg'] = df_tweets_count.retweetAvg.round(1)
df_tweets_count['likeAvg'] = df_tweets_count.apply(lambda row: (row.likeCount / row.tweetCount), axis=1)
df_tweets_count['likeAvg'] = df_tweets_count.likeAvg.round(1)
df_tweets_count['quoteAvg'] = df_tweets_count.apply(lambda row: (row.quoteCount / row.tweetCount), axis=1)
df_tweets_count['quoteAvg'] = df_tweets_count.quoteAvg.round(1)
df_tweets_count['reactionsAvg'] = df_tweets_count.apply(lambda row: (row.reactions / row.tweetCount), axis=1)
df_tweets_count['reactionsAvg'] = df_tweets_count.reactionsAvg.round(1)
reorder = df_tweets_count['contest']
df_tweets_count.drop(labels=['contest'], axis=1, inplace=True)
df_tweets_count.insert(11, 'contest', reorder)

# merge
df_merged = pd.merge(df_meteo_all, df_tweets_count, how='inner', on='date')
df_merged['date'] = pd.to_datetime(df_merged['date'], format='%d/%m/%Y')
df_merged = df_merged.sort_values(by='date')

# print(df_merged.info(verbose=False))
# print("\n")
# print(df_merged)

# sauvegarde merged csv
df_merged.to_csv('meteo_tweets.csv', index=False)

# print(df_merged.likeCount.sum())