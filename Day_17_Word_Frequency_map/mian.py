from collections import Counter
stopwords = {'for', 'it', 'is', 'am', 'are', 'to', 'and','of', 'in', 'a', 'the', 'this', 'that','their', 'these', 'those', 'was', 'warning', 'i'}
text = input("Enter text: ")
words = [w.strip('.,!?-"') for w in text.lower().split()]
filtered = [w for w in words if w not in stopwords]
counts = Counter(filtered)
for word, count in counts.most_common(5):
    print(f"{word}: {count}")