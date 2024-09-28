import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
df = pd.read_csv('convert.csv')
quotes = ' '.join(df['quote'])
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, max_font_size=110,background_color='skyblue').generate(text)
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation="none")
    plt.axis('off')
    plt.show()
generate_word_cloud(quotes)