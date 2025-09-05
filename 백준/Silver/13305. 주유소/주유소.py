N = int(input())

roads = list(map(int, input().split()))

prices = list(map(int, input().split()))

min_price = prices[0]

total_cost = 0

for i in range(N - 1):

    total_cost += min_price * roads[i]

    if prices[i + 1] < min_price:

        min_price = prices[i + 1]

print(total_cost)