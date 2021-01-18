import pandas as pd
import numpy as np
from datetime import datetime as dt

# chargement csv tweets
df_tweets = pd.read_csv('LDLC_tweets.csv')

# print(df_tweets.info())
# print("\n")

# suppression des colonnes non pertinentes
df_tweets = df_tweets.drop(columns=['url', 'renderedContent', 'outlinks', 'tcooutlinks', 'source', 'quotedTweet',\
                                   'user', 'sourceUrl', 'sourceLabel', 'mentionedUsers', 'retweetedTweet'])

# creation et remplissage colonne media type
df_tweets['media'] = df_tweets['media'].mask(pd.isnull, "none")

df_tweets['mediaType'] = pd.np.where(df_tweets['media'].str.contains("'type': 'photo'"), "photo",\
                                  pd.np.where(df_tweets['media'].str.contains("'type': 'gif'"), "gif",\
                                              pd.np.where(df_tweets['media'].str.contains("'type': 'video'"), "video",
                                                       "none")))

df_tweets = df_tweets.drop(columns=['media', 'conversationId'])

# reorganisation des dates
df_tweets['date'] = df_tweets['date'].str.split('+').str[0]
df_tweets['datetime'] = pd.to_datetime(df_tweets['date'], format='%Y-%m-%d %H:%M:%S')
df_tweets['new_date'] = [d.date() for d in df_tweets['datetime']]
df_tweets['time'] = [d.time() for d in df_tweets['datetime']]
df_tweets = df_tweets.drop(columns=['date', 'datetime'])
df_tweets = df_tweets.rename(columns={'new_date': 'date'})

# reperage meilleurs tweets (likes, replies)
df_tweets_best = df_tweets.sort_values(by='likeCount', ascending=False)
df_tweets_best = df_tweets_best.head(10)

df_tweets_reply = df_tweets.sort_values(by='replyCount', ascending=False)
df_tweets_reply = df_tweets_reply.head(10)

# sauvegarde csv meilleurs tweets
df_tweets_best.to_csv('best_tweets.csv', index=False)
df_tweets_reply.to_csv('reply_tweets.csv', index=False)

# elimination des tweets concours
words_to_ban = ['Gagne', 'gagne', 'gagnant(e)', 'Gagnant(e)', 'Gagner', 'gagner']
# df_tweets_contest = df_tweets[df_tweets.content.str.contains('|'.join(words_to_ban))]
# print(df_tweets_contest.info)
df_tweets['contest'] = df_tweets.content.apply(lambda x: any(word in x for word in words_to_ban))

# sauvegarde csv des tweets edites
df_tweets.to_csv('LDLC_tweets_edited.csv', index=False)

# version light du dataframe tweets
filtered_tweets = df_tweets.drop(columns='content')
filtered_tweets.to_csv('LDLC_tweets_edited_light.csv', index=False)
