import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('stopwords')
nltk.download('punkt')
# Read the contents of the "random_paragraphs.txt" file
with open("paragraphs.txt", "r") as file:
    text = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)  # Convert to lowercase

# Remove punctuation and stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower not in stop_words]

# Count the frequency of all words
word_freq = Counter(filtered_words)

# Display word frequency count (excluding stop words and punctuation)
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
