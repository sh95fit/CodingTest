def project_3d_to_2d(M, n):
    H = [[0] * n for _ in range(n)]
    R = [[0] * n for _ in range(n)]
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if M[i][j][k] == 1:
                    H[j][k] = 1
                    R[i][k] = 1
                    C[i][j] = 1
    
    return H, R, C

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    index += 1

    H_prime = []
    for _ in range(n):
        H_prime.append([int(x) for x in data[index]])
        index += 1
    
    R_prime = []
    for _ in range(n):
        R_prime.append([int(x) for x in data[index]])
        index += 1

    C_prime = []
    for _ in range(n):
        C_prime.append([int(x) for x in data[index]])
        index += 1

    M = [[[1] * n for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if H_prime[j][i] == 0:
                for k in range(n):
                    M[k][j][i] = 0
    
    for i in range(n):
        for j in range(n):
            if R_prime[i][j] == 0:
                for k in range(n):
                    M[i][k][j] = 0
    
    for i in range(n):
        for j in range(n):
            if C_prime[i][j] == 0:
                for k in range(n):
                    M[i][j][k] = 0

    H, R, C = project_3d_to_2d(M, n)

    if H == H_prime and R == R_prime and C == C_prime:
        print("YES")
        for i in range(n):
            for j in range(n):
                print("".join(map(str, M[i][j])))
    else:
        print("NO")

if __name__ == "__main__":
    main()