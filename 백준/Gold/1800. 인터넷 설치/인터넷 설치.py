import heapq

def can_connect_with_cost(mid, n, k, edges):
    graph = [[] for _ in range(n + 1)]  

    for u, v, cost in edges:
        if cost <= mid:
            graph[u].append((v, 0))
            graph[v].append((u, 0))

        else:
            graph[u].append((v, 1))
            graph[v].append((u, 1))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]     

    while pq:
        used_expensive, node = heapq.heappop(pq)
        
        if dist[node] < used_expensive:
            continue       

        for neighbor, cost in graph[node]:
            new_used_expensive = used_expensive + cost

            if new_used_expensive < dist[neighbor]:
                dist[neighbor] = new_used_expensive
                heapq.heappush(pq, (new_used_expensive, neighbor))
    
    return dist[n] <= k

def find_min_cost(n, p, k, edges):
    left, right = 0, max(cost for _, _, cost in edges)
    answer = -1

    while left <= right:
        mid = (left + right) // 2
      
        if can_connect_with_cost(mid, n, k, edges):
            answer = mid
            right = mid - 1

        else:
            left = mid + 1
    
    return answer

n, p, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(p)]

result = find_min_cost(n, p, k, edges)
print(result)

