def solution(A, B):
    cnt = 0
    l = ""
    for i in range(len(A)) :
        if A == B :
            return cnt
        else :
            l = A[-1]
            A = A[:len(A)-1]
            A= l + A
            cnt += 1       
    return -1