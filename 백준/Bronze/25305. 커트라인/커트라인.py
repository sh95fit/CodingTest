# 입력 받기
N, k = map(int, input().split())  # 응시자의 수 N, 상을 받는 사람의 수 k
scores = list(map(int, input().split()))  # 각 학생의 점수

# 점수를 내림차순으로 정렬
scores.sort(reverse=True)

# 상을 받는 커트라인 구하기
cut_line = scores[k - 1]

# 출력
print(cut_line)
