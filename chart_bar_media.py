import matplotlib.pyplot as plt
import pandas as pd

df_tweets = pd.read_csv('LDLC_tweets_media.csv')

# column chart
df_tweets.set_index('mediaType')[['replyCount', 'likeCount', 'retweetCount', 'quoteCount']].\
    plot(kind='bar', figsize=(14, 10))
plt.xticks(rotation=60)
plt.title("Réactions / média accompagnant le tweet", fontsize=18, y=1.01)
plt.xlabel("media type", labelpad=15)
plt.ylabel("count", labelpad=15)
plt.legend(['reply', 'likes', 'retweets', 'quotes'], fontsize=16, title="reaction type");

plt.show()