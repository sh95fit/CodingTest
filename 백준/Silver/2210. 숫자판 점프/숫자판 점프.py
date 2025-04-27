directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(board, x, y, num_str, count, visited):
    if count == 5:  
        visited.add(num_str)
        return
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:  
            dfs(board, nx, ny, num_str + str(board[nx][ny]), count + 1, visited)

def count_unique_numbers(board):
    visited = set()
    
    for i in range(5):
        for j in range(5):
            dfs(board, i, j, str(board[i][j]), 0, visited)
    
    return len(visited)

board = [list(map(int, input().split())) for _ in range(5)]

print(count_unique_numbers(board))
