import csv
import nltk
from nltk.tokenize import word_tokenize
with open('convert.csv','r',encoding='utf-8')as file:
    reader=csv.reader(file)
    a=" ".join(i[2] for i in reader)
b=word_tokenize(a)
c=nltk.pos_tag(b)
d=nltk.ne_chunk(c)
print(d)
print(d.draw())