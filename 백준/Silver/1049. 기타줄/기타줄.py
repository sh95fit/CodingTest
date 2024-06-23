def calculate_min_cost(N, M, price_list):

    min_package_price = float('inf')

    min_single_price = float('inf')

    for package_price, single_price in price_list:

        min_package_price = min(min_package_price, package_price)

        min_single_price = min(min_single_price, single_price)

    cost_if_package_only = ((N // 6) + 1) * min_package_price

    cost_if_single_only = N * min_single_price

    cost_if_mixed = (N // 6) * min_package_price + (N % 6) * min_single_price

    return min(cost_if_package_only, cost_if_single_only, cost_if_mixed)


N, M = map(int, input().split())

price_list = [tuple(map(int, input().split())) for _ in range(M)]


min_cost = calculate_min_cost(N, M, price_list)


print(min_cost)

