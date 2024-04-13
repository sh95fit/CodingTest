def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 입력 받기
N = int(input())
numbers = list(map(int, input().split()))

# 소수 개수 세기
count = 0
for number in numbers:
    if is_prime(number):
        count += 1

# 결과 출력
print(count)
