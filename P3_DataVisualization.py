import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/top10s_clean.csv', index_col=0).sort_values(by='valence', axis=0, ascending=False)

top100 = data.head(100)
bot100 = data.tail(100)

plt.scatter(top100.bpm, top100.valence, color='green', label='100 canciones con mas energia positiva')
plt.scatter(bot100.bpm, bot100.valence, color='red', label='100 canciones con mas energia negativa')
plt.legend()
plt.title('Relacion del bpm con la energia de la cancion')
plt.xlabel('BPM')
plt.ylabel('Valence')
plt.savefig('img/P3_Valence_BPM_Scatter.png')
plt.show()
plt.close()