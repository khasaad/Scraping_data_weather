import matplotlib.pyplot as plt
import pandas as pd

df_tweets = pd.read_csv('LDLC_tweets_edited_light.csv')

title_rating = df_tweets.groupby('mediaType').agg('count')
rating_labels = title_rating.id.sort_values().index
rating_counts = title_rating.id.sort_values()

# pie chart
explode = (0.1, 0, 0, 0)
plt.pie(rating_counts, labels=rating_labels, explode=explode, autopct='%1.1f%%', shadow=False)
plt.title("Types de médias", fontsize=18)

plt.show()
