from nltk.corpus import wordnet

def find_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

def find_antonyms(word):
    antonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    return antonyms

word = input("Enter a word: ")
print(f"Synonyms of '{word}': {find_synonyms(word)}")
print(f"Antonyms of '{word}': {find_antonyms(word)}")