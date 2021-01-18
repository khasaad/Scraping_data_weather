from pandas_profiling import ProfileReport
import pandas as pd

train = pd.read_csv('meteo_tweets.csv')
prof = ProfileReport(train)
prof.to_file(output_file='rapport-tweets.html')