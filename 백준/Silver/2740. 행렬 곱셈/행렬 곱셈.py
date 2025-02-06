# 행렬 A와 B의 크기와 원소를 입력받기

N, M = map(int, input().split())  
A = [list(map(int, input().split())) for _ in range(N)]

M2, K = map(int, input().split())  
B = [list(map(int, input().split())) for _ in range(M)]

C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(' '.join(map(str, row)))

