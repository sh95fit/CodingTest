from itertools import combinations

def calculate_chicken_distance(houses, selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chickens:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance
    return total_distance

def solve_chicken_city(N, M, city):
    houses = []
    chickens = []
    
    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                houses.append((r, c))
            elif city[r][c] == 2:
                chickens.append((r, c))
    
    min_city_distance = float('inf')
    for selected_chickens in combinations(chickens, M):
        min_city_distance = min(min_city_distance, calculate_chicken_distance(houses, selected_chickens))
    
    return min_city_distance

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

print(solve_chicken_city(N, M, city))