# Counters
sentence = "Python program is in majority field, in Computer Science Python is used in major domain, among them Data Science is one of them. In, 6th semeseter we were taught Introduction to Data Science using Python Program"


from collections import Counter
word_count = 0;
for word in sentence:
    word_count = Counter(sentence)

print(word_count)
