def min_operations_to_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1]) + 1

    min_operations = dp[0][n - 1]

    for i in range(n):
        for j in range(i + 1, n):
            if s[i] != s[j]:
                s_list = list(s)
                s_list[i], s_list[j] = s_list[j], s_list[i]
                t = ''.join(s_list)
                dp_swapped = [[0] * n for _ in range(n)]

                for length in range(2, n + 1):
                    for x in range(n - length + 1):
                        y = x + length - 1

                        if t[x] == t[y]:
                            dp_swapped[x][y] = dp_swapped[x + 1][y - 1]
                        else:
                            dp_swapped[x][y] = min(dp_swapped[x + 1][y], dp_swapped[x][y - 1], dp_swapped[x + 1][y - 1]) + 1

                min_operations = min(min_operations, dp_swapped[0][n - 1] + 1)

    return min_operations

s = input().strip()
print(min_operations_to_palindrome(s))

