def solution(a, b, n):
    cnt = 0
    el = 0
    
    while n//a != 0 :
        cnt += (n//a)*b
        el = n%a
        n = (n//a)*b + el
    
    return cnt