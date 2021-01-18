import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_meteotweets = pd.read_csv('meteo_tweets.csv')
df_meteotweets = df_meteotweets.groupby('Paris_weather').mean().reset_index()

# print(df_meteotweets)

# creation graphique
fig, ax1 = plt.subplots(figsize=(10, 6))
color = 'tab:green'

# bar plot
ax1.set_title('Reactions moyennes / Météo', fontsize=24)
ax1.set_xlabel('Qualité météo', fontsize=16)
ax1.set_ylabel('Réactions', fontsize=16)
ax1 = sns.barplot(x='Paris_weather', y='reactionsAvg', data=df_meteotweets, palette='summer')
ax1.tick_params(axis='y')

# sur le meme axe
ax2 = ax1.twinx()
color2 = 'tab:red'

# lineplot
ax2.set_ylabel('Tweet count', fontsize=16, color=color2)
ax2 = sns.lineplot(x='Paris_weather', y='tweetCount', data=df_meteotweets, sort=False, color=color2)
ax2.tick_params(axis='y', color=color2)

plt.show()