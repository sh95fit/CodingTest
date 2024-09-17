def kosaraju_scc(n, adj_list):
    from sys import setrecursionlimit

    setrecursionlimit(10**6)

    import sys

    sys.setrecursionlimit(10**6)  
       
    def dfs1(v):
        visited[v] = True

        for u in adj_list[v]:
            if not visited[u]:
                dfs1(u)

        order.append(v)
       
    def reverse_graph():
        rev_adj_list = [[] for _ in range(n)]

        for v in range(n):
            for u in adj_list[v]:
                rev_adj_list[u].append(v)

        return rev_adj_list
       
    def dfs2(v, current_scc):
        visited[v] = True
        scc[v] = current_scc

        for u in rev_adj_list[v]:
            if not visited[u]:
                dfs2(u, current_scc)
      
    order = []
    visited = [False] * n

    scc = [-1] * n
        
    for i in range(n):
        if not visited[i]:
            dfs1(i)
       
    rev_adj_list = reverse_graph()
      
    visited = [False] * n
    current_scc = 0
   
    while order:
        v = order.pop()

        if not visited[v]:
            dfs2(v, current_scc)
            current_scc += 1
    
    return scc, current_scc

def minimum_police_cost(n, cost, adj_matrix):   
    adj_list = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == '1':
                adj_list[i].append(j)
       
    scc, scc_count = kosaraju_scc(n, adj_list)
       
    scc_cost = [float('inf')] * scc_count

    for i in range(n):
        scc_cost[scc[i]] = min(scc_cost[scc[i]], cost[i])
        
    total_cost = sum(scc_cost)

    return total_cost

import sys

input = sys.stdin.read

data = input().split()

n = int(data[0])
cost = list(map(int, data[1:n+1]))
adj_matrix = data[n+1:]

print(minimum_police_cost(n, cost, adj_matrix))

