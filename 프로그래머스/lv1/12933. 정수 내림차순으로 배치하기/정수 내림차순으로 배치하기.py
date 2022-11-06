def solution(n):
    num = list(str(n))
    num.sort(reverse = True)
    num = int(''.join(num))
    return num