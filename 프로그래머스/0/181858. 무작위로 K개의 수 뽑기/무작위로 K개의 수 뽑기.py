def solution(arr, k):
    # seen = set()  
    answer = [] 

    for num in arr:
        if num not in answer:  
            # seen.add(num)
            answer.append(num)
        if len(answer) == k:  
            break

    while len(answer) < k:
        answer.append(-1)

    return answer