# 입력 받기
numbers = [int(input()) for _ in range(5)]

# 리스트 정렬
numbers.sort()

# 평균 구하기
average = sum(numbers) // len(numbers)

# 중앙값 구하기
if len(numbers) % 2 == 0:  # 리스트의 길이가 짝수인 경우
    median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) // 2
else:  # 리스트의 길이가 홀수인 경우
    median = numbers[len(numbers)//2]

# 결과 출력
print(average)
print(median)