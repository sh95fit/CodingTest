def solution(x):
    arr = str(x)
    k = 0
    for i in arr :
        k = k + int(i)
    if x%k == 0 :
        answer = True
    else :
        answer = False
    return answer