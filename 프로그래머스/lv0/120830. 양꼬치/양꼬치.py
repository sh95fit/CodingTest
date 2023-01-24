def solution(n, k):
    if n < 10 :
        answer = 12000*n + 2000*k
    elif n >=10 :
        answer = 12000*n + 2000*k - 2000*(n//10)
    return answer