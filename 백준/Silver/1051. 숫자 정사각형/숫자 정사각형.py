def find_largest_square(matrix, N, M):

    max_square_size = 1  # 최소 크기 정사각형은 항상 1

    for i in range(N):

        for j in range(M):

            for k in range(min(N - i, M - j)):

                if matrix[i][j] == matrix[i + k][j] == matrix[i][j + k] == matrix[i + k][j + k]:

                    max_square_size = max(max_square_size, (k + 1) ** 2)

    return max_square_size


N, M = map(int, input().split())

matrix = [input().strip() for _ in range(N)]

print(find_largest_square(matrix, N, M))

