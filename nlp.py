import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
text="Machine learning is fun, and NLTK makes it easier!"
token=word_tokenize(text)
sent=sent_tokenize(text)
stop_words = stopwords.words('english')
print("Given string:")
print(text)
print("Word_tokenization of string:")
print(token)
print("Sentence_tokenization of string:")
print(sent)
print("stop words in English:")
print(stop_words)
print("Stopwords removal in the string:")
for i in token:
    if i not in stop_words:
         print(i)