def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)   

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX

        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY

        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def kruskal(N, edges):
    parent = [i for i in range(N)]
    rank = [0] * N
    mst_weight = 0
    mst_edges = 0

    for cost, u, v in sorted(edges):
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += cost
            mst_edges += 1
            
            if mst_edges == N - 1:
                break    

    if mst_edges == N - 1:
        return mst_weight

    else:
        return -1

def main():
    N = int(input().strip())
    total_weight = 0
    edges = []
    
    for i in range(N):
        row = input().strip()

        for j in range(N):
            if row[j] != '0':
                if 'a' <= row[j] <= 'z':
                    cost = ord(row[j]) - ord('a') + 1

                elif 'A' <= row[j] <= 'Z':
                    cost = ord(row[j]) - ord('A') + 27

                total_weight += cost
                edges.append((cost, i, j))
    
    mst_weight = kruskal(N, edges)
  
    if mst_weight == -1:
        print(-1)

    else:
        print(total_weight - mst_weight)

if __name__ == "__main__":
    main()

