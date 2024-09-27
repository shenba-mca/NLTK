from nltk.tokenize import word_tokenize

# Sample data
names = ["Bala", "Priya"]
labels = ["python developer", "web developer"]

def extract_last_letter(names):
    last_letters = []
    for name in names:
        tokens = word_tokenize(name)
        last_letter = tokens[0][-1]
        last_letters.append(last_letter)
    return last_letters

def create_new_array(names, last_letters, labels):
    new_array = []
    for i in range(len(names)):
        new_array.append((names[i], last_letters[i], labels[i]))
    return new_array

last_letters = extract_last_letter(names)
new_array = create_new_array(names, last_letters, labels)

print("Original Data:")
print("Names:", names)
print("Labels:", labels)
print("\nNew Array:")
for i in new_array:
    print(i)