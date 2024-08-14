def count_ones(n):
    return bin(n).count('1')

def minimum_bottles_to_buy(N, K):
    bottles_to_buy = 0
    while count_ones(N) > K:
        bottles_to_buy += 1
        N += 1
    return bottles_to_buy

N, K = map(int, input().split())

print(minimum_bottles_to_buy(N, K))