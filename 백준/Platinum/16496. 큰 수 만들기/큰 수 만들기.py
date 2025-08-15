from functools import cmp_to_key

def compare(x, y):

    # x+y와 y+x 중 어떤 게 더 큰지 비교

    if x + y > y + x:

        return -1  # x가 앞

    elif x + y < y + x:

        return 1   # y가 앞

    else:

        return 0

N = int(input().strip())

nums = input().split()

# 문자열로 변환 후 정렬

nums.sort(key=cmp_to_key(compare))

# 이어붙임

result = ''.join(nums)

# 모두 0이면 0 하나만 출력

if result[0] == '0':

    print(0)

else:

    print(result)