from collections import defaultdict

def solve():
    n = int(input())
    words = [input().strip() for _ in range(n)]
   
    weight = defaultdict(int)

    for word in words:
        length = len(word)

        for i, ch in enumerate(word):
            weight[ch] += 10 ** (length - i - 1)
   
    sorted_weight = sorted(weight.items(), key=lambda x: -x[1])
   
    num = 9
    char_to_digit = {}

    for ch, _ in sorted_weight:
        char_to_digit[ch] = num

        num -= 1
   
    total = 0

    for word in words:
        value = 0

        for ch in word:
            value = value * 10 + char_to_digit[ch]

        total += value

    print(total)

solve()