import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
word_count = defaultdict(int)

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        word_count[word] += 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)
