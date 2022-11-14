import pandas as pd

data = pd.read_csv("data/top10s.csv", encoding='cp1252', index_col=0)

data.drop(columns=['live', 'val', 'acous', 'spch'], inplace=True)

data.rename(columns={'top genre': 'genre', 'nrgy': 'energy', 'dnce': 'dance', 'dur': 'duration', 'pop': 'popularity'}, inplace=True)

#data['genre'].apply(filterGenres) 

data.to_csv('data/top10s_clean.csv')

print(data)