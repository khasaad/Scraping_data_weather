import os
import pandas as pd

# CLI commande pour scrap twitter a l'aide de snscrape
os.system("snscrape --jsonl --max-results 17000 twitter-search 'from:LDLC'> user-tweets.json")

# creation du dataframe
df_tweets = pd.read_json('user-tweets.json', lines=True)

# sauvegarde csv des tweets
df_tweets.to_csv('LDLC_tweets.csv', index=False)
