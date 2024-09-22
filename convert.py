import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'http://quotes.toscrape.com/tag/inspirational/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='quote')
new_row = []
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    new_row.append({'quote': text, 'author': author})
print(new_row)
df=pd.DataFrame(new_row)
df.to_csv('convert.csv')