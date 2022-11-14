import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, shapiro

data = pd.read_csv('data/top10s_clean.csv', index_col=0)

contingency = pd.crosstab(data['bpm'], data['popularity'])
c, p, dof, expected = chi2_contingency(contingency)

if p > 0.05:
    print('El bpm y la popularidad de una cancion son independientes')
else:
    print('El bpm y la popularidad de una cancion tienen una relacion dependiente')

stat, p = shapiro(data['popularity'])
if p > 0.05:
	print('La probabilidad tiene una distribucion gaussiana')
else:
	print('La probabilidad no tiene una distribucion gaussiana')

aux = data.groupby(by=['bpm'])['bpm'].count()
aux.plot()
plt.title('BPM mas comunes')
plt.xlabel('BPM')
plt.ylabel('Cantidad')
plt.savefig('img/P4_BPM.png')
plt.show()
plt.close()