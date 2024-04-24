import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download('stopwords')
nltk.download('punkt')
with open('random_paragraphs.txt', 'r') as file:
    text = file.read()
stopwords_list = set(stopwords.words('english'))
words = nltk.word_tokenize(text)
filtered_words = [word for word in words if word.lower() not in stopwords_list]
word_counts = Counter(filtered_words)
for word, count in word_counts.most_common():
    print(f"{word}: {count}")
stopword_count_filtered = sum(1 for word in filtered_words if word.lower() in stopwords_list)

if stopword_count_filtered > 0:
    print("Stop words found in filtered text.")
    print(f"Number of stop words found: {stopword_count_filtered}")
else:
    print("No stop words found in filtered text.")
    
output_file_path = "filtered_text.txt"
with open('output.txt', 'w') as file:
    filtered_text = ' '.join(filtered_words)
    file.write(filtered_text)
print(f"Filtered text has been written to {output_file_path}")

