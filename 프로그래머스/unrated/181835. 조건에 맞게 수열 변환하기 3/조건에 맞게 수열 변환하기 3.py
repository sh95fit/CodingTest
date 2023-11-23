def solution(arr, k):
    if k%2 != 0 :
        for i, a in enumerate(arr) :
            arr[i] = a*k
        return arr
    else :
        for i, a in enumerate(arr) :
            arr[i] = a+k
        return arr