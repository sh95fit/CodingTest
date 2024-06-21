def get_cycle_length(N):

    original = N

    count = 0

    while True:

        count += 1

        # N이 10보다 작다면 앞에 0을 붙여서 두 자리 숫자로 만들기

        tens = N // 10

        ones = N % 10

        # 두 자리 숫자의 각 자리 숫자를 더하기

        sum_digits = tens + ones

        # 새로운 수 만들기

        N = (ones * 10) + (sum_digits % 10)

        # 사이클 길이 찾기

        if N == original:

            break

    return count

# 입력 받기

N = int(input().strip())

# 결과 출력

print(get_cycle_length(N))

