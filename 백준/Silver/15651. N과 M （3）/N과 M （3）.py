def dfs(N, M, sequence):   
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))

        return
       
    for i in range(1, N + 1):
        dfs(N, M, sequence + [i])

N, M = map(int, input().split())

dfs(N, M, [])

