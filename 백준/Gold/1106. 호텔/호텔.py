def min_cost_to_increase_customers(C, city_info):
    max_customers = C + 100  
    dp = [float('inf')] * (max_customers + 1)
    dp[0] = 0  

    for cost, customers in city_info:
        for current_customers in range(customers, max_customers + 1):
            dp[current_customers] = min(dp[current_customers], dp[current_customers - customers] + cost)

    return min(dp[C:max_customers + 1])

C, N = map(int, input().split())
city_info = [tuple(map(int, input().split())) for _ in range(N)]

print(min_cost_to_increase_customers(C, city_info))

