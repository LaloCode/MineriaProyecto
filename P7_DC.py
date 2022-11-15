import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/top10s_clean.csv', index_col=0).groupby(['genre']).size().sort_values(axis=0, ascending=False)
data = data.head(10)

data.plot.barh()

plt.savefig('img/P7_Classification.png')
plt.show()
plt.close()