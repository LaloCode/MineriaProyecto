import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def formatText(data):
    text = " ".join(key for key in data)
    text = text.replace("[", "")
    text = text.replace("'", "")
    text = text.replace("]", "")
    text = text.replace(",", "")
    return text

data = pd.read_csv('data/top10s_clean.csv', index_col=0)
text = formatText(data.artist)
wc_test = WordCloud(max_words=100, background_color="white").generate(text)
plt.imshow(wc_test, interpolation="bilinear")
plt.axis('off')
plt.title("Artistas mas populares 2010-2019")
plt.savefig("img/p9_textanalysis")
plt.show()
