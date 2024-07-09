def calculate_cost(s1, s2):
    if sorted(s1) != sorted(s2):
        return float('inf')

    cost = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cost += 1

    return cost

def minimum_cost(sentence, words):
    n = len(sentence)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for word in words:
            l = len(word)

            if i >= l and sorted(sentence[i-l:i]) == sorted(word):
                cost = calculate_cost(sentence[i-l:i], word)

                if dp[i - l] != float('inf'):
                    dp[i] = min(dp[i], dp[i - l] + cost)

    return dp[n] if dp[n] != float('inf') else -1

import sys

input = sys.stdin.read
data = input().split()

sentence = data[0]
N = int(data[1])
words = data[2:2+N]

result = minimum_cost(sentence, words)

print(result)

