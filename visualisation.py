import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading the CSV file
df_2018 = pd.read_csv('meteo_France-2018.csv')
df_2019 = pd.read_csv('meteo_France-2019.csv')
df_2020 = pd.read_csv('meteo_France-2020.csv')
df_LDLC = pd.read_csv('LDLC_tweets.csv')

df_meteo_tweets = pd.read_csv('meteo_tweets.csv')

temp_country_avg = []
temp_country_avg_2018 = []
temp_country_avg_2019 = []
temp_country_avg_2020 = []


def correlation_between_temperature_and_tweets(df, year='2018', month='08'):
    for i in range(len(df)):
        if df.loc[i, "Date"][3:5] == month:
            temp_country_avg.append(df.loc[i, 'Paris_avg'])

    print('length of temp_country_avg = ', len(temp_country_avg))
    likes_avg = []
    retweets_avg = []
    for y in range(len(df_meteo_tweets)):
        if df_meteo_tweets.loc[y, 'date'][0:7] == year + '-' + month:
            likes_avg.append(df_meteo_tweets.loc[y, 'likeAvg'])
            retweets_avg.append(df_meteo_tweets.loc[y, 'retweetAvg'])

    print('length of  likes average = ', len(likes_avg))
    print('length of  retweets average = ', len(retweets_avg))

    # Create some mock data
    t = np.arange(1, len(temp_country_avg) + 1)
    print('length of t = ', len(t))

    data1 = temp_country_avg
    data2 = likes_avg
    data3 = retweets_avg

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('month ' + month + '-' + year)
    ax1.set_ylabel('temp_avg', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    print('length of data1 = ', len(data1))
    print('length of data2 = ', len(data2))
    color = 'tab:blue'
    ax2.set_ylabel('Like and retweet avg', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, data2, color="blue", label="likes")
    ax2.plot(t, data3, color='green', label="retweets")
    ax2.tick_params(axis='y', labelcolor=color)
    plt.legend(loc='best')
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()


def show_temperature_same_months_in_18_19_20(month='01'):
    for i in range(len(df_2018)):
        if df_2019.loc[i, "Date"][3:5] == month:
            temp_country_avg_2018.append(df_2018.loc[i, 'Paris_avg'])

    for i in range(len(df_2019)):
        if df_2019.loc[i, "Date"][3:5] == month:
            temp_country_avg_2019.append(df_2019.loc[i, 'Paris_avg'])

    for i in range(len(df_2020)):
        if df_2020.loc[i, "Date"][3:5] == month:
            temp_country_avg_2020.append(df_2020.loc[i, 'Paris_avg'])

    temp_avg_2018 = np.array(temp_country_avg_2018)
    temp_avg_2019 = np.array(temp_country_avg_2019)
    temp_avg_2020 = np.array(temp_country_avg_2020)

    axis_x = np.arange(1, len(temp_country_avg_2018) + 1)

    plt.plot(axis_x, temp_avg_2018, 'green', label="2018")
    plt.plot(axis_x, temp_avg_2019, label='2019')
    plt.plot(axis_x, temp_avg_2020, label="2020")
    plt.legend(loc='best')
    plt.xlabel('Month ' + month + ' in 2018 - 2019 - 2020')
    plt.ylabel('Average temperature')

    plt.show()


correlation_between_temperature_and_tweets(df_2020, year='2020', month='08')
show_temperature_same_months_in_18_19_20(month='08')

"""
show_temperature_same_months_in_18_19_20(month='02') --> This does not work because February month has different
dimension between 2018, 2019 and 2020
"""

