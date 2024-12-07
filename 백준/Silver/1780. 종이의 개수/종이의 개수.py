def divide_and_count(matrix, N, count_neg, count_zero, count_pos):
    # 기본적으로 모든 원소가 같은지 확인
    first = matrix[0][0]
    is_same = True

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != first:
                is_same = False
                break

        if not is_same:
            break
    
    if is_same:
        if first == -1:
            count_neg[0] += 1
        elif first == 0:
            count_zero[0] += 1
        elif first == 1:
            count_pos[0] += 1

    else:
        # 9개로 나누어서 처리
        new_N = N // 3

        for i in range(0, N, new_N):
            for j in range(0, N, new_N):
                submatrix = [row[j:j + new_N] for row in matrix[i:i + new_N]]
                divide_and_count(submatrix, new_N, count_neg, count_zero, count_pos)

def main():
    N = int(input())  # N 크기
    matrix = [list(map(int, input().split())) for _ in range(N)]
   
    # 각 숫자의 개수를 저장할 리스트
    count_neg = [0]  # -1의 개수
    count_zero = [0]  # 0의 개수
    count_pos = [0]  # 1의 개수
    
    # 재귀적으로 처리
    divide_and_count(matrix, N, count_neg, count_zero, count_pos)

    

    # 결과 출력
    print(count_neg[0])
    print(count_zero[0])
    print(count_pos[0])

# 실행
main()

