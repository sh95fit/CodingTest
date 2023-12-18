def solution(arr):
    answer = []
    cnt = arr.count(2)
    idx = [i for i in range(len(arr)) if '2' in str(arr[i])]
    
    if cnt == 0 :
        answer.append(-1)
        return answer
    else :
        return arr[idx[0]:idx[-1]+1]