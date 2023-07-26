def solution(todo_list, finished):
    answer = []
    
    for i, f in enumerate(finished) :
        if f :
            pass
        else :
            answer.append(todo_list[i])
    return answer