N, K = map(int, input().split())  
coins = [int(input()) for _ in range(N)]  
count = 0

for coin in reversed(coins):  
    if K >= coin:
        count += K // coin  
        K %= coin  

    if K == 0:
        break  

print(count)

