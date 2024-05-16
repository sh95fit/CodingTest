import sys

# 입력 받기
N = int(sys.stdin.readline())

# 입력 받은 숫자를 저장할 배열 생성
counts = [0] * 10001

# 입력 받으면서 각 숫자의 개수 세기
for _ in range(N):
    number = int(sys.stdin.readline())
    counts[number] += 1

# 개수를 기반으로 정렬된 숫자 출력
for i in range(10001):
    if counts[i] > 0:
        for _ in range(counts[i]):
            sys.stdout.write(str(i) + '\n')
