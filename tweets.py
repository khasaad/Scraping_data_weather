import pandas as pd


"""
This code shows the best or the least interactive tweet: whether for a year, for a month in a year, 
for a day in a year, or all of them 
"""

df_LDLC = pd.read_csv('LDLC_tweets.csv')
df_2018 = pd.read_csv('meteo_France-2018.csv')
df_2019 = pd.read_csv('meteo_France-2019.csv')
df_2020 = pd.read_csv('meteo_France-2020.csv')

Dict_tweets = dict()


def Dict_max_min(val):
    Dict_tweets['date'] = df_LDLC.loc[val[0], 'date']
    Dict_tweets['replyCount'] = df_LDLC.loc[val[0], 'replyCount']
    Dict_tweets['retweetCount'] = df_LDLC.loc[val[0], 'retweetCount']
    Dict_tweets['likeCount'] = df_LDLC.loc[val[0], 'likeCount']
    Dict_tweets['quoteCount'] = df_LDLC.loc[val[0], 'quoteCount']
    Dict_tweets['mediaType'] = df_LDLC.loc[val[0], 'mediaType']
    Dict_tweets['id_tweet'] = df_LDLC.loc[val[0], 'id']
    return Dict_tweets


def info_tweet(df, year="2018", month=None, day=None, m='max', selon='likeCount'):
    aggregation = []
    for j in range(len(df_LDLC)):
        if day is None and month is not None:
            if df_LDLC.loc[j, 'date'][:4] == year and df_LDLC.loc[j, 'date'][5:7] == month:
                aggregation.append((j, df_LDLC.loc[j, selon]))
        if day is not None and month is not None:
            if df_LDLC.loc[j, 'date'][:4] == year and df_LDLC.loc[j, 'date'][5:] == month + '-' + str(day):
                aggregation.append((j, df_LDLC.loc[j, selon]))
        if month is None and day is None:
            if df_LDLC.loc[j, 'date'][:4] == year:
                aggregation.append((j, df_LDLC.loc[j, selon]))
    if m == 'max':
        Dict_max = Dict_max_min(max(aggregation, key=lambda item: item[1]))
        new_year_max = Dict_max['date']
        newYearMax = new_year_max[8:] + '/' + new_year_max[5:7] + '/' + new_year_max[0:4]
        list_max_dates = []
        for n in df['Date']:
            list_max_dates.append(n)
        for e, z in enumerate(list_max_dates):
            if str(newYearMax) != str(z):
                continue
            elif str(newYearMax) not in list_max_dates:
                continue

            else:
                Dict_tweets['Weather_condition'] = df.loc[e, 'Paris_weather']
                Dict_tweets['Temperature_average'] = df.loc[e, 'Paris_avg']
                return Dict_max
        return Dict_max

    if m == 'min':
        Dict_min = Dict_max_min(min(aggregation, key=lambda item: item[1]))
        new_year_min = Dict_min['date']
        newYearMin = new_year_min[8:] + '/' + new_year_min[5:7] + '/' + new_year_min[0:4]
        list_min_dates = []
        for f in df['Date']:
            list_min_dates.append(f)
        for s, d in enumerate(list_min_dates):
            if str(newYearMin) != str(d):
                continue
            elif str(newYearMin) not in list_min_dates:
                continue

            else:
                Dict_tweets['Weather_condition'] = df.loc[s, 'Paris_weather']
                Dict_tweets['Temperature_average'] = df.loc[s, 'Paris_avg']
                return Dict_min
        return Dict_min


print(info_tweet(df_2018, year="2018", month='01', day='21', m='max', selon='retweetCount'))
