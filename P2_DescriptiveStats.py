import pandas as pd

data = pd.read_csv('data/top10s_clean.csv', index_col=0)

data = data.sort_values('popularity', 0, False)

BpmMean = data.bpm.mean()

BpmDeviation = data.bpm.std()

MaxPopularity = data.popularity.max()

MostPopularSongTitle = data[data.popularity == MaxPopularity].title

MostPopularSongArtists = data[data.popularity == MaxPopularity].artist

print('El bpm promedio de las canciones mas populares del 2010 - 2019 es de ' + str(int(BpmMean)) + ' bpm')
print('Con una desviacion estandar de ' + str(BpmMean))
print('La cancion mas popular es ' + MostPopularSongTitle.iloc[0] + ' de ' + MostPopularSongArtists.iloc[0])