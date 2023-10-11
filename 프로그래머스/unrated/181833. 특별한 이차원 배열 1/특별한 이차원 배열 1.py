def solution(n):
    answer = []
    num_list = []
    for i in range(n) :
        for j in range(n) :
            if i==j :
                num_list.append(1)
            else :
                num_list.append(0)
        answer.append(list(num_list))
        num_list.clear()
    return answer