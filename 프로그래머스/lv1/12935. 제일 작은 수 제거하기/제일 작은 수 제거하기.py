def solution(arr):
    '''
    answer = arr[0]
    if arr == [10] :
        arr = [-1]  
    else :
        for i in arr :
            if answer >= i :
                answer = i
        arr.remove(answer)
    '''
    arr.remove(min(arr))
    if arr == [ ] :
        arr = [-1]
    return arr