from nltk.tokenize import word_tokenize

def join_at_symbol_words(words):
    result = []
    i = 0
    while i < len(words):
        if words[i].startswith('@') and i + 1 < len(words):
            result.append(''.join([words[i], words[i+1]]))
            i += 2
        else:
            result.append(words[i])
            i += 1
    return result

def remove_twitter_usernames(text):
    words = word_tokenize(text)
    joined_words = join_at_symbol_words(words)
    filtered_words = [word for word in joined_words if not word.startswith('@')]
    return ' '.join(filtered_words)

text = "Be the change you wish to see in the world @Gandhi"
print("Tweet:")
print(text)
print("Tweet without username:")
print(remove_twitter_usernames(text))