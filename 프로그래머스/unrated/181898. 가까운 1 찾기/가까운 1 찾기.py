def solution(arr, idx):
    answer = idx
    for i in range(idx,len(arr)):
        if arr[i] == 1 :
            return answer
        else :
            answer += 1
    if answer == len(arr) :
        return -1
    
    return answer