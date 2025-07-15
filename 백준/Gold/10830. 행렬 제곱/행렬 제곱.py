import sys

input = sys.stdin.readline

def mat_mult(A, B, mod=1000):
    N = len(A)
    result = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + A[i][k]*B[k][j]) % mod

    return result

def mat_pow(A, power):
    N = len(A)

    if power == 1:        
        return [[element % 1000 for element in row] for row in A]

    half = mat_pow(A, power // 2)
    half_sq = mat_mult(half, half)

    if power % 2 == 0:
        return half_sq

    else:
        return mat_mult(half_sq, A)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = mat_pow(A, B)

for row in result:
    print(' '.join(map(str, row)))