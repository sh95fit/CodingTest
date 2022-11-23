def solution(n):
    tmp = []
    k = ''
    while n :
        tmp.append(str(n%3))
        n = n//3
    tmp = ''.join(tmp)
    
    return int(tmp,3)