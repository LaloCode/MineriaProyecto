import pandas as pd

data = pd.read_csv("data/top10s.csv", encoding='cp1252', index_col=0)

data.drop(columns=['bpm', 'nrgy', 'dnce', 'dB', 'live', 'val', 'dur', 'acous', 'spch', 'pop'], inplace=True)

data.rename(columns={'top genre': 'genre'}, inplace=True)

#data['genre'].apply(filterGenres) 

data.to_csv('data/top10s_clean.csv')

print(data)