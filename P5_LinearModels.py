import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt

data = pd.read_csv('data/top10s_clean.csv', index_col=0).sort_values(by='dance', axis=0, ascending=False)
model = smf.ols('valence ~ energy', data=data)
model = model.fit()

sales_pred = model.predict()

plt.figure(figsize=(12, 6))
plt.plot(data['energy'], data['valence'], 'o')           # scatter plot showing actual data
plt.plot(data['energy'], sales_pred, 'r', linewidth=2)   # regression line
plt.xlabel('Energy in a song')
plt.ylabel('Valence')
plt.title('Energy and valence of songs')

plt.savefig('img/P5_LR.png')
plt.show()
plt.close()

# Calculate the mean of X and y
#xmean = np.mean(data.valence)
#ymean = np.mean(data.popularity)

# Calculate the terms needed for the numator and denominator of beta
#data['xycov'] = (data['valence'] - xmean) * (data['popularity'] - ymean)
#data['xvar'] = (data['valence'] - xmean)**2

# Calculate beta and alpha
#beta = data['xycov'].sum() / data['xvar'].sum()
#alpha = ymean - (beta * xmean)

#print(f'alpha = {alpha}')
#print(f'beta = {beta}')

#ypred = alpha + beta * data.valence
#print(ypred)