import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "http://quotes.toscrape.com/tag/inspirational/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quote elements
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(text+"\n-"+author+"\n")

