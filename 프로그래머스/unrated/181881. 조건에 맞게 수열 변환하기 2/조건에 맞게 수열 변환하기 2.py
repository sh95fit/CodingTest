def solution(arr):
    pre_arr = arr
    res = 0
    while True :
        arr = list(map(lambda x:x/2 if x>=50 and x%2==0 else (x*2+1 if x<50 and x%2==1 else x), arr))
        if pre_arr == arr :
            break
        else :
            res += 1
            pre_arr = arr
    return res