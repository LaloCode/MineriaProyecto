import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt

data = pd.read_csv('data/top10s_clean.csv', index_col=0).sort_values(by='dance', axis=0, ascending=False).groupby(['year']).mean()
data.reset_index(inplace=True)

model = smf.ols('popularity ~ year', data=data)
model = model.fit()
sales_pred = model.predict()

plt.figure(figsize=(12, 6))
plt.plot(data['year'], data['popularity'], 'o')           # scatter plot showing actual data
plt.plot(data['year'], sales_pred, 'r', linewidth=2)   # regression line
plt.xlabel('Year')
plt.ylabel('Popularity')
plt.title('Popularity of songs through the years')

plt.savefig('img/P5_LR.png')
plt.show()
plt.close()