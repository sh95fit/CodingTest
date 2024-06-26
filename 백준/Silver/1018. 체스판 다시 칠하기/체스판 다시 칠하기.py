def min_repaints(board, N, M):

    pattern1 = [
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW'
    ]

    pattern2 = [
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB'
    ]   

    min_changes = float('inf')

    for i in range(N - 7):
        for j in range(M - 7):
            changes_pattern1 = 0
            changes_pattern2 = 0

            for x in range(8):
                for y in range(8):
                    if board[i + x][j + y] != pattern1[x][y]:
                        changes_pattern1 += 1

                    if board[i + x][j + y] != pattern2[x][y]:
                        changes_pattern2 += 1

            min_changes = min(min_changes, changes_pattern1, changes_pattern2)

    return min_changes

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

result = min_repaints(board, N, M)

print(result)

