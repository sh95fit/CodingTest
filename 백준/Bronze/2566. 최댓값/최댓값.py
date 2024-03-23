def find_max_value(matrix):
    max_value = float('-inf')  # 최솟값으로 초기화
    max_row = -1
    max_col = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row = i+1
                max_col = j+1

    return max_value, max_row, max_col

nlist = []
for i in range(9) :
    nlist.append(list(map(int, input().split(' '))))
 

# 최댓값과 해당 행, 열 인덱스 찾기
max_value, max_row, max_col = find_max_value(nlist)

print(max_value)
print(max_row, max_col)