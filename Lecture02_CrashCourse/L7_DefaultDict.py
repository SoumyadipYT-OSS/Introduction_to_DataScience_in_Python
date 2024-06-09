document = "Data Science using Python"

from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1
    print(word)

print(len(document))
