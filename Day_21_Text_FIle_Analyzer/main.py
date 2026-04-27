from collections import Counter
import os
import re
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, 'sql.txt'),'r') as f:
    text = f.read()
words = re.sub(r'[^a-zA-Z\s]', '', text).lower().split()
#sentences = text.split('. ')
sentences = [s.strip() for s in re.split(r'[.?!]+', text) if s.strip()]
top5      = Counter(words).most_common(5)
avg_len   = sum(len(w) for w in words) / len(words) if words else 0
read_time = len(words) / 200
print(f'Words: {len(words)}, Sentences: {len(sentences)}')
print(f'Top 5 words: {top5}')
print(f'Average word length: {avg_len:.2f}')
print(f'Reading time: {read_time:.1f} minutes')