def solution(num_list, n):
    answer = []
    
    for num in num_list :
        if len(answer) < n :
            answer.append(num)    
    return answer