import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
with open('convert.csv','r',encoding='utf-8')as file:
    reader=csv.reader(file)
    a=" ".join(i[2] for i in reader)
b=word_tokenize(a)
stop_words = stopwords.words('english')
c= [i for i in b if i.lower() not in stop_words]
d=nltk.pos_tag(c)
e=nltk.ne_chunk(d)
print(e)
print(e.draw())