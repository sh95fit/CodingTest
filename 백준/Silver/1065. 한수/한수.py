def is_hansu(num):
    digits = list(map(int, str(num)))

    if len(digits) <= 2:
        return True

    diff = digits[1] - digits[0]

    for i in range(1, len(digits) - 1):
        if digits[i + 1] - digits[i] != diff:
            return False

    return True

def count_hansu(N):
    count = 0

    for i in range(1, N + 1):
        if is_hansu(i):
            count += 1

    return count

N = int(input().strip())
print(count_hansu(N))

