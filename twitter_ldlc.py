import os
import pandas as pd

"""
This code scrape all details of tweets from an twitter account
"""

# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --max-results 10000 twitter-search 'from:LDLC'> user-tweets.json")

# Reads the json generated from the CLI commands above and creates a pandas dataframe
tweets_df = pd.read_json('user-tweets.json', lines=True)

# saving the dataframe
tweets_df.to_csv('LDLC_tweets.csv', index=False)
